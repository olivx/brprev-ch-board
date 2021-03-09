from decouple import config

BOARD_LENGTH = config("BOARD_LENGTH", default=20, cast=int)
PLAYED_TIMES = config("PLYED_TIMES", default=300, cast=int)
TIMEOUT = config("TIMEOUT", default=1000, cast=int)
