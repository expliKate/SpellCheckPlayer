import Levenshtein
import PySimpleGUI as psguy

def SpellCheck(target,userInput):
    return str(Levenshtein.ratio(target,userInput))

myTarg = 'Jennifer'
uIn = 'Yennifer'

while True:
    event, values = psguy.Window(title="SpellCheck Player", layout=[[]], margins=(100, 50)).read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == psguy.WIN_CLOSED:
        break

psguy.Window.close()


print('Welcome to the SpellCheckPlayer.')
print('This is a tool to help you play with the setup of a spellchecker.')
print('You are going to enter some words, and instead of getting an answer to the question "Is this word spelled correctly?", you will get an answer to the question "How closely does the second word match the first word?')
print('A score of 1 means an exact match, and anything less than that is an impartial match.')
print('The score for ' + myTarg + ' and ' + uIn + ' is: ' + SpellCheck(myTarg,uIn))
print('Exiting...')