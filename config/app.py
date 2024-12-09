import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class SitesConfig:
    ui_url: str
    api_url: str


@dataclass
class TestAppConfig:
    sites_config: SitesConfig


def get_config():
    return TestAppConfig(
        sites_config=SitesConfig(
            ui_url=os.getenv("UI_BASE_URL"),
            api_url=os.getenv("API_BASE_URL")
        )
    )


test_app_config = get_config()
