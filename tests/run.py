import WtfPy as wtf
import numpy

x = 15
i = 15
name = "Joe"
pi = 3.14
ld = numpy.random.uniform(0.0, 5.0, 1250)
#Adding variables to wtfpy's variable dict. as data blocks.
wtf.vhl.CrtNewDB(x, "X")
wtf.vhl.CrtNewDB(pi, "Pi")
wtf.vhl.CrtNewDB(i, "for i")
wtf.vhl.CrtNewDB(name, "STR")
wtf.vhl.CrtNewDB(ld, "BIG D")

#Get all data blocks to see what's in our dict.
wtf.vhl.GetAllDB()

#Deleting data block named ,,Pi''
wtf.vhl.DelSingleDB("Pi")

#Let's see, if we deleted Pi
wtf.vhl.GetAllDB()

#Doing reference check with x and i
wtf.RefCheck(x,i)

#Get current value of x
wtf.GetRuntmDataVal(x, "X's value")

#Change value of x
x = 11

#Get updated value of x
wtf.GetRuntmDataVal(x, "X after change")

#Doing reference check again
wtf.RefCheck(x,i)

#Set the first value of x
x = 15

#Doing reference check again
wtf.RefCheck(x,i)

#Dereference x
x = wtf.deRef(x)

#Doing reference check again
wtf.RefCheck(x,i)

#Get size of x after dereferencing
print("Size of X: ", wtf.GetSize(x))
