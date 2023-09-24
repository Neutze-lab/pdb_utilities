function replaceBfactors(myPDB, myArray, selection)
%
% replaceBfactors - Generates a new PDB file with the 'tempFactor' column
%                   replaced by both the given array and atom selection. 
%                   Used for rendering in PyMol.
%
% Requirements:
%   Bioinformatics Toolbox
%
% Syntax:
%   replaceBfactors(myPDB, myArray, selection)
%
% Input Arguments:
%   - myPDB: Reference PDB structure to read Bfactors from.
%   - myArray: 1-D array to write out in the new PDB. 
%   - selection:  'All' atoms or 'CA' atoms only.
%
% Output Arguments:
%   - Generates a modified version of myPDB with new Bfactors.
%
% Example:
%   myFunction('193l.pdb', rand(1,N), 'CA')
%   The function above assigns random Bfactors to all '' atoms in the PDB
%   Iff parameter N is the same length as the number of 'CA' in the 
%
% Written by Adams Vallejos at Neutze-lab
%
selection = upper(selection);

if ~strcmp(selection, 'CA') && ~strcmp(selection, 'ALL')
    error("Unrecognized selection of atoms, use 'CA' or 'all'")
end

% LOAD PDB DATA
PDB_DATA = pdbread(myPDB); 

% MATCHES ATOMS WITH SELECTION CRITERION
if strcmp(selection,'CA')
    IS_MATCH = [strcmp({PDB_DATA.Model.Atom.AtomName},selection)];
else
    IS_MATCH = ones(1,length(PDB_DATA.Model.Atom(:)));
end

% TEST IF LENGTH OF ARRAY IS COMPATIBLE WITH SELECTED ATOMS
if length(myArray) ~= sum(IS_MATCH)
    error("Length of array does not match the atom selection.")
    % return
end

count = 1;
for row = 1:length(IS_MATCH)
    if IS_MATCH(row)
        PDB_DATA.Model.Atom(row).tempFactor = myArray(count);
        count = count + 1;
    else
        PDB_DATA.Model.Atom(row).tempFactor = -1;
    end
end

% GENERATE THE OUTPUT NAMESTRING
[path, filename, ~] = fileparts(which(myPDB));
PDB_OUT = sprintf('%s/%s_Bfactors_%.pdb', path,filename,selection);

% WRITE OUT FILE
pdbwrite(PDB_OUT,PDB_DATA)
fprintf('\tFile saved as: %s \n', PDB_OUT)
end

