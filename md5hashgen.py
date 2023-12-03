import hashlib

def md5(valore):
    hasher = hashlib.md5()
    hasher.update(valore.encode())
    return hasher.hexdigest()

if __name__ == "__main__":
    valore = input("Inserisci il valore: ")
    hash = md5(valore)
    print("L'hash MD5 è:", hash)