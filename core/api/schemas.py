from pydantic import BaseModel

class PingResposnSchema(BaseModel):
    result: bool