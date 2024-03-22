
# ONLY RUN FROM HUGO MAIN DIR !!!!!
from duckduckgo_search import DDGS
import re
import os
import time
from mdutils.mdutils import MdUtils

# names_done = ["C#", "C++", "Fortran", "Java", "JavaScript", "PHP", "Python", "SQL", "Visual Basic"]

names = []

os.system("rm content/start.md")
os.system("hugo new content start.md")
name_file = open("../data/names.txt", 'r')
for line in name_file.readlines():
    names.append(line.replace("\n", ""))

name_file.close()
names_done = []

names_done_file = open("../data/names_done.txt", "a+")
for line in names_done_file.readlines():
    names_done.append(line)

start_file = open("content/start.md", 'a+')

for name in names:
    # if name in names_done:
    #    continue

    results_temp = DDGS().suggestions(re.escape(name))
    print(results_temp)
    time.sleep(1)
    results_final = []
    for result in results_temp:
        for value in result.keys():
            results_final.append(DDGS().text(result[value], max_results=1))

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
    File = MdUtils(file_name=name + "_tmp", title=name)

    # potem dodaj content do strony
    File.new_header(1, name.capitalize())

    # File.new_inline_img( str, link)

    File.new_header(2, "Common searches for " + name)

    # usun stary post
    command = "rm content/posts/" + name + ".md"
    os.system(command)
    # najpierw generuj strone w hugo
    command = "hugo new content posts/" + name + ".md"
    os.system(command)

    File_to_write = open("content/posts/" + name + ".md", 'a+')

    File.create_md_file()
    File_read = open(name+"_tmp.md", 'r')
    File_to_write.write(File_read.read())

    for result in results_final:
        # File.new_inline_link(link=result[0]["href"], text=result[0]["title"])
        ref = "[" + result[0]["title"] + "](" + result[0]["href"] + ")\n"
        File_to_write.write("\n" + ref)
        File_to_write.write(result[0]["body"] + "\n")
        # File.new_paragraph(result[0]["body"])

    ref = "[" + name + "](posts/" + name + ".md)\n"
    start_file.write(ref)

        # zapisz


    print(File)
    print("\n\n\n")

    names_done_file.write(name + "\n")
    os.system("rm " + name + "_tmp.md")
    time.sleep(1)

names_done_file.close()
