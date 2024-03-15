import os
names = []

name_file = open("data/names.txt", 'r')
for line in name_file.readlines():
    names.append(line)

name_file.close()
# if working not from hugo_folder
# ROOT = os.getcwd()
# HUGO_ROOT = ROOT + "/lab_1/"

# print(ROOT)
# print(HUGO_ROOT)
# os.system("less " + HUGO_ROOT + "/hugo.toml")

ref_original = "[root]({{<ref start.md>}} Root)\n"

for name in names:
    command = "hugo new content posts/" + name + ".md"
    os.system(command)

    ref = "[" + name + "]({{<ref " + name + ".md>}} " + name + ")\n"

    os.system("echo " + ref + " > posts/start.md")

    content = ""
    s = "../data/lang_" + name
    content_file = open(s, "r")
    # change this
    for line in name_file.readlines():
        content.append(line)
        content.append("\n")
    # maybe change this in other file

    os.system("echo " + content + " > posts/" + name + ".md")
    os.system("echo " + ref_original + " > posts/" + name + ".md")
