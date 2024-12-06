import threading as th
import pandas as pd
import numpy as np
import datetime as dt
import time, re

from package1 import Cal_index1 as ci

import sys
sys.path.append("D:\\LearningAndWorking\\VSCode\\python\\project3\\")
import Option_pricing as op



class Class1(object):
    editor = "Jay"

    def func1(self, str_arg1, int_arg1):
        print("start: ", str_arg1, dt.datetime.now())
        time.sleep(int_arg1)
        print("end: ", str_arg1, dt.datetime.now())


object1 = op.Option_pricing()
sigma1 = object1.BAW_binary(3268.5, "C", 7520, 4350, 0.178082, 0.015315, 0, 0.2)


def main():
    #创建thread实例
    t1 = th.Thread(target=Class1().func1, args=("zhaobo1", 3))
    t2 = th.Thread(target=Class1().func1, args=("zhaobo2", 5))

    #启动线程运行
    t1.start()
    t2.start()

    #等待所有线程执行完毕
    t1.join()
    t2.join()



if __name__ == "__main__":
    pass


