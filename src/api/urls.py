from enum import Enum

from yarl import URL

BASE_URL = URL("https://api.prolific.co/")


class Endpoint(str, Enum):
    STUDIES = "/api/v1/studies/"
    STUDY = "/api/v1/studies/{id}/"
