'''
# Thesaurus.com unofficial api
# https://pypi.org/project/thesaurus/

# You can install the module by doing:
# $ pip install thesaurus
# $ pip install googletrans

# If for some reason the dependencies didn't install, you can install them by doing:
# $ pip install requests
# $ pip install beautifulsoup4

# Name: Simon Aizpurua
# Purpose: Build a fast list of synonyms to brainstorm

'''
# Import the necessary modules
from thesaurus import Word
from googletrans import Translator
import sys

import fire as f

# Initialize our translator object
translator = Translator()

# Words that we want to find synonyms for and translate to latin
# @DONE: Have these words read from a file. 
# TODO: Thinking about using a CSV


def translate(word, target='es'):
    word_to_targ_lang = translator.translate(word, dest=target, src='en')
    print("==", word, '->', word_to_targ_lang.text, "==")

    try:
        synonyms = Word(word).synonyms(allowEmpty=False)[:5]
        synonyms_translated = translator.translate(synonyms, dest=target)
        for translated_word in synonyms_translated:
            print(translated_word.origin, ' -> ', translated_word.text)
    except:
        print("Having trouble finding {}. Moving on...".format(word))


if __name__ == '__main__':
    # Load Words in Here
    words = ['Test']

    # Alternatively pass in a file with each word on a new line
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as in_file:
            words = [line.strip().lower() for line in in_file]

    # Begin Translating and Providing Synonyms
    for word in words:
        translate(word)

    # Expected Output
    # == Test -> Prueba ==
    # analysis  ->  análisis
    # approval  ->  aprobación
    # assessment  ->  evaluación
    # attempt  ->  intento
    # check  ->  comprobar

    # f.Fire(translate)