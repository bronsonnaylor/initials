def get_initials(fullname):
    initials = ""
    names = fullname.split()
    for i in names:
        initials += i[0]
    caps = initials.upper()
    return caps
        
def main():
    print(get_initials(input("What is your full name?")))

if __name__ == '__main__':
    main()
