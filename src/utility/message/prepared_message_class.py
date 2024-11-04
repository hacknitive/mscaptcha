from utilsweb.fastapi.response.message import PreparedMessage as _PrepareMessage


class PreparedMessage(_PrepareMessage):
    pass


messages = PreparedMessage(default_language='farsi')
