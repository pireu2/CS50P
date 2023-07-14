import sys
from PIL import Image
from PIL import ImageOps

def main():
    check_input()
    shirt = Image.open("shirt.png")
    image_input = Image.open(f"{sys.argv[1]}")
    image_output = image_input.copy()

    size = shirt.size
    image_output = ImageOps.fit(image_output,size)
    
    image_output.paste(shirt, (0,0), mask = shirt)

    image_output.save(f"{sys.argv[2]}")
    image_output.show()




def check_input():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _, extension_input = sys.argv[1].split(".")
    _, extension_output  = sys.argv[2].split(".")

    if extension_output != "jpg" and extension_output != "png":
        sys.exit("Invalid output")

    if extension_input != extension_output:
        sys.exit("Input and output have different extensions")

    try:
        Image.open(f"{sys.argv[1]}")
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

if __name__ == "__main__":
    main()