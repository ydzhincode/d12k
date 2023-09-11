import logging


class RequireDebugOrInfoLevel(logging.Filter):
    def filter(self, record):
        return record.levelname == 'DEBUG' or record.levelname == 'INFO'


class RequireWarningLevel(logging.Filter):
    def filter(self, record):
        return record.levelname == 'WARNING'


class RequireErrorOrCriticalLevel(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR' or record.levelname == 'CRITICAL'
