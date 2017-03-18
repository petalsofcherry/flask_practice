import time

num = 0

def gen_img_list():
    return [open(myfile + '.jpg', 'rb').read() for myfile in ['1', '2', '3']]

def get_num():
    global num
    while True:
        time.sleep(5)
        num += 1
        yield num

def get_img_list():
    return gen_img_list()[next(get_num()) % 3]
