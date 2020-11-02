# take two number form the user and perform arithmetical operations.

inputNumber1 = float(input("enter the first number:- "))
inputNumber2 = float(input("enter the second number:- "))

# print(inputNumber1)

add = inputNumber1 + inputNumber2
sub = inputNumber1 - inputNumber2
mul = inputNumber1 * inputNumber2
div = inputNumber1 / inputNumber2

print("sum of {0} and {1} is {2}".format(inputNumber1, inputNumber2, add))
print("sub of {0} and {1} is {2}".format(inputNumber1, inputNumber2, sub))
print("mul of {0} and {1} is {2}".format(inputNumber1, inputNumber2, mul))
print("div of {0} and {1} is {2}".format(inputNumber1, inputNumber2, div))