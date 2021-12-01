import string
import secrets
n = int(input("Enter Length of your password : "))
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(n))
print(password)