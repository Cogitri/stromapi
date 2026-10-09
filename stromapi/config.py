from pathlib import Path

import tomli


class Config:
    __client_secret: str
    __latitude: float
    __longitude: float

    def __init__(self, config_path: Path):
        if not config_path.exists():
            raise RuntimeError(f"Couldn't find config.toml: '{config_path}'")

        with open(config_path, "rb") as f:
            toml_dict = tomli.load(f)
        self.__client_secret = toml_dict["entsoe"]["client_secret"]
        self.__latitude = toml_dict["weather"]["latitude"]
        self.__longitude = toml_dict["weather"]["longitude"]

    @property
    def client_secret(self) -> str:
        return self.__client_secret

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude
