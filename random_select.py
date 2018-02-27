import random
def random_image():
    lines=[line.replace('\n','') for line in open('jeongyeon_image.txt','r')]
    url=random.choice(lines)
    return url
