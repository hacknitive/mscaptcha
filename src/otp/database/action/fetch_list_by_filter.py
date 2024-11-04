from typing import (
    Dict,
    Optional,
    Type,
)

from pydantic import BaseModel
from utilsdatabase.beanie.action.fetch.fetch_list_by_filter import fetch_list_by_filter as _fetch_list_by_filter
from utilsdatabase.beanie.enum import EnumOrderBy

from ..schema import Document


async def fetch_list_by_filter(
        filter_: Dict,
        order_by: Dict[str, EnumOrderBy] | None = None,
        project_model: Optional[Type[BaseModel]] = None,
):
    return await _fetch_list_by_filter(
        document=Document,
        filter_=filter_,
        current_page=1,
        page_size=0,  # this means we don,t have pagination
        order_by=order_by,
        project_model=project_model,
        fetch_links=False,
    )
