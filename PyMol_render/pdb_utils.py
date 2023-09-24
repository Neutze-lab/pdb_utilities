# pdb_utils.py

from numpy import array
from os.path import abspath, splitext

def replace_Bfactors(myPDB, myArray, selection='CA'):
    '''
    
    Generates a new PDB file with the 'tempFactor' column
                        replaced by both the given array and atom selection. 
                        Used for rendering in PyMol.
    
    Requirements:
        NumPy module
    
    Syntax:
        replace_Bfactors(myPDB, myArray, selection)
    
    Input Arguments:
       - myPDB: Reference PDB structure to read Bfactors from.
       - myArray: 1-D array to write out in the new PDB. 
       - selection:  'All' atoms or 'CA' atoms only.
    
    Output Arguments:
       - Generates a modified version of myPDB with new Bfactors.
    
    Example:
       myFunction('193l.pdb', rand(N,1), 'CA')
       The function above assigns random Bfactors to all '' atoms in the PDB
       Iff parameter N is the same length as the number of 'CA' in the 
    
    Written by Adams Vallejos at Neutze-lab
    
    '''
    
    myPDB = abspath(myPDB)
    selection = selection.upper()
    
    if selection != 'CA' and selection != 'ALL':
        raise TypeError("Unrecognized selection of atoms, use 'CA' or 'All'")
    
    # LOAD PDB DATA
    with open(myPDB, 'r') as f:
        PDB_DATA = f.readlines()
        
#         return PDB_DATA
        # MATCHES ATOMS WITH SELECTION CRITERION
        if selection == 'CA':
            IS_MATCH = [int(bool(line[12:16].strip() == selection)) for line in PDB_DATA if line[0:4] == "ATOM"]
        else:
            IS_MATCH = [int(bool(line[0:6].strip() == 'ATOM')) for line in PDB_DATA if line[0:4] == "ATOM"]

        # TEST IF LENGTH OF ARRAY IS COMPATIBLE WITH SELECTED ATOMS
        if len(myArray) != sum(IS_MATCH):
            raise TypeError("Length of array does not match the atom selection.")

        count = 0
        for row, line in enumerate(PDB_DATA):
            if line[0:4]=='ATOM':
                if IS_MATCH[count]:
                    PDB_DATA[row] = (line[0:60] + 
                            f'{myArray[sum(IS_MATCH[0:count ])][0]:>6.2f}' + 
                            line[66:])
                else:
                    PDB_DATA[row] = (line[0:60] + 
                            f'{-1:>6.2f}' + 
                            line[66:])
                count += 1
    
    # GENERATE THE OUTPUT NAMESTRING
#     path = dirname(myPDB)
    filename, _ = splitext(myPDB)
    PDB_OUT = f'{filename}_Bfactors_{selection}.pdb'
    
    with open(PDB_OUT,'w') as f:
        for line in PDB_DATA:
            f.write(line)
        
    return print(f'File saved as {PDB_OUT}\n')
