from utilsdatabase.beanie.action.delete.delete_list_by_filter import delete_list_by_filter \
    as _delete_list_by_filter

from ..schema import Document


async def delete_list_by_filter(filter_: dict) -> None:
    await _delete_list_by_filter(
        document=Document,
        filter_=filter_,
        fetch_links=False,
    )
