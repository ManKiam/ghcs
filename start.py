import time
with open('start.log', 'a') as fp:
    fp.write('\n')
    while 1:
        fp.write(f'{time.time()}\n')
        fp.flush()
        time.sleep(60*2)
