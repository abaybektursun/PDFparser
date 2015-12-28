# This script cleans the layout like Tide cleans your pants
import re
#/LOElement(.+?)/g

import os
from os      import listdir
from os.path import isfile, join,exists
from os      import makedirs
from os      import walk

#debug###############
recursionStack = 0
#debug###############


# Watch out, we got 'recursion' over here                                                                                                                                                                                                                                                                                                                                           what?
def shifter(line,layoutElements, recursionStack):

    #debug#############
    recursionStack += 1
    #debug#############
    
    tempList    = []
    replaceLine = ''
    
    #Split the line when a layout element is encountered
    tempList = line.split(layoutElements[0])

    #We do not need to shift down the element if it is the beggining of the line...
    if tempList[0] != '':
        for index, element in enumerate(tempList):
            if index == 0:
                replaceLine = element
            else:
                replaceLine = replaceLine + '\n' + layoutElements[0] + element

    # ...If we chop off the element, bring it back
    else:        
        for index, element in enumerate(tempList):
            if   index == 0:
                replaceLine = layoutElements[0]
            elif index == 1:
                replaceLine = replaceLine + element
            else:
                replaceLine = replaceLine + '\n' + layoutElements[0] + element
            
    layoutElements.pop(0)

    if len(layoutElements) > 0:
        replaceLine = shifter(replaceLine,layoutElements, recursionStack)
        
    #debug##################################################
    #print('Stack #' + str(recursionStack) + ' Returned!\n')
    #print('Results: ' + '\n\n' + replaceLine)
    #debug##################################################
    
    return replaceLine   

# This Just creates the list of possible LO Elements
layoutElementsString = 'LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine'
tempLayoutElements   = layoutElementsString.split(', ')
layoutElements       = []
for element in tempLayoutElements:
    layoutElements.append(element + '(')

# Clean All the Pages
outPageList = []
layoutPath  = r'C:\Projects\PDFparser\pageLayout'
allLayouts  = [x[0] for x in os.walk(layoutPath)]
allLayouts.pop(0)

for a_layoutFolderPath in allLayouts:

    #debug###########################
    #print('\n' + a_layoutFolderPath)
    #debug###########################

    cleanPageLayoutPath = r'C:\Projects\PDFparser\cleanPageLayout'
    cleanLayoutName     = a_layoutFolderPath.split('\\')[-1]
    layoutPages         = [f for f in listdir(a_layoutFolderPath) if isfile(join(a_layoutFolderPath, f))]
    
    if not os.path.exists(cleanPageLayoutPath + '\\' + cleanLayoutName):
        os.makedirs(cleanPageLayoutPath + '\\' + cleanLayoutName)
    
    for a_page in layoutPages:
    
        #debug###############
        #print('\t' + a_page)
        #debug###############
        
        layoutFile = open(a_layoutFolderPath + '\\' + a_page)
        for index, line in enumerate(layoutFile):
            layoutElementsSwapper = list(layoutElements)
            outPageList.append(shifter(line,layoutElements, recursionStack))
            layoutElements = list(layoutElementsSwapper)
        
        outPageFile = open(cleanPageLayoutPath + '\\' + cleanLayoutName + '\\' + a_page, 'w')
        
        for line in outPageList:
            outPageFile.write(str(line))
            
        outPageList = []
