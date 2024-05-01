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

# Command to Fetch Whitelist from Database
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

translations = {
    "API": "Application Programming Interface (API)",
    "CDN": "Content Delivery Network (CDN)",
    "CSS": "Cascading Style Sheets (CSS)",
    "OAuth": "Open Authorization Standard (OAuth)",
    "Hosting": "?????????????",
    "OCSP": "Online Certificate Status Protocol (OCSPs)",
}


# Translate the Type from Pihole's Abbreviation (CSS) to a "Presentable" Term
def translate(abbreviation):
    if abbreviation in translations.keys():
        return translations[abbreviation]
    else:
        return abbreviation


def findOccurrences(string):
    if string[:-1] == "\|":
        string = Str[: len(string) - 1]
    indexes = []
    indexes = indexes + [x.start() for x in re.finditer("\|", string)] + [len(string)]
    return indexes


def pairwise(l):
    return [(x, y) for x, y in zip(l[:-1], l[1:])]


# Run Command to Dabase, Decoding every line
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
                                (translate((comment[0 : comment.index("-") - 1])))
                            ).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                }
            else:
                whitelist[category] = {
                    group: [
                        {"Domain": str(domain).strip(), "Type": translate(str(comment))}
                    ]
                }
        else:
            if group not in whitelist[category].keys():
                if comment.find("-") != -1:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(
                                (translate((comment[0 : comment.index("-") - 1])))
                            ).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                else:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": translate(str(comment)),
                        }
                    ]
            else:
                if comment.find("-") != -1:
                    whitelist[category][group].append(
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(
                                (translate((comment[0 : comment.index("-") - 1])))
                            ).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    )
                else:
                    whitelist[category][group].append(
                        {
                            "Domain": str(domain).strip(),
                            "Type": translate(str(comment)),
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


# Create Files
def create_file(Title, Root_Domains, data):
    mdFile = MdUtils(file_name="README")
    mdFile.write('<h1 align="center">{}</h1>'.format(str(Title).strip()))
    mdFile.write("  \n\n")
    mdFile.new_header(level=2, title="Root Domains", add_table_of_contents="n")
    mdFile.insert_code(str("\n".join(Root_Domains)).strip(), language="html")
    mdFile.write("  \n\n")
    mdFile.write("<br>\n")

    Populate_Category(mdFile, "Application Programming Interface (API)", "API", data)
    Populate_Category(mdFile, "Content Delivery Networks (CDN)", "CDN", data)
    mdFile.create_md_file()


# The core of the data, regarding each domain, it's Type (CDN or API)  etc.
Database = {}

# The home domains, the root of any domain.
Root_Domains = []

# Static Assets = icons, thumbnails, buttons etc. that are rendered from different domains (eg. icons.bitwarden.com) - so anything CSS.
Static_Assets = []

# For each Category in the Whitelist
for x in whitelist.keys():
    for y in whitelist[x].keys():
        for z in whitelist[x][y]:
            # Place all unique Root Domains in a List
            if z["Type"] == "Domain":
                if z["Domain"] not in Root_Domains and "Comment" not in z.keys():
                    Root_Domains.append(z["Domain"])
            # Place all unique Root Domains in a List
            if z["Type"] == translate("CSS"):
                if z["Domain"] not in Static_Assets and "Comment" not in z.keys():
                    Static_Assets.append(z["Domain"])
            # Categorize all domains under API or CDN groups
            if z["Type"] == translate("API") or z["Type"] == translate("CDN"):
                if z["Type"] not in Database.keys():
                    Database[z["Type"]] = {z["Comment"]: [z["Domain"]]}
                if z["Comment"] not in Database[z["Type"]].keys():
                    Database[z["Type"]][z["Comment"]] = [z["Domain"]]
                elif z["Domain"] not in list(Database[z["Type"]][z["Comment"]]):
                    Database[z["Type"]][z["Comment"]].append(z["Domain"])

        Fpath = os.path.join(root_directory, "Whitelist", str(x), str(y))
        if os.path.exists(Fpath):
            os.chdir(Fpath)
            create_file(y, Root_Domains, Database)
            Database.clear()
            Root_Domains.clear()
            Static_Assets.clear()

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
