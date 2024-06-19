import os, random
os.system('cls')

def get_number(title="?!"):
    for i in range(2):
        number = int(input(title))
        if number > 0:
            return number
        else:
            print("Try again...",1 - i)
    
    return -1

def make_matrix(rows, cols, means):
    res_m = []
    values = []

    # make random values
    for i in range(means):
        values.append(i)
    
    if rows > 0 and cols > 0 and means > 0:
       for m_row in range(rows):
            res_m.append([])
            for m_col in range(cols):
                res_m[m_row].append(random.choice(values))

    return res_m

def show_matrix(*args): 
    print("Square view:")
    for i in args[0]:
        print(f"show_matrix(): ",i)            


print("Home work with functions...\n")
print("We are making matrix...\n")
m_rows = get_number("input number of rows: ")
if m_rows > 0:
    m_cols = get_number("input number of columns: ")
    if m_cols > 0:
        m_range = get_number("input range of matrix's elements: ")
        if m_range > 0:
            my_matrix = make_matrix(m_rows, m_cols, m_range)
            print("Here our matrix in line view: ", my_matrix)
            show_matrix(my_matrix)
    else: 
        print("We can't make matrix")
else:
    print("We can't make matrix")






input("\npress <Enter> tp leave...")