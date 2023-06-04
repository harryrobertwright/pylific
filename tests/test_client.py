from http import HTTPStatus
from unittest import TestCase

import mock
from requests import Session

from src.client import Client
from src.constants import TOKEN_KEY
from src.exceptions import PylificError

DUMMY_TOKEN = "1234"


@mock.patch.dict("os.environ", {TOKEN_KEY: DUMMY_TOKEN}, clear=True)
class TestClient(TestCase):
    @mock.patch.dict("os.environ", {}, clear=True)
    def test_client_initialization_raises_error_when_token_not_set(self):
        with self.assertRaises(PylificError):
            Client()

    def test_client_initialization_sets_session_with_correct_authorization_header_when_token_set(
        self,
    ):
        client = Client()
        session = client._session

        self.assertIsInstance(session, Session)
        self.assertEqual(session.headers.get("Authorization"), f"Token {DUMMY_TOKEN}")

    @mock.patch.object(Session, "get")
    def test_get_account_details_success(self, mock_get):
        data = {"key": "value"}
        mock_get.return_value = mock.Mock(json=lambda: data, status_code=HTTPStatus.OK)

        client = Client()
        account_details = client.get_account_details()

        self.assertEqual(account_details, data)

    @mock.patch.object(Session, "get")
    def test_get_account_details_raises_error_when_status_not_ok(self, mock_get):
        mock_get.return_value = mock.Mock(status_code=HTTPStatus.BAD_REQUEST)

        client = Client()

        with self.assertRaises(PylificError):
            client.get_account_details()
