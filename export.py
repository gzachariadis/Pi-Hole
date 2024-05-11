import subprocess
import sys 

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

try:
    blacks = subprocess.check_output(
        black_command, shell=True, executable="/bin/bash", stderr=subprocess.STDOUT
    )

    # Create a New File (named Number-Date) inside the last Iteration
    # Append to it line by line a formatted domain
    # Count the lines you write, every 10.000 lines
    # Save File - Switch to a new File (reset loop)
    # When input is complete nuke the exact blacklist
    # Verify the exact blacklist is nuked.
    
    for line in blacks.splitlines():
        # Fetch Data by line
        line = str(line.decode()).rstrip().strip()
    

    
except subprocess.CalledProcessError as cpe:
    blacks = cpe.output
    print(blacks)