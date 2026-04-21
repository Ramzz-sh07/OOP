"""
📊 THE DATA TYPES MASTERCLASS
=============================
A guide for MSc Data Science students to understand the 'Building Blocks' of Python.
"""

# -------------------------------------------------------------------------
# 1. INTEGER (int) - Whole numbers
# -------------------------------------------------------------------------
"""
WHAT: Whole numbers without decimals.
USE: Counting items, loops, or IDs (e.g., number of employees).
WHERE: When you need absolute precision with no fractional parts.
"""
age = 25  # Defining
print(f"Integer Example: {age}") # Accessing



# -------------------------------------------------------------------------
# 2. FLOAT (float) - Decimal numbers
# -------------------------------------------------------------------------
"""
WHAT: Numbers with decimal points.
USE: Measurements, prices, or probabilities in Data Science.
WHERE: Used for scientific calculations where precision matters.
"""
price = 19.99 
print(f"Float Example: {price}")



# -------------------------------------------------------------------------
# 3. STRING (str) - Text
# -------------------------------------------------------------------------
"""
WHAT: A sequence of characters wrapped in quotes.
USE: Names, addresses, or NLP text data.
WHERE: Used whenever you are handling labels or human-readable info.
"""
name = "London South Bank University"
print(f"String Example: {name[0:6]}") # Accessing a slice



# -------------------------------------------------------------------------
# 4. LIST (list) - Ordered & Changeable
# -------------------------------------------------------------------------
"""
WHAT: A collection of items in a specific order.
USE: Storing a sequence of values (e.g., a list of project teammates).
WHERE: Use when you need to add, remove, or sort items frequently.
"""
teammates = ["Ramya", "Ruthwik", "Priyanka"] 
print(f"List Access (First person): {teammates[0]}") 



# -------------------------------------------------------------------------
# 5. TUPLE (tuple) - Ordered & UNCHANGEABLE (Immutable)
# -------------------------------------------------------------------------
"""
WHAT: Like a list, but you cannot change it once it's created.
USE: Fixed data like GPS coordinates (lat, long) or constants.
WHERE: Use when you want to protect data from being accidentally changed.
"""
coordinates = (51.5074, 0.1278) 
print(f"Tuple Access: {coordinates[1]}")



# -------------------------------------------------------------------------
# 6. DICTIONARY (dict) - Key-Value Pairs
# -------------------------------------------------------------------------
"""
WHAT: A map of 'Keys' to 'Values' (like a real dictionary).
USE: Representing structured data (e.g., an Employee record).
WHERE: Best for fast lookups based on a specific label.
"""
employee = {"id": 101, "role": "Data Scientist", "salary": 55000}
print(f"Dictionary Access (Role): {employee['role']}")



# -------------------------------------------------------------------------
# 7. BOOLEAN (bool) - Logic
# -------------------------------------------------------------------------
"""
WHAT: Only two values: True or False.
USE: Flags, switches, and conditional logic (if/else).
WHERE: Used for checking if a condition is met (e.g., is_available?).
"""
is_graduated = False
print(f"Boolean Check: {is_graduated}")



# -------------------------------------------------------------------------
# QUICK COMMANDS FOR DATA TYPES:
# 1. Check type: print(type(variable_name))
# 2. Convert: str(10) turns number into text "10"
# -------------------------------------------------------------------------


"""Why this is helpful for your MSc Data Science projects:

Lists vs. Tuples: You’ll use Lists for your dataset rows because you might clean or change them. You’ll use Tuples for your model's settings (hyperparameters) so they stay locked.

Dictionaries: These are the "MVP" of Data Science. When you work with JSON data from APIs (like the Weather ETL project you did), it almost always comes as a Dictionary.

Floats: Since you're working with XAI and MLOps, almost all your model accuracy scores will be Floats (e.g., 0.98 accuracy)."""