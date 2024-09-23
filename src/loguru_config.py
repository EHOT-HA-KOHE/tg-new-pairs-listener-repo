import sys
import os

from loguru import logger


logger.remove()
logger.add(
    "logs/debug.log",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    diagnose=True
)

if not os.getenv('START_IN_DOCKER'):
    logger.add(
        sys.stdout,  # Стандартный вывод
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        diagnose=True,
        level="DEBUG"
    )
    