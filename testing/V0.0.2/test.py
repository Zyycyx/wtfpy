# Current version: 0.0.2.1

import WtfPy as wtf
from WtfPy import vhl

print("======================================================================= \n\n")
x = 1
y = 2

wtf.vhl.CrtNewDB(x, "x") # Create a new data block

wtf.vhl.GetAllDB() # Get all data blocks

wtf.vhl.SrcSingleDB("x") # Search for a single data block by it's name

wtf.vhl.DelSingleDB("x") # Delete a data block by it's name

wtf.RuntmVal(y, "y") # Get runtime value of a variable
wtf.SetRuntmVal(y, 3, "y") # Set runtime value of a variable
wtf.MemAddr(y) # Get memory address of a variable (the reference address)
wtf.RefCheck(y, x) # Check if two variables are referencing to the same address
wtf.GetSize(y) # Get size of a variable
wtf.GetMemoryUsage() # Get  the memory usage of your program
wtf.deRef(y) # De-reference a variable
print("\n\n =======================================================================")
