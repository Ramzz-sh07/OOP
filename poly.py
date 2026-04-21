"""
🎭 POLYMORPHISM: THE MANY-FACED METHODS
======================================
CONCEPT: Different classes using the same method name for different actions.
"""

import math

class Shape:
    """The Parent Interface"""
    def calculate_area(self):
        # This is a placeholder; children will provide the actual math
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        """Logic: Side * Side"""
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Logic: π * r²"""
        return math.pi * (self.radius ** 2)

# --- THE MAGIC OF POLYMORPHISM ---

# 1. Create a list of different shapes
shapes_list = [Square(10), Circle(5), Square(4)]

# 2. Iterate through them and call the SAME method name
print("📐 Calculating areas using Polymorphism:")
for item in shapes_list:
    # Python doesn't care if it's a Square or Circle; 
    # it just looks for the 'calculate_area' method.
    print(f"Area: {round(item.calculate_area(), 2)}")


    """Application & Important Details

1. The "Universal Remote" Analogy:
Imagine a universal remote with a "Power" button. It sends a signal to your TV, your Soundbar, and your Blu-ray player. Each device reacts differently (the TV turns on the screen, the Soundbar activates the speakers), but you only had to press one button. That is Polymorphism.

2. Important Detail: Overriding:
When a child class re-defines a method that already exists in the parent (like calculate_area), it is called Method Overriding. The child’s version "overwrites" the parent’s version for that specific object.

3. Use Case: MSc Data Science Models
In a real MLOps pipeline, you might test five different algorithms.

model_a.predict()

model_b.predict()

model_c.predict()
By using Polymorphism, you can write one evaluation script that loops through all your models and calls .predict() without needing five different if/else statements.

Final Study Note:

Inheritance is about sharing code.

Polymorphism is about changing behavior while keeping the name the same."""