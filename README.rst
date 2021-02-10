backports.strenum
=================

A backport of (copy and paste from) python 3.10's ``StrEnum`` class for >=3.8.6:

    Base class for creating enumerated constants that are also subclasses of ``str``.

See the `design discussion <https://discuss.python.org/t/built-in-strenum/4192>`_,
and `Ethan Furman <https://github.com/ethanfurman>`_'s `first <https://github.com/python/cpython/pull/22337>`_ and
`second <https://github.com/python/cpython/pull/22362>`_ PR with this implementation.

A slightly different implementation would likely be compatible with lower python versions;
PRs are welcome if they pass the test suite.
The existing (reference) implementation should still be the one used on supported versions.

Install with ``pip install backports.strenum``, and use with::

    try:
        # be ready for 3.10 when it drops
        from enum import StrEnum
    except ImportError:
        from backports.strenum import StrEnum

    class MyStrEnum(StrEnum):
        POTATO = "potato"
        ORANGE = "orange"
        SPADE = "spade"

    MyStrEnum.POTATO == "potato"  # True
    MyStrEnum.ORANGE.upper() == "ORANGE"  # True
    str(MyStrEnum.SPADE) == "spade"  # True

----

StrEnum
^^^^^^^

The second variation of ``Enum`` that is provided is also a subclass of
``str``.  Members of a ``StrEnum`` can be compared to strings;
by extension, string enumerations of different types can also be compared
to each other.  ``StrEnum`` exists to help avoid the problem of getting
an incorrect member::

    >>> class Directions(StrEnum):
    ...     NORTH = 'north',    # notice the trailing comma
    ...     SOUTH = 'south'

Before ``StrEnum``, ``Directions.NORTH`` would have been the ``tuple``
``('north',)``.

.. note::

    Unlike other Enum's, ``str(StrEnum.member)`` will return the value of the
    member instead of the usual ``"EnumClass.member"``.


----

Creating members that are mixed with other data types
"""""""""""""""""""""""""""""""""""""""""""""""""""""

When subclassing other data types, such as ``int`` or ``str``, with
an ``Enum``, all values after the `=` are passed to that data type's
constructor.  For example::

    >>> class MyEnum(IntEnum):
    ...     example = '11', 16      # '11' will be interpreted as a hexadecimal
    ...                             # number
    >>> MyEnum.example
    <MyEnum.example: 17>

----

``StrEnum`` and ``str.__str__``
"""""""""""""""""""""""""""""""""""

An important difference between ``StrEnum`` and other Enums is the
``__str__`` method; because ``StrEnum`` members are strings, some
parts of Python will read the string data directly, while others will call
``str()``. To make those two operations have the same result,
``StrEnum.__str__`` will be the same as ``str.__str__`` so that
``str(StrEnum.member) == StrEnum.member`` is true.
