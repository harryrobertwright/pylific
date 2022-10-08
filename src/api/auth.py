from dataclasses import dataclass

from requests import Request, auth


@dataclass
class TokenAuth(auth.AuthBase):
    token: str

    def __call__(self, request: Request) -> Request:
        request.headers["Authorization"] = f"Token {self.token}"
        return request
