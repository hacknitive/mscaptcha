from os.path import (
    basename,
    dirname,
)

from utilscommon.string_case_convertor import (
    string_case_convertor,
    EnumCaseStrategy,
)

NAME = basename(dirname(__file__))


CAMEL_CASE_NAME = string_case_convertor(
    text=NAME,
    split_char='_',
    join_char='',
    case_strategy=EnumCaseStrategy.CAMEL
)

PASCAL_CASE_WITH_SPACE_NAME = string_case_convertor(
    text=NAME,
    split_char='_',
    join_char=' ',
    case_strategy=EnumCaseStrategy.PASCAL,
)

LOWER_SNAKE_CASE_NAME = string_case_convertor(
    text=NAME,
    split_char='_',
    join_char='_',
    case_strategy=EnumCaseStrategy.LOWER,
)
