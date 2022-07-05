from base64 import decode
#Main file from where program starts

#Importing the Cryptography Module for encryption & decryption
import Cryptography 

if __name__ == '__main__':
    crypto=Cryptography.Cryptography()
    input_data=['ABC','XYZ','GHI','NOP','JKL','UTS']

    #Encoding the input_data
    encoded=[crypto.Encode(i) for i in input_data]
    #Decoding the encoded data
    decoded=[crypto.Decode(i) for i in encoded]
    print("Input Data:   ",input_data)
    print("Encoded Data: ",encoded)
    print("Decoded Data: ",decoded)
        

