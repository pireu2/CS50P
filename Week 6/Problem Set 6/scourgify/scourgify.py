import csv
import sys

def main():
    students = []
    with open(f"{sys.argv[1]}", "r") as input:
        reader = csv.DictReader(input)
        for row in reader:
            students.append(row)
        for student in students:
            name = student["name"]
            last, first = name.split(",")
            first = first.strip()
            last = last.strip()
            student["first"] = first
            student["last"] = last
            student.pop("name")

    with open(f"{sys.argv[2]}","w") as output:
        fields = ["first","last","house"]
        writer = csv.DictWriter(output, fieldnames = fields)
        writer.writeheader()
        for student in students:
            writer.writerow({"first" : student["first"], "last" : student["last"], "house" : student["house"]})



def check_input():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    try:
        open(f"{sys.argv[1]}", "r")
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")




if __name__ == "__main__":
    main()