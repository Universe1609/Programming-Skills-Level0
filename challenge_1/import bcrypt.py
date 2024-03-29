import bcrypt

password = b"universe"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# Verify
if bcrypt.checkpw(password, hashed):
    print("It matches!")
else:
    print("It does not match.")
