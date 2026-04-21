"""
🏢 EMPLOYEE OOP: LINE-BY-LINE MECHANICS
=======================================
Understanding exactly what happens in memory for every command.
"""

# 1. THE CLASS DEFINITION
class Employee:
    """
    COMMAND: class Employee:
    WHAT: Creates the blueprint. 
    APPLICATION: This tells Python, 'I am about to define a new type of data.'
    USE: Used to group related data (name/salary) and actions (raises) together.
    """

    # 2. THE CONSTRUCTOR (The Entry Point)
    def __init__(self, name, role, salary):
        """
        COMMAND: def __init__(self, name, role, salary):
        WHAT: The 'Arrival Gate' method.
        APPLICATION: Automatically runs when you create 'emp1' or 'emp2'.
        USE: Prepares the object by taking incoming 'cargo' (data).
        """
        
        self.name = name          
        """
        COMMAND: self.name = name
        WHAT: Assignment. Creates a permanent 'storage box' inside the object.
        APPLICATION: Saves the name provided during creation so it isn't lost.
        USE: Allows each employee to have their own unique identity.
        """

        self.role = role          
        """
        COMMAND: self.role = role
        WHAT: Assignment. Creates the 'role' attribute.
        APPLICATION: Maps the input string to the specific object.
        USE: Essential for categorizing employees (e.g., Data Scientist vs. Manager).
        """

        self.salary = salary      
        """
        COMMAND: self.salary = salary
        WHAT: Assignment. Creates the 'salary' attribute.
        APPLICATION: Stores the numerical value (int/float).
        USE: Allows us to perform math later (like adding a raise).
        """

    # 3. A METHOD (The Action)
    def display_info(self):
        """
        COMMAND: def display_info(self):
        WHAT: A Function inside a Class.
        APPLICATION: A 'read-only' action that looks at the internal data.
        USE: Used to report or print the current state of an employee.
        """
        print(f"Employee: {self.name} | Role: {self.role} | Salary: £{self.salary}")

    # 4. ANOTHER METHOD (The Logic)
    def give_raise(self, amount):
        """
        COMMAND: def give_raise(self, amount):
        WHAT: A 'write' action that modifies internal data.
        APPLICATION: Takes a new number and adds it to the existing salary.
        USE: Used to update data safely without manually changing variables.
        """
        self.salary += amount
        print(f"✨ {self.name} received a raise! New salary: £{self.salary}")


# --- USING THE CODE (The Execution) ---

# 5. CREATING THE OBJECT
emp1 = Employee("Alice", "Data Scientist", 50000)
"""
COMMAND: emp1 = Employee(...)
WHAT: Instantiation (Triggering the Constructor).
APPLICATION: Python 'jumps' to __init__ and builds 'emp1' in memory.
USE: This is how you turn your blueprint into a real 'item' you can use.
"""

# 6. RUNNING A METHOD
emp1.display_info()
"""
COMMAND: emp1.display_info()
WHAT: Method Call.
APPLICATION: Tells the 'emp1' object to look into its own boxes and print them.
USE: The primary way to interact with an object's data.
"""

# 7. UPDATING DATA
emp1.give_raise(5000)
"""
COMMAND: emp1.give_raise(5000)
WHAT: Passing an Argument to a Method.
APPLICATION: Sends '5000' into the 'amount' slot of the raise function.
USE: Updates the internal state of 'emp1' only (doesn't affect Alice).
"""

# 8. ADDING TEAMMATES
emp3 = Employee("Ramya", "Project Manager", 60000)
"""
COMMAND: emp3 = Employee(...)
WHAT: Creating a second unique object.
APPLICATION: Python creates a completely NEW set of boxes for Ramya.
USE: Shows how one class can manage hundreds of different people easily.
"""