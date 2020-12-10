import numpy
import WtfPy
from WtfPy import vhl

x = 15
i = 15
name = "Joe"
pi = 3.14
ld = numpy.random.uniform(0.0, 5.0, 1250)
#Adding variables to WtfPy's variable dict. as data blocks.
WtfPy.vhl.CrtNewDB(x, "X")
WtfPy.vhl.CrtNewDB(pi, "Pi")
WtfPy.vhl.CrtNewDB(i, "for i")
WtfPy.vhl.CrtNewDB(name, "STR")
WtfPy.vhl.CrtNewDB(ld, "BIG D")

#Get all data blocks to see what's in our dict.
WtfPy.vhl.GetAllDB()

#Deleting data block named ,,Pi''
WtfPy.vhl.DelSingleDB("Pi")

#Let's see, if we deleted Pi
WtfPy.vhl.GetAllDB()

#Doing reference check with x and i
WtfPy.RefCheck(x,i)

#Get current value of x
WtfPy.GetRuntmDataVal(x, "X's value")

#Change value of x
x = 11

#Get updated value of x
WtfPy.GetRuntmDataVal(x, "X after change")

#Doing reference check again
WtfPy.RefCheck(x,i)

#Set the first value of x
x = 15

#Doing reference check again
WtfPy.RefCheck(x,i)

#Dereference x
x = WtfPy.deRef(x)

#Doing reference check again
WtfPy.RefCheck(x,i)

#Get size of x after dereferencing
print("Size of X: ", WtfPy.GetSize(x))
