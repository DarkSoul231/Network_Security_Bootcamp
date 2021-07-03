import hashlib

##################################################

def md5Hash():
    print("-----------------------------------------------")
    print("<>>>>>>>>>><MD5 Hashing><<<<<<<<<<>")
    print("-----------------------------------------------")
    string = input("Enter a String: ")

    hash_object = hashlib.md5(str(string).encode('utf-8'))

    print(f'Hash of || {string} || is : ', hash_object.hexdigest())
    print("-----------------------------------------------")
    exit()

##################################################
def sha256Hash():
    print("-----------------------------------------------")
    print("<>>>>>>>>>><SHA256 Hashing><<<<<<<<<<>")
    print("-----------------------------------------------")
    string = input("Enter a String: ")

    sha_obj = hashlib.sha256()

    sha_obj.update(str(string).encode('utf-8'))

    print(f'sha256 Hash of || {string} || is : ', sha_obj.hexdigest())
    print("-----------------------------------------------")
    exit()

##################################################

def sha1Hash():
    print("-----------------------------------------------")
    print("<>>>>>>>>>><SHA1 Hashing><<<<<<<<<<>")
    print("-----------------------------------------------")
    string = input("Enter a String: ")

    sha_obj = hashlib.sha1()

    sha_obj.update(str(string).encode('utf-8'))

    print(f'sha1 Hash of || {string} || is : ', sha_obj.hexdigest())
    print("-----------------------------------------------")
    print()

    exit()

##################################################

def mul_hashlib(choice):

    if choice == 1:
        md5Hash()
    elif choice == 2:
        sha256Hash()
    elif choice == 3:
        sha1Hash()
    else:
        print("Select Correct Choice...!!")

    exit()

##################################################


# Driver program
if __name__ == "__main__":
    print("-----------------------------------------------")
    print("< 1. md5 > \n< 2. sha256 > \n< 3. sha1 >")
    print("-----------------------------------------------")

    choice = int(input("Enter The Choice : "))

    print(mul_hashlib(choice))


# Hashing of Hello String...
#   Using md5   8b1a9953c4611296a827abf8c47804d7
#   Using SHA256    b'\x18_\x8d\xb3"q\xfe%\xf5a\xa6\xfc\x93\x8b.&C\x06\xec0N\xdaQ\x80\x07\xd1vH&8\x19i'
#   Using SHA1  b'\xf7\xff\x9e\x8b{\xb2\xe0\x9bp\x93Z]x^\x0c\xc5\xd9\xd0\xab\xf0'