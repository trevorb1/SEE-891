'''Module holding tests for example package.'''

from example_package.example import add_one
from example_package.example import add_five


def test_add_one():
  assert add_one(8) == 9

def test_add_five():
  assert add_five(-10) == -5
