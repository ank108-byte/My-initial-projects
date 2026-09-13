import random
#print("\u25cF \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘
dice_art={1:("┌─────────┐",
             "│         │",
             "│    ●    │",
             "│         │",
             "└─────────┘"),
          2:("┌─────────┐",
             "│ ●       │",
             "│         │",
             "│       ● │",
             "└─────────┘"),
          3:("┌─────────┐",
             "│ ●       │",
             "│    ●    │",
             "│       ● │",
             "└─────────┘"), 
          4:("┌─────────┐",
             "│ ●     ● │",
             "│         │",
             "│ ●     ● │",
             "└─────────┘"),
          5:("┌─────────┐",
             "│ ●     ● │",
             "│    ●    │",
             "│ ●     ● │",
             "└─────────┘"),
          6:("┌─────────┐",
             "│ ●  ●  ● │",
             "│         │",
             "│ ●  ●  ● │",
             "└─────────┘"),  }
dices=[]
total=0
is_running=True
while is_running:
 rolls=int(input("Enter the no of dices you want to roll:"))
 if rolls==1 or rolls>1:
  is_running=False   
 #elif rolls<1:
 # print("No negative no!")
 elif rolls==0:
  print("No zero!")
 elif rolls<1:
  print("No negative no!")
for die in range(rolls):
    dices.append(random.randint(1,6))
#for dice in dice_art(rolls):
print(f"The no while rolling is given:{dices}")
print("In dice format they are:")
for line in range(5):
  for dice in dices:
    print(dice_art.get(dice)[line],end=" ")  
  print() 
for dice in dices:
    total+=dice
print(f"The sum of total of the digits {total}")