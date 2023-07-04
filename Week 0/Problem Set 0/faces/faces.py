def main():
    string=input()
    print(convert(string))


def convert(string):
    string=string.replace(':)','🙂')
    string=string.replace(':(','🙁')
    return string

main()