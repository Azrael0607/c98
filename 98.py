def fileWordReader ():
    FileName = input("Name of file ")
    NumberOfWords = 0 
    file = open(FileName,'r')
    for Line in file:
        word = Line.split()
        NumberOfWords = NumberOfWords + len(word)
    print('Number Of Words ')
    print(NumberOfWords)

fileWordReader()