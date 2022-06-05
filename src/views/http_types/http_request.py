from typing import Dict


class HttpRequest:

    def __init__(
        self,
        header: Dict = None,
        body: Dict = None,
        query_param: Dict = None,
        url: str = None,
        token_information: Dict = None
    ) -> None:
        self.header = header
        self.body = body
        self.query_param = query_param
        self.url = url
        self.token_information = token_information

    def __repr__(self) -> str:
        return (
            f"HttpRequest (header={self.header}, body={self.body}, query={self.query_param})"
        )
