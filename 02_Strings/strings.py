h1 = "Hello World"
h2 = "   Hello World   "
h3 = "A B C D"
h4 = "A, B, C, D"
h5 = ["A", "B", "C", "D"]
#print(h1) Hello World

first_char = h1[0]
#print(first_char) H

slice_char = h1[0:6]
# print(slice_char) Hello 

num_lsit = "0123456789"
# print(num_lsit[:]) 0123456789
# print(num_lsit[3:]) 3456789
# print(num_lsit[:7]) 0123456
# print(num_lsit[0:7:2]) 0246

#print(h1.lower()) hello world
#print(h1.upper()) HELLO WORLD
#print(h2.strip()) Hello World
#print(h3.replace("A", "Z")) Z B C D
#print(h3) A B C D
#print(h4.split(", ")) ['A', 'B', 'C', 'D']
#print(h1.find("World")) 6

chai_type = "masala"
quantity = 2
order = "I ordered {} supe of {} chai"

#print(order) I ordered {} supe of {} chai
#print(order.format(quantity, chai_type)) I ordered 2 supe of masala chai

#print("".join(h5)) ABCD
#print(" ".join(h5)) A B C D
#print(", ".join(h5)) A, B, C, D

#print(len(h1)) 11

# for letter in h1:
#     print(letter)

h6 = "A\nB"
#print(h6)


h7 = r"A\nB"
#print(h7) A\nB

#print("Hello" in h1) True
#print("Hello" in h3) False

