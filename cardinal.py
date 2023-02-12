from random import randint

import gtts
from playsound import playsound
from num2words import num2words


def guess_cardinal_num(min=1, max=100):
    # initial number
    random_num = randint(min, max)
    num_text = num2words(random_num, lang='es')

    tts = gtts.gTTS(str(random_num), lang="es")
    tts.save("num.mp3")
    playsound("num.mp3")
    print(num_text)

    while True:
        answer_number = input("Enter correct number: ")
        if answer_number == "q":
            break
        elif int(answer_number) == random_num:
            print(f'Correct! {num_text} is {random_num}')

            # generate a new number
            random_num = randint(1, 100)
            num_text = num2words(random_num, lang='es')
            tts = gtts.gTTS(str(random_num), lang="es")
            tts.save("num.mp3")
            playsound("num.mp3")
            print(num_text)

        elif int(answer_number) != random_num:
            print(f'Not correct! {num_text} is not {answer_number}, try again!')
            playsound("num.mp3")
