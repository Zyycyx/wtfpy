%define name wtfpy-memoman
%define version 0.0.2
%define unmangled_version 0.0.2
%define release 1

Summary: A basic module to work with memory addresses and references.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Zyycyx <peterschmidt5575@gmail.com>
Url: https://github.com/Zyycyx/wtfpy

%description
# WtfPy


### This module is created to:
  - Track variables
  - Search in variables
  - Help unit testing
  - Modify variables and log modifications
  - Make the memory management easier
  - Gather information about your memory usage (vhl)

## Version 0.0.2
### Functions
```python
	import wtf 

	wtf.vhl # Variable handler class

	wtf.vhl.CrtNewDB(variable, storedname) # Create new data block

	wtf.vhl.GetAllDB() # Get all data blockS

	wtf.vhl.SrcSingleDB(storedname) # Select single data block

	wtf.vhl.DelSingleDB(storedname) # Delete single data block

	# Displayname is always optional
	wtf.RuntmVal(variable, displayname) # Get runtime data value
	wtf.SetRuntmVal(variable, newvalue, displayname) # Set runtime data value
	wtf.MemAddr(variable) # Get memory address of a variable
	wtf.RefCheck(first_variable, second_variable) # Check if two variable are referencing to the same memory address
	wtf.GetSize(variable) # Get size of a variable
	wtf.GetMemoryUsage() # Get the memory usage of your program. Displaying in % and MB
	wtf.EchoTurnOff() # Turn off comfirmation messages from VHL
	wtf.deRef(variable) # De-reference a variable
```



# Data blocks
Data blocks are stored in a 2D array with their
size, name(Set by user) and memory address.
I implemented a standard data block just to check
that it's working. You can remove it if you want.
This data block is 'STD'.
You can search inside this data block array, you
can delete blocks and add blocks.




%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
