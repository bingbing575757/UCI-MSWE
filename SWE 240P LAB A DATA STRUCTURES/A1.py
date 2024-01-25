import math

class Account():
    # Initializes an account
    def __init__(self, name, address, socialAccount, initDeposit, next=None):
        self.name = name
        self.address = address
        self.socialAccount = socialAccount
        self.initDeposit = initDeposit
        # self.AccountID = Account.AccountID
        self.AccountID = 0
        # Account.AccountID += 1
        self.next = next
        self.deleted = False

    def desc(self):
        # Prints account information.
        print(self.AccountID, self.name, self.address, self.socialAccount, self.initDeposit)

class UserList():
    # Initializes a list of user accounts.
    def __init__(self):
        self.head = None
        self.length = 0

    def addUser(self, name, address, socialAccount, initDeposit):
        # Adds a new user to the list.
        if self.head == None:
            self.head = Account(name, address, socialAccount, initDeposit)
            self.length += 1
            print("Add User ： \n")
            self.head.desc()
        else:
            if (self.head):
                current = self.head
                while (current.next and current.deleted == False):
                    current = current.next

                if current.next == None:
                    current.next = Account(name, address, socialAccount, initDeposit)
                    current.next.AccountID = current.AccountID + 1
                    self.length += 1
                    current = current.next

                if current.deleted:
                    current.name = name
                    current.address = address
                    current.socialAccount = socialAccount
                    current.initDeposit = initDeposit
                    current.deleted = False
                print("Add User ： \n")
                current.desc()

    def deleteUserID(self, AccountID):
        # Deletes a user account by setting its 'deleted' flag to True.
        current = self.head
        while (current):
            if current.AccountID == AccountID:
                current.deleted = True
                print("Delete UserAccount")
            current = current.next

    def payUserToUser(self, payerID, payeeID, amount):
        # Transfers money from one user to another.
        current = self.head
        payer_found = False
        payee_found = False

        # Find payer and payee accounts
        while current:
            if current.AccountID == payerID:
                payer_found = True
            elif current.AccountID == payeeID:
                payee_found = True
            current = current.next

        # Check if payer and payee accounts exist
        if payer_found and payee_found:
            current = self.head
            while current:
                if current.AccountID == payerID:
                    if current.initDeposit >= amount:
                        current.initDeposit -= amount
                    else:
                        print("Insufficient balance. Transfer failed.")
                        return
                elif current.AccountID == payeeID:
                    current.initDeposit += amount
                current = current.next
            print("Transfer successful.")
        else:
            print("Invalid payer or payee ID. Transfer failed.")


    def getMedianID(self):
        # Finds the ID of the user in the middle of the list.
        current = self.head
        middlePoint = 0
        count = 0

        if self.length == 1:
            return current.AccountID
        elif self.length % 2 != 0:
            middlePoint = math.ceil(self.length / 2)
        elif self.length % 2 == 0:
            middlePoint = self.length / 2
        while (current):
            count += 1
            if count == int(middlePoint):
                return current.AccountID
            current = current.next

    def querybyID(self, ID):
        # Queries user information by ID.
        current = self.head
        while (current):
            if current.AccountID == ID:
                info = {
                    "Name": current.name,
                    "address": current.address,
                    "socialAccount": current.socialAccount,
                    "initDeposit": current.initDeposit
                }
                return info

            current = current.next

    def mergeAccounts(self, ID1, ID2):
        # Merges two user accounts if their essential info (name, address, social account) matches.
        info_1 = self.querybyID(ID1)
        info_2 = self.querybyID(ID2)
        keys_to_compare = ['Name', 'address', 'socialAccount']
        values_same = all(info_1[key] == info_2[key] for key in keys_to_compare if key in info_1 and key in info_2)
        if values_same:
            if ID1 > ID2:
                self.payUserToUser(ID1, ID2, info_1["initDeposit"])
                self.deleteUserID(ID1)
            elif ID1 < ID2:
                self.payUserToUser(ID2, ID1, info_2["initDeposit"])
                self.deleteUserID(ID2)
        else:
            print("The essential info of two account is not the same, unable to merge")

    def printList(self):
        # Prints the list of user accounts.
        current = self.head
        while current:
            if current.deleted == False:
                current.desc()
                current = current.next
            else:
                current = current.next

class BankOfSouthernCalifornia(UserList):
    def mergeBanks(self, bankOfOrangeCounty, bankOfLosAngeles):
        # Merges accounts from two banks into a new bank.
        current1 = bankOfOrangeCounty.head
        while current1 and current1.deleted == False:
            self.addUser(current1.name, current1.address, current1.socialAccount, current1.initDeposit)
            current1 = current1.next

        current2 = bankOfLosAngeles.head
        while current2 and current2.deleted == False:
            self.addUser(current2.name, current2.address, current2.socialAccount, current2.initDeposit)
            current2 = current2.next

# if __name__ == "__main__":
#     print("--MAIN--")
#     userlist = UserList()
#
#     # Add users
#     userlist.addUser("Alice", "123 Main St", "123-456-7890", 1000)
#     userlist.addUser("Bob", "456 Elm St", "234-567-8901", 1500)
#     userlist.addUser("LiuBingYao", "California", "04417463", 10000)
#     # userlist.addUser("LiuBingYao", "California", "04417463", 10000)
#     # userlist.deleteUserID(1)
#     userlist.addUser("Bob", "456 Elm St", "234-567-8901", 1500)
#     # Print user list
#     print("User List:")
#     userlist.printList()
#
#     #
#     # # Delete user
#     # userlist.deleteUserID(0)  # Assuming user ID is 0
#     # print("After deleting user with ID 0:")
#     # userlist.printList()
#
#     # Transfer money
#     userlist.payUserToUser(1,2,100000) # Transfer 200 from user ID 2 to user ID 1
#     print("After transferring 200 from user ID 2 to user ID 3:")
#     userlist.printList()
#     #
#     # # Find median user ID
#     # median_id = userlist.getMedianID()
#     # print("Median User ID:", median_id)
#     #
#     # Merge specific accounts
#     # userlist.addUser("David", "222 Maple St", "567-890-1234", 900)
#     # userlist.addUser("David", "222 Maple St", "567-890-1234", 900)
#     # print("Before merging specific accounts:")
#     # userlist.printList()
#     # userlist.mergeAccounts(2, 3)
#     # print("After merging specific accounts:")
#     # userlist.printList()
#     #
#     # Merge two banks into one bank
#     userlist2 = UserList()
#     userlist2.addUser("Charlie", "789 Oak St", "345-678-9012", 1200)
#     userlist2.addUser("Druis the III","New York","000178663",100000)
#     userlist2.addUser("BurgerKing","Moon","123456789",100000)
#     userlist2.addUser("Henry the VIII","England","987654321",10000000)
#     userlist3 = BankOfSouthernCalifornia()
#     userlist3.mergeBanks(userlist, userlist2)
#     print("Merged Bank:")
#     userlist3.printList()
    #
    #
    #
    #
    #

# no user/ negative amount  okkkk

if __name__ == "__main__":
    print("--MAIN--")
    userlist = UserList()

    # Add users
    userlist.addUser("Alice", "123 Main St", "123-456-7890", 1000)
    userlist.addUser("Bob", "456 Elm St", "234-567-8901", 1500)
    userlist.addUser("LiuBingYao", "California", "04417463", 10000)

    # Transfer money
    userlist.payUserToUser(1,2,100)
    print("After transferring 200 from user ID 1 to user ID 2:")
    userlist.printList()
    userlist.payUserToUser(1,2,100000)
    print("After transferring 200 from user ID 1 to user ID 2:")
    userlist.printList()
    userlist.payUserToUser(3,4,100000)
    print("After transferring 200 from user ID 3 to user ID 4:")
    userlist.printList()


