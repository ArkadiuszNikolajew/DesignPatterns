import abc
from typing import Any


class IObserver(abc.ABC):
    """Abstract class for Observer"""

    @abc.abstractmethod
    def update(self, data: dict[str, Any]) -> None:
        """Receive notifications from Subject"""
        pass
