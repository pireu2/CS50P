import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid Usage")
if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] !="--font":
    sys.exit("Invalid Usage")


fonts = figlet.getFonts()
if len(sys.argv) == 3:
    if sys.argv[2] in fonts:
        figlet.setFont(font=sys.argv[2])
    else:
        sys.exit("Invalid Usage")
else:
    f = random.choice(fonts)
    figlet.setFont(font=f)

string = input("Input: ")
print(figlet.renderText(string))

