# context:
#   the file 'real.txt' and 'imag.txt' are located in the same directory as the script
#   txt files contain one column of float numbers in scientific notation with the size of 19201
#   the last 19201st element is empty string ''
#   the task is to create list of complex data comprised from I and Q data from files 'real.txt' and 'imag.txt'
#   respectively

with open("real.txt") as r, open("imag.txt") as i:
    r_data = 1
    L = list()
    k = 0
    while r_data:
        try:
            k += 1
            r_data = r.readline()
            print(f"line {k}, value: {r_data} of type {type(r_data).__name__}")
            print(float(r_data))
        except ValueError:
            print(f"file reading is over at line {k}")
            break
