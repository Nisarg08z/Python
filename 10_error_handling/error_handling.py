file = open('youtube.txt', 'w')

try:
    file.write('hello')
finally:
    file.close()
    
    
with open('youtube.txt', 'w') as file:
    file.write('hello')
    