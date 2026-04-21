"""
🌳 THE INHERITANCE TREE: DON'T REPEAT YOURSELF (DRY)
===================================================
CONCEPT: A 'Child' class borrows all attributes and methods from a 'Parent'.
"""

# --- 1. SINGLE INHERITANCE (Parent to Child) ---
class User:
    """The Parent: Everyone has a login."""
    def __init__(self, username):
        self.username = username
        print(f"👤 User '{self.username}' created in the system.")

    def login(self):
        print(f"🔑 {self.username} is now logged in.")

class Student(User): # Student borrows from User
    """The Child: Inherits login, but adds academic actions."""
    def submit_assignment(self, task):
        print(f"📝 {self.username} submitted: {task}")

# --- 2. MULTI-LEVEL INHERITANCE (Grandparent to Parent to Child) ---
class LeadStudent(Student): # LeadStudent borrows from Student AND User
    """The Grandchild: Inherits from Student (and therefore User too)."""
    def manage_team(self):
        print(f"📢 {self.username} is organizing the project documentation.")

# --- 3. MULTIPLE INHERITANCE (Two Parents to one Child) ---
class Consultant:
    """A separate Skill set."""
    def give_advice(self):
        print(f"💡 Providing strategic business analysis...")

class MScDataScientist(User, Consultant): # Inherits from TWO different classes
    """The Hybrid: Has User powers AND Consultant powers."""
    def run_model(self):
        print(f"📈 {self.username} is running an XAI MLOps model.")

# --- EXECUTION ---
print("--- TEST 1: Single Inheritance ---")
student1 = Student("Ruthwik")
student1.login()            # Borrowed from User
student1.submit_assignment("NLP Project")

print("\n--- TEST 2: Multi-Level Inheritance ---")
lead = LeadStudent("Priyanka")
lead.login()                # Borrowed from User
lead.submit_assignment("KPI Documentation") # Borrowed from Student
lead.manage_team()          # Own unique method

print("\n--- TEST 3: Multiple Inheritance ---")
pro = MScDataScientist("Ramya")
pro.login()                 # From User
pro.give_advice()           # From Consultant
pro.run_model()             # Own unique method


"""🛠️ Application & Important Details

1. The "DRY" Principle (Don't Repeat Yourself):
Imagine if you changed the login logic to require two-factor authentication. Because of inheritance, you only have to change it in the User class. Every student, teacher, and consultant is updated automatically!

2. Important Detail: The super() command:
If you want a child to have its own constructor but still use the parent's constructor, you use super().__init__(). This ensures the Parent's "Arrival Gate" logic still runs before the Child's logic starts.

3. Use Case: LSBU Academic System
In your consultancy work, you might model a business.

Parent: LocalBusiness (has name, address).

Child: VirtualAssistant (inherits from Business, adds "Booking Link").

Child: StylingAgency (inherits from Business, adds "Portfolio Gallery").

Study Notes for the Future:

Single: Simple Parent -> Child.

Multi-level: A chain of inheritance (Family Tree).

Multiple: Combining different "skill sets" into one class.

When you run python3 the_inheritance_tree.py, pay attention to how lead can use three different levels of code. It’s like inheriting a house, a car, and a bank account all at once!"""