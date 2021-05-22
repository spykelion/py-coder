another_word = 'reach to me asap. in my dm'
test_word = ''

def remove_shorthand(word = '', file = 'file.txt'):
    test_word = ''
    new_word = ''
    seperated = word.split(' ')
    for i in range(len(seperated)):
        seperated[i] = seperated[i].strip('\.') # remove all periods after a word
    
    # open the file in read mode
    with open(file) as temp:
        dataFile = temp.readlines()

    # loop through file word and file to check for shorthand occurrences.
    for i in range(len(seperated)):
        for line in dataFile:
            if seperated[i] + ':' in line:
                test_word = line.split(seperated[i]+': ') # create list of seperated word
                test_word = test_word[1] # grab the second index in list
                seperated[i] = test_word.strip('\n')

    for i in range(len(seperated)):
        new_word += seperated[i] + ' '

    return new_word;
# remove_shorthand("meet me in the morning asap", "file.txt")