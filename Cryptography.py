
class Cryptography:
    def __init__(self) -> None:
        self.cons1=[chr(x) for x in range(ord('A'), ord('Z') + 1)]
        self.cons2=sorted(self.cons1,reverse=True)
    def Encode(self,message):
        encode_message=""
        for i in range(len(message)):
            index=self.cons1.index(message[i])
            if (index%2)==0:
                encode_message+=self.cons2[index]
            else:
                encode_message+=message[i]
                encode_message+=self.cons2[index]
        return encode_message
    def Decode(self,encoded_message):
        encoded_message=encoded_message[::-1]
        decoded_message=""
        i=0
        while i<len(encoded_message):
            index=self.cons1.index(encoded_message[i])
            if (index%2)==0:
                i+=1
                decoded_message+=encoded_message[i]
            else:
                decoded_message+=self.cons2[index]
            i+=1
        return decoded_message[::-1]
            

            

