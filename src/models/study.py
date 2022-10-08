from pydantic import BaseModel


class Study(BaseModel):
    id: str
    name: str
    status: str

    class Meta:
        extra = "ignore"
