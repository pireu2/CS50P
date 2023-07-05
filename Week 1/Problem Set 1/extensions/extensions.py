def main():
    string = input("File Name: ")
    string = string.strip()
    string = string.lower()
    part = string.rpartition(".")
    match part[2]:
        case "gif" | "jpeg" | "png"  :
            print(f"image/{part[2]}")
        case "pdf" | "zip":
            print(f"application/{part[2]}")
        case "txt":
            print(f"text/{part[0]}")
        case "jpg":
            print("image/jpeg")
        case _:
            print("application/octet-stream")

main()
