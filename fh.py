print ("File handling in python")

list_of_short_word = []

word = "I lol and it was nice on my side"
another_word = 'a man can speak for a women lol'
test_word = ''
seperated = another_word.split(' ')

# print(seperated)
new_word = []
new_i = ''

# for i in seperated:
#     print(i)


with open('file.txt') as temp:
   dataFile = temp.readlines()

for i in range(len(seperated)):
    for line in dataFile:
        if seperated[i] + ':' in line:
        #    i = new_word.append(line.split(i+': '))
           test_word = line.split(seperated[i]+': ')
           test_word = test_word[1]
           seperated[i] = test_word.strip()
           
        #    print(test_word)        
            # new_i = i
            # new_word.append(line.split(i+': '))
            
            
# print (new_word)
# for w in new_word:
#     print (w)
print(seperated)
