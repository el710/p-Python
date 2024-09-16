from os import system
system('cls')


def personal_number(numbers):
    incorrect_data = 0
    result = 0

    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f"wrong data - {i}: {exc}")
    return result, incorrect_data

def calculate_average(numbers):
    average = 0
    try:
        vars = personal_number(numbers)
        average = vars[0] / (len(numbers) - vars[1])
    except ZeroDivisionError as exc:
        # print(f"No numbers: {exc}")
        return 0
    except TypeError as exc:
        print(f"numbers has incorrect type: {exc}")     
        return None

    return average


if __name__ == "__main__":

    
    print(f'Result 1: {calculate_average("1, 2, 3")}')
    print(f'Result 2: {calculate_average([1, "string", 3, "more string"])}')
    print(f'Result 3: {calculate_average(567)}')
    print(f'Result 4: {calculate_average([42, 15, 36, 13])}')
