import win32gui
import win32print

from lib.shopping_list_interface import ShoppingListInterface

interface = ShoppingListInterface()

# if you just want to use the default printer, you need
# to retrieve its name.
# printer = win32print.GetPrinter()

# open the printer.
import win32ui
from win32con import DMPAPER_A5, DMPAPER_A5_ROTATED, DMRES_MEDIUM, DMRES_LOW

hprinter = win32print.OpenPrinter('HP Deskjet 2540 series (sieć)')
# hprinter = win32print.OpenPrinter('Microsoft Print to PDF')

# retrieve default settings.  this code does not work on
# win95/98, as GetPrinter does not accept two
devmode = win32print.GetPrinter(hprinter, 2)["pDevMode"]

# change paper size and orientation
# constants are available here:
# http://msdn.microsoft.com/library/default.asp?
#      url=/library/en-us/intl/nls_Paper_Sizes.asp
# number 10 envelope is 20
devmode.PaperSize = DMPAPER_A5
devmode.PrintQuality = 300
# devmode.YResolution = 300
# devmode.XResolution = 300
# devmode.FormName=u'a5'
# 1 = portrait, 2 = landscape
devmode.Orientation = 1

# create dc using new settings.
# first get the integer hDC value.  note that we need the name.
hdc = win32gui.CreateDC("WINSPOOL", 'HP Deskjet 2540 series (sieć)', devmode)
# hdc = win32gui.CreateDC("WINSPOOL", 'Microsoft Print to PDF', devmode)
# next create a PyCDC from the hDC.
dc = win32ui.CreateDCFromHandle(hdc)

dc.StartDoc('My Document')
# dc.StartDoc('My Document', 'c:\\Users\\marci\\Documents\\abc.pdf ')
dc.StartPage()
max_length = 0
for item in interface.shopping_list:
    length = dc.GetTextExtent(f'{item.name} {item.amount}\t')[0]
    if length > max_length:
        max_length = length

i = 1
y = 100
for value in interface.shopping_list:
    if i == 49:
        y += max_length
        i = 1
    dc.TextOut(y, i * 100, f'{value.name} {value.amount}')
    i += 1

# dc.TextOut(100,100, '1Python Prints!')
# dc.MoveTo(100, 102)
# dc.LineTo(1748, 102)
# dc.TextOut(100,200, '2Python Prints!')
# dc.TextOut(100,2400, '3Python Prints!')
# dc.TextOut(100,3400, '4Python Prints!')
# dc.TextOut(100,4400, '5Python Prints!')
# dc.TextOut(100,4900, '6Python Prints!')
dc.EndPage()
dc.EndDoc()

# now you can set the map mode, etc. and actually print.
