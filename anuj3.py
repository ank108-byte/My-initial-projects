import random
import string
chars=" " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
keys=chars.copy()
random.shuffle(keys)
#print(f"Chars :{chars}")
#print(f"Keys  :{keys}")

#Encryption part
plain_text=input("Enter the text you want to encrypt to make it private from unauthorized access: ")
print("Successfully encrypted!")
cipher_text=""
for letter in plain_text:
    index= chars.index(letter)
    cipher_text+=keys[index]
user_input=input("Do you want to see your text in encrypted form:(Y/N) ").lower() 
if user_input != 'y':
    pass
else:
    print(f"Cipher text:{cipher_text}")

# descryption
cipher_textinput=input("Enter the text you want to descrypt to see it in readable form: ")
plain_text=""
for letter in cipher_textinput:
    index=keys.index(letter)
    plain_text+=chars[index]

print(f"Orignal text:{plain_text}")    

        


