import os

posts = os.listdir("./content/posts/")
print(posts)

# input()
# os.system("cp content/posts/" + posts[2] + " " + posts[2])
# posts = [posts[2]]
# test 01

# for all posts
# if "_" in post
for post in posts:
    if "_" in post:
        s = post[0:len(post)-3]
        print(s)
        # input()

        File_old = open("./content/posts/" + post, 'r')
        File_new = open("temp.tmp", 'w')
        File_new.write(File_old.read().replace(s, s.replace("_", " ")))

        File_new.close()
        File_old.close()

        File_tmp = open("temp.tmp", 'r')
        File_old = open("./content/posts/" + post, 'w')
        File_old.write(File_tmp.read())

        File_tmp.close()
        File_old.close()
        print("fixed " + s)

        # os.system("rm content/posts/" + post)
