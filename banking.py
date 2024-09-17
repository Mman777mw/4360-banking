""" """

#Remind professor about GUI vs Command Line
class Account_Info:
	"""docstring for Account_Info"""
	def __init__(self, userName, password, currentBalance, accountNum, firstName, lastName):

		self.userName = userName
		self.password = password
		self.currentBalance = float(currentBalance)
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
			while True:
				newAmount = input("Please enter the correct amount: ").strip()
				try:
					amountEnt = float(newAmount)
					break
				except ValueError:
					print("Invalid amount. Please enter an integer.")
		else:
			print(f"Invalid response.\nPlease enter Yes or No.")

def negBalChecker(account, amount):
	while account.currentBalance - amount < 0:
		print(f"Error, current amount will result in negative balance.")
		amount = float(input("Please enter a new amount: "))

	return amount

def withdrawFunct(account):
	startingBal = account.currentBalance
	amount = float(input("Please enter the amount you would like to withdraw: "))
	amount = amountVerify(amount)
	amount = negBalChecker(account, amount)
	account.currentBalance -= amount
	print(f"Your starting balance is {startingBal} and the ending balance is now {account.currentBalance} M-Corp. Credits.")

	
def transFunct(curAccount, toAccount):
	startingBalance = curAccount.currentBalance
	amount = float(input(f"Please enter amount for transfer: "))
	amount = amountVerify(amount)
	amount = negBalChecker(curAccount, amount)
	print(f"Transfer processing...")
	curAccount.currentBalance -= amount
	toAccount.currentBalance += amount
	print(f"Transfer has been completed.\n{amount} M-Corp. Credits have been transfered to {toAccount.accountNum}.\nYour ending balance is {curAccount.currentBalance}.")


def main():
	currentUser = userLogin()
	currentOps = 0
	credAmount = 0
	startingBal = 0
	
	if currentUser:
		while currentOps < 3:
			print(f"\nYour current balance is {currentUser.currentBalance} M-Corp. Credits.\nWhat would you like to do today?")
			opSelect = input(f"Your current options are Deposit, Withdraw, Transfer, and  Exit\n").strip().lower()

			if opSelect == "deposit":
				credAmount = input("Please enter the amount you would like to deposit:\n")
				credAmount = amountVerify(credAmount)
				startingBal = currentUser.currentBalance
				currentUser.currentBalance += credAmount
				print(f"Your starting balance is {startingBal} and the ending balance is now {currentUser.currentBalance} M-Corp. Credits.")
				
				currentOps += 1
			elif opSelect == "withdraw":
				withdrawFunct(currentUser)

				currentOps += 1

			elif opSelect == "transfer":
				targetAccountNum = input("Please enter the account you'd like to transfer funds to: ")
				recAccount = None
				for accountNums in userList:
					if accountNums.accountNum == targetAccountNum:
						recAccount = accountNums
						break

				if recAccount:
					transFunct(currentUser, recAccount)

					currentOps += 1
				else:
					print("Error: Target account not found.")
			elif opSelect == "exit":
				print("Logout successful. Have a nice day.")
				break

			else:
				print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()