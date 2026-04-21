"""
📖 CONCEPT: THE CONSTRUCTOR (__init__)
--------------------------------------
DEFINITION: 
A special method that runs automatically when an object is created.

PURPOSE:
1. To set up the initial data (attributes) for the object.
2. To make sure the object is 'ready to use' immediately.

APPLICATION:
Used in everything from Bank Accounts (setting balance) 
to Data Science models (setting parameters).
"""

class SmartPhone:
    # THE CONSTRUCTOR
    def __init__(self, brand, model, battery=100):
        # Assigning values to 'self' (the specific object)
        self.brand = brand
        self.model = model
        self.battery_level = battery
        
        print(f"✨ FACTORY: {self.brand} {self.model} is ready!")

    def check_status(self):
        print(f"📱 Device: {self.brand} {self.model}")
        print(f"🔋 Battery: {self.battery_level}%")
        print("-" * 20)


        """
🏗️ THE ANATOMY OF A CONSTRUCTOR (Line-by-Line Breakdown)
======================================================

1. THE DEFINITION: def __init__(self, brand, model, battery=100)
   - Think of this as the "ARRIVAL GATE." 
   - Every object MUST pass through here to be born.
   - 'self' ensures that Phone A's data doesn't leak into Phone B.
   - 'brand, model, battery' are the "INCOMING CARGO."

2. THE ASSIGNMENT: self.brand = brand
   - This is "ORGANIZING THE WAREHOUSE."
   - 'self.brand' is a permanent storage box inside the object.
   - '= brand' takes the cargo and locks it in that box.
   - Without this, the object would "forget" its data immediately!

3. THE TRIGGER: phone1 = SmartPhone("Apple", "iPhone 15")
   - This line makes Python "JUMP" automatically to the Arrival Gate.
   - It turns raw text into a fully functional object in one move.
"""

# --- EXECUTION ---

# Create objects (This triggers the __init__ above)
phone1 = SmartPhone("Apple", "iPhone 15")
phone2 = SmartPhone("Samsung", "Galaxy S24", 85)

print("\n--- STATUS REPORT ---")
phone1.check_status()
phone2.check_status()

"""
QUICK COMMANDS FOR TERMINAL:
1. Save file: Cmd + S
2. Run file: python3 const.py
"""