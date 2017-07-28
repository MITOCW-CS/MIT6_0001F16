#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)
#
#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)
#
#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)



####################
## EXAMPLE: perfect squares
####################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
while ans**2 < x:
    ans = ans + 1
if ans**2 == x:
    print("Square root of", x, "is", ans)
else:
    print(x, "is not a perfect square")
    if neg_flag:
        print("Just checking... did you mean", -x, "?")


####################
## TEST YOURSELF!
## Modify the perfect squares example to print
## imaginary perfect sqrts if given a negative num.
####################