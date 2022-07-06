import Levenshtein
import PySimpleGUI as psguy

def SpellCheck(target,userInput):
    return str(Levenshtein.ratio(target,userInput))

# TODO: Add remaining text.
# TODO: Add a field for a second term.
thisLay = [[psguy.Text('Welcome to the SpellCheck Player.\nThis is where you will play around with spellcheck settings.\
    \nA typical spellchecker will tell you if a word is spelled correctly based on some reference word.\
    \nThis SpellCheck player instead tells you how closely any two words or phrases match.\
    \nA score of 1 means an exact match, and anything less than that is a partial match.\
    \n\nEnter your reference word ("correctly" spelled) here:')],
          #[psguy.Input()],
          [psguy.Input()],
          [psguy.OK('Check Spelling')]]

thisWin =psguy.Window('SpellCheck Player', thisLay, margins=(100, 50))

while True:
    event, values = thisWin.read()
    if event == 'Check Spelling':
        #TODO: Get actual values
        myTarg = 'Jennifer'
        uIn = 'Yennifer'
        #TODO: Display these results in the window instead of the terminal
        print('The score for ' + myTarg + ' and ' + uIn + ' is: ' + SpellCheck(myTarg,uIn))
    if event == psguy.WIN_CLOSED:
        break

thisWin.close()