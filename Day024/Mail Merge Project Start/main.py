#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []
with open('Input/Names/invited_names.txt') as f:
    names = f.readlines()
    # for name in names:
    #     print(name)
with open('Input/Letters/starting_letter.txt') as f:
    letter = f.readlines()
    for name in names:
        name = name.strip()
        letter_copy = letter.copy()
        # print(letter_copy[0].replace('[name]',name))
        letter_copy[0] = letter_copy[0].replace('[name]',name)
        # print(letter_copy)
        with open(f'Output/ReadyToSend/{name}.txt','w') as file:
            
            
            str = "".join(letter_copy)
            # print(str)
            file.write(str)


    
    
