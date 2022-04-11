'''Module holding tests for example package.'''

from example_package import example


def test_add_one():
  assert example.add_one(8) == 9

def test_add_five():
  assert example.add_five(-10) == -5
