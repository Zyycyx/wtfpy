#!/usr/bin/python
        ## Itt ki kéne találni hogy tabok alapján nézzem, hogy mennyi tartozik a for alá,
        ## vagy valahogy logikailag keressem ki, mondjuk a addig a sorig olvassa a forhoz
        ## ameddig nem vagyunk egy tabbal kisebbek mint a for eleje vagy nem vagyunk
        ## ugyan azon a szinten.
        ## line.count('    ', 0, 20) >= tabs


def a1(name):
    f = open(name+".py", "r")
    code = f.readlines()
    f.close()
    currentLine = 0
    forActive = False
    whileActive = False
    for line in code:
        currentLine += 1
        tabs = line.count('    ', 0, 20)

        if line.count("for", 0, 5):
            whileActive = False
            forActive = True
            print("It's a for loop with header: ["+' '.join(line.split())+"]")

        elif line.count("while", 0, 10):
            forActive = False
            whileActive = True
            print("It's a while loop with header: ["+' '.join(line.split())+"]")

        elif line.startswith('  '):
            if forActive:print("[FOR]:"+line)
            if whileActive:print("[WHILE]:"+line)

        else:
            exec(line)
        
a1("testInputs/test1")
