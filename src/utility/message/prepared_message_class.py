from utilsweb.fastapi.response.message import PreparedMessage as _PrepareMessage

from src.setting import SETTINGS


class PreparedMessage(_PrepareMessage):
    invalid_or_expired_captcha = {
        "farsi": ".شناسه کپچا نامعتبر بوده یا منقضی شده است",
        "english": "Invalid or expired CAPTCHA pid.",
    }

    captcha_succeeded = {
        "farsi": "کپچا با موفقیت تایید شد.",
        "english": "CAPTCHA verification succeeded.",
    }

    captcha_failed = {
        "farsi": "کپچا تایید نشد.",
        "english": "CAPTCHA verification failed.",
    }


messages = PreparedMessage(default_language=SETTINGS.GENERAL.LANGUAGE)
