import hashlib

# print(hashlib.algorithms_available)

string = input("Enter a String: ")

hash_object = hashlib.md5(str(string).encode('utf-8'))

print(f'Hash of "{string}" is : ', hash_object.hexdigest())


