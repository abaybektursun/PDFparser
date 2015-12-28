import os

from os      import listdir
from os.path import isfile, join,exists
from os      import makedirs

from pdfminer.pdfparser   import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage     import PDFPage
from pdfminer.pdfpage     import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp   import PDFResourceManager
from pdfminer.pdfinterp   import PDFPageInterpreter
from pdfminer.pdfdevice   import PDFDevice
from pdfminer.layout      import LAParams
from pdfminer.converter   import PDFPageAggregator
from pdfminer.layout      import LTTextBox, LTTextLine, LTFigure, LTImage, LTTextLineHorizontal, LTTextBoxHorizontal, LTChar, LTRect, LTLine

# This will be written to a file
layoutStream = []

# Convert the given unicode string to a bytestring, using the standard encoding, unless it's already a bytestring
def to_bytestring (s, enc='utf-8'):

    if s:
        if isinstance(s, str):
            return s
        else:
            return s.encode(enc)

# Thanks to Matt Swain for the function (http://stackoverflow.com/questions/25248140/how-does-one-obtain-the-location-of-text-in-a-pdf-with-pdfminer)
# Original function was modified due to encoding errors and a need to generate files
def parse_layout(layout):                                                  
    """Function to recursively parse the layout tree."""
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)   
        layoutStream.append(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        layoutStream.append(lt_obj.bbox)        
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(to_bytestring(lt_obj.get_text()))  
            layoutStream.append(to_bytestring(lt_obj.get_text()))
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recursive                              


def parsing(pdfPath, pdfFileName):
    fp = open(pdfPath + '\\' + pdfFileName, 'rb')
    parser      = PDFParser(fp)
    document    = PDFDocument(parser)
    rsrcmgr     = PDFResourceManager()
    laparams    = LAParams()
    device      = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pathOut     = r'C:\Projects\PDFparser\pageLayout'
    layoutName  = pdfFileName.split('.', 1)[0].replace(' ','_')
    
    # Create a folder for each pdf file layout
    if not os.path.exists(layoutName):
        os.makedirs(pathOut + '\\' + layoutName)
    for pageNum, page in enumerate(PDFPage.create_pages(document)):
        interpreter.process_page(page)
        layout = device.get_result()
        parse_layout(layout)

        # .pmlo stands for PDFminer Layout
        fileOut = open(pathOut + '\\' + layoutName + '\\' + str(pageNum + 1) + '.pmlo','w')
        
        for line in layoutStream:
            fileOut.write(str(line))

        #Start a new page
        del layoutStream[:]

    fp.close()  
    
    
pdfPath = r'C:\Projects\PDFparser\samplePDFs'
pdfFileNames = [f for f in listdir(pdfPath) if isfile(join(pdfPath, f))]
for pdfFileName in pdfFileNames:
    parsing(pdfPath, pdfFileName)
    
