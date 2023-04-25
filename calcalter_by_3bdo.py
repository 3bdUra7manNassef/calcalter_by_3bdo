#calcalater dont hav any end
# leys start ヾ(≧▽≦*)o#


#(1) inputs

number_1 = float(input('enter first number:'))
number_2 = float(input('enter second number:'))
#(2) input factor
factor = input('enter factor:')

#(3)tools condion 
if factor == '+':
    e = number_1+number_2
    print(e)
elif factor == '/':
    e = number_1 / number_2
    print(e)
elif factor == '-':
    e = number_1 - number_2
    print(e)
elif factor == '*':
    e = number_1 * number_2
    print(e)
else:
    print('worng !!!')
    
#(4)the while to continue

while True:
    #(5)inputs agin
    number_no_end = float(input('enter number:'))
    #(6)input factor
    factor = input('enter factor:')
    
    #(7)if condion tools
    if factor == '+':
        
        e2 = e+number_no_end
        print(e2)
    elif factor == '/':
        
        e2 = e/number_no_end
        print(e2)
    elif factor == '-':
        e2 = number_no_end - e
        print(e2)
    elif factor == '*':
        e2 = number_no_end*e
        print(e2)
    else:
        print('worng !!!')
