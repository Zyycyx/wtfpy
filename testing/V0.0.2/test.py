import WtfPy as wtf
from WtfPy import vhl

print("=======================================================================")
x = 1
y = 2

wtf.vhl.CrtNewDB(x, "x") # Create a new data block

wtf.vhl.GetAllDB() # Get all data blocks

wtf.vhl.SrcSingleDB("x") # Search for a single data block by it's name

wtf.vhl.DelSingleDB("x") # Delete a data block by it's name

wtf.GetRuntmDataVal(y, "y") # Get runtime value of a variable
wtf.SetRuntmDataVal(y, 3, "y") # Set runtime value of a variable
wtf.MemAddr(y) # Get memory address of a variable (the reference address)
wtf.RefCheck(y, x) # Check if two variables are referencing to the same address
wtf.GetSize(y) # Get size of a variable
wtf.EchoTurnOff() # Turn off confirmation messages from VHL
wtf.deRef(y) # De-reference a variable
wtf.um.getMemoryUsage()
wtf.um.getCPUUsage()
print("=======================================================================")
