number_of_terms  = int(input('please enter a number: '))

num1 = 0
num2 = 1

# Print the first two Fibonacci numbers
print(num1, num2, end=" ")

count = 2
# loop to generate the fib numbers up to our number_of_term chosen
while count <= number_of_terms :
    next_num = num1 + num2
    print(next_num, end=" ")
    num1 = num2
    num2 = next_num
    count += 1



