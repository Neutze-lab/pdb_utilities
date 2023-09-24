# PyMOL_render
Scripts used for rendering figures in PyMol coloured by B-factor

- Reference structure:
    - 193l.pdb  The X-Ray structure of hen egg white lysozyme:
        - Contains 1012 'ATOM' entries.
        - Contains 129 alpha carbon atoms 'CA'.

- MATLAB functions
    -
- `replaceBfactors(myPDB, myArray, selection)` writes out a modified version of `myPDB` with a modified B-factor column according to the values given by `myArray`.
    - Parameters:
        - `myPDB`:   Template PDB file to select atoms from.
        - `myAray`:  Array of custom B-factors, its size should match the atom selection.
        - `selection`:   Either 'All' atoms or 'CA' only atoms.
    - Examples:
        - For `replaceBfactors('193l.pdb', myArray, 'CA')`, then `myArray` should be of size (1, 129).
        - For `replaceBfactors('193l.pdb', myArray, 'All')`, then `myArray` should be of size (1, 1012).

- Python functions
    - 
- All functions are contained in the module `pdb_utils.py`.
- `replace_Bfactors(myPDB, myArray, selection)` is the python equivalent of the function above.
    - Examples:
        - First load the module: `import pdb_utils`
        - For `replace_Bfactors('193l.pdb', myArray, 'CA')`, then `myArray` should be of size (129,1).
        - For `replace_Bfactors('193l.pdb', myArray, 'All')`, then `myArray` should be of size (1012,1).

- PyMol scripts
    -

    