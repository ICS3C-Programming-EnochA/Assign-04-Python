# !/user/bin/env.python3
# Created By: Enoch Amedjrovi
# Created on April 2
# This program will prompt the user to input a positive integer.


def main():

    #It will print out the initial greeting
    print ("Hello and welcome to Enoch math problem")
    user_num_as_string = input("Enter a positive integer = ")
    
    # we are using a try statement 
    try:
        num = int(user_num_as_string)
        if num > 0:
            for counter in range(num, 0, -1):
                if num % counter == 0:
                    print(f"{num} / {counter} = {num / counter}")
        else:
            print("Enter positive numbers only.")
    except:
        print(f"{user_num_as_string} Enter a valid input.")
    finally:
        print("Thank you for playing")
if __name__ == "__main__":
    main()
