from unittest import TestCase

import mock
from requests import Session

from src.client import Client
from src.constants import TOKEN_KEY
from src.exceptions import PylificError

DUMMY_TOKEN = "1234"


class TestClient(TestCase):
    @mock.patch.dict("os.environ", {}, clear=True)
    def test_client_initialization_raises_error_when_token_not_set(self):
        with self.assertRaises(PylificError):
            Client()

    @mock.patch.dict("os.environ", {TOKEN_KEY: DUMMY_TOKEN}, clear=True)
    def test_client_initialization_sets_session_with_correct_authorization_header_when_token_set(
        self,
    ):
        client = Client()
        session = client._session

        self.assertIsInstance(session, Session)
        self.assertEqual(session.headers.get("Authorization"), f"Token {DUMMY_TOKEN}")
