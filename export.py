import subprocess
import sys 
import os 

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

try:
    blacks = subprocess.check_output(
        black_command, shell=True, executable="/bin/bash", stderr=subprocess.STDOUT
    )

    # Fetch all Subfolders inside Adlists > Sources
    root_directory = dir_path = os.path.dirname(os.path.realpath(__file__))
    subdirectory = os.path.join(root_directory, "Blacklist", "Adlists")
    subfolders = [f.path for f in os.scandir(subdirectory) if f.is_dir()]
    
    print(subfolders)

    
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
    
    
