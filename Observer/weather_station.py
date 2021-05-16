from collections.abc import Sequence
from ABCs.iobservable import IObservable
from ABCs.iobserver import IObserver


class WeatherStation(IObservable):
    """The Subject"""

    def __init__(self, observers: Sequence[IObserver] = None) -> None:
        if not observers:
            self._observers = set()
        else:
            self._observers = set(observers)
        self.data: dict = dict()

    def add(self, observer: IObserver) -> None:
        if isinstance(observer, IObserver):
            self._observers.add(observer)
        else:
            raise TypeError('Registering failed. Object must be an instance of Observer abstract class')

    def remove(self, observer: IObserver) -> None:
        self._observers.discard(observer)

    def remove_all(self) -> None:
        self._observers.clear()

    def notify(self) -> None:
        for obs in self._observers:
            obs.update(self.data)

    def set_temperature(self, temperature: float) -> None:
        self.data['temperature'] = temperature

    def set_pressure(self, pressure: float) -> None:
        self.data['pressure'] = pressure
