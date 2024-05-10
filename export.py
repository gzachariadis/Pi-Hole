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

    for line in blacks.splitlines():
        # Fetch Data by line
        line = str(line.decode()).rstrip().strip()
        print(line)

    
except subprocess.CalledProcessError as cpe:
    blacks = cpe.output
    print(blacks)