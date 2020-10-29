from Cryptodome import Hash, Random, PublicKey, Protocol, IO, Cipher, Math, Signature, SelfTest, Util
from Cryptodome.Hash import SHA256


class Encryption:
    """
    Encryption
    """

    def LTE_1(self, object_data):
        """
        LTE 1
        """ 
        object_data = Hash.SHA256.new(data = b"P")
        print(object_data.digest())
        #self.e= object_data


    

Encryption.LTE_1()

#print(Encryption.LTE_1(object_data=b"WW#"))


