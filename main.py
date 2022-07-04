email = input("Enter your Email: ")

# Removing any trailing white-spaces from the entered email
email.strip()

# Email address can be broken down into pieces using slicing operations
# finding the index of '@'
ind = email.index('@')

username = email[:ind]
domain_name = email[ind+1:]
print("Your Username is \"{}\", and your Domain Name is \"{}\"".format(username, domain_name))
