from cryptography.fernet import Fernet
import FCrypt
from F import DATE

_DATE = DATE.to_month_day_year_str()
_RS = FCrypt.rs()

class BasicEncryption:
    KEY: Fernet = None

    def __init__(self, key=None):
        if not key:
            self.load_key(_RS)
        else:
            self.load_key(key)

    @staticmethod
    def create_new_key(file_name_and_path:str):  # TESTED!
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open(file_name_and_path, "wb") as key_file:
            key_file.write(key)
        print(f"Key CREATED: [ {file_name_and_path} ]")

    def load_key(self, key):  # TESTED!
        """ Loads the key from the current directory named `key.key` """
        self.KEY = Fernet(key)
        return self.KEY

    def encrypt_string(self, string):  # TESTED!
        """ Given a string (str) and key (bytes), it encrypts the string and returns it """
        # encrypt data
        print("Encrypting String. . .")
        encrypted_data = self.KEY.encrypt(str.encode(string))
        print("ENCRYPTED!")
        return encrypted_data

    def decrypt_string(self, bytestring):  # TESTED!
        """ Given a bytestring and key (bytes), it decrypts the string and returns it """
        # decrypt data
        print("Decrypting String. . .")
        decrypted_data = self.KEY.decrypt(bytestring)
        print("DECRYPTED!")
        return decrypted_data.decode()

    def encrypt_file(self, file_name_and_path: str):  # TESTED!
        """ Given a filename (str) and key (bytes), it encrypts the file and write it """

        with open(file_name_and_path, "rb") as file:
            # read all file data
            file_data = file.read()
            print("Reading File. . .")
        # encrypt data
        print("Encrypting File. . .")
        encrypted_data = self.KEY.encrypt(file_data)
        # write the encrypted file
        with open(file_name_and_path, "wb") as file:
            file.write(encrypted_data)
        print("ENCRYPTED!")

    def decrypt_file(self, file_name_and_path: str):  # TESTED!
        """ Given a filename (str) and key (bytes), it decrypts the file and write it """
        with open(file_name_and_path, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
            print("Reading File. . .")
        # decrypt data
        print("Decrypting File. . .")
        decrypted_data = self.KEY.decrypt(encrypted_data)
        # write the original file
        with open(file_name_and_path, "wb") as file:
            file.write(decrypted_data)
        print("DECRYPTED!")

