Solution to Simple Text Editor:

s=''
ls=[]
n=int(input())    
for i in range(n):
    k=input().split()
    if len(k)>1:
        if k[0]=='1':ls.append(s);s+=k[1];
        elif k[0]=='2':ls.append(s);m=int(k[1]);s=s[0:len(s)-m]
        else:print(s[int(k[1])-1])
    else:s=ls.pop()
