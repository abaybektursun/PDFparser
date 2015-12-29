# This script cleans the layout like Tide(c) cleans your pants
import os
import re
import cPickle as pickle


#Temp
from Tkinter import *

from os.path import isfile, join,exists
from os      import makedirs
from os      import listdir
from os      import walk

from time    import sleep


# PDF Miner Layout Object 
class PMLO:
    def __init__(self, rawData):
        self.y       = 0.0
        self.x       = 0.0
        self.width   = 0.0
        self.height  = 0.0
        self.content = ''
        self.type    = ''
        
        self.type    = rawData.split('(')[0]
        coords       = rawData.split('(')[1].replace(')','').split(',')
        self.x       = float(coords[0])
        self.y       = float(coords[1])
        self.width   = float(coords[2])
        self.height  = float(coords[3])
                     
#debug##self.height#############
recursionStack = 0
#debug###############

# Watch out, we got recursion over here                                                                                                                                                                                                                                                                                                                                           what?
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

# This Just creates a list of possible layout elements
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

        # Make each element correspond to a line
        outPageListLines = []
        for element in outPageList:
            if element.count('\n') > 1:
                for a_line in element.split('\n'):
                    #debug
                    #print(a_line)
                    #debug
                    outPageListLines.append(a_line + '\n')
            else:
                #debug
                #print(element)
                #debug
                outPageListLines.append(element)

        listPMLO        = []
        current_obj     = -1
        for line in outPageListLines:
            for counter, a_layoutType in enumerate(layoutElements):
                # There can be only one layout element per line
                # so if one encountered, start reading, and break from loop 
                if a_layoutType in line:
                    current_obj += 1

                    regex_compiled = re.compile(a_layoutType.replace('(','') + "\((.+?)\)")
                    found = regex_compiled.search(line)
                    listPMLO.append( PMLO(found.group() ) )
                    listPMLO[current_obj].content += line.replace(found.group(), '')

                    #debug
                    #print(found.group())
                    #debug
                    
                    break
                
                if counter + 1 == len(layoutElements):
                    if len(listPMLO) != 0: 
                        listPMLO[current_obj].content += line

        # Write the results to a file
        for line in outPageListLines:
            outPageFile.write(str(line))
        
        # Debug ##################
        root = Tk()
        y_dimension = 793.6801
        frame = Canvas(root, width=617.7601, height=y_dimension)
        frame.pack()
        root.update_idletasks()
        
        for index, an_obj in enumerate(listPMLO):
            sleep(0.1)
            the_color = '#' + str( (306000 + index * 3) )
            #frame.delete("all")
            frame.create_rectangle(an_obj.width, an_obj.height, an_obj.x, an_obj.y, fill=the_color)
            # force widget to display
            frame.pack()
            # force refresh of the widget to be sure that thing are displayed
            frame.update_idletasks()
            #print(an_obj.content)

        #root.quit()
        root.destroy()
        # Debug ##################
        
        del outPageList[:]
        del outPageListLines[:]


