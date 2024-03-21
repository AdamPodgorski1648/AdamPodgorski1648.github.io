import os


posts = os.listdir("./content/posts/")
print(posts)
post = 'Fortran.md'
if True:
    post_file0 = open("./content/posts/" + post, 'r+')
    post_file_tmp = open("temp.tmp", 'w')
    for line in post_file0.readlines():
        if line == "draft = true\n":
            post_file_tmp.write("draft = false\n")
            print("fixed " + post)
        else:
            post_file_tmp.write(line)
    post_file0.close()
    post_file_tmp.close()

    post_file0 = open("./content/posts/" + post, 'w')
    post_file_tmp = open("temp.tmp", 'r')
    post_file0.write(post_file_tmp.read())

    post_file0.close()
    post_file_tmp.close()

input()

for post in posts:
    post_file0 = open("./content/posts/" + post, 'r+')
    post_file_tmp = open("temp.tmp", 'w')
    for line in post_file0.readlines():
        if line == "draft = true\n":
            post_file_tmp.write("draft = false\n")
            print("fixed " + post)
        else:
            post_file_tmp.write(line)
    post_file0.close()
    post_file_tmp.close()

    post_file0 = open("./content/posts/" + post, 'w')
    post_file_tmp = open("temp.tmp", 'r')
    post_file0.write(post_file_tmp.read())

    post_file0.close()
    post_file_tmp.close()
