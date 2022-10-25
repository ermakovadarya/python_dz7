

def log(k):
    with open('log.txt', 'a') as fh:  
        fh.writelines(f'{k} \n')