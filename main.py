import argparse

from stromapi.config import Config
from stromapi.collector import Collector
from stromapi.day_ahead_prices import DayAheadPrices
from stromapi.weather import Weather


def main():
    parser = argparse.ArgumentParser(prog="stromapi")
    parser.add_argument(
        "--output-path",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    config = Config()
    weather = Weather.from_config(config)
    day_ahead_prices = DayAheadPrices.from_config(config)
    collector = Collector()
    cells = collector.run(day_ahead_prices, weather)
    collector.dump_csv(args.output_path, cells)


if __name__ == "__main__":
    main()
