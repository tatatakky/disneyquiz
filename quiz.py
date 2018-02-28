import linecache,random
def Solve(text,data):
    if data == text:
        return "正解だよ！！"
    else:
        return "残念。正解は{}だよ！".format(text)
# import random
# def random_image():
#     lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
#     url=random.choice(lines)
#     return url
