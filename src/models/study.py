from pydantic import BaseModel
from src.api import Client


class Study(BaseModel):
    id: str
    name: str
    status: str

    class Meta:
        extra = "ignore"

    @classmethod
    def get_all(cls, token: str) -> list["Study"]:
        from src.parsers import StudyParser

        studies = Client(token).get_studies()
        return [StudyParser(study).parse() for study in studies]
