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

		currentAttempts += 1
		print("Error: Invalid username or password. Please try again.")
	
	print("Extraneous logins detecting. Security closure engaged.")
	return None

def main():
	currentUser = userLogin()
	if currentUser:
		while True:
			print(f"Your current balance is {currentUser.currentBalance")

if __name__ == "__main__":
    main()