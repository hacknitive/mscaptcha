from asyncpg import create_pool, connect
from asyncpg.pool import PoolConnectionProxy
from fastapi import Depends

from src.setting import SETTINGS

CONNECTION_STRING = (f"postgres://{SETTINGS.POSTGRESQL.USERNAME}:{SETTINGS.POSTGRESQL.PASSWORD}"
                     f"@{SETTINGS.POSTGRESQL.HOST}:{SETTINGS.POSTGRESQL.PORT}/{SETTINGS.POSTGRESQL.DATABASE}")

db_pool = None


async def get_db_pool():
    global db_pool
    if db_pool is None:
        db_pool = await create_pool(
            dsn=CONNECTION_STRING,
            min_size=1,
            max_size=10,
            max_inactive_connection_lifetime=10,
        )
    return db_pool


async def get_one_connection():
    return await connect(dsn=CONNECTION_STRING)


async def get_postgresql_db(pool=Depends(get_db_pool)) -> PoolConnectionProxy:
    async with pool.acquire() as connection:
        yield connection
