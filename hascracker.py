#leighTrinity
# Jan 25 2022

import hashlib

type_of_hash = str(input('Which hash are we bruteforcing today?    '))
file_path = str(input('Enter path to file to bruteforce with:  '))
hash_to_decrypt = str(input("Enter hash value to bruteforce:   "))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[***] Found Password in list:   ' + line.strip())
                exit(0)

        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[***] Found Password in list:   ' + line.strip())
                exit(0)

        if type_of_hash == 'sha512':
            hash_object = hashlib.sha512(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[***] Found Password in list:   ' + line.strip())
                exit(0)

        if type_of_hash == 'sha256':
            hash_object = hashlib.sha256(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[***] Found Password in list:   ' + line.strip())
                exit(0)





    print("Password not in file.")


