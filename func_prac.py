def greeting():
    print('Hello user!')

def pack(x, y, z):
    a = (x, y, z)
    print(list(a))

#looked at the soultion after a few hours diecide to not pay attention to it but it gave me a place to start.
#Works probably should have left some of the eairlier parts of this attpemt alone to show progress but this took long enough as it is.
def eat_lunch(*a):
    b = len(a)

    for i, val in enumerate(a):
        c = 'First I eat '+(val)+'.'
        d = 'Next I eat '+(val)+'.'
        while i < b:
            if (i < b and i <= 0):
                print(c)
            elif (i < b):
                print(d)
            i = i + b
    print('My lunchbox is empty.')

            
    
greeting()
pack('clothes', 'toiletries', 'snacks')
eat_lunch('sandwich','chips', 'pickle','fruit snacks', 'whiskey', 'soda')