import random
shows = ["Waiting for Godot", "Clyde's", "Newsies", "The Prom", "Les Mis", "Fefu and Her Friends", "Carrie", "Spring Awakening",
             "Summer and Smoke", "Great Comet", "Hamilton", "Dear Evan Hansen","The Chairs", "The Ruling Class", "Blasted", "How I Learned to Drive", "Amadeus", "Oklahoma",
             "Company"]
year = ["1952","2021","2011","2016","1986","1977","1988","2006","1948","2016","2015","2016","1958", "1968", "1995","1997", "1979","1943","1970"];
genre = ["Absurdist play","Comedic play", "Dance musical", "bad musical","dramatic musical", "Absurdist play","flop musical", "dramatic musical","dramatic play","actor muso musical","biographical musical","bad musical", "absurdist play", "comedic play", "dramatic play", "dramatic play" ,"dramatic play", "golden age musical",
"Sondheim musical"]
theater = ["John Golden", "Hayes", "Nederlander", "Longacre", "Broadway", "American Place", "Virginia", "Eugene O'Neill", "Music Box", "Imperial", "Richard Rodgers","Music Box", "Phoenix", "Nottingham", "Royal court", "Vineyard", "National","St. James", "Alvin Theatre"]
noms = ["0","5","8","7","12","0","0","11","0","12","16","nine", "0", "0", "0", "0", "7", "0","12"]
stars = ["Kasznar","Uzo Aduba","Jeremy Jordan","Caitlin Kinnunen","Colm Wilkinson","Margaret Harrington","Linzi Hately","Lea Michele", "Maragret Phillips","Josh Groban","Lin Manuel Miranda", "Ben Platt", "Eli Wallach","Derek Godfrey", "Pip Donaghy", "Mary-Louise Parker", "Ian McKellen", "Alfred Drake","Dean Jones"]
produced = ["Michael Myerberg","Second Stage Theater","Disney","The Shubert Organization","Cameron Mackintosh","New York Theatre Strategy", "The Royal Shakespeare Company", "Atlantic theater company", "Margo Jones","The American Repertory Theater", "The Public Theater", "Double Gemini Productions", "The Phoenix Theater","Jules Buck", "Royal Court Theater","T.Schreiber Studio","Her Majesty's Theatre", "The Schubert Organization",
"Harold Prince"]
used = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False, False, False]
num = random.randint(0,len(shows)-1)
def done():
    for x in used:
        if used[x] == False:
            return False
    return True
def correct():
    print("You are correct!")
    i = input("Play again? (Y/N)")
    if i.lower() == "Y".lower() and done() == False:
        Again()
    if done() == True:
        print("Goodbye!")
        quit()


def Again():
    print("_________________________________")
    num = random.randint(0,len(shows)-1)
    if used[num] == True:
        while used[num] == True:
            num = random.randint(0,len(shows)-1)   
    if used[num] == False:
        print("the show is a(n) " + genre[num] + " that was produced in " + year[num] + " at the " + theater[num] + " theater" )
        print("____________________________________________")
        print("tony nominations: " + noms[num])
        print("starring: " + stars[num])
        print("produced by:" + produced[num])
        used[num] = True
        guess = input("your guess: ")
        if guess.lower() == shows[num].lower():
           correct()
        if guess.lower() != shows[num].lower() and num == 4 or num == 9:
            if num == 4 and guess.lower() == "les miserables":
                correct()
            elif num == 9 and guess.lower() == "natasha, pierre, and the great comet of 1812" or guess.lower() == "the great comet of 1812":
                correct()
            else: 
                print("sorry, wrong.")
                again = input("Try again? (Y/N): ")
                if again.lower() == "Y".lower():
                    while guess.lower() != shows[num].lower():
                            if guess.lower() == "hint":
                                print("the title starts with the letter " + shows[num][0])
                                newguess = input("Your guess: ")
                                if newguess.lower() == shows[num].lower():
                                    correct()
                            elif guess!= shows[num] and guess!= "hint":
                                guess = input("your guess:")
                    print("that is correct!")
                    pAgain = input("Play again? (Y/N)")
                    if pAgain.lower() == "Y".lower() and done() == False:
                        Again()
                    elif done() == True:
                        print("Okay! I love you, see you next time")
                        quit()
                elif (again.lower() == "n"):
                    print("Okay! I love you, see you next time")
                    quit()
        elif guess.lower() == "hint":
            print("the title starts with the letter " + shows[num][0])
            newguess = input("Your guess: ")
            if newguess.lower() == shows[num].lower():
                correct()
            else:
                print("sorry, wrong.")
                again = input("Try again? (Y/N): ")
                if again.lower() == "Y".lower():
                    while guess.lower() != shows[num].lower():
                            guess = input("your guess:")
                    print("that is correct!")
                    pAgain = input("Play again? (Y/N)")
                    if pAgain.lower() == "Y".lower() and done() == False:
                        Again()
                    elif done() == True:
                        print("Okay! I love you, see you next time")
                        quit()
        elif guess.lower()!= "hint" and guess.lower!= shows[num] and num!= 4 and num!=9:
            #error here
            print("sorry, wrong.")
            again = input("Try again? (Y/N): ")
            if again.lower() == "Y".lower():
                    while guess.lower() != shows[num].lower():
                            if guess.lower() == "hint":
                                print("the title starts with the letter " + shows[num][0])
                                newguess = input("Your guess: ")
                                if newguess.lower() == shows[num].lower():
                                    correct()
                            elif guess!= shows[num] and guess!= "hint":
                                guess = input("your guess:")
                    print("correct!")
                    pAgain = input("Play again? (Y/N)")
                    if pAgain.lower() == "Y".lower() and done() == False:
                        Again()
                    elif done() == True:
                        print("Goodbye!")
                        quit()
            else:
                print("Okay! I love you, see you next time")
                quit()
print("____________________")
print("Your tweet is my command! Welcome to your theater trivia game")
print("Here's how it works")
print("_____________________")
print("I will randomly generate information about a show, including year and place it was produced, genre, writer, and Tony nominations")
print("you will then guess the title of the play or musical, or request a hint (a hint will reveal the first letter)")
print("You are the love of my life and this is your game.  If you want to change anything about it, let me know.")
play = input("play? (Y/N)")
if play.lower() == "y":
    Again()