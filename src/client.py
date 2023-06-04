import os
from http import HTTPStatus
from typing import Any

from requests import Session

from src import constants
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
        key = constants.TOKEN_KEY
        token = os.environ.get(key)

        if token is None:
            raise PylificError(
                f"{key} environment variable not set. Please ensure you have set it for Pylific to authenticate correctly."
            )

        session = Session()
        session.headers.update({"Authorization": f"Token {token}"})

        return session

    def get_account_details(self) -> dict[str, Any]:
        """Retrieve the account details for the authenticated user.

        Raises:
            If the HTTP response status code is not `HTTPStatus.OK`, it raises a `PylificError`,
            indicating an error in fetching the account details.

        Returns:
            A dictionary containing the user's account details.
        """

        response = self._session.get(f"{constants.DOMAIN}/api/v1/users/me/")
        status_code = response.status_code

        if response.status_code != HTTPStatus.OK:
            raise PylificError(
                f"Failed to get account details. Received status code {status_code}. "
                f"Please check your authentication and ensure the account associated with the token exists."
            )

        return response.json()
