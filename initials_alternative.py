def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here

    initials = ""
    cap_initials = ""
    accumulator = 0
    iterator = 0
    lower_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_case = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    #Identifies initials
    for i in fullname:
        if accumulator == 0:
            initials = initials + i
            accumulator += 1
        if i == " ":
            accumulator -= 1

    #Makes sure initials are capitalized.
    for each in initials:
        for caps in upper_case:
            if each == caps:
                cap_initials = cap_initials + caps
        for letter in lower_case:
            if each == letter:
                cap_initials = cap_initials + upper_case[iterator]
            iterator = iterator + 1
        iterator = 0 #forgetting to add this line to reset the iterator caused much frustration!
    return(cap_initials)
        
def main():
    print(get_initials(input("What is your full name?")))

if __name__ == '__main__':
    main()