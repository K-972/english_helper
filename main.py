#nothing to say just adding a comment to test pushing on my macbook
import time
import pyperclip


# i don't know what this does or why it is here. but it stays because everytime i remove it my programme breaks
import os
print(os.getcwd())

#################
### main menu ###
#################
def main_menu(main_decision_made):
    main_decision = input("\npetal or petaletal or peel or peecee or peeeel (e to exit) >> ")
    if main_decision == 'petal':
        main_decision_made = True
        petal_function()
    elif main_decision == 'petaletal':
        main_decision_made = True
        petaletal_function()
    elif main_decision == 'peel':
        main_decision_made = True
        peel_function()
    elif main_decision == 'peecee':
        main_decision_made = True
        peecee_function()
    elif main_decision == 'peeeel':
        main_decision_made = True
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
  3: how a theme is presented in a poem
  
  >> """)

    if type_of_petal == '1':
        print('source A\n')
        idea = input('In source A the idea of ...')
        technique = input('is presented through the use of ...')
        quote = input('this is evident through the quote ...')
        zoom_in_word = input('enter ther word you want to zoom in on ...')
        wordclass = input('enter word class of word ...')
        feeling = input('enter feeling created in the readers head, because of the word ...')
        why_it_creates_the_feeling = input('why is the feeling created ...')
        print('\nsource B\n')
        technique_2 = input('enter another technique to explore ...')
        quote_2 = input('enter another quote to explode ...')
        zoom_in_word_2 = input('enter word to zoom in on ...')
        wordclass_2 = input('enter word class of word ...')
        image_constructed = input('enter image constructed in the readers head ...')
        why_it_creates_the_feeling_2 = input('enter why is the feeling created ...')


        petal = (f"In source A the idea of {idea} is presented through the use of {technique} this is evident in the quote \'{quote}\'. the {wordclass} \'{zoom_in_word}\' create\'s a {feeling} feeling in the reader\'s head and presents the idea of {idea} because {why_it_creates_the_feeling}. However in source B the idea of {idea} is presented through the use of {technique_2} this is shown in the quote \'{quote_2}\'. the {wordclass_2} \'{zoom_in_word_2}\' create\'s a {image_constructed} image in the reader\'s head and presents the idea of {idea} because {why_it_creates_the_feeling_2}.\n")

        with open('paragraphs.txt', 'a') as f:
            f.write(petal)

        end_decision = input('\nthis has been written in paragraphs.txt or press c to copy and e to exit >> ')
        if end_decision == 'e':
            quit()
        if end_decision == 'c':
            pyperclip.copy(petal)

    if type_of_petal == '2':
        print('character\n')
        character_name = input('enter character name ... ')
        how_character_is_presented = input('how the character is presented ... ')
        quote = input('enter quote to explode ... ')
        technique = input('enter technique to explore ... ')
        idea_it_gives_the_reader = input('idea it gives the reader ... ')
        zoom_in_word = input('enter word to zoom in on ... ')
        wordclass = input('enter word class of word ... ')
        idea = input('what feeling it constructs in the readers head ... ')
        context_option = input('do you want to input some context y/n >> ')
        if context_option == 'y':
            context_prompt = 'This links to the time period as '
            context = input('this links to the time period as ....   or type n to exit >> ')
            if context == 'n':
                pass
            else:
                petal = (f"In the text, {character_name} is presented as {how_character_is_presented}. This is shown through the quote \'{quote}\'. The use of a {technique} gives the reader the idea that {idea_it_gives_the_reader}. The {wordclass} \'{zoom_in_word}\'construct\'s the {idea} feeling in the reader\'s head. this reinforces the idea of how {character_name} is presented in the text. {context_prompt}{context} and ultimately shows how {character_name} is prestented as {how_character_is_presented} in the text.")
        else:
            petal = (f"In the text, {character_name} is presented as {how_character_is_presented}. This is shown through the quote \'{quote}\'. The use of a {technique} gives the reader the idea that {idea_it_gives_the_reader}. The {wordclass} \'{zoom_in_word}\'construct\'s the {idea} feeling in the reader\'s head. this reinforces the idea of how {character_name} is presented in the text. ")

        with open('paragraphs.txt', 'a') as f:
            f.write(petal)

        end_decision = input('\nthis has been written in paragraphs.txt or press c to copy and e to exit >> ')
        if end_decision == 'e':
            quit()
        if end_decision == 'c':
            pyperclip.copy(petal)


    if type_of_petal == '3':
        print('How a theme is presaented in poetry \n')

        name_of_poem = input('enter the name of the poem ... ')
        theme_presented = input('enter the theme shown ... ')
        theme_shown_through = input(f'{theme_presented} is shown through a ... ')
        quote = input('enter quote you want to explode ... ')
        what_the_quote_shows = input('this quote shows ... ')
        zoom_in_word = input('enter ther word you want to zoom in on ... ')
        wordclass = input('enter word class of word ... ')
        what_it_relates_to = input(f'this shows how {theme_presented} is presented as it has relations to ... ')

        context_option = input('do you want to input some context y/n >> ')
        if context_option == 'y':
            context_prompt = 'This is contextually relevant as '
            context = input(f'{context_prompt}....   or type e to exit ... ')
            if context == 'e':
                pass
            else:
                 petal = (f"in the poem {name_of_poem} the theme of {theme_presented} is shown through {theme_shown_through} . This is evident in the quote \'{quote}\'. This quote shows {what_the_quote_shows}. The {wordclass} \'{zoom_in_word}\' construct\'s how the theme of {theme_presented} is presented as it relates to {what_it_relates_to}. {context_prompt}{context}")
        else:
            petal = (f"in the poem {name_of_poem} the theme of {theme_presented} is shown through {theme_shown_through} . This is evident in the quote \'{quote}\'. This quote shows {what_the_quote_shows}. The {wordclass} \'{zoom_in_word}\' construct\'s how the theme of {theme_presented} is presented as it relates to {what_it_relates_to}")



        with open('paragraphs.txt', 'a') as f:
            f.write(petal)

        end_decision = input('\nthis has been written in paragraphs.txt or press c to copy and e to exit >> ')
        if end_decision == 'e':
            quit()
        if end_decision == 'c':
            pyperclip.copy(petal)
#####################
### peel function ###
#####################

def peel_function():
    type_of_peel = input("""
enter number of what you want
  1: how a character is presented
  2: how a theme is shown
  3: how a -- custom option -- is shown
  
  >> """)

    if type_of_peel == '1':
        print('source A\n')
        what_the_character_is_in = input('is it a book, poem, extract or... ')
        what_the_text_is_called = input('what the text is called ... ')
        character_name = input('enter character name ... ')
        how_character_is_presented = input(f'{character_name} is presented as ... ')
        quote = input('pick a quote that shows this ... ')
        how_it_is_shown = input(f'this quote shows {character_name}\'s {how_character_is_presented} because ... ')

        if what_the_character_is_in == 'extract':

            petal = (f"in the {what_the_character_is_in} from {what_the_text_is_called} the character {character_name} is presented as {how_character_is_presented}. This is shown through the quote \'{quote}\', because {how_it_is_shown}")

        else:

            petal = (f"in the {what_the_character_is_in}, {what_the_text_is_called} the character {character_name} is presented as {how_character_is_presented}. This is shown through the quote \'{quote}\', because {how_it_is_shown}")


        with open('paragraphs.txt', 'a') as f:
            f.write(petal)

        end_decision = input('\nthis has been written in paragraphs.txt or press c to copy and e to exit >> ')
        if end_decision == 'e':
            quit()
        if end_decision == 'c':
            pyperclip.copy(petal)






########################
### WELCOME MESSEDGE ###
########################

# just made this bit for some fun
print('\nwelcome to English-Helper \nBy K972')
time.sleep(3)
start_countdown_number = 5
start_countdown = 0
while start_countdown < 5:
    start_countdown = start_countdown + 1
    print(f'ready in {start_countdown_number}')
    start_countdown_number = start_countdown_number - 1
    time.sleep(1)
print('\nbooted successfully')


##############################
### main menu being called ###
##############################

main_decision_made = False
while main_decision_made == False:
    main_menu(main_decision_made)







