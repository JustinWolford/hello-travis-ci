import pytest
import unittest.mock as mock
import builtins
import fizzbuzz

def mockInput(x,y):
	print(x)
	return y
def test_fizzbuzz():
	with mock.patch.object(builtins, "input", lambda x: mockInput(x, 15)):
		fizzbuzz.fizzBuzz();
	assert 1==0;