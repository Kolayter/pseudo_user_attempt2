# application/ports/llm_provider.py
from abc import abstractmethod, ABC

class ILLMProvider(ABC):
    @abstractmethod
    async def send_query(self, full_converstaion: dict[str, str]) -> str:
        ...