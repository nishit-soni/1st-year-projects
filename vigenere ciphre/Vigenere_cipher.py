f=open('english_random.txt')#open the file
s=f.read()
def textstrip(s):
    '''This takes the file and converts it to a string with all the spaces and other
    special characters removed. What remains is only the lower case letters,
    retain only the lowercase letter'''
    n="abcdefghijklmnopqrstuvwxyz"#lowercase letters
    m=""#empty string
    for i in s:#for loop to check each character in the file
        if i in n:#if the character is a lowercase letter
            m+=i#add it to the empty string
    return m#return the string
#print(textstrip(s))

def letter_distribution(s):
    '''Consider the string s which comprises of only lowercase letters. Count
    the number of occurrences of each letter and return a dictionary'''
    d={}#empty dictionary
    a="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(a)):
        c=s.count(a[i])
        d.update({a[i]:c})
    return d#return the dictionary
#print(letter_distribution(s))

l={"a":'x','b':'y','c':'z','d':'a','e':'b','f':'c','g':'d','h':'e','i':"f",'j':"g","k":"h","l":'i',"m":"j","n":"k","o":"l","p":"m","q":"n","r":'o','s':"p","t":"q","u":"r","v":"s","w":"t","x":"u","y":"v","z":"w"}#dictonary of the substitutions

def substitution_encrypt(s,l):
    '''encrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    string_1=''#empty string
    for i in s:#for loop to check each character in the string
        string_1+=l[i]#add the value of the key to the empty string
    return string_1#return the string    
#print(substitution_encrypt(s,l))

def substitution_decrypt(s,l):
    '''decrypt the contents of s by using the dictionary d which comprises of
    the substitutions for the 26 letters. Return the resulting string'''
    m={}#empty dictionary
    for (i,j) in l.items():#converting dictionary into the tuples
        m[j]=i
    string_1=''#empty string
    for i in s:#for loop to check each character in the string
        string_1+=m[i]#add the value of the key to the empty string
    return string_1#return the string      
#print(substitution_decrypt(s,l))#using inverted dictionary



def cryptanalyse_substitution(s):
    '''Given that the string s is given to us and it is known that it was
    encrypted using some substitution cipher, predict the d'''
    a=letter_distribution(textstrip("Nishit_60.txt"))#creating dictionary
    a1=sorted(a.items(), key=lambda x: x[1], reverse=True)#sorted dictionary in decending order
    b=letter_distribution(s)
    b1=sorted(b.items(), key=lambda x: x[1], reverse=True)#sorted dictionary in decending order
    c={}
    for i in range(26):
        c[a1[i][0]]=b1[i][0]
    return c
#print(cryptanalyse_substitution(s))
#now we find dictionary of encrypted substitution

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    a=""#create an empty string
    b="abcdefghijklmnopqrstuvwxyz"
    for i in range (len(s)):
        #given password given,shift each leeter in s by the index of passaword
        a+=b[(b.index(s[i])+b.index(password[i%len(password)])-1)%26]
    return a
#password="nishit"
#print(vigenere_encrypt(s,password))
  
def vigenere_decrypt(s,password):
    '''Decrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    a=''#create an empty string
    b="abcdefghijklmnopqrstuvwxyz"
    for i in range (len(s)):
        #for the password given,again back shift the letter in s
        a+=b[(b.index(s[i])-b.index(password[i%len(password)])-1)%26]
    return a
#password="nishit"
#print(vigenere_decrypt(s,password))

def rotate_compare(s,r):
    '''This rotates the string s by r places and compares s(0) with s(r) and
    returns the proportion of collisions'''
    a=''#creating a empty string
    for i in range (len(s)):
        a+=s[(i+r)%len(s)]
    count=0
    for i in range(len(s)):
        #if words of rotated string collide then count is increase by 1
        if a[i]==s[i]:
            count+=1
    return (count/len(s))*100        
         #percentage collision
#r=2
#print(rotate_compare(s,r))
 
def cryptanalyse_vigenere_afterlength(s,k):
    '''Given the string s which is known to be vigenere encrypted with a
    password of length k, find out what is the password'''
    a=''
    b="abcdefghijklmnopqrstuvwxyz"
    t="etaoinshrdlcumwfgypbvkjxqz"
    for i in range(k):
        c=''
        for j in range(i,len(s),k):
            c+=s[j]#creating a string of every kth letter in the given string
        d=letter_distribution(c)
        d1=sorted(d.items(), key=lambda x :x[1], reverse=True)
        a+=b[b.index(d1[0][0])-b.index(t[0])-1]
       #add most frequent words
    return a
#k=10
#print(cryptanalyse_vigenere_afterlength(s,k))

def cryptanalyse_vigenere_findlength(s):
    '''Given just the string s, find out the length of the password using which
    some text has resulted in the string s. We just need to return the number
    k'''
    i=1
    while(i<len(s)):
        a=rotate_compare(s,i)
        if a>5:
            return i
        else:
            i+=1
#print(cryptanalyse_vigenere_findlength(s))    

def cryptanalyse_vigenere(s):
    '''Given the string s cryptanalyse vigenere, output the password as well as
    the plaintext'''
    k=cryptanalyse_vigenere_findlength(s)#call the function for finding the length of password
    print(k)
    a=cryptanalyse_vigenere_afterlength(s,k)#call the function to find the password
    print(a)
    print(vigenere_decrypt(s,a))#decrypted the string using the password and print it
#cryptanalyse_vigenere(vigenere_encrypt(textstrip("Nishit_60.txt"))#function for decrypt the string
print(cryptanalyse_vigenere(s))




