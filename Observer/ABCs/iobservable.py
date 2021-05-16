import abc
from .iobserver import IObserver


class IObservable(abc.ABC):
    """Abstract class for Subject"""

    @abc.abstractmethod
    def add(self, observer: IObserver) -> None:
        """Register method for Observer"""
        pass

    @abc.abstractmethod
    def remove(self, observer: IObserver) -> None:
        """Method for removing Observer"""
        pass

    @abc.abstractmethod
    def notify(self) -> None:
        """Method for notifying Observers"""
        pass
