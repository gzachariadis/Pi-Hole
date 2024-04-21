import re
import json
import os
import shutil
from mdutils.mdutils import MdUtils
from mdutils import Html
import sys

root_directory = dir_path = os.path.dirname(os.path.realpath(__file__))
whitelist = {}


def findOccurrences(string):
    if string[:-1] == "\|":
        string = Str[: len(string) - 1]
    indexes = []
    indexes = indexes + [x.start() for x in re.finditer("\|", string)] + [len(string)]
    return indexes


def get_immediate_subdirectories(directory):
    return [f.name for f in os.scandir(directory) if f.is_dir()]


def pairwise(l):
    return [(x, y) for x, y in zip(l[:-1], l[1:])]


print("\nProcessing data...")

# Fetch Data and Create a Dictionary
with open("output.txt", "r", encoding="UTF-8") as file:
    while line := file.readline():
        line = str(line.rstrip()).strip()
        indexes = findOccurrences(line)
        pairs = pairwise(indexes)
        comment = str(line[pairs[0][0] + 1 : pairs[0][1]]).strip()
        group = str(line[pairs[1][0] + 1 : pairs[1][1]]).strip()
        category = str(line[pairs[2][0] + 1 : pairs[2][1]]).strip()
        domain = str(line[0 : pairs[0][0]]).strip()

        if category not in whitelist.keys():
            if comment.find("-") != -1:
                whitelist[category] = {
                    group: [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment[0 : comment.index("-") - 1]).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                }
            else:
                whitelist[category] = {
                    group: [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment).strip(),
                        }
                    ]
                }
        else:
            if group not in whitelist[category].keys():
                if comment.find("-") != -1:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment[0 : comment.index("-") - 1]).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    ]
                else:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment).strip(),
                        }
                    ]
            else:
                if comment.find("-") != -1:
                    whitelist[category][group].append(
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment[0 : comment.index("-") - 1]).strip(),
                            "Comment": str(comment[comment.index("-") + 1 :]).strip(),
                        }
                    )
                else:
                    whitelist[category][group] = [
                        {
                            "Domain": str(domain).strip(),
                            "Type": str(comment).strip(),
                        }
                    ]

print("\nSuccessfully processed %d categories." % (int(len(whitelist.keys()))))


# Reset the Structure before re-creating
def reset(path):
    shutil.rmtree(path, ignore_errors=True)


print("\nPerforming reset on File Structure...")
reset(os.path.join(root_directory, "Whitelist"))


# Create & Populate the Folder Structure based on Data
def populate_structure(category, subcategories):
    path = os.path.join(root_directory + "\\Whitelist\\" + category)
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            for sub in subcategories:
                sPath = path + "\\" + sub + "\\"
                if not os.path.exists(sPath):
                    os.makedirs(sPath)
    except OSError:
        pass


print("\nPopulating Folders...")
for k, v in whitelist.items():
    populate_structure(k, list(whitelist[k].keys()))


def Populate_Category(mdFile, Title, Type, data):
    for k, v in data.items():
        if k == Type:
            for x in v.keys():
                mdFile.new_header(
                    level=2, title=f"{Title} - {x}", add_table_of_contents="n"
                )
                mdFile.insert_code(str("\n".join(v[x])).strip(), language="html")
                mdFile.write("\n")


# Create Files
def create_file(Title, Root_Domains, data):
    mdFile = MdUtils(file_name="README")
    mdFile.write("# {}".format(str(Title).strip()), align="center")
    mdFile.write("\n")
    mdFile.new_header(level=2, title="Domains", add_table_of_contents="n")
    mdFile.insert_code(str("\n".join(Root_Domains)).strip(), language="html")
    mdFile.write("\n")

    Populate_Category(mdFile, "Application Programming Interface (API)", "API", data)
    Populate_Category(mdFile, "Content Delivery Networks (CDN)", "CDN", data)
    mdFile.create_md_file()


Doms = {}
Root_Domains = []

# For each Category in the Whitelist
for x in whitelist.keys():
    for y in whitelist[x].keys():
        for z in whitelist[x][y]:
            # Place all unique Root Domains in a List
            if z["Type"] == "Domain":
                if z["Domain"] not in Root_Domains and "Comment" not in z.keys():
                    Root_Domains.append(z["Domain"])
            # Categorize all domains under API or CDN groups
            if z["Type"] == "API" or z["Type"] == "CDN":
                if z["Type"] not in Doms.keys():
                    Doms[z["Type"]] = {z["Comment"]: [z["Domain"]]}
                if z["Comment"] not in Doms[z["Type"]].keys():
                    Doms[z["Type"]][z["Comment"]] = [z["Domain"]]
                elif z["Domain"] not in list(Doms[z["Type"]][z["Comment"]]):
                    Doms[z["Type"]][z["Comment"]].append(z["Domain"])

        Fpath = os.path.join(root_directory, "Whitelist", str(x), str(y))
        if os.path.exists(Fpath):
            os.chdir(Fpath)
            create_file(y, Root_Domains, Doms)
