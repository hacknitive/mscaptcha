from utilsdatabase.beanie.action.delete.delete_one_by_filter import delete_one_by_filter \
    as _delete_one_by_filter

from ..schema import Document


async def delete_one_by_filter(
        filter_: dict,
        fetch_links: bool = False,
) -> None:
    await _delete_one_by_filter(
        document=Document,
        filter_=filter_,
        fetch_links=fetch_links,
    )
