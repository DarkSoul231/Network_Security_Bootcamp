import hashlib, uuid

print("-----------------------------------------------------------------------------------")
itrLen = int(input("How many time you want to Iterate : "))
print("-----------------------------------------------------------------------------------")
strToIterate = input("Enter a String Which u want to Salt and Iterate : ")

# Here we hashed original string given by user..
hashed = hashlib.sha1()
hashed.update(str(strToIterate).encode('utf-8'))

# Loop used to iterate up to specified number given by user and generate hash value..
for i in range(itrLen):
    hashed = hashlib.sha1()
    hashed.update(str(hashed).encode('utf-8'))

# Convert Hashed byte into Hexadecimal for printing..
hashed = hashed.hexdigest()

# Final printing of original string into Iterated Hashed Hex Value...
print("-----------------------------------------------------------------------------------")
print(f'SHA1 Hash Iteration {itrLen} of || {strToIterate} || is : ', hashed)
print("-----------------------------------------------------------------------------------")

# Convert Hex Hased value to byte for Salting..
StrToSalt = str(hashed).encode('utf-8')

# Convert Salt to byte..
# UUID is Users Unique ID
# UUID4 used to Generate a random UUID.
salt = uuid.uuid4().bytes

hashed_password = hashlib.sha1(StrToSalt + salt).hexdigest()

# Final printing of original string into Salted Hex Hash Value...
print(f'SHA1 salting of Iterated || {strToIterate} || is : ', hashed_password)
print("-----------------------------------------------------------------------------------")

# Example Output-->>>
# String is || Hello ||
# For No of Iterations..
#   0: f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0
#   1: 4d8f920c06291b21ae69ae4d3e309d2a60582cba
#   2: 8e97e82bd9c2aa4e4d5108fa1247ae8b30e1c584
#   3: d3bf48a040a8b454c2087b5de4388b875d55f4a1
#   3: 95fd1b6b13a44e8b45956bf7f65c1423ff76d306

# -----------------------------------------------------------------------------------
# Enter a String Which u want to Salt and Iterate : Hello
# -----------------------------------------------------------------------------------
# How many time you want to Iterate : 2
# -----------------------------------------------------------------------------------
# SHA1 Hash Iteration 2 of || Hello || is :  35b18fbd818a71b4b505650915407dcc65fbee75
# -----------------------------------------------------------------------------------
# SHA1 salting of Iterated || Hello || is :  4e57f07a2f6c4d062acffb5c69fab039b86eda03
# -----------------------------------------------------------------------------------
