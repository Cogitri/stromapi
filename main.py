import argparse

from stromapi.authenticator import Authenticator
from stromapi.config import Config
from stromapi.collector import Collector
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
    authenticator = Authenticator(config)
    authenticator.query_token()
    weather = Weather.from_config(config)
    collector = Collector(authenticator.token)
    cells = collector.run(weather)
    collector.dump_csv(args.output_path, cells)


if __name__ == "__main__":
    main()
