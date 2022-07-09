def max_num(a, b, c):
    if (a > b and a > c):
        print(str(a),'is the largest number.')
    elif (b > a and b > c):
        print(str(b),'is the largest number.')
    elif (c > a and c > b):
        print(str(c),'is the largest number.')
    elif (a == b and a > c):
        print(str(a),'and,',str(b),'are equal and greater than',str(c)+'.')
    elif (a == c and a > b):
        print(str(a),'and,',str(c),'are equal and greater than',str(b)+'.')
    elif (b == c and b > a):
        print(str(b),'and,',str(c),'are equal and greater than',str(a)+'.')
    elif(a == b == c):
        print(str(a), str(b),'and,',str(c),'are equal.')

# still not sure if this functionwas supposed to be a flexible list so i pulled a flexible list verions of the function off https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
'''
def mult_list(d, e, f, g, h):
    ha = d*e*f*g*h
    print(ha)
'''
def mult_list(*d):
    e = list(d)
    result = 1
    for x in e:
        result = result * x
    print(result)

def rev_string(j):
    k = j[::-1]
    print(k)


#Once agian not sure if this function was supposed to be a flexible list I assume it was and thus this is wrong
#also im probably supoosed to use range would be my guess but i didn't
def num_within(lowest, highest, comparison):
    if(comparison >= lowest and comparison <= highest):
        print('True')
    elif(comparison > highest or comparison < lowest):
        print('False')

#had rip this of a website cause I had no clue howto do any of it https://www.delftstack.com/howto/python/python-pascal-triangle/ tried the first solution but it didn't work for me this the last solution.
def pascal(p):
    for n in range(p):
        print(' '*(p-n), end='')

        print(' '.join(map(str, str(11**n))))




max_num(220, 85, 1000)
mult_list(2, 5, 3, 5, 3)
rev_string('January Jones')
num_within(1, 10, 1)
pascal(5)