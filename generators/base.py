
from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    @abstractmethod
    def get_text(self, len: int) -> str: pass
