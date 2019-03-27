                                                        # Carter Wrobel
                                                        # 10/24/17
                                                        # CS #186
                                                        # Section 1
'''
    This program will find the sum of cubes for a given number
'''



# for loop
num_list = [10, 20, 100]

for n in num_list:
    cubes = ((n*(n+1))//2)**2
    print (cubes)


print("          ")

# while loop
def sum_of_cubes(n):
    sum = 0
    while (n>0):
        sum += n**3
        n -= 1
    return sum

print(sum_of_cubes(10))
print(sum_of_cubes(20))
print(sum_of_cubes(100))
