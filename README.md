# stromapi

This project can generate a CSV file containing energy price and weather data.

## Requirements

This projects needs python >=3.11 and `uv` as package manager. See [uv's documentation](https://docs.astral.sh/uv/getting-started/installation/) on how to install `uv`.
Once installed, the project can be run with `uv run main.py --output-path=output.csv`

## Configuration

Some configuration values are required in the following format in the file `config.toml`:

```toml
[entsoe]
client_secret = "xyz"
# Different prices depending on 60 or 15 minute settlement perioid
resolution_in_minutes = 60

[weather]
latitude = 1.1
longitude = 2.2
```
