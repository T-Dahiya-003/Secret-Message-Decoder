# define a power function that finds the truth by shifting the letter by specific amount
def lassoLetter( letter, shiftAmount ):
    # use the ord power to translate the letter to a special number called its ASCII code 
    letterCode = ord(letter.lower())
    
    # shift the ASCII code to find the true letter's ASCII code
    trueLetterCode = ord("a") + ((letterCode - ord("a"))+shiftAmount) % 26
   
    # reveal the true letter by using the chr power to translate back from ASCII
    return chr(trueLetterCode)

# define a power function that finds the truth by shifting all the letters in a word by specific amount
def lassoWord( word, shiftAmount ):
    trueWord = ""

    for letter in word:
        # invoke the power (function) lassoLetter to reveal the true letter and update the codename trueWord
        trueWord = trueWord + lassoLetter( letter, shiftAmount )

    return trueWord

# example this will return green
print( "Shifting terra by 13 gives: \n" + lassoWord( "terra", 13 ) )


print(lassoWord("WHY",13))
print(lassoWord("oskza",-18))
print(lassoWord("ohupo",-1))
print(lassoWord("ED",25))
