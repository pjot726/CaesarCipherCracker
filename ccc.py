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


if __name__ == '__main__':
    # Import the data from words.txt
    with open('words.txt') as rawText:
        wordList = set(rawText.read().split())
    print('fox' in wordList)
