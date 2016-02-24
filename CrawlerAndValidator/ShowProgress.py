

def show(current, finishvalue):    
    print 'progress : ', current,'/', finishvalue,
    if (current < finishvalue):
        print '\r',
    else:
        print