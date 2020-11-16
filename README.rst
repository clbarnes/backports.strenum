backports.strenum
=================

A backport of (copy and paste from) python 3.10's StrEnum class:

    Base class for creating enumerated constants that are also
    subclasses of :class:`str`.

See `here <https://discuss.python.org/t/built-in-strenum/4192>`_ for design discussion.

----

StrEnum
^^^^^^^

The second variation of :class:`Enum` that is provided is also a subclass of
:class:`str`.  Members of a :class:`StrEnum` can be compared to strings;
by extension, string enumerations of different types can also be compared
to each other.  :class:`StrEnum` exists to help avoid the problem of getting
an incorrect member::

    >>> class Directions(StrEnum):
    ...     NORTH = 'north',    # notice the trailing comma
    ...     SOUTH = 'south'

Before :class:`StrEnum`, ``Directions.NORTH`` would have been the :class:`tuple`
``('north',)``.

.. note::

    Unlike other Enum's, ``str(StrEnum.member)`` will return the value of the
    member instead of the usual ``"EnumClass.member"``.

.. versionadded:: 3.10

----

Creating members that are mixed with other data types
"""""""""""""""""""""""""""""""""""""""""""""""""""""

When subclassing other data types, such as :class:`int` or :class:`str`, with
an :class:`Enum`, all values after the `=` are passed to that data type's
constructor.  For example::

    >>> class MyEnum(IntEnum):
    ...     example = '11', 16      # '11' will be interpreted as a hexadecimal
    ...                             # number
    >>> MyEnum.example
    <MyEnum.example: 17>

----

``StrEnum`` and :meth:`str.__str__`
"""""""""""""""""""""""""""""""""""

An important difference between :class:`StrEnum` and other Enums is the
:meth:`__str__` method; because :class:`StrEnum` members are strings, some
parts of Python will read the string data directly, while others will call
:meth:`str()`. To make those two operations have the same result,
:meth:`StrEnum.__str__` will be the same as :meth:`str.__str__` so that
``str(StrEnum.member) == StrEnum.member`` is true.

