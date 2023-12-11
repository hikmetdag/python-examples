# Given two integer numbers, return their product only if the product is equal to or lower than 1000.
#  Otherwise, return their sum.
def sum_or_times(num1, num2):
    product=num1*num2
    if product<=1000:
        return product
    else:
        return num1+num2
    
result= sum_or_times (3, 6)
print(result)
