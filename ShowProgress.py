

def show(current, finishvalue):    
    print 'progress : ', current,'/', finishvalue,
    if (current < finishvalue):
        print '\r',
    else:
        print
def check():
    for i in range(100000):
        show(i+1, 100000)

check()