# lines that start with '#' are a comment
# multiple line comments start and end with three double quotes

"""
multiline comment
"""

# in PyCharm, right click and select run 'programming_101' to execute

print('Hello, world!')

# -----------------
#  PRIMITIVE DATA TYPES
# -----------------
"""
  str - string
  'hello world'

  PRACTICE: Print a string to the console
"""
print('hello world')

"""
  bool - boolean
  True/False

  PRACTICE: Print a boolean value to the console
"""
print(1 < 0)

"""
  int - integer
  0

  PRACTICE: Print a int to the console
"""
print(1)

"""
  float - decimal
  0.0

  PRACTICE: Print a float to the console
"""
print(1.5)

# -----------------
# COMPLEX DATA TYPES
# -----------------

"""
  list
  [], ['word']

  PRACTICE: Create a list that contains the names of three people
"""
names = ['Jason', 'Justin', 'Josh']
print('!!!!!')
print(names)

"""
  dict
  {}, {'key': 'value}

  PRACTICE: Create a dictionary that is name as a key and gender as the value
"""
sex = {
    'Jason': 'Male',
    'Josh': 'Male'
}
print(sex)

print('======= CASTING')
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
print('1' + str(1))
print(1 + int('1'))
print(bool(''))
print(bool(' '))  # 4
print('CAST INT TO FLOAT =====')

print(float(3) / 2)

# -----------------
# SCOPE
# -----------------
# white space in Python defines scope
#     block of code associated with a control structure

# -----------------
print('CONTROL STRUCTURES')
# -----------------
"""
-- variable assignment --
  =
  my_variable = 'value'

  PRACTICE: Create a variable with a name of your choosing that contains the value 'hello'
"""

# --comparisons--
#  ==       -> equals
#  !=       -> not equals
#   >       -> greater than
#  >=       -> greater than equal
#   <       -> less than
#  <=       -> les than equal


"""
-- logical --
  if <bool>:
      <statement>
  elif <bool>:  # 'else if'
      <statement>
  else:
      <statement>

  PRACTICE: Write an if check to see if a value is equal to 'hello world', 
                if true print 'hello', else print 'bye'
"""
greeting = 'Josh'

if greeting == 'hello world':
    print('hello')
elif greeting == 'britney spears':
    print('hit me one more time')
elif greeting == 'jason':
    print('old man')
elif greeting == 'josh':
    print('asshole didnt come visit on his way to wooster')
else:
    print('bye')

print('')

"""
-- exception handling --
  try <expression>:
    <statement>
  except [error_type]:
    <handle error>

  PRACTICE: In a try block, divide 1 by 0, except a ZeroDivisionError and print 'zero divison error' 
"""
print('start exception handler')
try:
    1 / 0
    # 1 / 1
except ZeroDivisionError:
    print('not possible')
except Exception:
    print('hit this exception')
else:
    print('divided successfully')

"""
-- while loops --
  while <bool>:
    <statement>

  PRACTICE: print the value of count while count > 0, decrement count each iteration
"""
count = 5

while count > 0:
    print(count)
    count = count - 1

# --for loops--
# for {variable_name} in <collection>:
#     <statement>

print('for loop')
number_list = [1, 2, 3, 4, 5]

for number in number_list:
    print(number)

"""
  PRACTICE: print each letter in a given string
"""
alphabet = "abcdefg"
# _alphabet = ['a', 'b', 'c', 'e', 'f', 'g']

for character in alphabet:
    print(character)

print('$$$$$$$$$$$$$')

"""
  PRACTICE: create a function that takes an input,
  then prints each character of the input
"""

print('')


def print_characters(input_str):
    print('starting to print each letter in: ' + input_str)

    for letter in input_str:
        print(letter)

    print('done printing each letter in: ' + input_str)
    print('')


print_characters('blue')
print_characters('red')
print_characters('green')

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
