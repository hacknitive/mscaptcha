from datetime import datetime

from pydantic import Field
from beanie import Indexed
from beanie import Document as _Document

from ...utility.setting.global_variable import list_of_documents
from .. import LOWER_SNAKE_CASE_NAME


class Document(_Document):
    class Settings:
        name = LOWER_SNAKE_CASE_NAME
        keep_nulls = False

    phone_number: Indexed(str)
    code: Indexed(str)
    who_send: Indexed(str)
    created_at: Indexed(datetime) = Field(default_factory=datetime.utcnow)


list_of_documents.append(Document)

FIELDS_NAMES_FOR_X = {
    'fields_names_for_regex': (
        'phone_number',
        'code',
    ),
    'fields_names_for_datetime': (
        'created_at',
    ),
    'fields_names_for_in': (
        'who_send',
    ),
    'fields_names_for_search': (
        'phone_number',
        'code',
        'who_send',
    ),
}
