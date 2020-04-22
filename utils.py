import logging.config, sys

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

DEFAULT_LOGGING = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': color.RED + '%(asctime)-4s' + color.END + color.PURPLE + ' %(levelname)-8s' + color.END + '%(message)s',
            'datefmt': '%Y-%m-%d | %H:%M:%S' },
    },
    'handlers': {
        'console':  {'class': 'logging.StreamHandler',
                     'formatter': "standard",
                     'level': 'DEBUG',
                     'stream': sys.stdout},
        'file':     {'class': 'logging.FileHandler',
                     'formatter': "standard",
                     'level': 'DEBUG',
                     'filename': '/var/log/app.log','mode': 'w'},
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'file'],
        'propagate': False
    }
}

logging.config.dictConfig(DEFAULT_LOGGING)