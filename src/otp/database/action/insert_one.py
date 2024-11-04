from utilsdatabase.beanie.action import insert_one_without_pid as _insert_one

from ..schema import Document


async def insert_one(inputs: dict) -> Document:
    return await _insert_one(
        document=Document,
        inputs=inputs
    )
