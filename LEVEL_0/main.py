#3. Create an university enrollment system with the following characteristics:
#* 	(X)	The system has a login with a username and password.
#* 	(X)	Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
#* 	(X)	The user must input their first name, last name, and chosen program.
#* 	(X)	Each program has only 5 available slots. The system will store the data of each registered user, 
# and if it exceeds the limit, it should display a message indicating the program is unavailable.
#* 	(X)	If login information is incorrect three times, the system should be locked.
#* 	( )	The user must choose a campus from three cities: London, Manchester, Liverpool.
#* 	( )	In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool,
#       there is 1 slot per program. If the user selects a program at a campus that has no available slots,
#       the system should display the option to enroll in the program at another campus.
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

class enrollment():
    
    def __init__(self, username, password) -> None:
        
        self.username = username
        self.set_security_password(password)
        self.login_attempts = 0
        self.locked = False
    
    def set_security_password(self, password) -> None:
        
        self.password = pwd_context.hash(password)
        
    def verify_password(self, password) -> bool:
        
        if self.locked:
            print("Account is locked")
            return False
        
        if pwd_context.verify(password, self.password):
            self.login_attempts = 0
            return True
        
        else:
            self.login_attempts += 1 
            if self.login_attempts >= 3:
                self.locked = True
                print("Failed 3 times, Account Locked")
                return False
            
    #def enroll_user(self, programs, first_name, last_name, program, campus) -> bool:
    #    self.program = programs.get(program)
    #    
    #    if self.program is None:
    #        print("Invalid Program selected")
    #        return False
    #    
    #    self.campus = programs.get(campus)
    #    
    #    if self.campus is None:
    #        print("Invalid campus selected")
    #        return False
    #    
    #    #I THINK THIS IS WRONG, IT'S TOO LATE TO THINK ABOUT IT, GONNA CHANGE THIS TOMORROW 07/04
    #    if len(self.campus['enroll']) < self.campus['slots']:
    #        self.campus['enroll'].append(f"{first_name} {last_name}")
    #        print(f"Enrolled in {program} in {campus}")
    #        
    #
    # 
    # return True

def enroll_user(first_name, last_name, program_name, campus_name):
    if program_name not in programs:
        print("Invalid program selected")
        return False
    if campus_name not in programs[program_name]:
        print("Invalid campus selected")
        return False
    program_campus = programs[program_name][campus_name]
    
    if len(program_campus['enroll']) >= program_campus['slots']:
        print("No available slots, please select other campus")
        return 
    #
    # if len(program_campus['enroll']) < program_campus['slots']:
    program_campus['enroll'].append(f"{first_name} {last_name}")
    print(f"Enrolled in program: {program_name} in campus: {campus_name}")
    return True

def convert_program(program):
    program_mapping = {
        '1': 'Computer Science',
        '2': 'Medicine',
        '3': 'Marketing',
        '4': 'Arts'
    }
    return program_mapping.get(program, "Invalid Program")

def convert_campus(campus):
    campus_mapping = {
        '1' : 'London',
        '2' : 'Manchester',
        '3' : 'Liverpool'
    }
    return campus_mapping.get(campus, "Invalid Program")

accounts = {}
current_account = None

while True:
    
    
    programs = {
        'Computer Science': {'London': {'slots': 1,
                                        'enroll': []},
                             'Manchester': {'slots': 3,
                                            'enroll': []},
                             'Liverpool': {'slots': 3,
                                           'enroll': []}},
        'Medicine': {'London': {'slots': 1,
                                'enroll': []},
                    'Manchester': {'slots': 3,
                                    'enroll': []},
                    'Liverpool': {'slots': 3,
                                   'enroll': []}},
        'Marketing': {'London': {'slots': 1,
                                 'enroll': []},
                      'Manchester': {'slots': 3,
                                     'enroll': []},
                      'Liverpool': {'slots': 3,
                                    'enroll': []}},
        'Arts': {'London': {'slots': 1,
                            'enroll': []},
                 'Manchester': {'slots': 3,
                                'enroll': []},
                 'Liverpool': {'slots': 3,
                               'enroll': []}}
        }
        
    print("Please Enter your credencialts:")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in accounts:
        if accounts[username].verify_password(password):
            current_account = accounts[username]
            print("Login Succesfull")
    else:
        accounts[username] = enrollment(username, password)
        current_account = accounts[username]
    #Verify credentials
    
    print("++++++++++++++++++++++++++++++++++++")
    print("These are the available programs: ")
    print("1. Computer Science")
    print("2. Medicine0")
    print("3. Marketing")
    print("4. Arts")
    print("++++++++++++++++++++++++++++++++++++")    
    
    print("Please enter your first name, last name and choose the program u want: ")
    first_name = input("first name: ")
    last_name = input("last name: ")
    program = input("Program you want: ")
    program = convert_program(program)
    
    print("++++++++++++++++++++++++++++++++++++")
    print("There are three campus you can choice:")
    print("1. London")
    print("2. Manchester")
    print("3. Liverpool")
    print("++++++++++++++++++++++++++++++++++++")
    
    print("Please enter your choice")
    campus = input("Campus you want")
    campus = convert_campus(campus) 
    
    if current_account:
        enroll_user(first_name, last_name, program, campus)