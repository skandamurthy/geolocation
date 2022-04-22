from decouple import config


async def fetch_config(config_name):
    return config(config_name)
