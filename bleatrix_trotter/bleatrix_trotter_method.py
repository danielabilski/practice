
# script to solve the following challenge: https://codingcompetitions.withgoogle.com/codejam/round/0000000000201bee/0000000000201c8a

import logging
logging.basicConfig(level=logging.NOTSET)

def bleatrix_trotter_method(n: int) -> str:

    numbers = [] # initialize list
    value = 0 # initialize variable

    if n == 0: 
        
        # if bleatrix choose 0 (N), she will count forever, so print INSOMNIA
        value = 'INSOMNIA'
        return value

    while len(numbers) < 10: 
        
        # sum the value of N to the variable "value"
        value += n

        # if we have more than 1 digit in "value" (e.g. 35):
        if len(str(value)) > 1: 
            
            #create a list separating those 2 digits
            v = [str(x) for x in str(value)]

            # append those 2 digits to the original list "numbers"
            numbers.extend(v)
            # remove duplicates to make sure that Bleatrix will see all the number from 0 to 9
            numbers = list(set(numbers))

        else:
            # append value if it's just 1 digit
            numbers.append(str(value))

    return value


# sample data
with open('c-input.txt', 'r') as f:
    numbers = [line.strip() for line in f]

# test cases
x=0
while x < 100:

    for n in numbers[1:]:

        x += 1

        last_num_seen = bleatrix_trotter_method(int(n))

        logging.info(f'Case #{x}: {last_num_seen}')
