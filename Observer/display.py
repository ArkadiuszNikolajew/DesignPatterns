from ABCs.iobserver import IObserver
from typing import Any


class Display(IObserver):
    """Concrete Observer"""

    def __init__(self) -> None:
        self.data = None

    def update(self, data: dict[str, Any]) -> None:
        self.data = data

    def display(self) -> None:
        for k, v in self.data.items():
            print(f'{k.capitalize()}: {v}')
