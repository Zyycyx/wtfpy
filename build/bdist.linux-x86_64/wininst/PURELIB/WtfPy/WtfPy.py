import sys

#ECHO VARIABLE
toEcho = 0
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
				print("[WTF-DBS] Variable added with name: "+gvnName)
		except:
			print("CNDB - ERROR AT INSERTING TO DBS")
	#GET ALL DATA BLOCKS
	def GetAllDB():
		print("|---------[WTFPY - DBS]---------|")
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
			print("[WTF-DBS] SSDB - DATABLOCK NOT FOUND")

	#DELETE SINGLE DATA BLOCK BY IT'S NAME
	def DelSingleDB(name):
		print("[WTF-DBS] Deleting: "+name)
		for x in dbs:
			for y in x:
				if name == y:
					dbs.remove(x)
					if toEcho == 1:
						print("[WTF-DBS] Removed: "+str(x))

#________FUNCTIONS________

#GET KWARGS DICT
def variable_kwargs(**kwargs):
     return kwargs

#GET RUNTIME DATA VALUE
def GetRuntmDataVal(var, name):
	print("[OUTPUT OF "+str(name)+"]: "+str(var))

#SET RUNTIME DATA VALUE
def SetRuntmDataVal(var, val, name):
	oldvar = var
	var = val
	print("["+str(name)+" is changed TO: "+str(val)+" FROM: "+str(oldvar)+"]")

#GET MEMORY ADDRESS OF A VARIABLE WHAT'S NOT STORED AS A DATA BLOCK
def MemAddr(var):
	return hex(id(var))

#CHECK IF TWO VARIABLES ARE REFERENCED TO THE SAME OBJECTS
def RefCheck(var1, var2):
	if id(var1) == id(var2):
		bln = True
		print("[REFCHECK]: ",bln, "(",var1,",",var2,")")
	else:
		bln = False
		print("[REFCHECK]: ",bln, "(",var1,",",var2,")")

#GET SIZE OF A VARIABLE
def GetSize(var):
	return sys.getsizeof(var)

#SET ECHO OFF
def EchoTurnOff():
	toEcho = 0
	#print(str(toEcho))

#DEREFERENCE VARIABLE BY SETTING IT'S VALUE TO NONE / NULL
def deRef(var):
	var = None
