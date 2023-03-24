"""Config for the pytest"""

SUPPORTED_ENVS = ["dev", "qa"]


class Config:
    """Config class for the pytest"""

    def __init__(self, env: str) -> None:
        if env.lower() not in SUPPORTED_ENVS:
            raise NotImplementedError(f"{env} is not a supported environment.")

        self.base_url = {
            "dev": "https://mydev-env.com",
            "qa": "https://myqa-env.com",
        }[env]

        self.app_port = {
            "dev": 8080,
            "qa": 80,
        }[env]

