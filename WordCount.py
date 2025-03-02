#WordCount.py
#Name: Jacob Oetken
#Date: 03/02/2025
#Assignment: LAB 6


def count_file(fileName): #user can prompt which of the 2 files available (gettysberg.txt or fish.txt) is there a better use than to use a "try"? i used it to prevent the code from throwing an error 
    try:
        textFile = open(fileName, 'r')
    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
        return

    lineCount = 0
    wordCount = 0
    charCount = 0

    for line in textFile:
        lineCount = lineCount + 1 #line count
        wordCount = wordCount + len(line.split()) #split line into words, count them
        charCount = charCount + len(line) #count characters in lines

    print("File Name:", fileName) #outputs
    print("Line Count:", lineCount) #outputs
    print("Word Count:", wordCount) #outputs
    print("Character Count:", charCount) #outputs
    textFile.close()

def main():
    fileName = input("Enter the name of the text file: (gettysberg.txt or fish.txt) ") #ask user for name
    count_file(fileName) #allows users input to be used

if __name__ == '__main__':
    main()