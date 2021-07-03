import hashlib

#print(hashlib.algorithms_available)

print("-----------------------------------------------")
print("<>>>>>>>>>><MD5 Hashing><<<<<<<<<<>")
print("-----------------------------------------------")
string = input("Enter a String: ")

hash_object = hashlib.md5(str(string).encode('utf-8'))

print(f'Hash of || {string} || is : ', hash_object.hexdigest())
print("-----------------------------------------------")


# Hashing of << Hello >> String...
# Using md5 : 8b1a9953c4611296a827abf8c47804d7
