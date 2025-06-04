import logging.config
import os
import copy

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            # 'filename' 字段将在 setup_logging() 里动态设置
            # 'filename': os.getenv('LOG_FILE', 'app.log'),
            'encoding': 'utf-8',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': os.getenv('LOG_LEVEL', 'INFO'),
    },
}

def setup_logging():
    # 确保 dist 目录存在，避免静态文件挂载时报错
    if not os.path.exists('dist'):
        os.makedirs('dist')
    config = copy.deepcopy(LOGGING_CONFIG)
    config['handlers']['file']['filename'] = os.getenv('LOG_FILE', 'app.log')
    logging.config.dictConfig(config)
