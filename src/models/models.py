from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean, TIMESTAMP, ForeignKey

metadata = MetaData()

instrument_types = Table(
    "instrument_types",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("price", Integer, nullable=False)
)

instruments = Table(
    "instruments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("type_id", Integer, ForeignKey("instrument_types.id")),
    Column("brand", String, nullable=False),
    Column("model", String, nullable=False)
)

rooms = Table(
    "rooms",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("square", Integer, nullable=False),
    Column("price", Integer, nullable=False)
)

users = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("phone", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String(length=1024), nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False)
)

rehearsals = Table(
    "rehearsals",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("time_from", TIMESTAMP, nullable=False),
    Column("time_to", TIMESTAMP, nullable=False),
    Column("room_id", Integer, ForeignKey("rooms.id")),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("price", Integer, nullable=False)
)

required_istruments = Table(
    "required_istruments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rehearsal_id", Integer, ForeignKey("rehearsals.id")),
    Column("instrument_id", Integer, ForeignKey("instruments.id"))
)