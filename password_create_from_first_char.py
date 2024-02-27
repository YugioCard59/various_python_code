'''
Course assignment.  Create password from sentence given.
First char of each word is either returned as is
or is replaced by a different char as given.
'''


def createPassword(sentence):
    password = ""
    takeNextChar = True
    originalChars = "OoSslbqAi"
    replace = "00551694!"
    for char in sentence:
        #condition for alphanumeric case insensitive char
        if char.isalnum():
            #start loop to check if char needs replacing
            if takeNextChar:
                for index in range(len(originalChars)):
                    tempChar = originalChars[index]
                    if char == originalChars[index]:
                        tempChar = replace[index]
                        char = tempChar
                        password += char
                        #if char is replaced set condition to false
                        takeNextChar = False
            #if replacement not needed place alphanumerical char in pw
            if takeNextChar:
                password += char
                #if char added to pw then condition sets to false
                #return to .isalum(), since conditions set to false
                #conditionals do not run, loop is exhausted until char
                #not alphanumerical
                takeNextChar = False
        #condition for space char
        elif char == ' ':                     
            # New word!
            takeNextChar = True
        #condition for punctuation char
        else:                                  
            password += char
            takeNextChar = False             
        print(f"{char} added to {password} password.")

    return password

def main():
    #sentence = "Do or do not. There is no try."
    sentence = "The quick brown fox jumped over the lazy, silly, Amazing, impatient dog in 2024."
    # sentence = input("Give a sentence: ")
    # predicted = "Dodn.Tint."
    # predicted = "Tqbfjotldi2."
    # predicted = "T96fj0t1d."
    password = createPassword(sentence)
    print(f'Sentence for password "{sentence}" is "{password}".')

main()
