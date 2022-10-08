from requests import Response
from requests import Session as BaseSession
from src.api import auth, urls
from yarl import URL


class Session(BaseSession):
    def __init__(
        self, token: str, raise_deprecations: bool = False, *args, **kwargs
    ) -> None:
        super().__init__(*args, **kwargs)
        self.auth = auth.TokenAuth(token)
        self.raise_deprecations = raise_deprecations

    def request(self, *args, endpoint: str, **kwargs) -> Response:
        endpoint = URL(endpoint)
        url = str(urls.BASE_URL.join(endpoint))
        response = super().request(url=url, *args, **kwargs)
        is_deprecated = response.headers.get("Deprecation", False)

        if is_deprecated and self.raise_deprecations:
            raise DeprecationWarning()

        return response
