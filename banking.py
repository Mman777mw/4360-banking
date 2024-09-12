""" """

#Remind professor about GUI vs Command Line
class Account_Info:
	"""docstring for Account_Info"""
	def __init__(self, userName, password, currentBalance, accountNum, firstName, lastName):

		self.userName = userName
		self.password = password
		self.currentBalance = currentBalance
		self.accountNum = accountNum
		self.firstName = firstName
		self.lastName = lastName
	
	def fullName(self):
		return f"{self.firstName} {self.lastName}"

user1 = Account_Info("Mman777mw", "M@Corp@Est2010", "4500000", "29696", "Michael", "Wright")
user2 = Account_Info("Mant1s01", "L3tM3@in", "5500000", "62496", "Michaelle", "Wright")
user3 = Account_Info("Meta01", "SerDesSCMCM-01", "750000", "626601", "Isaac", "MC")
user4 = Account_Info("Meta04", "100Pr@@f7&62", "200000", "626604", "Amish", "MC")

userList = [user1, user2, user3, user4]
def userLogin():
	currentAttempts = 0
	print("Welcome to the M-Corporation Banking system. Please Log In.")

	while currentAttempts < 3 :
		userEntry = input("Username: ")
		passEntry = input("Password: ")

		for user in userList:
			if user.userName == userEntry and user.password == passEntry :
				if user.userName == "Mman777mw":
				   print(f"Welcome, Commander {user.firstName}. How may we assist you today?")
				else:
					print(f"Login successful. Welcome, {user.fullName}.")

				return user
			else:
				print("Error: Invalid username or password. Please try again.")

		currentAttempts += 1
		
	print("Extraneous logins detecting. Security closure engaged.")
	return None

def amountVerify(amountEnt):
	amVerLoop = True
	while amVerLoop:
		confirmAm = input(f"You have entered {amountEnt} is this correct?\nPlease enter Yes or No").strip().lower()
		if confirmAm in ["yes", "y"]:
		    return amountEnt
		elif confirmAm in ["no", "n"]:
			newAmount = input("Please enter the correct amount: ")

		

def main():
	currentUser = userLogin()
	currentOps = 0
	if currentUser:
		while currentOps < 3:
			print(f"\nYour current balance is {currentUser.currentBalance} M-Corp. Credits.\nWhat would you like to do today?")
			opSelect = input(f"Your current options are Deposit, Withdraw, Transfer, and  Exit\n").strip().lower()

			if opSelect == "deposit":
			elif opSelect == "withdraw":

			elif opSelect == "transfer":

			elif opSelect == "exit":
				print("Logout successful. Have a nice day.")
				break

			else:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()