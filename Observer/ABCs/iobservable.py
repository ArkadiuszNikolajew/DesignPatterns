import abc
from .iobserver import IObserver


class IObservable(abc.ABC):
    """Abstract class for Subject"""

    @abc.abstractmethod
    def add(self, observer: IObserver):
        """Register method for Observer"""
        pass

    @abc.abstractmethod
    def remove(self, observer: IObserver):
        """Method for removing Observer"""
        pass

    @abc.abstractmethod
    def notify(self, *args):
        """Method for notifying Observers"""
        pass
