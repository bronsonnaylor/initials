def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    
    #Identifies initials
    initials = ""
    names = fullname.split()
    for i in names:
        initials += i[0]
    caps = initials.upper()
    return caps
        
    #Makes sure initials are capitalized.
        
def main():
    print(get_initials("Oscar the grouch"))
    print(get_initials(input("What is your full name?")))

if __name__ == '__main__':
    main()