import random
class game:
    def __init__(self):
        self.score = 0
        self.Curr_score = 0
        self.Highscore = 0
        
    def readwritewin(self):
        c = open("score.txt", "r")
        self.Highscore = c.read()
        highscore_int = self.Highscore
        c.close()
        if highscore_int == "":
            c = open("score.txt", "a")
            c.write("0")
            c.close()
            self.readwritewin()
        elif int(highscore_int) < self.score:
            c = open("score.txt", "w")
            c.write(str(self.score))
            c.close()
            print("HIGHSCORE:",self.score)
        else:
            print("HIGHSCORE:",highscore_int)
        
    def game(self):
        i = 0
        tryagain = ""
        if startgame == "y":
            while True:
                gamesize = input("Size of the game?\n")
                if gamesize.isdigit() == False:
                    print("Just numbers")
                    continue
                else:
                    randomnumber = random.randint(1,int(gamesize))
                    print("Let's begin")
                    break
        while True:
            i += 1
            if startgame == "n" or tryagain == "n":
                break
            guessnumber = input("What is the number? ")
            listwords = ["than that fuckface", "prick!!", ", what is wrong with you?!", "than that phatass", "little shit", "motherfucker", "fat fuck", "rubbish cunt"]
            if guessnumber.isdigit() == True:
                if randomnumber == int(guessnumber):
                    print("Congratz!!")
                    print("It did take",str(i),"guesses to win")
                    print("The number was",randomnumber)
                    self.score = int(int(gamesize)/i)
                    print("Your score is:",self.score)
                    self.readwritewin()
                    while True:
                        tryagain = input("Try again? y|n\n")
                        if tryagain == "y":
                            obj.game()
                        elif tryagain == "n":
                            break
                        else:
                            continue
                elif int(guessnumber) < randomnumber:
                    print("Higher",random.choice(listwords))
                elif int(guessnumber) > randomnumber:
                    print("Lower",random.choice(listwords))
                else:
                    print("That's not a number shithole")
                    continue
            elif guessnumber.isdigit() == False:
                continue
            else:
                break
startgame = input("Guess the number with a twist\nStart the game? y|n\n")
obj = game()
obj.game()
