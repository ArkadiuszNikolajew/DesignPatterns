import abc


class IObserver(abc.ABC):
    """Abstract class for Observer"""

    @abc.abstractmethod
    def update(self, *args):
        """Receive notifications from Subject"""
        pass
