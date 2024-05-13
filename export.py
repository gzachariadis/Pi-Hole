import subprocess
import sys 
import os 
import pathlib
from pathlib import Path
import glob
from datetime import date

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

def create_path(folder,subfolder):
    return Path(os.path.join(folder,subfolder))
       
try:
    
    # Run the black command to Fetch Domains
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
    os.chdir(Path(last_iteration))

    # Get all Txt Files in Current Directory
    txtFiles = [f for f in os.listdir(os.curdir) if f.endswith('.txt')]
       
    today = date.today().strftime("%d-%m-%Y")
    counter = 1 

    # Search txtFiles to append to counter
    for Fname in txtFiles:
        if str(today) in Fname:
            counter = counter + 1
    
    # Create a New Text File (named [Number]. Date inside the folder
    with open('.'.join([str("{:02d}".format(counter)),str(today),'txt']), 'w') as f:
        lines = 0 
        for line in blacks.splitlines():
            # Fetch Data by line
            line = str(line.decode()).rstrip().strip()
            # Append to it line by line a formatted domain entry.
            f.write(line + '\n')
            lines  = lines + 1
        # Save the File
        f.close()

    # Count the lines you write, every 10.000 lines
    print(lines)

    
    # Save File - Switch to a new File (reset loop)
    # When input is complete 
    # Nuke the exact blacklist by using the delete_command
    
    
    # Verify the exact blacklist is nuked.
    subprocess.run(["pihole", "-b", "--nuke"]) 
    subprocess.call(["pihole", "-b", "--nuke"])
    
    
    ## pihole -b --nuke ---> Another way to delete
    
    ## pihole -b --list ---> Must be "Not showing empty list"
    
    """

    """

    
except subprocess.CalledProcessError as cpe:
    blacks = cpe.output
    
    
