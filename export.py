import subprocess
import sys 
import os 
import pathlib
from pathlib import Path

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

black_command = " ".join(
    [
        "sqlite3",
        '"/etc/pihole/gravity.db"',
        '"SELECT',
        'domain',
        "FROM",
        "domainlist",
        "WHERE",
        "enabled=1",
        "AND",
        'type=1;"',
    ]
)

# sudo sqlite3 /etc/pihole/gravity.db "delete from domainlist where type=1;"

delete_command = " ".join(
    [
        "sqlite3",
        '"/etc/pihole/gravity.db"',
        '"DELETE',
        "FROM",
        "domainlist",
        "WHERE",
        'type=1;"',
    ]
)


def return_subDirs(subdirectory):
    return [f.name for f in os.scandir(subdirectory) if f.is_dir()]

def create_path(folder,file):
    return os.path.join(folder, file.replace(" ", "\\ ") + '//')
       
try:
    blacks = subprocess.check_output(
        black_command, shell=True, executable="/bin/bash", stderr=subprocess.STDOUT
    )

    # Project Root Directory
    root_directory = dir_path = os.path.dirname(os.path.realpath(__file__))
    
    # Set Search onto Adlists > Sources
    subD = os.path.join(root_directory, "Blacklist", "Adlists","Sources")
    
    # Fetch all Subfolders inside Adlists > Sources
    subF = return_subDirs(subdirectory=subD)
    
    # Sort them so you add to the last One
    selected = sorted(subF)[-1]
    
    # Change Working Directory to Last Source
    last_iteration = create_path(subD,str(selected))
    print(last_iteration)
    os.chdir(Path(last_iteration))
    
    print(os.getcwd())
    
    """
    #Return all Files
    arr = os.listdir()
    
    print(arr)
    
    import glob

    txtfiles = []
    for file in glob.glob("*.txt"):
        txtfiles.append(file)
    
    print(txtfiles)
    """
 
    # Find the Last One, cd to it
    
    # Fetch all Text Files inside of it.
    
    # Create a New Text File (named [Number]. Date inside the folder
    
    # Append to it line by line a formatted domain entry.
    
    # Count the lines you write, every 10.000 lines
    # Save File - Switch to a new File (reset loop)
    # When input is complete 
    # Nuke the exact blacklist by using the delete_command
    # Verify the exact blacklist is nuked.
    
    ## pihole -b --nuke ---> Another way to delete
    
    ## pihole -b --list ---> Must be "Not showing empty list"
    
    """
    for line in blacks.splitlines():
        # Fetch Data by line
        line = str(line.decode()).rstrip().strip()
    """

    
except subprocess.CalledProcessError as cpe:
    blacks = cpe.output
    
    
