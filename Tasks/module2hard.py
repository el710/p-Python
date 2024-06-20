import os, random
from time import sleep


def show(stage=0, code=0, key = 'xx'):
    os.system("cls")
    print("************* The Gate ****************")
    if stage == 0:
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        print("*                                      ")
        print("*                                      ")
        print("*                                      ")        
    elif stage == 1:
        print("*                                      ")
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        print("*                                      ")
        print("*                                      ")        
    elif stage == 2:
        print("*                                      ")
        print("*                                      ")
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        print("*                                      ")        
    else:     
        print("*                                      ")
        print("*                                      ")
        print("*                                      ")        
        print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
        
    
    print("*                                      ")
    print("*       [Code] ----- [Pass]")
    print("*       | %02d | ----- |" % code, key)
    
    if key == 'xx':
        print("************** Closed *****************")
    else:
            print("************** Opened *****************")
                     
def find_key(code):
      my_key = ''
      base_dig = 1
    
      
      while base_dig + 1 < code:
           for i in list(range(base_dig + 1, code - base_dig + 1)):
                my_sum = base_dig + i
                #print(f"{base_dig}: {i} = {my_sum}")
                if code % my_sum == 0:
                     my_key = my_key + str(base_dig) + str(i) + '-'
                     print(f"{base_dig}: {i} = {my_sum}")
                
           base_dig = base_dig + 1

      return my_key
      

stone_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

code = '00'
get_key = 0
show(0)

input("\nPress <Enter> to choose Code...")
for i in stone_1:
    show(1, i)
    #sleep(0.1)

code = random.choice(stone_1)
show(2, code)
input("\nPress <Enter> to findout the Key...")

get_key = find_key(int(code))
show(3, code, get_key)

input("\npress <Enter> to leave...")





