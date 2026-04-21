class chatbook:
    # --- STATIC VARIABLE (Shared by all users) ---
    __user_id = 1

    def __init__(self):
        # 1. Assign unique ID and increment the global counter
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        
        # 2. Private attribute (The 'Locked Box')
        self.__name = "Default User"
        
        # 3. Instance attributes
        self.username = ''
        self.password = ''
        self.loggedin = False
        
        # 4. THE TRIGGER: This starts the program automatically!
        self.menu() 

    # --- STATIC METHODS (Class-level logic) ---
    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id = val

    # --- GETTER & SETTER (Accessing the Locked Box) ---
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value

    # --- THE ACTIONS (Methods) ---
    def menu(self):
        user_input = input("""
Welcome to Chatbook !! How would you like to proceed?
1. Press 1 to signup
2. Press 2 to signin
3. Press 3 to write a post
4. Press 4 to message a friend
5. Press any other key to exit
-> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("enter your email here -> ")
        pwd = input("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("✅ You have signed up successfully !!\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("❌ Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("🌟 You have signed in successfully !!")
                self.loggedin = True
            else:
                print("❌ Incorrect credentials..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            print(f"📝 Posted: {txt}")
        else:
            print("🛑 You need to signin first to post!")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg? -> ")
            print(f"📧 Message sent to {frnd}")
        else:
            print("🛑 You need to signin first to send messages!")
        self.menu()

# --- THE SPARK ---
# Creating 'user1' now triggers the __init__ which triggers the menu!
user1 = chatbook()