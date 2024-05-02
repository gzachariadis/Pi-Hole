import re
import json
import os
import shutil
from mdutils.mdutils import MdUtils
from mdutils import Html
import sys
import subprocess

# Home Directory of Script eg. /root/Pi-Hole
root_directory = dir_path = os.path.dirname(os.path.realpath(__file__))
whitelist = {}

# Command to Fetch Whitelist from API_Dict
command = " ".join(
    [
        "sqlite3",
        '"/etc/pihole/gravity.db"',
        '"SELECT',
        'domain,comment,\\"group\\".name,\\"group\\".description',
        "FROM",
        "domainlist",
        "INNER",
        "JOIN",
        "domainlist_by_group",
        "ON",
        "domainlist_by_group.domainlist_id=domainlist.id",
        "INNER",
        "JOIN",
        '\\"group\\"',
        "ON",
        '\\"group\\".id=domainlist_by_group.group_id',
        "WHERE",
        'domainlist.type=0"',
    ]
)

def findOccurrences(string):
    if string[:-1] == "\|":
        string = Str[: len(string) - 1]
    indexes = []
    indexes = indexes + [x.start() for x in re.finditer("\|", string)] + [len(string)]
    return indexes


def pairwise(l):
    return [(x, y) for x, y in zip(l[:-1], l[1:])]


# Run Command to Database, Decoding every line
try:
    result = subprocess.check_output(
        command, shell=True, executable="/bin/bash", stderr=subprocess.STDOUT
    )

    for line in result.splitlines():
        # Fetch Data by line
        line = str(line.decode()).rstrip().strip()
        pairs = pairwise(findOccurrences(line))

        # From Pair of Intexes - Get strings
        comment = str(line[pairs[0][0] + 1 : pairs[0][1]]).strip()
        group = str(line[pairs[1][0] + 1 : pairs[1][1]]).strip()
        category = str(line[pairs[2][0] + 1 : pairs[2][1]]).strip()
        domain = str(line[0 : pairs[0][0]]).strip()
        
        # Create a Dictionary
        if category not in whitelist.keys():
            if comment.find("-") != -1:
                whitelist[category] = {
                    group: [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(
                                (comment[0 : comment.index("-") - 1])).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                }
            else:
                whitelist[category] = {
                    group: [
                        {"Domain": str(domain).strip(), "Type": str(comment)}
                    ]
                }
        else:
            if group not in whitelist[category].keys():
                if comment.find("-") != -1:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(
                                (comment[0 : comment.index("-") - 1])).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                else:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment),
                        }
                    ]
            else:
                if comment.find("-") != -1:
                    whitelist[category][group].append(
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(
                                ((comment[0 : comment.index("-") - 1]))).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    )
                else:
                    whitelist[category][group].append(
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment),
                        }
                    )

except subprocess.CalledProcessError as cpe:
    result = cpe.output

# print(json.dumps(whitelist, sort_keys=False, indent=4))

# Reset the Structure before re-creating
shutil.rmtree(os.path.join(root_directory, "Whitelist"), ignore_errors=True)


# Create & Populate the Folder Structure based on Data
def populate_structure(category, subcategories):
    path = os.path.join(root_directory, "Whitelist", category)
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            for sub in subcategories:
                if not os.path.exists(os.path.join(path, sub)):
                    os.makedirs(os.path.join(path, sub))
    except OSError:
        pass


for k, v in whitelist.items():
    populate_structure(k, list(whitelist[k].keys()))


# Populate the Categories inside the README.md
def Populate_Category(mdFile, Title, Type, data):
    for k, v in data.items():
        if k == Type:
            for x in v.keys():
                mdFile.new_header(
                    level=2, title=f"{Title} - {x}", add_table_of_contents="n"
                )
                mdFile.insert_code(str("\n".join(v[x])).strip(), language="html")
                mdFile.write("  \n\n")
                mdFile.write("<br>\n")


translations = {
    "CSS": "Cascading Style Sheets (CSS)",
    "CDN": "Content Delivery Network (CDN)",
    "API": "Application Programming Interface (API)",
    "OCSP": "Online Certificate Status Protocol (OCSPs)",
    "NTP": "Network Time Protocol Servers (NTPs)",
    "OAuth": "Open Authorization Standard (OAuth)",
    "DNS": "Domain Name System (DNS)",
}


# Translate the Type from Pihole's Comment Abbreviation to a "Presentable" Term
def translate(abbreviation):
    if abbreviation in translations.keys():
        return translations[abbreviation]
    else:
        return abbreviation

# Create Files
def create_file(Title, Roots, CSS, OCSP, NTP, OAUTH, DNS, data):
    mdFile = MdUtils(file_name="README")
    mdFile.write('<h1 align="center">{}</h1>'.format(str(Title).strip()))
    mdFile.write("  \n\n")
    mdFile.new_header(level=2, title="Root Domains", add_table_of_contents="n")
    mdFile.insert_code(str("\n".join(Roots)).strip(), language="html")
    mdFile.write("  \n\n")
    mdFile.write("<br>\n")
    
    Populate_Category(mdFile, "Application Programming Interface (API)", "API", data)
    Populate_Category(mdFile, "Content Delivery Networks (CDN)", "CDN", data)
    
    mdFile.create_md_file()


# API - Application Programming Interface (APIs)
API_Dict = {}

# CDN - Content Delivery Network (CDNs)
CDN_Dict = {}

# The home domains, the root of any domain.
Roots = []

# CSS - Static Assets as interpreted by Pi-Hole Comments
CSS = []

# OCSP - Online Certificate Status Protocol (OCSP)
OCSP = []

# NTP - Network Time Protocol Servers (NTPs)
NTP = []

# OAuth - Open Authorization Standard (OAuth)
OAUTH = []

# DNS - Domain Name System (DNS)
DNS = []


# For each Category in the Whitelist
for x in whitelist.keys():
    for y in whitelist[x].keys():
        for z in whitelist[x][y]:
          
            # Place all unique Root Domains in a List
            if z["Type"] == "Domain":
                if z["Domain"] not in Roots and "Comment" not in z.keys():
                    Roots.append(z["Domain"])
          
            # Place all unique CSS Domains
            if z["Type"] == "CSS":
                if z["Domain"] not in CSS and "Comment" not in z.keys():
                    CSS.append(z["Domain"])
            
            # Place all unique oCSP Domains
            if z["Type"] == "OCSP":
                if z["Domain"] not in OCSP and "Comment" not in z.keys():
                    OCSP.append(z["Domain"])
            
            # Place all unique NTP Domains
            if z["Type"] == "NTP":
                if z["Domain"] not in NTP and "Comment" not in z.keys():
                    NTP.append(z["Domain"])
            
            # Place all unique DNS Domains
            if z["Type"] == "DNS":
                if z["Domain"] not in DNS and "Comment" not in z.keys():
                    DNS.append(z["Domain"])
            
            # Place all unique DNS Domains
            if z["Type"] == "OAuth":
                if z["Domain"] not in OAUTH and "Comment" not in z.keys():
                    OAUTH.append(z["Domain"])
            
            # Categorize all domains under API
            if z["Type"] == "API" and "Comment" in z.keys():
                if z["Type"] not in API_Dict.keys():
                    API_Dict[z["Type"]] = {z["Comment"]: [z["Domain"]]}
                if z["Comment"] not in API_Dict[z["Type"]].keys():
                    API_Dict[z["Type"]][z["Comment"]] = [z["Domain"]]
                elif z["Domain"] not in list(API_Dict[z["Type"]][z["Comment"]]):
                    API_Dict[z["Type"]][z["Comment"]].append(z["Domain"])
                        
            print(API_Dict)        
                    
            """
            # Categorize all domains under CDN
            if z["Type"] == "CDN":
                if z["Type"] not in CDN_Dict.keys():
                    CDN_Dict[z["Type"]] = {z["Comment"]: [z["Domain"]]}
                if z["Comment"] not in API_Dict[z["Type"]].keys():
                    CDN_Dict[z["Type"]][z["Comment"]] = [z["Domain"]]
                elif z["Domain"] not in list(CDN_Dict[z["Type"]][z["Comment"]]):
                    CDN_Dict[z["Type"]][z["Comment"]].append(z["Domain"])

        Fpath = os.path.join(root_directory, "Whitelist", str(x), str(y))
        if os.path.exists(Fpath):
            os.chdir(Fpath)
            create_file(y, Roots, API_Dict)
            API_Dict.clear()
            CDN_Dict.clear()
        """
          
        # Clear Lists
        Roots.clear()
        CSS.clear()
        OCSP.clear()
        NTP.clear()
        OAUTH.clear()
        DNS.clear()

"""
# Push Changes to Github
from git import Repo

repo = Repo(root_directory)  # if repo is CWD just do '.'
repo.git.add("-A")
repo.git.commit("-m", "Automated Push")
origin = repo.remote(name="origin")
origin.pull()
origin.push()

"""
