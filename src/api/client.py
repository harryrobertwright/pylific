from requests import Session
from src.api import auth, urls
from src.types import JSON


class Client:
    def __init__(self, token: str) -> None:
        self.session = Session()
        self.session.auth = auth.TokenAuth(token)

    def _get(self, endpoint: urls.Endpoint) -> JSON:
        url = str(urls.BASE_URL.join(endpoint.value))
        return self.session.get(url).json()

    def get_studies(self) -> JSON:
        return self._get(urls.Endpoint.STUDIES)
