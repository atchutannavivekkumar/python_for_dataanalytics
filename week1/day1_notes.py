# ============================================================
#  DAY 1 — Python Basics: Variables, Data Types, Type Conversion
#  Python for Data Analytics — Study Plan
# ============================================================

# ─────────────────────────────────────────────
# SECTION 1: VARIABLES
# ─────────────────────────────────────────────
# A variable is a named container that holds a value.
# Python is dynamically typed — no need to declare types.

name = "Alice"          # string
age = 28                # integer
salary = 75000.50       # float
is_analyst = True       # boolean

print(name)
print(age)
print(salary)
print(is_analyst)

# Multiple assignment
x = y = z = 0
print(x, y, z)          # 0 0 0

# Swap values (Python trick — no temp variable needed)
a, b = 10, 20
a, b = b, a
print(a, b)             # 20 10

# ─────────────────────────────────────────────
# SECTION 2: DATA TYPES
# ─────────────────────────────────────────────
# The 5 core types you'll use daily in data analytics:

# 1. int — whole numbers
employees = 150
print(type(employees))          # <class 'int'>

# 2. float — decimal numbers
revenue = 1_250_000.75          # underscore makes large numbers readable
print(type(revenue))            # <class 'float'>

# 3. str — text
city = "New York"
product = 'Laptop'
multi_line = """This is
a multi-line
string"""
print(type(city))               # <class 'str'>

# 4. bool — True or False (used heavily in filtering data)
has_discount = True
is_active = False
print(type(has_discount))       # <class 'bool'>

# 5. NoneType — represents missing/no value (like NULL in SQL)
customer_email = None
print(type(customer_email))     # <class 'NoneType'>
print(customer_email is None)   # True

# ─────────────────────────────────────────────
# SECTION 3: CHECKING TYPES
# ─────────────────────────────────────────────
# type()  — tells you what type something is
# isinstance() — checks if a value IS a certain type (preferred in real code)

print(type(100))                # <class 'int'>
print(type(3.14))               # <class 'float'>
print(type("hello"))            # <class 'str'>

print(isinstance(100, int))     # True
print(isinstance(3.14, float))  # True
print(isinstance("hi", str))    # True
print(isinstance(True, int))    # True  ← bool is a subtype of int in Python!

# ─────────────────────────────────────────────
# SECTION 4: TYPE CONVERSION (CASTING)
# ─────────────────────────────────────────────
# In data analytics, raw data often comes as strings — you convert them.

# str → int
age_str = "25"
age_int = int(age_str)
print(age_int + 5)              # 30

# str → float
price_str = "199.99"
price_float = float(price_str)
print(price_float * 2)          # 399.98

# int → float
units = 7
units_float = float(units)
print(units_float)              # 7.0

# float → int  ← truncates (does NOT round)
pi = 3.99
pi_int = int(pi)
print(pi_int)                   # 3  (not 4!)

# int/float → str  (needed when building messages)
score = 95
message = "Your score is: " + str(score)
print(message)

# bool conversion
print(int(True))    # 1
print(int(False))   # 0
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False  ← empty string is falsy
print(bool("Hi"))   # True   ← non-empty string is truthy

# ─────────────────────────────────────────────
# SECTION 5: STRINGS IN DEPTH
# ─────────────────────────────────────────────
# Strings are everywhere in data — column names, categories, text data.

first = "John"
last  = "Doe"

# Concatenation
full_name = first + " " + last
print(full_name)                # John Doe

# f-strings (modern, preferred way to format strings)
age = 30
intro = f"My name is {full_name} and I am {age} years old."
print(intro)

# f-strings with expressions
price = 49.9
tax = 0.1
print(f"Total: ${price * (1 + tax):.2f}")   # Total: $54.89

# Useful string methods
text = "  Hello, Data Analytics!  "
print(text.strip())             # remove whitespace
print(text.lower())             # hello, data analytics!
print(text.upper())             # HELLO, DATA ANALYTICS!
print(text.replace("Hello", "Welcome"))
print(text.split(","))          # ['  Hello', ' Data Analytics!  ']
print(len(text))                # length

# Checking content
email = "user@example.com"
print(email.startswith("user")) # True
print(email.endswith(".com"))   # True
print("@" in email)             # True

# ─────────────────────────────────────────────
# SECTION 6: ARITHMETIC OPERATORS
# ─────────────────────────────────────────────
a = 17
b = 5

print(a + b)    # 22   — addition
print(a - b)    # 12   — subtraction
print(a * b)    # 85   — multiplication
print(a / b)    # 3.4  — division (always returns float)
print(a // b)   # 3    — floor division (whole number)
print(a % b)    # 2    — modulo (remainder) ← used to check even/odd
print(a ** b)   # 1419857 — exponentiation (17 to the power 5)

# Practical: check even or odd
number = 42
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# ─────────────────────────────────────────────
# SECTION 7: COMPARISON & LOGICAL OPERATORS
# ─────────────────────────────────────────────
# These are the foundation of filtering data (WHERE clause equivalent)

x = 85

print(x > 80)          # True
print(x < 80)          # False
print(x >= 85)         # True
print(x <= 85)         # True
print(x == 85)         # True
print(x != 85)         # False

# Logical operators: and, or, not
age = 25
income = 60000
print(age > 18 and income > 50000)     # True — both must be true
print(age < 18 or income > 50000)      # True — at least one is true
print(not (age < 18))                  # True — reverses the boolean

# Real analytics use case: filter condition
score = 72
passed = score >= 60
print(f"Passed: {passed}")             # Passed: True

# ─────────────────────────────────────────────
# SECTION 8: INPUT & PRINT (useful for small scripts)
# ─────────────────────────────────────────────
# print() — output
print("Hello", "World", sep=" | ")     # Hello | World
print("Line 1", end=" ")
print("still same line")

# input() — user input (always returns a string, convert as needed)
# Uncomment below to try:
# user_age = int(input("Enter your age: "))
# print(f"In 10 years you will be {user_age + 10}")

# ─────────────────────────────────────────────
# KEY TAKEAWAYS
# ─────────────────────────────────────────────
# 1. Python has 5 key types: int, float, str, bool, NoneType
# 2. Use type() to check, isinstance() to validate
# 3. Type conversion: int(), float(), str(), bool()
# 4. Raw data always comes as strings — casting is critical
# 5. f-strings are the best way to format output
# 6. None represents missing values (like NULL in databases)
