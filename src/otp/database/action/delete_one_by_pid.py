from utilsdatabase.beanie.action import delete_one_by_pid as _delete_one_by_pid

from ..schema import Document


async def delete_one_by_pid(pid: str):
    return await _delete_one_by_pid(
        document=Document,
        pid=pid,
    )
