import random
import pickle
import string



def random_alpha_gen(randomLetter=''):
     for i in range(3):
         randomLetter += random.choice(string.ascii_letters)
     return randomLetter.lower()

def main():
    print("Choose what you want to do 1. Encrypt 2. Decrypt ")
    a=int(input())
    if(a==1):
        paragraph=input("Enter your paragraph to be Encrypted here ")
        paragraph1=paragraph.lower()
        words=paragraph1.split()
        coded_para=''
        for word in words:
            if (len(word)<3):
                coded_para+=word[::-1]+' '
            else:
                coded_para+=random_alpha_gen()+word[1:]+word[0]+random_alpha_gen()+' '
        print("Encrypted string is "+coded_para)
        text_file = open("sample.txt", "w")
        text_file.write(coded_para)
        #pickle.dump(coded_para,n)
        text_file.close()
    else:
        paragraph=input("Enter your paragraph to be Decrypted here ")
        paragraph1=paragraph.lower()
        words=paragraph1.split()
        decoded_para=''
        for word in words:
            if (len(word)<3):
                decoded_para+=word[::-1]+' '
            else:
                decoded_para+=word[-4]+word[3:-4]+' '
        print("Decrypted string is "+decoded_para)


# Using the special variable 
# __name__
if __name__=="__main__":
    main()


#nkzehliadvse
#f
#dawanketsayt ivroveslurl drnehliadqke raleryvnrh zbjuchmxzn

