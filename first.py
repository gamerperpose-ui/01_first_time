import random 

def history(n , chances):
    with open("result.txt" , "a") as f :
        f.write(f" you win you gusses correct number {n} in {chances} chancess \n")
     

def show_history():
    with open("result.txt", "r") as f:
        print(f.readline())
while True:
    n = random.randint(1,100)
    print(n)
    a = -1
    chances = 0
    while(n != a ):
        chances += 1
        a = int(input("Enter a number"))
        if(a < n):               
            print("random number is higher ")
        elif(a > n):
            print("Random number is lower")
        elif( n == a ):
            print(f" you win you gusses correct number {n} in {chances} chancess")
    break      
history(n , chances)
num = int(input("""1.show history
2.exit"""))
if num == 1 :
    show_history()
elif num == 2 :
    print("""Thanks for visiting
    visit us again1""")



