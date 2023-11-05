accountRequest={}
accountPassword={}

class student:
    id=""
    issueRequest={}
    returnRequest={}

    def logIn(self):
        print("\nWELCOME TO STUDENT MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        match userLogIn:
            case '1':
                self.id=password('S')
                self.studentFunctions()
            case '2':
                self.issuelist=[]
                self.returnlist=[]
                main()
            case _:
                print("Invalid Choice!")
                self.logIn()
            
    def studentFunctions(self):
        print("\nLOGGED IN SUCCESSFULLY")
        studentChoice=input("Enter 1: To Add Book Issue Request\nEnter 2: To Add Book Return Request\nEnter 3: To View Book Information\nEnter 4: To Log Out\nEnter your choice: ")
        match studentChoice:
            case '1':
                self.addIssueRequest()
            case '2':
                self.addReturnRequest()
            case '3':
                viewBookInfo()
                self.studentFunctions()
            case '4':
                print("LOGGED OUT SUCCESSFULLY")
                main()
            case _:
                print("Invalid Choice")
                self.studentFunctions()

    def addIssueRequest(self):
        print("\nWELCOME TO BOOK ISSUE PORTAL")
        recordpresent=False
        with open ("studentIssueRecord.txt","r") as file:
            data=file.readlines()
            for line in data:
                if(self.id in line):
                    recordpresent=True
                    if(' 5 ' in line):
                        print("ERROR: Cannot Make Issue Request: 5 books already issued")
                        self.studentFunctions()
                    else:
                        bookid=input("Enter the Book Reference ID: ")
                        bookpresent=False
                        with open ("bookInfo.txt") as file:
                            data=file.readlines()
                        for line in data:
                            if(bookid in line):
                                bookpresent=True
                                record=line.split("\t")
                                break
                        if(bookpresent):
                            if("Copies:0" in record):
                                print(f"ERROR: No copies of Book ID: {bookid} are currently available.")
                            else:
                                print("BOOK AVAILABLE")
                                issuelist=[]
                                if self.id in self.issueRequest:
                                    issuelist=self.issueRequest[self.id]
                                issuelist.append(bookid)
                                self.issueRequest[self.id]=issuelist
                                print("SUCCESSFUL QUERY: Request Added")
                        else:
                                print(f"ERROR: Book ID: {bookid} Not Found")
                                self.addIssueRequest()
                    break
            if(not recordpresent):
                print("ERROR: Student Issue Records Unavailable. Please contact the Admin")

        self.studentFunctions()

    def addReturnRequest(self):
        print("\nWELCOME TO BOOK RETURN PORTAL")
        with open("studentIssueRecord.txt","r") as file:
            data=file.readlines()
        for line in data:
            if(self.id in line):
                if(' 0 ' in line):
                    print("ERROR: Cannot Make Return Request: No current issues present in record")
                    self.studentFunctions()
                else:
                    bookid=input("Enter the Book Reference ID: ")
                    if(bookid+":Issued" not in line):
                        print(f"ERROR: Cannot Make Return Request: Book ID: {bookid} not found in record")
                        self.studentFunctions()
                    else:
                        returnlist=[]
                        if self.id in self.returnRequest:
                            returnlist=self.returnRequest[self.id]
                        returnlist.append(bookid)
                        self.returnRequest[self.id]=returnlist
                        print("SUCCESSFUL QUERY: Request Added")                   
                break
        self.studentFunctions()


class admin(student):

    def logIn(self):
        print("\nWELCOME TO ADMIN MODE")
        userLogIn=input("Enter 1: To Log-In to your account: \nEnter 2: To switch mode: \nEnter your choice: ")
        match userLogIn:
            case '1':
                password('A')
                self.adminFunctions()
            case '2':
                main()
            case _:
                print("Invalid Choice!")
                self.logIn()
        
    def adminFunctions(self):
        print("\nLOGGED IN SUCCESSFULLY")
        adminChoice=input("Enter 1: To View Issue/Return Requests\nEnter 2: To View Student Book Issue Records\nEnter 3: To View Student Library Information\nEnter 4: To View Book Information\nEnter 5: To Edit/Add Book Information\nEnter 6: To Add Admin Accounts\nEnter 7: To View and Approve New Student Account\nEnter 8: To Log Out\nEnter your choice: ")
        match adminChoice:
            case '1':
                self.Requests(student)
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
    
    def Requests(self,student):
        print("\nWELCOME TO ISSUE/RETURN APPROVAL PORTAL")
        noissues=False
        noreturns=False
        if(student.issueRequest=={}):
            print("No Issue Request")
            noissues=True
        else:
            print("ISSUE REQUESTS: \n",student.issueRequest)
        if(student.returnRequest=={}):
            print("No Return Request")
            noreturns=True
        else:
            print("RETURN REQUESTS: \n",student.returnRequest)
        if(noissues and noreturns):
            print("NO REQUESTS AVAILABLE. Redirection to Menu")
            self.adminFunctions()
        choice=input("Enter 1: To Approve Issue Request\nEnter 2: To Approve Return Request\nEnter 3: To Return to Menu\nEnter your choie: ")
        match choice:
            case '1':
                id=input("Enter the ID to Approve Request of: ")
                books=student.issueRequest[id]
                
                for bookid in books:
                    index=0
                    record=[]
                    with open ("studentIssueRecord.txt", "r+") as file:
                        data=file.readlines()
                        for line in data:
                            if(id in line):
                                record=line.split("\t")
                                break
                            index+=1
                        record[1]=str(int(record[1])+1)
                        record.append(bookid+":Issued")
                        data[index]="".join(str(r)+"\t" for r in record)
                        file.seek(0)
                        file.writelines(data)
                    
                    index=0
                    record=[]
                    with open ("bookInfo.txt","r+") as file:
                        data=file.readlines()
                        for line in data:
                            if(bookid in line):
                                record=line.split("\t")
                                break
                            index+=1
                        tag=record[2][:(record[2].index(":")+1)]
                        num=int(record[2][(record[2].index(":")+1):])-1
                        record[2]=tag+str(num)
                        data[index]="".join(str(r)+"\t" for r in record)
                        file.seek(0)
                        file.writelines(data)
                    print(bookid,": Approved")

                print("SUCCESSFUL QUERY: Issue Request Approved")
                del student.issueRequest[id]

            case '2':
                id=input("Enter the ID to Approve Request of: ")
                books=student.returnRequest[id]
                
                for bookid in books:
                    index=0
                    record=[]
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
                        data[index]="".join(str(r)+"\t" for r in record)
                        file.seek(0)
                        file.writelines(data)

                    index=0
                    record=[]
                    with open ("bookInfo.txt","r+") as file:
                        data=file.readlines()
                        for line in data:
                            if(bookid in line):
                                record=line.split("\t")
                                break
                            index+=1
                        tag=record[2][0:(record[2].index(":")+1)]
                        num=str(int(record[2][(record[2].index(":")+1):])+1)
                        record[2]=tag+num
                        data[index]="".join(str(r)+"\t" for r in record)
                        file.writelines(data)
                    print(bookid,": Approved")
                
                print("SUCCESSFUL QUERY: Return Request Approved")
                del student.returnRequest[id]
                    
            case '3':
                print("Redirecting...")
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

        print(f"PRN: {record[0]} \nNumber of Active Issues: {record[1]} \nBOOKS:")
        try:
            for r in record[2:]:
                    print(r)
        except IndexError:
            print("No Books In Issue Record History")

        if not present:
            print("ERROR: STUDENT RECORD DOES NOT EXIST")
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
            print("ERROR: STUDENT ACCOUNT DOES NOT EXIST")
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
                    print(f"ERROR: Book ID: {bookid} Not fount in record")
                    self.editBookInfo()
                else:
                    print("The Book Information is: ",record)
                    i=int(input("Enter Index to be Editted: "))
                    if(i>=len(record)):
                        print("ERROR: Invalid Index")
                        self.editBookInfo()

                    tag=record[i][:record[i].index(":")+1]
                    change=input("Enter New "+tag," ")
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
            print("No New Account Requests\nRedirecting to Previous Menu")
            self.adminFunctions()
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
                    print("SUCCESSFUL QUERY: Account Added")
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
    record=[]
    for line in data:
        if ref_id in line:
            record=line.split("\t")
            present=True
            break
    for r in record:
        print(r)
    if not present:
        print("ERROR: BOOK WITH THIS REFERENCE ID DOES NOT EXIST")
    
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
    mode=input("Enter 1: To Enter Admin Mode\nEnter 2: To Enter Student Mode\nEnter 3: To Create New Student Account\nEnter 4: To Exit\nEnter your choice: ")
    match mode:
        case '1':
            adminObj=admin()
            adminObj.logIn()
        case '2':
            studentObj=student()
            studentObj.logIn()
        case '3':
            newAccount()
        case '4':
            print("GoodBye")
            return
        case _:
            print("Invalid Mode")

main()