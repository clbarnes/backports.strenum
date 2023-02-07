backports.strenum
=================

A backport of (copy and paste from) python 3.11's ``StrEnum`` class for >=3.8.6:

See the `design discussion <https://discuss.python.org/t/built-in-strenum/4192>`_,
and `Ethan Furman <https://github.com/ethanfurman>`_'s `first <https://github.com/python/cpython/pull/22337>`_ and
`second <https://github.com/python/cpython/pull/22362>`_ PR with this implementation.

A slightly different implementation would likely be compatible with lower python versions;
PRs are welcome if they pass the test suite.
The existing (reference) implementation should still be the one used on supported versions.

Install with ``pip install backports.strenum``, and use with:

.. code-block:: python

    import sys

    if sys.version_info >= (3, 11):
        from enum import StrEnum
    else:
        from backports.strenum import StrEnum

    class MyStrEnum(StrEnum):
        POTATO = "potato"
        ORANGE = "orange"
        SPADE = "spade"

    MyStrEnum.POTATO == "potato"  # True
    MyStrEnum.ORANGE.upper() == "ORANGE"  # True
    str(MyStrEnum.SPADE) == "spade"  # True


Gotchas
^^^^^^^

A number of behaviours relating to the treatment of enum classes as containers of their members (e.g. iterating and containment checks) will be changing in python 3.12.

This package intends only to allow pre-3.11 users to get 3.11-like behaviour; after that, stick with the standard library.

----

These are the `docs provided with python 3.11 <https://docs.python.org/3.11/library/enum.html#enum.StrEnum>`_:

``class enum.StrEnum``
^^^^^^^^^^^^^^^^^^^^^^

*StrEnum* is the same as *Enum*, but its members are also strings and can be used in most of the same places that a string can be used.
The result of any string operation performed on or with a *StrEnum* member is not part of the enumeration.

.. Note::
    There are places in the stdlib that check for an exact `str <https://docs.python.org/3.11/library/enum.html#enum.StrEnum>`_ instead of a `str <https://docs.python.org/3.11/library/enum.html#enum.StrEnum>`_ subclass (i.e. ``type(unknown) == str`` instead of ``isinstance(unknown, str)``), and in those locations you will need to use ``str(StrEnum.member)``.

.. Note::
    Using `auto <https://docs.python.org/3.11/library/enum.html#enum.auto>`_ with `StrEnum <https://docs.python.org/3.11/library/enum.html#enum.StrEnum>`_ results in the lower-cased member name as the value.

.. Note::
    `__str__() <https://docs.python.org/3.11/reference/datamodel.html#object.__str__>`_ is str.__str__() to better support the replacement of existing constants use-case. `__format__() <https://docs.python.org/3.11/reference/datamodel.html#object.__format__>`_ is likewise ``str.__format__()`` for that same reason.
