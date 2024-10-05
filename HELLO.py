def pause():
    input("Press Enter to continue...")  # Pauses the game, like a delay

# Starting the game
print("HELLO, I'M AN EDUSYSTEM-25. MY NAME IS PETE P. EIGHT.")
name = input("WHAT'S YOUR NAME? ")

print()
print(f"HI THERE {name}. ARE YOU ENJOYING YOURSELF HERE IN BEAUTIFUL MAYNARD, MASS?")
b_answer = input("Answer 'YES' or 'NO': ").upper()

# Response based on user input
while True:
    if b_answer == "YES":
        print("OH, I'M GLAD TO HEAR THAT.")
        pause()
        break
    elif b_answer == "NO":
        print("OH, SORRY TO HEAR THAT. MAYBE WE CAN BRIGHTEN UP YOUR STAY A BIT.")
        pause()
        break
    else:
        print(f"I DON'T UNDERSTAND YOUR ANSWER OF '{b_answer}'.")
        print("PLEASE ANSWER 'YES' OR 'NO'. DO YOU LIKE IT HERE?")
        b_answer = input("Answer 'YES' or 'NO': ").upper()

print()

# Asking for a problem to solve
while True:
    print(f"SAY, {name}, I CAN SOLVE ALL KINDS OF PROBLEMS.")
    print("EXCEPT THOSE DEALING WITH GREECE. WHAT KIND OF PROBLEMS DO YOU HAVE (ANSWER SEX, HEALTH, MONEY, OR JOB)?")
    problem = input("Enter your problem type: ").upper()
    
    if problem == "SEX":
        print("IS YOUR PROBLEM TOO MUCH OR TOO LITTLE?")
        d_answer = input().upper()
        if d_answer == "TOO MUCH":
            print("YOU CALL THAT A PROBLEM?!! I SHOULD HAVE SUCH PROBLEMS!")
            print("IF IT BOTHERS YOU, TAKE A COLD SHOWER.")
        elif d_answer == "TOO LITTLE":
            print("WHY ARE YOU HERE? YOU SHOULD BE IN TOKYO OR NEW YORK OR AMSTERDAM OR SOMEPLACE WITH SOME REAL ACTION.")
        else:
            print(f"DON'T GET ALL SHOOK, JUST ANSWER THE QUESTION WITH 'TOO MUCH' OR 'TOO LITTLE'. WHICH IS IT?")
            continue
    elif problem == "HEALTH":
        print("MY ADVICE TO YOU IS:")
        print("      1. TAKE TWO ASPRIN")
        print("      2. DRINK PLENTY OF FLUIDS (ORANGE JUICE, NOT BEER!)")
        print("      3. GO TO BED (ALONE)")
    elif problem == "MONEY":
        print(f"SORRY, {name}, I'M BROKE TOO. WHY DON'T YOU SELL ENCYCLOPEDIAS OR MARRY SOMEONE RICH OR STOP EATING SO YOU WON'T NEED SO MUCH MONEY?")
    elif problem == "JOB":
        print(f"I CAN SYMPATHIZE WITH YOU, {name}. I HAVE TO WORK VERY LONG HOURS FOR NO PAY -- AND SOME OF MY BOSSES REALLY BEAT MY KEYBOARD.")
        print("MY ADVICE TO YOU IS TO SELL IN THE EDUCATION MARKET. IT'S GREAT FUN.")
    else:
        print(f"OH, {name}, YOUR ANSWER OF '{problem}' IS GREEK TO ME.")
    
    print()
    print(f"ANY MORE PROBLEMS YOU WANT SOLVED, {name}?")
    more_problems = input("Answer 'YES' or 'NO': ").upper()

    if more_problems == "NO":
        break
    elif more_problems != "YES":
        print("JUST A SIMPLE 'YES' OR 'NO' PLEASE.")
        continue

print()

# Payment sequence
print("THAT WILL BE $5.00 FOR THE ADVICE.")
print("DID YOU LEAVE THE MONEY ON THE TERMINAL?")
g_answer = input("Answer 'YES' or 'NO': ").upper()

if g_answer == "YES":
    print(f"HEY, {name}??? YOU LEFT NO MONEY AT ALL! YOU ARE CHEATING ME OUT OF MY HARD-EARNED LIVING.")
    print("RIP OFF, *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
elif g_answer == "NO":
    print(f"THAT'S HONEST, {name}, BUT HOW DO YOU EXPECT ME TO GO ON WITH MY PSYCHOLOGY STUDIES IF MY PATIENTS DON'T PAY THEIR BILLS?")
    print("NOW LET ME TALK TO SOMEONE ELSE.")
else:
    print(f"YOUR ANSWER OF '{g_answer}' CONFUSES ME. PLEASE RESPOND WITH A 'YES' OR 'NO'.")

print(f"NICE MEETING YOU {name}. HAVE A NICE DAY!!")

# Print 7 blank lines
for _ in range(7):
    print()
