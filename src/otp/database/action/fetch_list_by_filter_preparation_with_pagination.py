from utilsdatabase.beanie.action import (
    fetch_list_by_filter_with_pagination,
    prepare_filter,
)
from utilsdatabase.beanie.enum import EnumOrderBy


from ..schema import (
    Document,
    FIELDS_NAMES_FOR_X,
)


async def fetch_list_by_filter_preparation_with_pagination(
        inputs: dict,
        current_page: int = 1,
        page_size: int = 10,
        order_by: dict[str, EnumOrderBy] | None = None,
) -> dict:
    filter_ = prepare_filter(
        inputs=inputs,
        search_field_name='search',
        **FIELDS_NAMES_FOR_X,
    )

    return await fetch_list_by_filter_with_pagination(
        document=Document,
        filter_=filter_,
        current_page=current_page,
        page_size=page_size,
        order_by=order_by,
        project_model=None,
        fetch_links=False,
    )
