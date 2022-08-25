from enum import Enum
from types import DynamicClassAttribute
from typing import TypeVar

Self = TypeVar("Self")

class StrEnum(str, Enum):
    def __new__(cls: type[Self], value: str) -> Self: ...
    _value_: str
    @DynamicClassAttribute
    def value(self) -> str: ...
