import os

posts = os.listdir("./content/posts/")
print(posts)

input()
os.system("cp content/posts/" + posts[2] + " " + posts[2])
posts = [posts[2]]
# test 01

# for all posts
# if "_" in post
for post in posts:
    if "_" in post:

        File_old = open("./content/posts/" + post, 'r')
        # os.system("hugo new content posts/\'" + post.replace("_", " ") + "\'")
        File_new = open("./content/posts/\'" + post.replace("_", " ") + "\'",'a+')
        i = 0
        for line in File_old.readlines():
            if (i < 5):
                File_new.write(line.replace("_", " "))
                i += 1
            else:
                File_new.write(line)

        File_new.close()
        File_old.close()
        # os.system("rm content/posts/" + post)
