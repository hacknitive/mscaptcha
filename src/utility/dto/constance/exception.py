from utilscommon.exception import ProjectBaseException

from .status_code import *
from .message import *


EXCEPTION_UNAUTHORIZED_SERVICE = ProjectBaseException(
    status_code=HTTP_401_UNAUTHORIZED,
    success=False,
    data=None,
    error=MESSAGE_UNAUTHORIZED_SERVICE,
    message=MESSAGE_UNAUTHORIZED_SERVICE,
)