import os

class Config:
    API_ID = int(os.getenv("API_ID",29616312 ))
    API_HASH = os.getenv("API_HASH", 'dd1a05ab4c47a5a037cc067cf4bded27')
    BOT_TOKEN = os.getenv("BOT_TOKEN", '5966666716:AAHIXeBsuFAi9sq4H0TGQjhm0KA9hpfzZL8')
