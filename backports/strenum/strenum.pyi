from enum import Enum
from types import DynamicClassAttribute
from typing import Type

class _magic_enum_attr(DynamicClassAttribute):
    def __set_name__(self, ownerclass: Type[Enum], name: str) -> None: ...
    name: str
    clsname: str

class StrEnum(str, Enum):
    def __new__(cls, value: str): ...
    _value_: str
    @_magic_enum_attr
    def value(self) -> str: ...
