import os

os.system('cls')

print("Make function to parse data structures...\n")

def parse_sum(*args):
    '''
      function parse_sum(*args) counts sum of digits & string lengths in tuff structures
      returns summary
    '''
    result = 0

    # print(f"\n-parse_sum(): args - ", args[0])
    # print(f"-parse_sum(): len - ", len(args[0]))

    for i in args[0]:
        if isinstance(i, str):
           result += len(i)
           print(f"{i}: result + {len(i)}")
        elif  isinstance(i, int) or isinstance(i, float):
            result += i
            print(f"{i}: result + {i}")
        elif  isinstance(i, dict):
            print(f"\n-parse_sum(): item - ", i)
            print(f"-parse_sum(): len - ", len(i))            
            for d_key in dict(i).keys():
                result += len(d_key)
                print(f"{d_key}: result + {len(d_key)}")
            for d_val in dict(i).values():
                if isinstance(d_val, int) or isinstance(d_val, float):
                    result += d_val
                    print(f"{d_val}: result + {d_val}")
                elif isinstance(d_val, str):
                    result += len(d_val)
                    print(f"{d_val}: result + {len(d_val)}")
        else:
            print(f"\n{i}: --- parse")
            result += parse_sum(i)

    print(f"---from {args[0]} have got {result}")    

    return result


data_structure = [ [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ( (), [{ (2, "Urban", ('Urban2', 35) ) }] ) ]

print(f"Our example: {data_structure} \n")

print("Get sum of digits & lengths of strings: ", parse_sum(data_structure))

input("\npress <Enter> to leave...")