# lines that start with '#' are a comment
# multiple line comments start and end with three double quotes

"""
multiline comment
"""

# in PyCharm, right click and select run 'programming_101' to execute
import random

print('Hello, world!')

# -----------------
#  PRIMITIVE DATA TYPES
# -----------------
"""
  str - string
  'hello world'

  PRACTICE: Print a string to the console
"""
print('Jason')
"""
  bool - boolean
  True/False

  PRACTICE: Print a boolean value to the console
"""
print(5 > 6)
print(5 < 6)
"""
  int - integer
  0

  PRACTICE: Print a int to the console
"""
print(1)
print(-1)
"""
  float - decimal
  0.0

  PRACTICE: Print a float to the console
"""

# -----------------
# COMPLEX DATA TYPES
# -----------------
print(1.8567)
"""
  list
  [], ['word']

  PRACTICE: Create a list that contains the names of three people
"""
brothers = ["Jason", "Justin", "Josh"]
print(brothers)
"""
  dict
  {}, {'key': 'value'}

  PRACTICE: Create a dictionary that is name as a key and gender as the value
"""
cards = {
    'A': ['spades', 'clubs', 'hearts', 'dimonds'],
    'K': ['spades', 'clubs', 'hearts', 'dimonds'],
    'Q': ['spades', 'clubs', 'hearts', 'dimonds'],
    'J': ['spades', 'clubs', 'hearts', 'dimonds'],
    '10': ['spades', 'clubs', 'hearts', 'dimonds'],

}
face_values = list(cards.keys())
face_value = face_values[random.randint(0, 4)]
card = cards[face_value][random.randint(0, 3)]
print(face_value + ' ' + card)
# for _ in range (20):
#     print(random.randint(0,4))

# -----------------
# CASTING
# -----------------
"""
  data types can be forced from one type to another under certain conditions
    str()
    bool()
    float()
    int()

  PRACTICE: 1. Add the string of '1' to the int of 1 to output the string '11'
            2. Add the int of 1 to the string of '1' to output the int 2
            3. Cast an empty string value to a boolean to output False
            4. Cast any non-empty string value to a boolean to output True
            5. Cast the result of 3/2 to a float values to produce an output of 1.5
"""
# -----------------
# SCOPE
# -----------------
# white space in Python defines scope
#     block of code associated with a control structure

# -----------------
# CONTROL STRUCTURES
# -----------------
"""
-- variable assignment --
  =
  my_variable = 'value'

  PRACTICE: Create a variable with a name of your choosing that contains the value 'hello'
"""


# --comparisons--
# ==     -> equals
# !=     -> not equals
# >      -> greater than
# >=     -> greater than equal
# <      -> less than
# <=     -> les than equal

"""
-- logical --
  if <bool>:
    <statement>
  elif <bool>:
    <statement>
  else <bool>:
    <statement>

  PRACTICE: Write an if check to see if a value is equal to 'hello world', 
                if true print 'hello', else print 'bye'
"""


"""
--for loops--
for {variable_name} in <collection>:
    <statement>

  PRACTICE: print each letter in a given string
"""


"""
Functions

def <name>([input [, ...]]):
   <statement>

  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""

"""
  PRACTICE: create a function that takes two inputs,
  then prints True/False whether or not the first input
  is contained within the second input
"""

# print(search_string('a', text_value))  # False
# print(search_string('s', text_value))  # True
# print(search_string('S', text_value))  # False


"""
  PRACTICE: Create a diction that contains a list of 
  employee titles stored by the name, then print each record 
  such that each employee name and title is printed on a line
"""

"""
-- exception handling --
  try <expression>:
    <statement>
  except [error_type]:
    <handle error>

  PRACTICE: In a try block, divide 1 by 0, except a ZeroDivisionError and print 'zero divison error' 
"""

"""
-- while loops --
  while <bool>:
    <statement>

  PRACTICE: Write a while loop that starts at 5 and prints each number to 10
"""
