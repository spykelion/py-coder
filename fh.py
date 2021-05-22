print ("File handling in python")

list_of_short_word = []

word = "I lol and it was nice on my side"
another_word = 'a man can speak for a women lol'
seperated = another_word.split(' ')
new_word = []
new_i = ''

# for i in seperated:
#     print(i)


with open('file.txt') as temp:
   dataFile = temp.readlines()

for line in dataFile:
    for i in seperated:
        if i + ':' in line:
            new_i = i;
            new_word.append(line.split(i+': '))
            # print(line)
            
    # if 'man'+':' in line:
    #     print("word is found ")
    #     # print(line)
    #     # break
    # else:
    #     print("not found")

# print (new_word)
for w in new_word:
    print (w)
# print(new_word.split(new_i+': '))