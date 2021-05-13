from weather_station import WeatherStation
from display import Display


if __name__ == '__main__':
    station = WeatherStation()
    display = Display()
    station.add(display)
    station.set_temperature(28.2)
    station.set_pressure(1013.2)
    station.notify()
    display.display()
