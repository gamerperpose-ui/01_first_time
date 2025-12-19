
import random 

def retry () : 
        print("Game is loading.................")
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
            with open("result.txt" , "a") as f :
                f.write(f" you win you gusses correct number {n} in {chances} chancess \n")    

def show_history():
    with open("result.txt", "r") as f:
        print(f.read())

def clear_history():
    print("History is wipeout")
    with open("result.txt", "w") as f:
        f.write(" ")

while True:
    num = int(input("""
    1.play game 
    2.Show history
    3.Clear history  
    4.Exit                              
    """))
    if num == 1 :
        retry()
    elif num == 2 :
        show_history()
    elif num ==  3:
        clear_history()
    elif num == 4:
        print("""Thanks for visiting
        visit us again  !!!!!!""")
        break   

