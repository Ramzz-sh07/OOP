"""
🤖 THE SELF MYSTERY: WHO AM I?
==============================
CONCEPT: 'self' is the internal name for the SPECIFIC object currently running.
"""

class Robot:
    def __init__(self, name):
        """
        COMMAND: def __init__(self, name)
        WHAT: The constructor.
        APPLICATION: When 'Robot("Chappie")' is called, 'self' becomes that specific robot.
        """
        self.name = name
        
        # --- THE REVEAL ---
        print(f"\n[SYSTEM]: Creating Robot {self.name}...")
        print(f"📍 My internal 'self' memory address is: {id(self)}")

    def check_identity(self):
        """
        COMMAND: id(self)
        WHAT: Python's unique identification number for this object in your RAM.
        USE: To prove that two objects from the same class are NOT the same thing.
        """
        print(f"🤖 I am {self.name}. My 'self' address is still {id(self)}")

# --- EXECUTION ---

# 1. Create two separate objects
robot_a = Robot("Chappie")
robot_b = Robot("Wall-E")

# 2. Check their identities
print("\n--- IDENTITY CHECK ---")
robot_a.check_identity()
robot_b.check_identity()

# 3. The "Aha!" Moment
print(f"\n--- EXTERNAL CHECK ---")
print(f"External address of robot_a: {id(robot_a)}")
print(f"External address of robot_b: {id(robot_b)}")


"""🛠️ Application & Important Details

1. The "Isolated State" Rule:
In your MSc coursework, you might create a class for a Neural Network. If you create model_1 and model_2, they both use the same code, but their weights (the data) stay separate because their self addresses are different.

2. Important Detail: The First Argument
In Python, self must always be the first argument in your methods. Even if you don't use it, Python automatically passes the object's identity into that slot. If you forget self, your code will crash with a "positional argument" error.

3. Use Case: Large Scale Data Processing
When you provide consultancy for those Croydon businesses (like Teal Zeal), you might have a Business class. You can process 100 businesses in a loop, and self ensures that the SWOT analysis for Business A never gets saved into Business B's file."""
