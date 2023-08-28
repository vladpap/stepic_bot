from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str      # Пароль к базе данных


@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту
    admin_ids: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int,
                                                  env.list('ADMIN_IDS',
                                                           default=[])))),
                  db=DatabaseConfig(database=env('DATABASE',
                                                 default=''),
                                    db_host=env('DB_HOST',
                                                default=''),
                                    db_user=env('DB_USER',
                                                default=''),
                                    db_password=env('DB_PASSWORD',
                                                    default='')))
