# TODO: Add header

import Levenshtein
import PySimpleGUI as psguy

# Here is the original contents of the window that the user sees.
thisLay = [[psguy.Text('Welcome to the SpellCheck Player.\nThis is where you will play around with spellcheck settings.\
    \nUse the slider to choose a threshold for your spellchecker. (1 means exact matches only.)\
    \nThen enter a "correctly" spelled word and a word to spell-check against that.', key = 'lblInfo')],
        [psguy.Text('Select the threshold spellcheck score:', key = 'sld1')],
        [psguy.Slider(range=(0,1), default_value=0.87, resolution=0.01, size=(20,15), orientation='horizontal', key = 'sld01')],
        [psguy.Text('Enter your reference word ("correctly" spelled) here:', key = 'lbl1')],
        [psguy.Input(key='inp01')],
        [psguy.Text('Enter the word you are checking against that reference here:', key = 'lbl2')],
        [psguy.Input(key = 'inp02')],
        [psguy.Text('\n', key = 'lblOutput')],
        [psguy.OK('Check Spelling')]]

thisWin =psguy.Window('SpellCheck Player', thisLay, margins=(100, 50))

# This loop waits for the user to click "Check Spelling" or close the window, taking the expected action when the user does so.
while True:
    event, values = thisWin.read()
    if event == 'Check Spelling':
        # Parse the input into useful variable names
        threshold = float(values['sld01'])
        myTarg = values['inp01']
        uIn = values['inp02']
        # Get the Levenshtein distance.
        score = Levenshtein.ratio(myTarg.lower(),uIn.lower())
        
        # Display results and update background color to match.
        if score > threshold:
            op = 'PASS'
            thisWin['inp01'].update(background_color='teal')
            thisWin['inp02'].update(background_color='teal')
        else:
            op = 'FAIL'
            thisWin['inp01'].update(background_color='#7a1726')
            thisWin['inp02'].update(background_color='#7a1726')

        # This will update just the informational text with the results of the Levenshtein ratio of the two phrases that were input (used this before adding the slider)
        # thisWin['lblInfo'].update('The score for ' + myTarg + ' and ' + uIn + ' is: ' + score)

        # Update output text.
        thisWin['lblOutput'].update(op + ' (score: ' + str(round(score,2)) + ')\n')

    if event == psguy.WIN_CLOSED:
        break

thisWin.close()