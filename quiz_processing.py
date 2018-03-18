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
    text="ボタンを押してみよう！\n\n<リトルグリーンメン>\nQuizができるよ！\n\n<ミニー>\nディズニー公式のtwitterが見られるよ！\n\n<プーさん>\nディズニーの公式サイトが見られるよ！\n\n<ミッキーの手>\n占いができるよ！\n\n<サリー＆マイク>\nディズニー公式のInstagramが見られるよ！\n"
    return text
def Uranai():
    d={
      'ミッキー':'https://pics.prcm.jp/16fdd6c0cd5c2/74326233/png/74326233.png',
      'ミニー':'https://pics.prcm.jp/ebb62e71080b4/74370259/png/74370259.png',
      'プルート':'https://pics.prcm.jp/f1b7482dbf870/74042413/jpeg/74042413.jpeg'
    }
    chara = random.choice(list(d.keys()))
    return chara,d[chara]

# import random
# def random_image():
#     lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
#     url=random.choice(lines)
#     return url
