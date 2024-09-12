# 4360-banking

Get Started:
Open banking.py through the Python IDLE shell, then under the Run dropdown on the banking.py window select Run Module.

The user may use existing usernames and passwords within the program to login, or enter their own in the program.

Existing Usernames and Passwords are:
UserName: "Mman777mw" Password: "M@Corp@Est2010"
UserName: "Mant1s01" Password: "L3tM3@in"
UserName: "Meta01" Password: "SerDesSCMCM-01"
UserName: "Meta04" Password: "100Pr@@f7&62"

To create new users please utilize the following template replacing the brackets [] with the correlating information.
[User Object Name] = Account_Info("[Username]", "[Password]", "[Current Balance]", [“Account Number”], "[First Name]", "[Last Name]")
Best to paste the template below the last existing user and enter the correlating information.
Do not forget to update userList with the name of the User Object Name, otherwise the login information will not be properly registered in the program.

User interface:
Upon successful login, the user will have the following options:
Deposit: The terminal will ask the user to enter a numerical amount that the user would like to deposit. 
	Once the user has entered the amount, it will display deposit amount and ask the user to verify the amount. 
	If the amount is incorrect, the user must enter the amount and it will verify again. 
	This will loop until the user have the verified the amount as being correct. It will then display the starting balance and the ending balance.

Withdraw: The terminal will ask the user to enter a numerical amount that the user would like to withdraw. 
	Once the user has entered the amount, it will display withdraw amount and ask the user to verify the amount. If the amount is incorrect, the user must enter the amount and it will verify again. 
	This will loop until the user have the verified the amount as being correct. The program will then check to see if the withdraw amount will result in a negative balance. 
	If it does, it will display an error message and ask the user if they wish to try again. If they do not, the user will be returned to the root menu to select another option. 
	If they wish to try again, they will be returned to the amount loop. If the check does not result in a negative balance, then it will display the starting balance and the ending balance.

Transfer: The terminal will ask the user to enter a numerical amount that the user would like to transfer. 
	Once the user has entered the amount, it will display transfer amount and ask the user to verify the amount. If the amount is incorrect, the user must enter the amount and it will verify again. 
	This will loop until the user have the verified the amount as being correct. The program will then check to see if the transfer amount will result in a negative balance. 
	If it does, it will display an error message and ask the user if they wish to try again. If they do not, the user will be returned to the root menu to select another option. 
	If they wish to try again, they will be returned to the amount loop. If the check does not result in a negative balance, then it will ask for the account number the user wishes to transfer to. 
	Once again the user will be placed in a loop that verifies if the entered account number is correct, otherwise the user will have to reenter the account number until they verify it is correct. 
	Once the account number is verified, the program will check the userList to see if the entered account number is valid. 
	If it is valid, the program will print that the transfer was successful, update the balances of both accounts, and display the user’s starting and ending balance.

Exit: This option exits the program.

Requirements
	Functional Requirements:
		User inputs username and password information that the program verifies
		Only 3 Login Attempts are allowed, unless changed in program code
		Software displays menu options on successful login
		Software displays current balance on successful login
		Software deposits input funds into account that is logged in
		Software withdraws input funds from account that is logged in, unless input amount results in negative balance
		Software transfers input funds from account that is logged in to input account, unless input amount results in negative balance
		Software will display an error and allow user to input a new amount if initial input results in negative balance, and will keep allowing reentry until an amount that does not result in a negative balance is input
		Three maximum deposits, withdrawals, transfers, or any combination thereof per login
		Application exits after third operation
	
	Non-Functional Requirements:
		IDLE shell terminal interface
		Use while loop for main operations
		No process should take more than 1 sec to return an input