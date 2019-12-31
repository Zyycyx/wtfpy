import sys
from array import *

#PREDEFINED VARIABLES
__author__= "Speti03@gmail.com"
__version__= "A0.1.BETA"


#ECHO VARIABLE
toEcho = 1
#DEFAULT INTEGER TO TEST DATA BLOCKS
dInt = 255

#2D ARRAY TO STORE DATABLOCKS
dbs = [
	#STORING STANDARD DATA BLOCK WITH NAME: 'STD'
        [sys.getsizeof(dInt), "STD", hex(id(dInt))]
      ]

#__________CLASSES__________

#VARIABLE HANDLER
class vhl:

	"""THIS IS THE VARIABLE HANDLER CLASS"""

	#CREATE NEW DATA BLOCK
	def CrtNewDB(var, gvnName):
		gvnSize = sys.getsizeof(var)
		gvnMemAddr = hex(id(var))
		try:
			#print(toEcho) Just in case of echo is throwing error

			#INSERTING TO THE TOP, AFTER STANDARD BLOCK
			dbs.insert(1,[gvnSize, gvnName, gvnMemAddr])
			if toEcho == 1:
				print("Variable added with name: "+gvnName)
		except:
			print("CNDB - ERROR AT INSERTING TO DBS")
	#GET ALL DATA BLOCKS
	def GetAllDB():
		print("|SIZE\t|NAME\t|Mem. Addr\t|")
		print("--------------------------------|")
		for x in dbs:
                	for y in x:
                        	print(y, end = "\t|")
                	print("\n--------------------------------|")

	#SEARCH FOR SINGLE DATA BLOCK BY IT'S NAME
	def SrcSingleDB(name):
		print("Searching for: " + name)
		try:
			for x in dbs:
				for y in x:
					if name == y:
						print("SIZE | NAME | Mem Addr. |")
						print(x)
						print("--------------------------------|")
		except:
			print("SSDB - DATABLOCK NOT FOUND")

	#DELETE SINGLE DATA BLOCK BY IT'S NAME
	def DelSingleDB(name):
		print("Deleting: "+name)
		try:
			for x in dbs:
				for y in x:
					if name == y:
						dbs.remove(x)
						if toEcho == 1:
							print("Removed: "+x)
		except:
			print("DSDB - DATABLOCK NOT FOUND")

#________FUNCTIONS________

#GET CREDITS AND INFORMATION
def GetCredits():
	print ("AUTHOR: \t"+__author__+"\nVERSION: \t"+__version__)

#GET KWARGS DICT
def variable_kwargs(**kwargs):
     return kwargs

#GET RUNTIME DATA VALUE
def GetRuntmDataVal(var, name):
	print("[OUTPUT OF "+str(name)+"]: "+str(var))

#GET MEMORY ADDRESS OF A VARIABLE WHAT'S NOT STORED AS A DATA BLOCK
def MemAddr(var):
	return hex(id(var))

#CHECK IF TWO VARIABLES ARE REFERENCED TO THE SAME OBJECTS
def RefCheck(var1, var2):
	if id(var1) == id(var2):
		print("[YES] " + str(variable_kwargs(var1 = var1, var2 = var2)) + " are ref. to the same obj.")
	else:
		print("[NO] " +str(variable_kwargs(var1 = var1, var2 = var2))+  " are NOT ref to the same obj.")

#GET SIZE OF A VARIABLE
def GetSize(var):
	return sys.getsizeof(var)

#SET ECHO OFF
def EchoTurnOff():
	toEcho = 0
	#print(str(toEcho))
