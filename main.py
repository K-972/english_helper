#nothing to say just adding a comment to test pushing on my macbook
import time


# i don't know what this does or why it is here. but it stays because everytime i remove it my programme breaks
import os
print(os.getcwd())

#################
### main menu ###
#################
def main_menu(main_decision_made):
    main_decision = input("petal or petaletal or peel or peecee or peeeel (e to exit) >> ")
    if main_decision == 'petal':
        main_decision_made = True
        return main_decision_made
        petal_function()
    elif main_decision == 'petaletal':
        main_decision_made = True
        return main_decision_made
        petaletal_function()
    elif main_decision == 'peel':
        main_decision_made = True
        return main_decision_made
        peel_function()
    elif main_decision == 'peecee':
        main_decision_made = True
        return main_decision_made
        peecee_function()
    elif main_decision == 'peeeel':
        main_decision_made = True
        return main_decision_made
        peeeel_function()
    elif main_decision == 'e':
        quit()
    else:
        pass


######################
### PETAL FUNCTION ###
######################

def petal_function():
    type_of_petal = input("""
enter number of what you want
  1: comparing ideas sources a and b
  2: how a character is presented
  3: how a them is presented in a poem
  
  >> """)

    if type_of_petal == '1':
        print('source A\n')
        idea = input('In source A the idea of ...')
        technique = input('is presented through the use of ...')
        quote = input('enter quote to explode')
        zoom_in_word = input('enter word to zoom in on')
        wordclass = input('enter word class of word')
        feeling = input('enter feeling created in the readers head')
        why_it_creates_the_feeling = input('why is the feeling created')
        print('\nsource B\n')
        technique_2 = input('enter another technique to explore')
        quote_2 = input('enter another quote to explode')
        zoom_in_word_2 = input('enter word to zoom in on')
        wordclass_2 = input('enter word class of word')
        image_constructed = input('enter image constructed in the readers head')
        why_it_creates_the_feeling_2 = input('enter why is the feeling created')


        petal = (f"""In source A the idea of {idea} is presented through the use of {technique} this is evident in the quote \'{quote}\'.
the {wordclass} \'{zoom_in_word}\' create\'s a {feeling} feeling in the reader\'s head and presents the idea of {idea} because
{why_it_creates_the_feeling}. However in source B the idea of {idea} is presented through the use of {technique_2} this is
shown in the quote \'{quote_2}\'. the {wordclass_2} \'{zoom_in_word_2}\' create\'s a {image_constructed} image in the reader\'s 
head and presents the idea of {idea} because {why_it_creates_the_feeling_2}.\n""")

        with open('paragraphs.txt') as f:
            f.write(petal)

    if type_of_petal == '2':
        print('character\n')
        character_name = input('enter character name')
        how_character_is_presented = input('how the character is presented')
        quote = input('enter quote to explode')
        technique = input('enter technique to explore')
        idea_it_gives_the_reader = input('idea it gives the reader')
        zoom_in_word = input('enter word to zoom in on')
        wordclass = input('enter word class of word')
        idea = input('what feeling it constructs in the readers head')
        context_option = input('do you want to input some context y/n')
        if context_option == 'y':
            context_prompt = 'This links to the time period as '
            context = input('this links to the time period as ....   or type n to exit')
            if context == 'n':
                pass
            else:
                petal = (f"""In the text, {character_name} is presented as {how_character_is_presented}. This is shown through the quote 
                \'{quote}\'. The use of a {technique} gives the reader the idea that {idea_it_gives_the_reader}. The {wordclass} \'{zoom_in_word}\'
                construct\'s the {idea} feeling in the reader\'s head. this reinforces the idea of how {character_name} is presented in the text. 
                {context_prompt}{context} and ultimately shows how {character_name} is prestentd as {how_character_is_presented} in the text.""")
        else:
            petal = (f"""In the text, {character_name} is presented as {how_character_is_presented}. This is shown through the quote 
            \'{quote}\'. The use of a {technique} gives the reader the idea that {idea_it_gives_the_reader}. The {wordclass} \'{zoom_in_word}\'
            construct\'s the {idea} feeling in the reader\'s head. this reinforces the idea of how {character_name} is presented in the text. 
            """)

        with open('paragraphs.txt') as f:
            f.write(petal)



########################
### WELCOME MESSEDGE ###
########################

print('welcome to English-Helper \nBy K972')
time.sleep(3)
start_countdown_number = 5
start_countdown = 0
while start_countdown < 5:
    start_countdown = start_countdown + 1
    print(f'ready in {start_countdown_number}')
    start_countdown_number = start_countdown_number - 1
    time.sleep(1)
print('booted successfully')


##############################
### main menu being called ###
##############################

main_decision_made = False
while main_decision_made == False:
    main_menu(main_decision_made)







