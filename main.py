import argparse
from pathlib import Path

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
    parser.add_argument(
        "--config-path",
        type=str,
        default="config.toml",
        help="Path to config.toml",
    )
    args = parser.parse_args()

    config = Config(Path(args.config_path))
    weather = Weather.from_config(config)
    day_ahead_prices = DayAheadPrices.from_config(config)
    collector = Collector()
    cells = collector.run(day_ahead_prices, weather)
    collector.dump_csv(args.output_path, cells)


if __name__ == "__main__":
    main()
