from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime

from src.auth.models import User
from src.rehearsals.schemas import Request
from src.database import get_async_session
from src.models.models import rehearsals, rooms

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

@router.get("/")
async def list_rooms(session: AsyncSession = Depends(get_async_session)):
    query = select(rooms)
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/booking/{room_id}")
async def list_future_rehearsals_by_room(room_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(rehearsals).where(rehearsals.c.room_id == room_id).where(rehearsals.c.time_from >= datetime.now())
    result = await session.execute(query)
    return result.mappings().all()

@router.get("/free")
async def list_free_rooms(time_from: datetime, time_to: datetime, session: AsyncSession = Depends(get_async_session)):
    all_rooms = await list_rooms(session)

    free_rooms = []

    for room in all_rooms:
        room_rehearsals = await list_future_rehearsals_by_room(room.id, session)
        is_free = True
        for rehearsal in room_rehearsals:
            if rehearsal.time_from >= time_from and time_to > rehearsal.time_from \
                or rehearsal.time_to <= time_to and time_from < rehearsal.time_to:
                is_free = False
                break
        if (is_free):
            free_rooms.append(room)
    
    return {
        "free_rooms": free_rooms
    }