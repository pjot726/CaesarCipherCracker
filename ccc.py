# rotateText
# Input: inputString: String of alphanumeric text to be shifted.
#        offset: integer shift of caesar sipher.
def rotateText(inputString, offset):
    inputString = inputString.lower()
    # These lists are of the English alphabets,
    # for use in the rotation of input strings.
    lowercaseAlpha = ['a', 'b', 'c', 'd', 'e',
                      'f', 'g', 'h', 'i', 'j',
                      'k', 'l', 'm', 'n', 'o',
                      'p', 'q', 'r', 's', 't',
                      'u', 'v', 'w', 'x', 'y',
                      'z']
    resultString = ""
    offsetCharacter = ''
    # Iterate through the input string, and append the corresponding shifted
    # character to the result.
    for character in inputString:
        if character in lowercaseAlpha:
            offsetCharacter = \
                lowercaseAlpha[(lowercaseAlpha.index(character) + offset) % 26]
        else:
            offsetCharacter = character
        resultString = resultString + offsetCharacter
    return resultString

# Return the error score. The lower the score, the more the actual English
# words exist in the string.
def calcErrorScore(inputString, wordList):
    inputList = inputString.split(' ')
    score = 0
    for word in inputList:
        if word not in wordList:
            score = score + 1
    return score

if __name__ == '__main__':
    # Import the data from words.txt
    with open('words.txt') as rawText:
        wordList = set(rawText.read().split())
    # Take in the encoded string.
    inputString = input("Enter your encoded text here.\n")
    # Calculate all possible error scores.
    errorScoreList = []
    for offset in range(26):
        errorScoreList.append(calcErrorScore(rotateText(inputString, offset), \
         wordList))
    # Generate the lowest scoring list.
    idealOffset = errorScoreList.index(min(errorScoreList))
    output = rotateText(inputString, idealOffset)
    # Report the lowest scoring result.
    print("Ideal offset was " + str(idealOffset))
    print("Decoded output was \"" + output +"\"")
