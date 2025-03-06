# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food)

Type = "cat"
Age = 3

if Type == "Dog":
    if Age < 2:
        print("Puppy food")
    else:
        print("Adult food")
elif Type == "cat":
    if Age > 5:
        print("Senior cat food")
    else:
        print("junior cat food")
        
