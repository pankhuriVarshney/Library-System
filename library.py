def libraryRecord(name, bookName, bookID, dateOfIssue ):

def admin():
    print("WELCOME TO ADMIN MODE")
    userStatus=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
    if(userStatus=='1'):
        AdminLogIn()
    elif(userStatus=='2'):
        main()
    else:
        print("Invalid Choice!" )
    
    if(pass):
        print("Logged in SUCCESSFULLY")
        adminChoice=input("Enter 1: To View Student/Staff Issue Records\nEnter 2: To View Book Records\nEnter 3: To Edit/Add Book Information\nEnter 4: To Add/Edit Student Information\nEnter 5: To Add/Edit Staff Information\nEnter 6: To Add/Edit Admin Accounts\nEnter your choice: ")
        if(adminChoice=='1'):
            viewMode=input("Enter 1: To View Student Records\nEnter 2: To view Staff Records\nEnter your choice: ")
            if(viewMode=='1'):
                viewStudentRecord()
            elif(viewMode=='2'):
                viewStaffRecord()
            else:
                print("Invalid Choice!")
        elif(adminChoice=='2'):
            viewBookRecord()
        elif(adminChoice=='3'):
            bookRecord()
        elif(adminChoice=='4'):
            studentRecord()
        elif(adminChoice=='5'):
            staffRecord()
        elif(adminChoice=='6'):
            adminRecord()
        else:
            print("Invalid Choice!" )

def student():
    print("WELCOME TO STUDENT MODE")
    userStatus=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
    if(userStatus=='1'):
        StudentLogIn()
    elif(userStatus=='2'):
        main()
    else:
        print("Invalid Choice!" )
    
    if(pass):
        print("Logged in SUCCESSFULLY")
        studentChoice=input("Enter 1: To View Your Issue Record\nEnter 2: To Issue a Book")
    
def main():
    print("Welcome to the library: " )
    mode=input("Enter your Access Mode: (Student/Staff/Admin): ")
    if(mode=="Admin"):
        admin()
    elif(mode=="Student"):
        student()
    elif(mode=="Staff"):
        staff()
    else:
        print("Invalid Mode")
    