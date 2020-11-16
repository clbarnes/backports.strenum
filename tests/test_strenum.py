import unittest
from enum import Enum, unique

from backports.strenum import StrEnum


import pydoc
import sys
from io import StringIO


# for pickle test and subclass tests
class Name(StrEnum):
    BDFL = "Guido van Rossum"
    FLUFL = "Barry Warsaw"


class TestEnum(unittest.TestCase):
    def test_enum_str_override(self):
        class MyStrEnum(Enum):
            def __str__(self):
                return "MyStr"

        class MyMethodEnum(Enum):
            def hello(self):
                return "Hello!  My name is %s" % self.name

        class Test1Enum(MyMethodEnum, int, MyStrEnum):
            One = 1
            Two = 2

        self.assertEqual(str(Test1Enum.One), "MyStr")
        #
        class Test2Enum(MyStrEnum, MyMethodEnum):
            One = 1
            Two = 2

        self.assertEqual(str(Test2Enum.One), "MyStr")

    def test_strenum_from_scratch(self):
        class phy(str, Enum):
            pi = "Pi"
            tau = "Tau"

        self.assertTrue(phy.pi < phy.tau)

    def test_strenum_inherited_methods(self):
        class phy(StrEnum):
            pi = "Pi"
            tau = "Tau"

        self.assertTrue(phy.pi < phy.tau)
        self.assertEqual(phy.pi.upper(), "PI")

    def test_multiple_inherited_mixin(self):
        @unique
        class Decision1(StrEnum):
            REVERT = "REVERT"
            REVERT_ALL = "REVERT_ALL"
            RETRY = "RETRY"

        class MyEnum(StrEnum):
            pass

        @unique
        class Decision2(MyEnum):
            REVERT = "REVERT"
            REVERT_ALL = "REVERT_ALL"
            RETRY = "RETRY"

    def test_strenum(self):
        class GoodStrEnum(StrEnum):
            one = "1"
            two = "2"
            three = b"3", "ascii"
            four = b"4", "latin1", "strict"

        self.assertEqual(GoodStrEnum.one, "1")
        self.assertEqual(str(GoodStrEnum.one), "1")
        self.assertEqual(GoodStrEnum.one, str(GoodStrEnum.one))
        self.assertEqual(GoodStrEnum.one, "{}".format(GoodStrEnum.one))
        #
        class DumbMixin:
            def __str__(self):
                return "don't do this"

        class DumbStrEnum(DumbMixin, StrEnum):
            five = "5"
            six = "6"
            seven = "7"

        self.assertEqual(DumbStrEnum.seven, "7")
        self.assertEqual(str(DumbStrEnum.seven), "don't do this")
        #
        class EnumMixin(Enum):
            def hello(self):
                print("hello from %s" % (self,))

        class HelloEnum(EnumMixin, StrEnum):
            eight = "8"

        self.assertEqual(HelloEnum.eight, "8")
        self.assertEqual(HelloEnum.eight, str(HelloEnum.eight))
        #
        class GoodbyeMixin:
            def goodbye(self):
                print("%s wishes you a fond farewell")

        class GoodbyeEnum(GoodbyeMixin, EnumMixin, StrEnum):
            nine = "9"

        self.assertEqual(GoodbyeEnum.nine, "9")
        self.assertEqual(GoodbyeEnum.nine, str(GoodbyeEnum.nine))
        #
        with self.assertRaisesRegex(TypeError, "1 is not a string"):

            class FirstFailedStrEnum(StrEnum):
                one = 1
                two = "2"

        with self.assertRaisesRegex(TypeError, "2 is not a string"):

            class SecondFailedStrEnum(StrEnum):
                one = "1"
                two = (2,)
                three = "3"

        with self.assertRaisesRegex(TypeError, "2 is not a string"):

            class ThirdFailedStrEnum(StrEnum):
                one = "1"
                two = 2

        with self.assertRaisesRegex(
            TypeError,
            "encoding must be a string, not %r" % (sys.getdefaultencoding,),
        ):

            class ThirdFailedStrEnum(StrEnum):
                one = "1"
                two = b"2", sys.getdefaultencoding

        with self.assertRaisesRegex(
            TypeError, "errors must be a string, not 9"
        ):

            class ThirdFailedStrEnum(StrEnum):
                one = "1"
                two = b"2", "ascii", 9


expected_help_output_with_docs = """\
Help on class Color in module %s:
class Color(enum.Enum)
 |  Color(value, names=None, *, module=None, qualname=None, type=None, start=1)
 |\x20\x20
 |  An enumeration.
 |\x20\x20
 |  Method resolution order:
 |      Color
 |      enum.Enum
 |      builtins.object
 |\x20\x20
 |  Data and other attributes defined here:
 |\x20\x20
 |  blue = <Color.blue: 3>
 |\x20\x20
 |  green = <Color.green: 2>
 |\x20\x20
 |  red = <Color.red: 1>
 |\x20\x20
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from enum.Enum:
 |\x20\x20
 |  name
 |      The name of the Enum member.
 |\x20\x20
 |  value
 |      The value of the Enum member.
 |\x20\x20
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from enum.EnumMeta:
 |\x20\x20
 |  __members__
 |      Returns a mapping of member name->value.
 |\x20\x20\x20\x20\x20\x20
 |      This mapping lists all enum members, including aliases. Note that this
 |      is a read-only view of the internal mapping."""

expected_help_output_without_docs = """\
Help on class Color in module %s:
class Color(enum.Enum)
 |  Color(value, names=None, *, module=None, qualname=None, type=None, start=1)
 |\x20\x20
 |  Method resolution order:
 |      Color
 |      enum.Enum
 |      builtins.object
 |\x20\x20
 |  Data and other attributes defined here:
 |\x20\x20
 |  blue = <Color.blue: 3>
 |\x20\x20
 |  green = <Color.green: 2>
 |\x20\x20
 |  red = <Color.red: 1>
 |\x20\x20
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from enum.Enum:
 |\x20\x20
 |  name
 |\x20\x20
 |  value
 |\x20\x20
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from enum.EnumMeta:
 |\x20\x20
 |  __members__"""


class TestStdLib(unittest.TestCase):

    maxDiff = None

    class Color(Enum):
        red = 1
        green = 2
        blue = 3

    def test_pydoc(self):
        # indirectly test __objclass__
        if StrEnum.__doc__ is None:
            expected_text = expected_help_output_without_docs % __name__
        else:
            expected_text = expected_help_output_with_docs % __name__
        output = StringIO()
        helper = pydoc.Helper(output=output)
        helper(self.Color)
        result = output.getvalue().strip()
        self.assertEqual(result, expected_text)


if __name__ == "__main__":
    unittest.main()
