"""
📈 ML PIPELINE DESIGN: THE DATA CLEANER
=======================================
CONCEPT: Building a reusable toolkit for Data Science tasks.
APPLICATION: This mimics how professional libraries like scikit-learn are built.
"""

class DataCleaner:
    def __init__(self, filename):
        """
        COMMAND: __init__(self, filename)
        WHAT: The Constructor.
        LOGIC: Sets up the 'Warehouse' by taking the path to your data.
        """
        self.filename = filename
        self.is_cleaned = False
        print(f"📂 Pipeline Initialized for: {self.filename}")

    def remove_duplicates(self):
        """
        COMMAND: .remove_duplicates()
        WHAT: Data Pre-processing Method.
        LOGIC: Operates on the internal state of the data to ensure quality.
        """
        print(f"🧹 Scrubbing duplicates from {self.filename}...")
        # (In a real scenario, you'd use self.df.drop_duplicates() here)
        print("✅ Duplicates removed.")

    def scale_features(self):
        """
        COMMAND: .scale_features()
        WHAT: Feature Engineering Method.
        LOGIC: Normalizes numbers (e.g., 0 to 1) so the ML model isn't biased.
        """
        print(f"⚖️ Scaling features for machine learning readiness...")
        self.is_cleaned = True
        print("✅ Features scaled successfully.")

    def get_status(self):
        """
        COMMAND: .get_status()
        WHAT: State Reporter.
        APPLICATION: Tells the MLOps engineer if the data is ready for the model.
        """
        if self.is_cleaned:
            return "🚀 DATA READY FOR MODEL TRAINING"
        else:
            return "⚠️ DATA STILL MESSY - DO NOT TRAIN"

# --- EXECUTION (The MLOps Workflow) ---

# 1. Setup the pipeline for a specific dataset
housing_data = DataCleaner("london_housing_2026.csv")

# 2. Run the cleaning steps
housing_data.remove_duplicates()
housing_data.scale_features()

# 3. Check if we are ready to move to the next stage of the pipeline
print(f"\nPipeline Status: {housing_data.get_status()}")

# --- STUDY NOTES (Fixed the Quotes here) ---
"""
STUDY GUIDE:

1. self.is_cleaned (State Variable)
   - WHAT: A "Status Flag" stored in the object's memory.
   - LOGIC: Safety gate to track whether "Scrubbing" has happened.
   - APPLICATION: Prevents training on dirty data.

2. remove_duplicates() (Action Method)
   - WHAT: A transformation step in the pipeline.
   - LOGIC: Fixes redundant data without rewriting logic every time.
   - APPLICATION: Standardizes processing for all your consultancy clients.

3. get_status() (Validation Method)
   - WHAT: The "Inspector."
   - LOGIC: In MLOps, this is Data Validation.
   - APPLICATION: Essential for performance measurement and "Go/No-Go" signals.

4. Modularity
   - WHY: You can add new methods (like handle_missing_values) without breaking the old ones.
"""