from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie as _init_beanie
from utilscommon.setting.enum import EnumRunMode
from utilsdatabase.create_connection_string_mongodb import create_connection_string_mongodb

from src.setting import (
    SETTINGS,
    RUN_MODE,
)
from ..setting.global_variable import list_of_documents

if RUN_MODE == EnumRunMode.test:
    db_config = getattr(SETTINGS, "MONGODB_TEST")

else:
    db_config = getattr(SETTINGS, "MONGODB")

connection_string, database = create_connection_string_mongodb(config=db_config)


async def init_beanie():
    client = AsyncIOMotorClient(connection_string)

    await _init_beanie(
        database=client[database],
        document_models=list_of_documents,
    )
