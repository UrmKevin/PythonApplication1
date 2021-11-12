#--------------------
# 1
#t=0 #arvude kogus
#q=0 #int
#while t<15:
#    t+=1
#    a=float(input("Sisesta arv: "))
#    if a==round(a): q+=1
#print("Täisarvud kogus: ", q)

#---------------------
# 1
#q=0
#for i in range(15):
#    a=float(input("Sisesta arv: "))
#    if a==round(a): q+=1
#print("Täisarvud kogus: ", q)

#---------------------
# 2
#A=int(input("Sisesta arv: "))
#B=0
#for i in range(1,A+1):
#    print(i)
#    B+=i
#print("Summa: ", B)

#---------------------
# 4
#sq=0
#for i in range(10,21):
#    sq=i**2
#    print(sq)

#---------------------
# 3
#from random import*
#korrutis=1
#for i in range(8):
#    B=randint(-100,100)
#    if B>0:
#       korrutis*=B
#       print(B)
#print("Korrutis on ",korrutis)

#----------------------
# 5
#from random import*
#n=1
#for i in range(10):
#    N=randint(-100,50)
#    if N<0:
#       n+=N
#       print(N)
#print("Korrutis on ",n)

#----------------------
# 6
#from random import*
#N=int(input("Mitu: "))
#p=n=o=0
#While N>0:
#    N-=1
#    B=randint(-100,100)
#    print(B)
#    if B>0:
#        p+=1
#    else:
#        o+=1
#print("Pos: ",p)
#print("Neg: ",n)
#print("Nullid: ",o)

#-----------------------
# 7
#A=int(input("From:"))
#B=int(input("To:"))+1
#K=int(input("K:"))
#for i in range(A,B):
#    if i%K==0:
#        print(i)

#-----------------------
# 8
#for i in range(1,21):
#    cm=i*2.5
#    print(i," = ",cm)

#-----------------------
# 9
#key="слон"
#c=""
#print("Купи слона!")
#c=str(input()).lower()
#if c!=key:
#    print("Купи слона!")
#while c!=key:
#    c=str(input()).lower()
#    if c!=key:
#        print("Все говорят",c," А ты купи!")
#print("Слон твой!")

#----------------------
# 22
#p=0
#for i in range(100,200):
#    if i%17==0:
#        p+=i
#print(p)

#-----------------------
# столбик таблица умножения
#for i in range(1,10):
#    for j in range(1,10):
#        print(f"{(i*j):2}",end=" ")
#    print()

#-----------------------
# 16
#for j in range(1,10):
#    for i in range(1,10):
#        if i==j:
#            print(j,end=" ")
#        else:
#            print("0",end=" ")
#    print()

#------------------------
# 28
#from random import*
#secret=randint(1,10)
#ans=0
#att=0
#while ans!=secret:
#    ans=int(input("Guess a number from 1 to 10: "))
#    att+=1
#print("U got this! with ",att,"attemts")

#-------------------------
# 31

K=int(input("How many cutlets do you have? "))
while K<0:
    K=int(input("How many cutlets do you have? "))
M=4
while K>4:
    K=K%M
print(K," cutlets left")




































































#print("FOR".center(60,"#"))
#for i in range(5):
#    print("Hello world!")

#print("WHILE TRUE".center(60,"#"))

#k=0
#while True:
#    k+=1
#    print("Hello world!")
#    if k==5: break

#print("WHILE a<5".center(60,"#"))
#a=0
#while a<5:
#    print("Hello world!")
#    a+=1