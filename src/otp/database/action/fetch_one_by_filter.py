from typing import (
    Dict,
    Union,
    List,
    Tuple,
)

from beanie import SortDirection
from utilsdatabase.beanie.action.fetch.fetch_one_by_filter import fetch_one_by_filter \
    as _fetch_one_by_filter

from ..schema import Document


async def fetch_one_by_filter(
        filter_: Dict,
        sort: Union[None, str, List[Tuple[str, SortDirection]]] = None,
) -> Union[Document, None]:
    return await _fetch_one_by_filter(
        document=Document,
        filter_=filter_,
        project_model=None,
        fetch_links=False,
        skip=None,
        sort=sort,
    )
