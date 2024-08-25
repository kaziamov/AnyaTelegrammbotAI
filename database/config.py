import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

DB_CONFIG = {
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("HOST"),
    "port": os.getenv("PORT"),
}

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",  # Отправляем все логи в stderr
            "formatter": "simple",
            "stream": "ext://sys.stderr",
        }
    },
    "root": {"level": "DEBUG", "handlers": ["console"]},
}
