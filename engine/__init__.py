# engine/__init__.py
from .logger import setup_logger

def initialize_logger():
    """Initialize a default logger for the engine."""
    global logger
    logger = setup_logger("IntegrationEngine")

initialize_logger()