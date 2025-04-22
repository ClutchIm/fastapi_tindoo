from authx import AuthX, AuthXConfig

from src.core.config import settings

config = AuthXConfig()

config.JWT_SECRET_KEY = settings.JWT_SECRET_KEY
config.JWT_ALGORITHM = settings.JWT_ALGORITHM
config.JWT_TOKEN_LOCATION = settings.JWT_TOKEN_LOCATION

config.JWT_ACCESS_TOKEN_EXPIRES = settings.JWT_ACCESS_TOKEN_EXPIRES
config.JWT_REFRESH_TOKEN_EXPIRES = settings.JWT_REFRESH_TOKEN_EXPIRES

auth = AuthX(config=config)
