from ABCs.iobserver import IObserver


class Display(IObserver):
    """Concrete Observer"""

    def __init__(self):
        self.data = None

    def update(self, data: dict):
        self.data = data

    def display(self):
        for k, v in self.data.items():
            print(f'{k.capitalize()}: {v}')
