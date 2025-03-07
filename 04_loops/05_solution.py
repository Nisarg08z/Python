# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

str = "teetsseer"

for s in str:
    if str.count(s) == 1:
        print(s)
        break
    

