# NetWiki - CTCL 2024
# File: /netwiki/config.py
# Purpose: Configuration file class module
# Created: November 11, 2024
# Modified: November 22, 2024

from pydantic import BaseModel, PositiveInt, ValidationError
from enum import Enum, IntEnum
import logging
import os
import json

logger = logging.getLogger(__name__)

class ConfigCacheEnum(str, Enum):
    memcache = "memcache"

class ConfigCache(BaseModel):
    cachetype: ConfigCacheEnum

class ConfigDbTypeEnum(str, Enum):
    mysql = "mysql"

class ConfigDb(BaseModel):
    dbtype: ConfigDbTypeEnum
    server: str
    dbname: str
    username: str
    password: str

class Config(BaseModel):
    bindip: str
    bindport: int
    sitename: str
    siteurl: str
    cache: ConfigCache
    db: ConfigDb

def loadconfig() -> Config | None:
    try:
        with open("config.json") as f:
            configtxt = f.read()
    except FileNotFoundError:
        logger.error("File config/config.json not found")
        logger.info(f"Current working directory {os.getcwd()}")
        return None

    try:
        configjson = json.loads(configtxt)
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        return None

    try:
        config = Config(**configjson)
    except ValidationError as e:
        logger.error(e.errors())
        return None

    return config