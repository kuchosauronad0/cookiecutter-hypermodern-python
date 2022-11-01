"""{{cookiecutter.friendly_name}}."""
from importlib.metadata import version
from logging import getLogger

logger = getLogger(__name__)

try:
    __version__ = version(__name__)
except Exception:
    logger.error("Error determining version from importlib.metadata")
