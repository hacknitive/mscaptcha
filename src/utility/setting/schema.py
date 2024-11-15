from pydantic import BaseModel


class Captcha(BaseModel):
    DEFAULT_ALLOWABLE_CHARACHTERS: str
    DEFAULT_NUMBER_OF_CHARACHTERS: int
    DEFAULT_VALIDITY_PERIOD_IN_SECONDS: int
