
#path

import time

def logger(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs) # will run
        end_time=time.time()
        diff=end_time-start_time
        txt=f"function:{func.__name__} time taken {diff}"
        f_name="logger.txt"
        write_file(f_name=f_name,txt=txt)
    return wrapper

def write_file(f_name,txt):
    with open(f_name,'a') as file:
        file.write(f"{txt} \n")
        
@logger
def counter():
    for n in range(0,100000000):
        # print(n)
        pass


counter()