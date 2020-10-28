from Cryptodome import Hash
from Cryptodome.Hash import SHA256
from Cryptodome import Random
#import Crypto

class Encryption():
    """
    Encryption
    """

    def LTE_1(object_data):
        """
        LTE 1
        """ 
        object_data = Hash.SHA256.new(data = b"AS")
        print(object_data.digest())
        #raise object_data
        return object_data

    

Encryption.LTE_1
#print(Encryption.LTE_1(object_data=b"WW#"))


