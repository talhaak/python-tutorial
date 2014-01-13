# Creating pyg latin translator for a string

# pyg variable which store appendix value
pyg = 'ay'

#Taking input from user.
original = input()
print('Enter a word to translate to pyglatin!')


#Using lower method to create pyg latin word of the string.
name = original.lower()

# Taking first letter of string 
word = name[0]

# Checking conditions is the string appropriate for translation.
if len(original) > 0 and original.isalpha():
    
    # Checking first letter of string to check it is vowel or consonant
    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u" :
        
        # If it is vowel just adding pyg variable to end of string
        new_word = name + pyg
        print(new_word)
    
    else :
        
        # If it is not just taking first letter and adding pyg variable to end of string
        new_word = name[0:1] + pyg
        print(new_word)
    
else:
    print('empty')