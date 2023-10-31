studentInfo={}
class student:
    id
    def logIn(self):
        print("WELCOME TO STUDENT MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        if(userLogIn=='1'):
            self.id=password('S')
        elif(userLogIn=='2'):
            main()
        else:
            print("Invalid Choice!")
            self.logIn()
        
    def studentFunctions(self):
        print("LOGGED IN SUCCESSFULLY")
        studentChoice=input("Enter 1: To Add Book Issue Request\nEnter 2: To Add Book Return Request\nEnter 3: To View Book Information\nEnter your choice:")
        match studentChoice:
            case '1':
                self.addIssueRequest()
            case '2':
                self.addReturnRequest()
            case '3':
                viewBookInfo()
            case _:
                print("Invalid Choice")
                self.studentFunctions()
    def addIssueRequest():
        print("WELCOME TO BOOK ISSUE PORTAL")
        with open ("studentIssueRecord.txt","r") as file:
            data=file.readlines()
            for line in data:
                record=line.split()
                if(id==record[0]):
                    if("Late" in )

    def addReturnRequest():

class admin(student):
    studentObj=student()
    def logIn(self):
        print("WELCOME TO ADMIN MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        if(userLogIn=='1'):
            password('A')
        elif(userLogIn=='2'):
            main()
        else:
            print("Invalid Choice!")
            self.logIn()
        
    def adminFunctions(self):
        print("LOGGED IN SUCCESSFULLY")
        adminChoice=input("Enter 1: To View Issue/Return Requests\nEnter 2: To View Late Returns\nEnter 3: To View Student Book Issue Records\nEnter 4: To View Student Library Information\nEnter 5: To View Book Information\nEnter 6: To Edit/Add Book Information\nEnter 7: To Add Admin Accounts\nEnter 8: To View and Approve New Student Account\nEnter your choice: ")
        match adminChoice:
            case '1':
                self.issueRequests()
            case '2':
                self.pendingReturns()
            case '3':
                self.viewIssueRecord()
            case '4':
                self.viewStudentInfo()
            case '5':
                viewBookInfo()
            case '6':
                self.editBookInfo()
            case '7':
                self.addAdminAccount()
            case '8':
                self.approveNewAccount()()
            case _:
                print("Invalid Choice")
                self.adminFunctions()
    
    def issueRequests():

    def pendingReturns():

    def viewIssueRecord():

    def viewStudentInfo():

    def editBookInfo():

    def addAdminAccount():
    
    def approveNewAccount():

def password(mode):
    if(mode=='A'):
        pfile="adminPasswords.txt"
        id=input("Enter Your Username: ")
    else:
        pfile="studentPasswords.txt"
        id=input("Enter Your PRN: ")   
    pw=input("Enter Your Password: ")
    login=False;
    with open(pfile,"r") as file:
        data=file.readlines()
        for line in data:
            if(line==(id+" "+pw)):
                login=True
                break
    if(login):
        return id
    else:
        print("Incorrect Username or Password")
        while():    
            ch=input("Enter 1: To Try Again\nEnter 2: To Return to Main Menu")
            if(ch=='1'):
                password(mode)
                break
            elif(ch=='2'):
                main()
                break
            else:
                print("INVALID CHOICE")



def viewBookInfo():

def newAccount():

def main():
    print("Welcome to the library: " )
    mode=input("Enter 1: To Enter Admin Mode\nEnter 2: To Enter Student Mode\nEnter 3: To Create New Student Account\nEnter your choice:")
    match mode:
        case '1':
            adminObj=admin()
        case '2':
            studentObj=student()
        case '3':
            newAccount()
        case _:
            print("Invalid Mode")