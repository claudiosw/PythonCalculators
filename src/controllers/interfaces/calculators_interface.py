from typing import Dict
from abc import ABC, abstractclassmethod


class CalculatorsInterface(ABC):

    @abstractclassmethod
    def run(self, calculator_informations: Dict) -> Dict[bool, float]:
        """ abstractmethod  """

        raise Exception("Method not implemented")
