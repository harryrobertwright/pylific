from functools import cached_property
from typing import Any

from src.api import sessions, urls
from src.types import JSON


class Client:
    def __init__(self, token: str, raise_deprecations: bool = False) -> None:
        self._token = token
        self._raise_deprecations = raise_deprecations

    @property
    def token(self) -> str:
        return self._token

    @property
    def raise_deprecations(self) -> bool:
        return self._raise_deprecations

    @token.setter
    def token(self, value: str) -> None:
        self._token = value
        self.session.auth.token = value

    @raise_deprecations.setter
    def raise_deprecations(self, value: bool) -> None:
        self._raise_deprecations = value
        self.session.raise_deprecations = self._raise_deprecations

    @cached_property
    def session(self) -> sessions.Session:
        return sessions.Session(self.token, raise_deprecations=self.raise_deprecations)

    def _request(self, method: str, endpoint: str) -> JSON:
        return self.session.request(method, endpoint=endpoint).json()

    def _get(self, endpoint: str) -> JSON:
        return self._request("GET", endpoint)

    def get_studies(self) -> list[dict[str, Any]] | None:
        data = self._get(urls.Endpoint.STUDIES.value)
        return data.get("results")

    def get_study(self, id: str) -> dict[str, Any] | None:
        return self._get(urls.Endpoint.STUDY.value.format(id=id))
