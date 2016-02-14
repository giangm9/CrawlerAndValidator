

def show(current, finishvalue):    
    print 'progress : %2.4f%%' % (float(current * 100) / finishvalue),
    if (current < finishvalue):
        print '\r',
    else:
        print

for i in range(100000):
    show(i+1, 100000)
