""" """

#Remind professor about GUI vs Command Line
class Account_Info:
	"""docstring for Account_Info"""
	def __init__(self, userName, password, currentBalance, firstName, lastName):
		super(Account_Info, self).__init__()
		self.userName = userName
		self.password = password
		self.currentBalance = currentBalance
		self.firstName = firstName
		self.lastName = lastName
	
	def fullName(self):
		return f"{self.firstName} {self.lastName}"

user1 = Account_Info("Mman777mw", "M@Corp@Est2010", "4500000", "Michael", "Wright")
user2 = Account_Info("Mant1s01", "L3tM3@in", "5500000", "Michaelle", "Wright")
user3 = Account_Info("Meta01", "SerDesSCMCM-01", "750000", "Isaac", "MC")
user4 = Account_Info("Meta04", "100Pr@@f7&62", "200000", "Amish", "MC")

def userLogin():


def main():


if __name__ == "__main__":
    main()