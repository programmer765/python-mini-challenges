# --------------
#Code starts here
import sys
def palindrome(num):
    nums = str(num)
    for i in range(num+1,sys.maxsize):
        if(str(i)==str(i)[::-1]):
            return i
print(palindrome(131))


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_3 = str_1.lower()
    c=0
    l = len(str_2)
    for i in str_2.lower():
        if i in str_3:
            c=c+1
            a = str_3.index(i)
            str_3 = str_3[:a] + " " + str_3[a+1:]
    if(c==l):
        return True
    else:
        return False
    
print(a_scramble("eatcher","teacher"))


# --------------
#Code starts here
def check_fib(num):
    t2=1;t1=0
    t=t1+t2
    while(t<=num):
        t1=t2
        t2=t
        t=t1+t2
    if(t2==num):
        return True
    else:
        return False
print(check_fib(145))


# --------------
#Code starts here
def compress(word):
    c=1;i=0
    a = list(word.lower())
    l = len(word)
    s=[]
    while(i<l):
        s.append(a[i])
        j=i+1
        while(j<l):
            if(a[i]==a[j]):
                c+=1
                j=j+1
                
            else:
                break
        i=j
        s.append(str(c)) 
        c=1
    return ''.join(s)
print(compress("xxxbbbcdexx"))


# --------------
#Code starts here
def k_distinct(string,k):
    a=list(string.lower())
    b = string.lower()
    l = len(b)
    for i in range(l):
        for j in range(i+1,l):
            if(a[i]==a[j]):
                b = b[:j] + " " + b[j+1:]
    b = b.replace(" ","")
    l = len(b)
    if(l==k):
        return True
    else:
        return False    
print(k_distinct("messopotamia",8))


