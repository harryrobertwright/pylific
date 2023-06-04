import os

from requests import Session

from src.constants import TOKEN_KEY
from src.exceptions import PylificError


class Client:
    """A class representing a client for interacting with the Prolific API."""

    def __init__(self) -> None:
        self._session = self._get_session()

    def _get_session(self) -> Session:
        """Get a `requests.Session` object with the necessary headers.

        Raises:
            If the `TOKEN_KEY` environment variable is not set, it raises a `PylificError`.

        Returns:
            A `requests.Session` object with the `Authorization` header set.
        """
        token = os.environ.get(TOKEN_KEY)

        if token is None:
            raise PylificError(
                f"{TOKEN_KEY} environment variable not set. Please ensure you have set it for Pylific to authenticate correctly."
            )

        session = Session()
        session.headers.update({"Authorization": f"Token {token}"})

        return session
