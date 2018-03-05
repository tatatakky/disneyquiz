import linecache,random
def ChooseQustion():
    data=[]
    LineNum=len(open('disney_quiz.txt').readlines())
    mojiretsu = linecache.getline('disney_quiz.txt', random.randint(1,LineNum)).replace('\n','').split("    ")
    for i in range(len(mojiretsu)):
        data.append(mojiretsu[i])
    return data
def Solve(text,D):
    if D == text:
        return "正解！！", 125
    else:
        return "残念。正解は{}だよ！".format(D[-1:]), 131
def Usage():
    text="ボタンを押してみよう！\nリトルグリーンメン: Quizができるよ！\nミニー: ディズニー公式のtwitterが見られるよ！\n プーさん: ディズニーの公式サイトが見られるよ！\nミッキーの手: 運勢を占えるよ！\nサリー＆マイク: ディズニー公式のInstagramが見られるよ！"
    return text

# import random
# def random_image():
#     lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
#     url=random.choice(lines)
#     return url
