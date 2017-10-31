from abc import ABC, abstractmethod


class EventPublisher(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def publish(self, message: dict) -> str:
        raise NotImplementedError
