from abc import ABC, abstractmethod
from typing import Any


class LLMBase(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def generate_response(self, prompt: str, **kwargs) -> str:
        pass

    @abstractmethod
    def batch_generate_responses(self, prompts: list[str], **kwargs) -> list[str]:
        pass