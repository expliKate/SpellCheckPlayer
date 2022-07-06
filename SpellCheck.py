import Levenshtein
import PySimpleGUI as psguy

# Here is the original contents of the window that the user sees.
thisLay = [[psguy.Text('Welcome to the SpellCheck Player.\nThis is where you will play around with spellcheck settings.\
    \nA typical spellchecker will tell you if a word is spelled correctly based on some reference word.\
    \nThis SpellCheck player instead tells you how closely any two words or phrases match.\
    \nA score of 1 means an exact match, and anything less than that is a partial match.', key = 'lblInfo')],
        [psguy.Text('Enter your reference word ("correctly" spelled) here:', key = 'lbl1')],
        [psguy.Input()],
        [psguy.Text('Enter the word you are checking against that reference here:', key = 'lbl2')],
        [psguy.Input()],
        [psguy.OK('Check Spelling')]]

thisWin =psguy.Window('SpellCheck Player', thisLay, margins=(100, 50))

# This loop waits for the user to click "Check Spelling" or close the window, taking the expected action when the user does so.
while True:
    event, values = thisWin.read()
    if event == 'Check Spelling':
        # Parse the input into useful variable names
        myTarg = values[0]
        uIn = values[1]
        # Update just the informational text with the results of the Levenshtein ratio of the two phrases that were input.
        thisWin['lblInfo'].update('The score for ' + myTarg + ' and ' + uIn + ' is: ' + str(Levenshtein.ratio(myTarg.lower(),uIn.lower())))
    if event == psguy.WIN_CLOSED:
        break

thisWin.close()