from fpdf import FPDF
from fpdf import Align

class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.add_page()
    
    def add_header(self, text):
        self.set_font("helvetica", "B", 50)
        self.ln(20)
        self.cell(80)
        self.cell(30, 10, text, align = "C")

    def add_image(self, image):
        self.image(image, x = Align.C, y = 70, w = 190, h = 190)

    def add_name(self, name):
        self.set_font("helvetica", size = 20)
        self.set_text_color(255,255,255)
        width = self.get_string_width(f"{name} took CS50")
        self.set_y(135)
        self.set_x((210 - width) / 2)
        self.cell(width, 0, f"{name} took CS50", align = "C")


def main():

    pdf = PDF()
    pdf.add_header("CS50 Shirtificate")
    pdf.add_image("shirtificate.png")
    pdf.add_name(input("Name: "))
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()