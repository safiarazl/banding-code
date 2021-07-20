import timeit

setup_code = "from math import factorial"

statement = """
def cek_urut1(data):
    for kali in range(len(data)):
        for index in range(len(data) - 1):
            if data[index] > data[index+1]:
                return False
        else:
            return True
            break

list1 = [3, 5, 38, 44, 47] 
list2 = [3, 44, 38, 5, 47] 
list3 = [2, 15, 26, 27, 36] 
list4 = [15, 36, 27, 2, 26]

print(cek_urut1(list1)) # true
print(cek_urut1(list2)) # false
print(cek_urut1(list3)) # true
print(cek_urut1(list4)) # false
"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)}")