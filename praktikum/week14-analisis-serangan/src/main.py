import hashlib

# target hash MD5 dari password "admin"
target_hash = "21232f297a57a5a743894a0e4a801fc3"

wordlist = ["12345", "password", "admin", "qwerty"]

for word in wordlist:
    hash_word = hashlib.md5(word.encode()).hexdigest()
    if hash_word == target_hash:
        print("Password ditemukan:", word)
        break