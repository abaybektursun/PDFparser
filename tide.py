# This script cleans the layout like Tide cleans your pants
import re
#/LOElement(.+?)/g

from os      import listdir
from os.path import isfile, join,exists
from os      import makedirs

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
        
    #debug#################DELETE
    #print('Stack #' + str(recursionStack) + ' Returned!\n')
    #print('Results: ' + '\n\n' + replaceLine)
    #debug#################DELETE
    
    return replaceLine   

# This Just creates the list of possible LO Elements
layoutElementsString = 'LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine'
tempLayoutElements   = layoutElementsString.split(', ')
layoutElements       = []
for element in tempLayoutElements:
    layoutElements.append(element + '(')

# Clean All the Pages
outFileList     = []
layoutPath      = r'C:\Projects\PDFparser\pageLayout\05_28_2015_Blankenship_MD_Charles'
layoutFileNames = [f for f in listdir(layoutPath) if isfile(join(layoutPath, f))]
layoutFile      = open(r'C:\Projects\PDFparser\pageLayout\05_28_2015_Blankenship_MD_Charles\1.pmlo')

for index, line in enumerate(layoutFile):
    layoutElementsSwapper = list(layoutElements)
    outFileList.append(shifter(line,layoutElements, recursionStack))
    layoutElements = list(layoutElementsSwapper)

   
for line in outFileList:
    #outlayoutFiles.write(line)
    print(line)