issueRequest={}
issuelist=[]
returnRequest={}
returnlist=[]
accountRequest={}
accountPassword={}
class student:
    id=""
    def logIn(self):
        print("\nWELCOME TO STUDENT MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        if(userLogIn=='1'):
            self.id=password('S')
            self.studentFunctions()
        elif(userLogIn=='2'):
            main()
        else:
            print("Invalid Choice!")
            self.logIn()
        
    def studentFunctions(self):
        print("\nLOGGED IN SUCCESSFULLY")
        studentChoice=input("Enter 1: To Add Book Issue Request\nEnter 2: To Add Book Return Request\nEnter 3: To View Book Information\nEnter 4: To Log Out\nEnter your choice:")
        match studentChoice:
            case '1':
                self.addIssueRequest()
            case '2':
                self.addReturnRequest()
            case '3':
                viewBookInfo()
                self.studentFunctions()
            case '4':
                main()
            case _:
                print("Invalid Choice")
                self.studentFunctions()
    def addIssueRequest(self):
        print("\nWELCOME TO BOOK ISSUE PORTAL")
        with open ("studentIssueRecord.txt","r") as file:
            data=file.readlines()
            for line in data:
                if(self.id in line):
                    if(' 5 ' in line):
                        print("Cannot Make Issue Request: 5 books already issued")
                        self.studentFunctions()
                    else:
                        bookid=input("Enter the Book Reference ID: ")
                        present=False
                        with open ("bookInfo.txt") as file:
                            data=file.readlines()
                            for line in data:
                                if(bookid in line):
                                    present=True
                                    record=line.split("\t")
                                    break
                            if(present):
                                if("Copies:0" in record):
                                    print("BOOK NOT AVAILABLE CURRENTLY")
                                else:
                                    print("BOOK AVAILABLE")
                                    issuelist.append(bookid)
                                    issueRequest[self.id]=issuelist
                                    print("Request Added")
                            else:
                                print("BOOK ID NOT FOUND")
                                self.addIssueRequest()
                    break
                else:
                    print("Error: Student Issue Records Unavailable")

        self.studentFunctions()

    def addReturnRequest(self):
        print("\nWELCOME TO BOOK RETURN PORTAL")
        with open("studentIssueRecord.txt","r") as file:
            data=file.readlines()
            for line in data:
                if(self.id in line):
                    if(' 0 ' in line):
                        print("Cannot Make Return Request: No current issues present to return")
                        self.studentFunctions()
                    else:
                        bookid=input("Enter the Book Reference ID: ")
                        if(bookid+":Issued" not in line):
                            print("Cannot Make Return Request: Book not Issued")
                            self.studentFunctions()
                        else:
                            returnRequest[self.id]=returnlist.append(bookid)
                            print(returnRequest)
                            print("Request Added")                        
                    break
        self.studentFunctions()

class admin:
    def logIn(self):
        print("\nWELCOME TO ADMIN MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        if(userLogIn=='1'):
            password('A')
            self.adminFunctions()
        elif(userLogIn=='2'):
            main()
        else:
            print("Invalid Choice!")
            self.logIn()
        
    def adminFunctions(self):
        print("\nLOGGED IN SUCCESSFULLY")
        adminChoice=input("Enter 1: To View Issue/Return Requests\nEnter 2: To View Student Book Issue Records\nEnter 3: To View Student Library Information\nEnter 4: To View Book Information\nEnter 5: To Edit/Add Book Information\nEnter 6: To Add Admin Accounts\nEnter 7: To View and Approve New Student Account\nEnter 8: To Log Out\nEnter your choice: ")
        match adminChoice:
            case '1':
                self.Requests()
            case '2':
                self.viewIssueRecord()
            case '3':
                self.viewStudentInfo()
            case '4':
                viewBookInfo()
                self.adminFunctions()
            case '5':
                self.editBookInfo()
            case '6':
                self.addAdminAccount()
            case '7':
                self.approveNewAccount()
            case '8':
                main()
            case _:
                print("Invalid Choice")
                self.adminFunctions()
    
    def Requests(self):
        print("\nWELCOME TO ISSUE/RETURN APPROVAL PORTAL")
        i=False
        r=False
        if(issueRequest=={}):
            print("No Issue Request")
            i=True
        else:
            print("ISSUE REQUESTS: \n",issueRequest)
        if(returnRequest=={}):
            print("No Return Request")
            r=True
        else:
            print("RETURN REQUESTS: \n",returnRequest)
        if(i and r):
            print("NO REQUESTS AVAILABLE. Redirection to Menu")
            self.adminFunctions()
        choice=input("Enter 1: To Approve A Request\nEnter 2: To Return to Menu\nEnter your choie: ")
        match choice:
            case '1':
                ch=input("Enter 1: To Approve Issue Request\nEnter 2: To Approve Return Request\nEnter your choice: ")
                match ch:
                    case '1':
                        id=input("Enter the ID to Approve Request of: ")
                        books=issueRequest[id]
                        index=0
                        for bookid in books:
                            with open ("studentIssueRecord.txt", "r+") as file:
                                data=file.readlines()
                                record=[]
                                for line in data:
                                    if(id in line):
                                        record=line.split("\t")
                                        print(record)
                                        break
                                    index+=1
                                record[1]=str(int(record[1])+1)
                                record.append(bookid+":Issued")
                                data[index]="".join(str(r)+"\t" for r in record)+"\n"
                                file.seek(0)
                                file.writelines(data)
                            
                            index=0
                            with open ("bookInfo.txt","r+") as file:
                                data=file.readlines()
                                record=[]
                                for line in data:
                                    if(bookid in line):
                                        record=line.split("\t")
                                        break
                                    index+=1
                                tag=record[2][:(record[2].index(":")+1)]
                                num=int(record[2][(record[2].index(":")+1):])
                                num-=1
                                record[2]=tag+num
                                data[index]="".join(str(r) for r in record)+"\n"
                                file.seek(0)
                                file.writelines(data)
                            print(bookid,": Approved")
                        del issueRequest[id]

                    case '2':
                        id=input("Enter the ID to Approve Request of: ")
                        books=returnRequest[id]
                        index=0
                        for bookid in books:
                            with open ("studentIssueRecord.txt", "r+") as file:
                                data=file.readlines()
                                for line in data:
                                    if(id in line):
                                        record=line.split("\t")
                                        break
                                    index+=1
                                record[1]=str(int(record[1])-1)
                                i=record.index(bookid+":Issued")
                                record[i]=bookid+":Returned"
                                data[index]="".join(str(r) for r in record)+"\n"
                                file.seek(0)
                                file.writelines(data)
                            index=0
                            with open ("bookInfo.txt","r+") as file:
                                data=file.readlines()
                                record=[]
                                for line in data:
                                    if(bookid in line):
                                        record=line.split("\t")
                                        break
                                    index+=1
                                tag=record[2][0:(record[2].index(":")+1)]
                                num=int(record[2][(record[2].index(":")+1):])
                                num+=1
                                record[2]=tag+num
                                data[index]="".join(str(r) for r in record)+"\n"
                                file.writelines(data)
                            print(bookid,": Approved")
                        
                        del returnRequest[id]
                    case _:
                        print("Invalid Choice")
            case '2':
                self.adminFunctions()
            case _:
                print("Invalid Choice")
                self.Requests()
        self.adminFunctions()
   
    #def pendingReturns():

    def viewIssueRecord(self):
        print("\nWELCOME TO STUDENT ISSUE RECORDS PORTAL")
        prn_no = input("Enter PRN NO. To View Issue Record:")
        with open("studentIssueRecord.txt", "r") as file:
            data = file.readlines()
            present=False
            for line in data:
                if prn_no in line:
                    record=line.split("\t")
                    present=True
                    break
            for r in record:
                print(r)
        if not present:
            print("STUDENT RECORD DOES NOT EXIST")
        self.adminFunctions()

    def viewStudentInfo(self):
        print("\nWELCOME TO STUDENT INFORMATION PORTAL")
        prn_no = input("Enter PRN NO. To View Student Info:")
        present=False
        with open("studentInfo.txt", "r") as file:
            data = file.readlines()
            for line in data:
                if prn_no in line:
                    record=line.split("\t")
                    present=True
                    break
            for r in record:
                print(r)
        if not present:
            print("STUDENT ACCOUNT DOES NOT EXIST")
        self.adminFunctions()

    def editBookInfo(self):
        print("\nWELCOME TO BOOK EDIT PORTAL")
        choice=input("Enter 1: To Add Book Info\nEnter 2: To Edit Book Info\nEnter Your Choice: ")
        match choice:
            case '1':
                name=input("Enter the Name of the Book: ").upper()
                bookid=input("Enter the Book Reference ID: ")
                copy=input("Enter No. of Copies of the Book: ")
                genre=input("Enter the Genre/Section of the Book: ").upper()
                record={"Name:":name,"BookID:":bookid,"Copies:":copy,"Section:":genre}
                with open ("bookInfo.txt","a") as file:
                    for r,q in record.items():
                        file.write(r+q+"\t")
                    file.write("\n")
                print("Book Information Added")
            case '2':
                bookid=input("Enter the Book Reference ID or Name: ").upper()
                present=False
                index=0
                with open ("bookInfo.txt", "r") as file:
                    data=file.readlines()
                    for line in data:
                        if(bookid in line):                            
                            present=True
                            record=line.split("\t")
                            break
                        index+=1
                if(not present):
                    print("BOOK ID INVALID")
                    self.editBookInfo()
                else:
                    print("The Book Information is: ",record)
                    i=int(input("Enter Index to be Editted: "))
                    tag=record[i]
                    colon=record[i].index(":")
                    tag=tag[:colon+1]
                    change=input("Enter New "+tag)
                    record[i]=tag+change
                    data[index]="".join(str(r+"\t") for r in record)+"\n"
                    with open ("bookInfo.txt","w") as file:
                        file.writelines(data)
        self.adminFunctions()

    def addAdminAccount(self):
        print("\nWELCOME TO ADD ADMIN ACCOUNT PORTAl")
        with open ("adminPasswords.txt","a") as file:
            admin_name=input("ENTER USERNAME:")
            password=input("ENTER PASSWORD:")
            file.write(admin_name+"\t"+password+"\n")
        print ("Account Added")
        self.adminFunctions()

    def approveNewAccount(self):
        print("\nWELCOME TO ADD NEW ACCOUNT PORTAL")
        if(accountRequest=={}):
            print("No New Account Requests")
        else:
            print("New Account Requests: ",accountRequest)
            ch=input("Enter 1: To Approve New Account\nEnter 2: To Return to Previous Menu\nEnter your choice: ")
            match ch:
                case '1':
                    id=input("Enter ID to be Approved: ")
                    with open ("/Users/pankh/Documents/Library-System/studentInfo.txt","a") as file:
                        for key,value in accountRequest[id].items():
                            file.write(key+value+"\t")
                        file.write("\n")
                    with open ("studentIssueRecord.txt","a")as file:
                        file.write(id+"\t0"+"\n")
                    with open ("studentPasswords.txt","a") as file:
                        file.write(accountPassword[id]+"\n")
                    del accountRequest[id]
                    del accountPassword[id]
                    print("Account Added")
                case '2':
                    self.adminFunctions()
                case _:
                    print("Invalid Choice")
                    self.approveNewAccount()
        self.adminFunctions()


def password(mode):
    if(mode=='A'):
        pfile="/Users/pankh/Documents/Library-System/adminPasswords.txt"
        id=input("Enter Your Username: ")
    else:
        pfile="studentPasswords.txt"
        id=input("Enter Your PRN: ")   

    pw=input("Enter Your Password: ")
    login=False;
    with open(pfile,"r") as file:
        data=file.readlines()
        for line in data:
            if((id in line) and (pw in line)):
                login=True
                break
    if(login):
        return id
    else:
        print("Incorrect Username or Password")
        ch=input("Enter 1: To Try Again\nEnter 2: To Exit\nEnter your choice: ")
        match ch:
            case '1':
                password(mode)
            case '2':
                main()
            case _:
                print("Invalid Choice! Restarting Password Confirmation")
                password(mode)


def viewBookInfo():
    print("\nWELCOME TO BOOK INFORMATION PORTAL")
    present=False
    ref_id=input("Enter the Book Reference ID or Name To View Book Info:").upper()
    with open ("bookInfo.txt","r") as file:
        data=file.readlines()
        for line in data:
            if ref_id in line:
                record=line.split("\t")
                present=True
                break
        for r in record:
            print(r)
    if not present:
        print("BOOK WITH THIS REFERENCE ID DOES NOT EXIST")
    
def newAccount():
    print("\nWELCOME TO NEW ACCOUNT")
    username=input("ENTER NAME: ").upper()
    prn_no=input("ENTER PRN NO.: ")
    email_id=input("ENTER STUDENT EMAIL ID: ")
    contact_info=input("CONTACT NUMBER: ")
    Class=input("ENTER CLASS: ").upper()
    batch=input("ENTER BATCH: ")
    password=input("ENTER PASSWORD: ")
    new_account={'Name:':username,"PRN:":prn_no,"Email ID:":email_id,"Contact No.:":contact_info,"Class:":Class,"Batch:":batch}
    new_password=prn_no+"\t"+password
    accountRequest[prn_no]=new_account
    accountPassword[prn_no]=new_password
    print("Note: REQUEST SENT TO ADMIN. You can access your account after approval from the admin\n")
    main()

def main():
    print("\nWELCOME TO THE LIBRARY" )
    mode=input("Enter 1: To Enter Admin Mode\nEnter 2: To Enter Student Mode\nEnter 3: To Create New Student Account\nEnter your choice: ")
    match mode:
        case '1':
            adminObj=admin()
            adminObj.logIn()
        case '2':
            studentObj=student()
            studentObj.logIn()
        case '3':
            newAccount()
        case _:
            print("Invalid Mode")

main()