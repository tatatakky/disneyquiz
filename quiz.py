import linecache,random
def ChooseQustion():
    LineNum=len(open('disney_quiz.txt').readlines())
    data = linecache.getline('disney_quiz.txt', random.randint(1,LineNum)).replace('\n','').split("    ")
    return data
def Solve(text,data):
    if data[5] == text:
        return "正解だよ！！"
    else:
        return "残念。正解は{}だよ！".format(data[5])
# import random
# def random_image():
#     lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
#     url=random.choice(lines)
#     return url
