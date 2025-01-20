def sort_digits(number):
    # Input validation

    # Convert the number to a list of digits
    digits = list(str(number))

    # Sort digits in ascending and descending order
    ascending = ''.join(sorted(digits))
    descending = ''.join(sorted(digits, reverse=True))

    # Convert back to integers for display
    ascending_num = int(ascending)
    descending_num = int(descending)

    #print(f"Ascending order: {ascending_num}")
    #print(f"Descending order: {descending_num}")
    return ascending_num, descending_num

def pick_a_number():
    while True:
        try:
            number = int(input("Enter a four-digit number: "))
            if 1000 <= number <= 9999:
                break
            else:
                print("Please enter a valid four-digit number.")
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
    return number

def iterate_sequence(number):

    #print("Starting with ", number)    
    iterations = 0
    while True:
        # Run the function
        low,high = sort_digits(number)
        #print(f"Sorted numbers are {high} and {low}")
        number = high - low
        #print(f"The difference {high} - {low} = {number}")
        #print("New number = ", number)
        iterations += 1
        if (number == 6174):
            break
        if (iterations > 665):
            break
    #print("Number of iterations is ",iterations)    
    return iterations

import time

#iterate_sequence(1001)
for i in range(8999-1):
#number = pick_a_number()
    number = i + 1001
    its=iterate_sequence(number)
    if (its > 665):
        print("Failed with - ",number, its)
        time.sleep(1)
   
    

