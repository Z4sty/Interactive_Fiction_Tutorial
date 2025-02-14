name = input('Enter your name: ')

print(f'Hello, {name}!')

## Start Interactive Fiction

print(""" You are in a room with a table anda a chair.
      
Options:
1. Look under the table
2. Sit down
3. It's finally time to make good use of your carpentering skills!
""")

while True:
    choice = input("What do you do? ")

    if choice == "1":
        print("You find a key under the table.")
        break  
    elif choice == "2":
        print("You sit down and relax.")
        break
    elif choice == "3":
        print("You use your handy carpentering knowledge and combine the table and chair into a nice bed frame.")
        break
    else:
        print("Invalid choice. Try again.\n")