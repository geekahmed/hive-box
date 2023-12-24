from pydantic import BaseModel

class SystemInfoSchema(BaseModel):
    version: str
     