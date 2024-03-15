
# ONLY RUN FROM HUGO MAIN DIR !!!!!
from duckduckgo_search import DDGS
import re
import os
import time
from mdutils.mdutils import MdUtils

# names_done = ["C#", "C++", "Fortran", "Java", "JavaScript", "PHP", "Python", "SQL", "Visual Basic"]

names = []
os.system("hugo new content start.md")
name_file = open("../data/names.txt", 'r')
for line in name_file.readlines():
    names.append(line.replace("\n", ""))

name_file.close()
names_done = []

names_done_file = open("../data/names_done_wiki.txt", "a+")
for line in names_done_file.readlines():
    names_done.append(line)

start_file = open("content/start.md", 'w+')

for name in names:
    if name in names_done:
        continue

    results_final = DDGS().text(name + " language", max_results=1)

    for item in results_final:
        print("\n")
        print(item)

    # s = input("end? \n")
    # if s == "c":
    #    continue
    # write this to file
    # s = "data/lang_" + name + ".txt"
    # new_file = open(s, "w")
    # new_file.truncate(0)
    # tutaj dodaj generator markdowna
    # potem wczytaj strone z markdowna
    File = MdUtils(file_name=name, title=name)

    # potem dodaj content do strony
    File.new_header(1, name.capitalize())

    # File.new_inline_img( str, link)

    File.new_header(2, "Common searches for " + name)

    for result in results_final:
        File.new_paragraph(result[0]["body"])
        File.new_inline_link(link=result[0]["href"], text=result[0]["title"])
        # title -> name of link
        # href -> link
        # body write below

    ref = "[" + name + "]({{<ref " + name + ".md>}} " + name + ")\n"
    start_file.write(ref)

    # usun stary post
    command = "rm content/posts/" + name + ".md"
    os.system(command)
    # najpierw generuj strone w hugo
    command = "hugo new content posts/" + name + ".md"
    os.system(command)

    # zapisz
    File_to_write = open("content/posts/" + name + ".md", 'a+')
    File_to_write.write("\n" + File.get_md_text())

    print(File)
    print("\n\n\n")
    names_done_file.write(name + "\n")
    time.sleep(2)

names_done_file.close()
