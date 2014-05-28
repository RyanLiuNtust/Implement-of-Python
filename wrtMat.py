import numpy
import scipy.io

list = ['hello','world']
#save the list into .mat file with char type
#in matlab list(1,:)
#ans = hello
scipy.io.savemat('type1.mat', mdict={'list':list})

list2 = numpy.array(list, dtype=numpy.object)
#save the list into mat with cell type
#list2{1}
#ans = hello
scipy.io.savemat('type2.mat', mdict={'list2':list2})

