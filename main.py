
def is_palindrome(string):
    cleanstring = []

    for char in string:
        if char.isalnum():
            cleanstring.append(char)
        else:
            continue

    fullstring = "".join(cleanstring)
    return fullstring[::-1] == fullstring

def prog_start():
    print("Welcome to the Palindrome Check Application")

    while True:
        word_check = input("Enter in the word or phrase which you wish to check if it is Palindrome:\n")
        if len(word_check) == 0:
            print("Please enter atleast one character")
        else:
            result = is_palindrome(word_check.lower())
            if result:
                print("{} is a palindrome".format(word_check))
            else:
                print("{} is not a palindrome".format(word_check))

            end_simulation = input("Enter Y to end simulation.")

            if len(end_simulation) == 0:
                print("Continuing Simulation")
            elif end_simulation[0].lower() == "y":
                print("Ending Simulation")
                break
            else:
                print("Continuing Simulation")


if __name__ == '__main__':
    prog_start()
