
from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @abstractmethod
    def get(self, len: int) -> str: pass
