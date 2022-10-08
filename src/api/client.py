from functools import cached_property
from typing import Any

from src.api import sessions, urls
from src.types import JSON


class Client:
    def __init__(self, token: str) -> None:
        self._token = token

    @property
    def token(self) -> str:
        return self._token

    @token.setter
    def token(self, value: str) -> None:
        self._token = value
        session_key = "session"

        if session_key in self.__dict__:
            del self.__dict__[session_key]

    @cached_property
    def session(self) -> sessions.Session:
        return sessions.Session(self.token)

    def _get(self, endpoint: urls.Endpoint) -> JSON:
        url = str(urls.BASE_URL.join(endpoint.value))
        return self.session.get(url).json()

    def get_studies(self) -> list[str, Any] | None:
        data = self._get(urls.Endpoint.STUDIES)
        return data.get("results")
