#WordIndex.py
#Name: Jacob Oetken
#Date: 03/02/2025
#Assignment: LAB 6

import string

def main():
    fileName = input("Enter the name of the text file: (gettysberg.txt or fish.txt) ")
    
    try:
        textFile = open(fileName, 'r')
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
        return
  
    words = {}  #create an empty dictionary
    lineNum = 0

    for line in textFile:
        lineNum = lineNum + 1
        for word in line.split():
            word = word.translate(str.maketrans('', '', string.punctuation)).capitalize()
            if word in words:
                words[word].append(lineNum)
            else:
                words[word] = [lineNum]

    textFile.close()

    print(f"Word Index for file: {fileName}")
    for word in sorted(words):
        print(word, ":", words[word])

if __name__ == '__main__':
    main()

