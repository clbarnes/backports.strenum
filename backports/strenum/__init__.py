import sys
from .version import version as __version__  # noqa: F401
if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from .strenum import StrEnum

__all__ = ["StrEnum"]
