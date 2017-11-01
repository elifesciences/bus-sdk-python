from abc import ABC, abstractmethod
from bus_sdk.messages import Message


class EventPublisher(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def publish(self, message: Message) -> str:
        raise NotImplementedError
