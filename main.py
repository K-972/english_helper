import time


######################
### PETAL FUNCTION ###
######################

def petal_function():
    type_of_petal = input("""
enter number of what you want
  1: comparing ideas sources a and b
  2: how a character is presented
  3: how a them is presented in a poem""")

    if type_of_petal == '1':
        print('source A\n')
        idea = input('enter idea to explore')
        technique = input('enter technique to explore')
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

        file = open('paragraphs.txt', 'a')
        file.write(petal)

    if type_of_petal == '2':
        print('character\n')
        character_name = input('enter character name')
        how_character_is_presented = input('how the character is presented')
        quote = input('enter quote to explode')
        technique = input('enter technique to explore')
        

        petal = (f"""In the text {character_name} is presented as {how_character_is_presented}. This is shown through the quote 
\'{quote}\'. The use of a {technique}""")

        file = open('paragraphs.txt', 'a')
        file.write(petal)



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


#################
### main menu ###
#################
decision = input("petal or petaletal")
decision = decision.lower()


if decision == 'petal':
    petal_function()
elif decision == 'petaletal':
    petaletal_function()
elif decision == 'peel':
    peel_function()
elif decision == 'peecee':
    peecee_function()
else:
    quit()





