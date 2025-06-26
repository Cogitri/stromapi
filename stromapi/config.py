import tomli


class Config:
    __client_id: str
    __client_secret: str
    __latitude: float
    __longitude: float

    def __init__(self):
        with open("config.toml", "rb") as f:
            toml_dict = tomli.load(f)
        self.__client_id = toml_dict["netztransparenz"]["client_id"]
        self.__client_secret = toml_dict["netztransparenz"]["client_secret"]
        self.__latitude = toml_dict["weather"]["latitude"]
        self.__longitude = toml_dict["weather"]["longitude"]

    @property
    def client_id(self) -> str:
        return self.__client_id

    @property
    def client_secret(self) -> str:
        return self.__client_secret

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude
