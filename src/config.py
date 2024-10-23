from dotenv import load_dotenv
from os import getenv
from dataclasses import dataclass

load_dotenv()


@dataclass
class Configuration:
    token: str


CONFIG = Configuration(token=getenv("TOKEN"))
