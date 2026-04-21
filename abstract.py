"""
🏦 ABSTRACTION: THE BLACK BOX PRINCIPLE
======================================
CONCEPT: Hiding complex internal logic and showing only necessary features.
"""

class BankTransfer:
    def __init__(self, sender, balance):
        self.sender = sender
        self.__balance = balance  # Private: Hidden from accidental change
        self.__security_token = "LSBU-2026-X"

    # --- THE INTERNAL "ENGINE" (Hidden from User) ---

    def __check_token(self, token):
        """Internal check: Is the security key valid?"""
        return token == self.__security_token

    def __verify_balance(self, amount):
        """Internal check: Do we have enough money?"""
        return self.__balance >= amount

    def __recipient_active(self, recipient):
        """Internal check: Is the other person's account open?"""
        # In a real app, this would check a database
        active_users = ["Ramya", "Ruthwik", "Kathy"]
        return recipient in active_users

    # --- THE "KEY" (The Simple Button for the User) ---

    def send_money(self, amount, recipient, token):
        """
        COMMAND: .send_money()
        WHAT: The only method the user needs to interact with.
        APPLICATION: It triggers all the hidden 'engine' checks automatically.
        """
        print(f"\n🚀 Initiating transfer of £{amount} to {recipient}...")

        # The user just calls ONE function, but 3 hidden things happen:
        if not self.__check_token(token):
            print("❌ Access Denied: Invalid Security Token.")
        elif not self.__verify_balance(amount):
            print("❌ Transfer Failed: Insufficient Funds.")
        elif not self.__recipient_active(recipient):
            print(f"❌ Transfer Failed: {recipient} is not an active recipient.")
        else:
            self.__balance -= amount
            print(f"✅ Success! £{amount} sent to {recipient}.")
            print(f"💰 Remaining Balance: £{self.__balance}")

# --- EXECUTION (The User Experience) ---

my_account = BankTransfer("Priyanka", 1000)

# The user doesn't need to know HOW the balance is verified or HOW tokens work.
# They just turn the key:
my_account.send_money(250, "Ramya", "LSBU-2026-X")

# Try a failed one (Wrong Token)
my_account.send_money(100, "Ruthwik", "WRONG-KEY")


"""🛠️ Application & Important Details

1. The "ATM" Analogy:
When you use an ATM, you press "Withdraw £20." You don't see the ATM communicating with the central server, verifying your chip, checking the cash tray, and updating the ledger. You only see the cash. That is Abstraction.

2. Important Detail: Code Maintenance:
Because the engine is hidden, you can change how you verify the balance (maybe move it from a local list to a cloud database) without ever changing the send_money command. The user's experience stays exactly the same.

3. Use Case: MLOps Pipelines
In your aerospace MLOps dissertation, you might have a class FlightModel. The user calls .predict(sensor_data). Inside that method, you are:

Normalizing data.

Checking for NaN values.

Running the XAI explainer.
The user doesn't need to see those 3 steps; they just want the prediction.

Study Note for the Future:

Encapsulation was about protecting the data (putting it in a box).

Abstraction is about simplifying the view (hiding the complexity of the box).

When you run python3 abstraction_bank.py, notice how clean the execution part looks compared to the logic inside the class."""