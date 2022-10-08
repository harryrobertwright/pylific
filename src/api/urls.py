from enum import Enum

from yarl import URL

BASE_URL = URL("https://api.prolific.co/")


class Endpoint(Enum):
    STUDIES = URL("api/v1/studies/")
