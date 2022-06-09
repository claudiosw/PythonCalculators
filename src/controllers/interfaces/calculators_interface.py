from typing import Dict
from abc import ABC, abstractclassmethod
from src.models.http_types.http_request import HttpRequest


class CalculatorsInterface(ABC):

    @abstractclassmethod
    def run(self, http_request: HttpRequest) -> Dict[bool, float]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
