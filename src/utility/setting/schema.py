from pydantic import BaseModel


class StreamServer(BaseModel):
    ADDRESS: str


class Asset(BaseModel):
    PATH: str
