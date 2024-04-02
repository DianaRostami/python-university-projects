#checking password validity
# s = sharte smallalphabets 
# c = sharte capitalalphabets
# d = sharte digits
# r = sharte specialchar

s, c, d, r = 0, 0, 0, 0

print("enter your password")
p = input()
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="@#"
digits="0123456789"

for i in p:
 
    # counting lowercase alphabets
    if (i in smallalphabets):
        s+=1           
 
    # counting uppercase alphabets
    if (i in capitalalphabets):
        c+=1           
 
    # counting digits
    if (i in digits):
        d+=1           
 
    # counting the mentioned special characters
    if(i in specialchar):
        r+=1       
        
            

    
if (len(p)>=8 and len(p)<=12):            
    if (s>=1 and c>=1 and d>=1 and r>=1 and s+c+d+r==len(p)):
        print("Valid Password")
        print("The password is between 8 and 12 characters\nThe password contain at least one lowercase letter\nThe password contain at least one capital letter")
        print("The password contains numbers\nThe password has special characters")
else:
    print("Invalid Password")
    print("The number of characters is not appropriate")
    if s==0 :
        print("The password does not contain any lowercase letters")
    if c==0 :
        print("The password does not contain any capital letters")
    if d==0 :
        print("The password does not contain any numbers")
    if r==0 :
        print("The password does not contain any special characters")