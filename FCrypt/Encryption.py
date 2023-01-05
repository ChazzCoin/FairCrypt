from cryptography.fernet import Fernet
from F import OS



class EncryptionKey:
    HOME_DIRECTORY = str(OS.get_parent_directory())
    KEY_DIRECTORY_NAME = ""
    KEY_DIRECTORY = ""
    KEY_NAME = ""
    KEY: Fernet = None

    def __init__(self, key_path):
        self.KEY_DIRECTORY = key_path

    def create_new_key(self):  # TESTED!
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open(self.KEY_DIRECTORY_NAME, "wb") as key_file:
            key_file.write(key)
        print("Key CREATED: ")

    def load_key(self):  # TESTED!
        """
        Loads the key from the current directory named `key.key`
        """
        key_file = open(self.KEY_DIRECTORY_NAME, "rb").read()
        self.KEY = Fernet(key_file)
        return self.KEY

    def encrypt_string(self, string):  # TESTED!
        """
        Given a string (str) and key (bytes), it encrypts the string and returns it
        """
        # encrypt data
        print("Encrypting String. . .")
        encrypted_data = self.KEY.encrypt(str.encode(string))
        print("ENCRYPTED!")
        return encrypted_data

    def decrypt_string(self, bytestring):  # TESTED!
        """
        Given a bytestring and key (bytes), it decrypts the string and returns it
        """

        # decrypt data
        print("Decrypting String. . .")
        decrypted_data = self.KEY.decrypt(bytestring)
        print("DECRYPTED!")
        return decrypted_data.decode()

    def encrypt_file(self, filename):  # TESTED!
        """
        Given a filename (str) and key (bytes), it encrypts the file and write it
        """

        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
            print("Reading File. . .")
        # encrypt data
        print("Encrypting File. . .")
        encrypted_data = self.KEY.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print("ENCRYPTED!")

    def decrypt_file(self, filename):  # TESTED!
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
            print("Reading File. . .")
        # decrypt data
        print("Decrypting File. . .")
        decrypted_data = self.KEY.decrypt(encrypted_data)
        # write the original file
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        print("DECRYPTED!")



def get_rs_key():
    print("LOADING -> rs.key")
    return open("/home/aoki/bin/.keys/rs.key", "rb").read()


# def create_new_key(filepath, keyname):  # TESTED!
#     """
#     Generates a key and save it into a file
#     """
#     key = Fernet.generate_key()
#     if filepath == ".keys":
#         with open("/home/aoki/bin/.keys/"+keyname+".key", "wb") as key_file:
#             key_file.write(key)
#     elif filepath != "":
#         with open(filepath+keyname+".key", "wb") as key_file:
#             key_file.write(key)
#     else:
#         with open(keyname+".key", "wb") as key_file:
#             key_file.write(key)
#     print("Key CREATED: " + filepath)


# def load_key(filepath, keyname):  # TESTED!
#     """
#     Loads the key from the current directory named `key.key`
#     """
#     # DEFAULT -> /home/aoki/bin/.keys/key.key
#     if filepath.endswith("/"):
#         f = filepath+keyname+".key"
#     else:
#         f = filepath+"/"+keyname+".key"
#     if filepath == ".keys":
#         print(".key LOADED!")
#         return open("/home/aoki/bin/.keys/"+keyname+".key", "rb").read()
#     else:
#         print("Key from filepath LOADED!")
#         return open(f, "rb").read()


# def encrypt_string(string, key="rs.key"):  # TESTED!
#     """
#     Given a string (str) and key (bytes), it encrypts the string and returns it
#     """
#     if key == "rs.key":
#         key = get_rs_key()
#     f = Fernet(key)
#     # encrypt data
#     print("Encrypting String. . .")
#     encrypted_data = f.encrypt(str.encode(string))
#     print("ENCRYPTED!")
#     return encrypted_data
#
#
# def decrypt_string(bytestring, key="rs.key"):  # TESTED!
#     """
#     Given a bytestring and key (bytes), it decrypts the string and returns it
#     """
#     if key == "rs.key":
#         key = get_rs_key()
#     f = Fernet(key)
#     # decrypt data
#     print("Decrypting String. . .")
#     decrypted_data = f.decrypt(bytestring)
#     print("DECRYPTED!")
#     return decrypted_data.decode()


# def encrypt_file(filename, key="rs.key"):  # TESTED!
#     """
#     Given a filename (str) and key (bytes), it encrypts the file and write it
#     """
#     if key == "rs.key":
#         key = get_rs_key()
#     f = Fernet(key)
#     with open(filename, "rb") as file:
#         # read all file data
#         file_data = file.read()
#         print("Reading File. . .")
#     # encrypt data
#     print("Encrypting File. . .")
#     encrypted_data = f.encrypt(file_data)
#     # write the encrypted file
#     with open(filename, "wb") as file:
#         file.write(encrypted_data)
#     print("ENCRYPTED!")
#
#
# def decrypt_file(filename, key="rs.key"):  # TESTED!
#     """
#     Given a filename (str) and key (bytes), it decrypts the file and write it
#     """
#     if key == "rs.key":
#         key = get_rs_key()
#     f = Fernet(key)
#     with open(filename, "rb") as file:
#         # read the encrypted data
#         encrypted_data = file.read()
#         print("Reading File. . .")
#     # decrypt data
#     print("Decrypting File. . .")
#     decrypted_data = f.decrypt(encrypted_data)
#     # write the original file
#     with open(filename, "wb") as file:
#         file.write(decrypted_data)
#     print("DECRYPTED!")


# key = load_key(".keys", "rs")
# testString = "Super Secret Message"
# eString = encrypt_string(testString, key)
# print(eString)
# dString = decrypt_string(eString, key)
# print(dString)
# encrypt_file("/home/aoki/bin/message.txt", key)
# decrypt_file("/home/aoki/bin/message.txt", key)
