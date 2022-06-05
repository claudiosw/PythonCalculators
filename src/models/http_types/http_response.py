from typing import Dict


class HttpResponse:

    def __init__(
        self,
        body: Dict = None,
        status_code: int = None
    ) -> None:
        self.body = body
        self.status_code = status_code

    def __repr__(self) -> str:
        return (
            f"HttpRequest (body={self.body}, status_code={self.status_code})"
        )
