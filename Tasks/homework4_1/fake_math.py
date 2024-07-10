def divide(first, second):
    if second == 0:
        return 'Error: division by zero'
    else:
        return first / second
    

if __name__ =='__main__':
    print(divide(5, 0))
    print(divide(5, 3))

