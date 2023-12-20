from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, and_, or_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import current_user
from src.auth.models import User
from src.rehearsals.schemas import Request
from src.database import get_async_session
from src.models.models import rehearsals, rooms, required_istruments, instruments

router = APIRouter(
    prefix="/rehearsals",
    tags=["Rehearsals"]
)

@router.get("/")
async def list_rehearsals(session: AsyncSession = Depends(get_async_session)):
    query = select(rehearsals)
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/")
async def add_rehearsal(request: Request, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    prepared_values = request.dict()
    prepared_values["user_id"] = user.id

    time_to = request.time_to.hour * 60 + request.time_to.minute
    time_from = request.time_from.hour * 60 + request.time_from.minute
    duration =  (time_to - time_from) // 60

    price_query = select(rooms.c.price).where(rooms.c.id == request.room_id)
    price = await session.execute(price_query)
    prepared_values["price"] = price.one()[0] * duration
    
    stmt = insert(rehearsals).values(**prepared_values)
    result = await session.execute(stmt)
    await session.commit()
    return {
        "status": "ok",
        "id": result.inserted_primary_key[0],
        "data": prepared_values,
    }

@router.get("/{rehearsal_id}")
async def get_rehearsal(rehearsal_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(rehearsals).where(rehearsals.c.id == rehearsal_id)
    result = await session.execute(query)
    return result.mappings().all()

@router.delete("/{rehearsal_id}")
async def delete_rehearsal(rehearsal_id: int, session: AsyncSession = Depends(get_async_session), user: User = Depends(current_user)):
    query = delete(rehearsals).where(rehearsals.c.id == rehearsal_id)
    result = await session.execute(query)
    return {
        "status": "ok",
        "message": "Successfully deleted",
    }

@router.get("/users/{user_id}")
async def get_rehearsal_by_user(user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    user_id = user.id
    query = select(rehearsals).where(rehearsals.c.user_id == user_id)
    result = await session.execute(query)
    return result.mappings().all()

@router.post("/instruments/{rehearsal_id}")
async def add_instruments(rehearsal_id: int, instrument_type: int, user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    current_rehearsal = await get_rehearsal(rehearsal_id, session)

    same_time_query = select(rehearsals.c.id) \
        .where(
            or_(
                and_(rehearsals.c.time_from >= current_rehearsal[0].time_from, current_rehearsal[0].time_to > rehearsals.c.time_from),
                and_(rehearsals.c.time_to <= current_rehearsal[0].time_to, current_rehearsal[0].time_from > rehearsals.c.time_to)
            )
        )
    same_time_result = await session.execute(same_time_query)

    unavailable_instruments = []

    for id in same_time_result.all():
        unavailable_query = select(required_istruments.c.instrument_id) \
            .where(required_istruments.c.rehearsal_id == id[0])
        result = await session.execute(unavailable_query)
        for item in result.all():
            unavailable_instruments.append(item[0])

    same_type_query = select(instruments.c.id).where(instruments.c.type_id == instrument_type)
    same_type_result = await session.execute(same_type_query)

    for instrument in same_type_result.all():
        if not(instrument[0] in unavailable_instruments):
            inserted_dict = {
                "rehearsal_id": rehearsal_id,
                "instrument_id": instrument[0]
            }
            stmt = insert(required_istruments).values(**inserted_dict)
            await session.execute(stmt)
            await session.commit()
            return {
                "status": "ok",
                "user_id": user.id,
                "data": inserted_dict,
            }
    
    return {
        "status": "failed",
        "message": "There are no available instrumemts of scuh time in this period",
    }