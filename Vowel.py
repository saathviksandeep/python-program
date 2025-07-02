string=input("Enter a word:")

vowels=("a", "e", "i", "o", "u","A", "E", "I", "O", "U")

count=0

for char in string:
    if char in vowels:
        count=count+1

print(count, "vowels were found.")
