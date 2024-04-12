#project no. 3 prototype version 2

#checking password validity
# s = sharte smallalphabets 
# c = sharte capitalalphabets
# d = sharte digits
# r = sharte specialchar

s, c, d, r = 0, 0, 0, 0

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
    else:
        print("Invalid Password")