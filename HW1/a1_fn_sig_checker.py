'''a1_fn_sig_checker.py

This program can be used to check whether your Assignment 1 Part A Python file
is using correct function names, parameter types, and return types.

Usage:
python3 a1_fn_sig_checker.py

Your file a1.py must be in the same folder as this checking program.

S. Tanimoto, Sept. 25, 2019.
'''

import a1

print("""-----------------------------------------------------------------------
Welcome to the function signature checker for Assignment 1.
Note: If your program printed anything above this message, then it is
NOT in compliance with the specifications.  All the functions you
define should RETURN values but SHOULD NOT PRINT ANYTHING.
-----------------------------------------------------------------------
""")

result1 = a1.five_x_cubed_plus_2(2)

import numbers
if not isinstance(result1, numbers.Number):
  print("WARNING: Your function three_x_cubed_plus_7 did not return a number:")
else:
  print("OK: Your function three_x_cubed_plus_7 returned a number:")

print(result1)

result2 = a1.triple_up([1, 2, 3, 4, 5, 'a', 'b', ['x', 'y'], ['z'], 'second from last', 'last'])

if not isinstance(result2, list):
  print("WARNING: Your function triple_up did not return a list:")
else:
  print("OK: Your function triple_up returned a list:")

print(result2)

result3 = a1.mystery_code("abcde")

if not isinstance(result3, str):
  print("WARNING: Your function mystery_code did not return a string:")
else:
  print("OK: Your function mystery_code returned a string:")

print(result3)

result4 = a1.future_tense(['He','did','it','. ','He', 'ate', 'all', 'the', 'cookies'])

if not isinstance(result4, list):
  print("WARNING: Your function future_tense did not return a list:")
else:
  print("OK: Your function future_tense returned a list:")

print(result4)

print("""-----------------------------------------------------------------------
This concludes this simple compliance test.  Passing this test DOES NOT
MEAN that your functions are correct. It simply helps you make sure
that they are named correctly, take the right numbers and types of
arguments, and they return the right type of values.
-----------------------------------------------------------------------
""")

