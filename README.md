# WtfPy


### This module is created to:
  - Track variables
  - Search in variables
  - Help unit testing
  - Modify variables and log modifications
  - Make easy the memory management
  -	Gathering information about your memory usage

## Version 0.0.2
### Examples
```python
	import wtf 

	wtf.vhl # VARIABLEHANDLER

	wtf.vhl.CrtNewDB(VARIABLE, STOREDNAME) # CREATE NEW DATA BLOCK

	wtf.vhl.GetAllDB() # GET ALL DATA BLOCKS

	wtf.vhl.SrcSingleDB(STOREDNAME) # SELECT SINGLE DATA BLOCK

	wtf.vhl.DelSingleDB(STOREDNAME) # DELETE SINGLE DATA BLOCK

	wtf.GetRuntmDataVal(VARIABLE, DISPLAYNAME) # GET RUNTIME DATA VALUE
	wtf.SetRuntmDataVal(VARIABLE, NEWVALUE, DISPLAYNAME) # SET RUNTIME DATA VALUE
	wtf.MemAddr(VARIABLE) # GET MEMORY ADDRESS OF A VARIABLE
	wtf.RefCheck(FIRSTVARIABLE, SECVARIABLE) # CHECK IF TWO VARIABLES ARE REFERENCING TO THE SAME MEMORY ADDRESS
	wtf.GetSize(VARIABLE) # GET SIZE OF A VARIABLE
	wtf.EchoTurnOff() # TURN OFF CONFIRMATION MESSAGES FROM VHL
	wtf.deRef(VARIABLE) # DE-REFERENCE A VARIABLE
```
# Data blocks
Data blocks are stored in a 2D array with their
size, name(Set by user) and memory address.
I implemented a standard data block just to check
that it's working. You can remove it if you want.
This data block is 'STD'.
You can search inside this data block array, you
can delete blocks and add blocks.


