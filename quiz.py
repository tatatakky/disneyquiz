import linecache,random
def IMG(data):
    return data[6]
def Question(data):
    return data[0]
def Choices_1(data):
    return data[1]
def Choices_2(data):
    return data[2]
def Choices_3(data):
    return data[3]
def Choices_4(data):
    return data[4]
def Solve(text,data):
    ans = data[5]
    if ans == text:
        return "正解だよ！！"
    else:
        return "残念。正解は{}だよ！".format(ans)
# import random
# def random_image():
#     lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
#     url=random.choice(lines)
#     return url
