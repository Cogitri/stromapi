import requests


class ApiError(Exception):
    message: str

    def __init__(self, resp: requests.Response):
        self.message = f"HTTP Code {resp.status_code}: {resp.text}"
        super().__init__(self.message)