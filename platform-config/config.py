"""Config access, v1 and v2.

v1: module-level `get_config("key")`. Deprecated.
v2: `Config.get("key")`. The migration replaces every v1 call with the v2 form.
"""

_STORE = {
    "timeout": 30,
    "retries": 3,
    "region": "us-east-1",
    "batch_size": 100,
    "currency": "USD",
    "rate_limit": 1000,
}


def get_config(key: str):  # v1 (deprecated)
    return _STORE.get(key)


class Config:  # v2
    @staticmethod
    def get(key: str):
        return _STORE.get(key)
