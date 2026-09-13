#hangman_art program
import random
#words=("Coconut","Banana")
words=("Apple","Orange","Mango","Pineapple","Coconut")
hangman_art={0:("    ",
                "    ",
                "    "),
             1:(" o  ",
                "    ",
                "    "),
             2:(" o  ",
                " |  ",
                "    "),
             3:(" o  ",
                "/|  ",
                "    "),
             4:(" o  ",
                "/|\\",
                "    "),
             5:(" o  ",
                "/|\\",
                "/   "),   
             6:(" o  ",
                "/|\\",
                "/ \\")}
#for line in hangman_art[6]:
 #   print(line)
def display_man(wrongguesses):
     print("**************")
     for line in hangman_art[wrongguesses]:
          print(line) 
     print("**************")        
def provide_hint(hint):
    print(" ".join(hint))   
def game_won():
    print("You Won!")
def game_lost():
    print("You lost!")
def display_answer(answer):
     print(" ".join(answer))
     
def main():
    answer=random.choice(words).lower()
    wrongguesses=0
    is_running=True
    guessed_ans=set()
    hint=["_"] * len(answer)
    #print(hint)
    while is_running:
        display_man(wrongguesses)
        provide_hint(hint)
        user_ans=input("Enter the letter you want to make a guess: ")
        if not user_ans.isalpha():
                    print("Only alphabets are allowed!")
                    continue
        if len(user_ans) !=1:
            print("Invalid input(enter one character at a time!)")
            continue
        if user_ans in guessed_ans:
             print(f"{user_ans} is already guessed!")
             continue
        guessed_ans.add(user_ans)
        if user_ans in answer:
             for x in range(len(answer)):
                  if answer[x]==user_ans:
                       hint[x]=user_ans
        else:
            wrongguesses+=1
        if "_" not in hint:
             display_man(wrongguesses)
             display_answer(answer)
             game_won()
             is_running=False
        if wrongguesses >= len(hangman_art) -1 :
             display_man(wrongguesses)
             provide_hint(hint)
             print(f"The answer is:{answer}")
             game_lost()
             is_running=False
if __name__=='__main__':
    main()

