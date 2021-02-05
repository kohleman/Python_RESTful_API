import os

class DevelopmentConfig:
    port = 5000
    debug = True
    log_path = "boardgames.log"

class ProductionConfig:
    port = 8000
    debug = False
    log_path = "boardgames.log"

configurations = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}

environment = os.environ.get("BG_CONFIG", "dev")
config = configurations[environment]