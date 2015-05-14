import logging
import logging.config
import yaml

# config logging
with open('config/log.yml') as log_config:
        logging.config.dictConfig(yaml.load(log_config))
