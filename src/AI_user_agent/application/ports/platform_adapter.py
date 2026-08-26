# application/ports/platform_adapter.py
from abc import abstractmethod, ABC

class IMessageReceiver(ABC):
    # @abstractmethod
    # def _register_events(self):
    #     ...
    ...


class IMessageSender(ABC):

    @abstractmethod
    async def send_message(self, chat_id: int, text: str) -> None:
        ...
    
    # @abstractmethod
    # async def send_reaction(self, chat_id: int, message_id: int) -> None:
    #     ...

    # @abstractmethod
    # async def typing_status(self, chat_id) -> None:
    #     ...