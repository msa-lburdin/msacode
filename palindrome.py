
def remove_non_alpha_numeric(sentence):
    #create a variable to store the cleaned sentence
    cleaned = ""

    #loop through each character in the sentence 
    for character in sentence:
    #if the character is alphanumeric, add it to the cleaned sentence
        if character.isalnum():
            cleaned = cleaned + character 
   
    #return the cleaned sentence 
    return cleaned 

def main():
    sentence = "A man, a plan, a canal: Panama"
    cleaned = remove_non_alpha_numeric(sentence)
    #print(cleaned)
    
    backwards = ""
    for index in range(len(cleaned) -1, -1, -1):
        backwards = backwards + cleaned[index]
    print(backwards)
    if cleaned == backwards:
        print(True)
    else:
        print(False)



main()

