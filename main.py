import numpy as np
from typing import *
from tkinter import *
import re
import os

VERSION = "1.1.2"
AUTHOR = "BSL"


Datastype = List[Union[int, float]]
user_datas = []
calculates = []


# dispersion
def var(datas: Datastype):
    # variance
    return np.var(datas)


def sam_var(datas: Datastype):
    # sample variance
    n = len(datas)
    return var(datas) * n / (n - 1)


def stdev(datas: Datastype):
    # standard deviation
    return np.std(datas)


def sam_stdev(datas: Datastype):
    n = len(datas)
    return stdev(datas) * n / (n - 1)


def coef_var(datas: Datastype):
    # coefficient of variance
    return stdev(datas) / ari_mean(datas)


def mdev(datas: Datastype):
    # mean deviation
    mean = ari_mean(datas)
    return np.mean([abs(i - mean) for i in datas])


def mad(datas: Datastype):
    # median absolute deviation
    median = med(datas)
    return np.mean([abs(i - median) for i in datas])


# means
def ari_mean(datas: Datastype):
    # arithmetic mean
    return np.mean(datas)


def har_mean(datas: Datastype):
    # harmonic mean
    try:
        return 1 / np.mean([1 / xi for xi in datas])
    except ZeroDivisionError:
        return "meaningless"


def geo_mean(datas: Datastype):
    # geometry mean
    return np.prod(datas) ** (1 / len(datas))


# others
def med(datas: Datastype):
    # median
    # when an even number of numbers are given, return the arithmetic mean of two median numbers
    return np.median(datas)


# tkinter
def submit(*args):
    global entry, checks, user_datas, calculates, variables
    try:
        user_datas = [int(i) for i in re.split('[\s\,]', entry.get(1.0, END)) if i != '']
    except ValueError:
        print("Please enter number(and available spliter)！")
        os.system("pause")
        exit()
    calculates = [key for key, value in variables.items() if value.get() == '1']
    res_win = Tk()
    Label(res_win, text="Results(in order):").pack(side=TOP)
    for calculate in calculates:
        Label(res_win, text=str(eval(f"{calculate}({user_datas})"))).pack(side=TOP)
    res_win.title("Result")
    res_win.mainloop()


if __name__ == '__main__':
    root = Tk()
    tip = Label(root, text="Input some datas(Separated by newline, space, tab or comma)：")
    entry = Text(root)
    variables = {"var": StringVar(value='0'),
                 "sam_var": StringVar(value='0'),
                 "stdev": StringVar(value='0'),
                 "sam_stdev": StringVar(value='0'),
                 "coef_var": StringVar(value='0'),
                 "mdev": StringVar(value='0'),
                 "mad": StringVar(value='0'),
                 "ari_mean": StringVar(value='0'),
                 "har_mean": StringVar(value='0'),
                 "geo_mean": StringVar(value='0'),
                 "med": StringVar(value='0'),
                 "max": StringVar(value='0'),
                 "min": StringVar(value='0')}
    checks = {"var": Checkbutton(root, text="variance", variable=variables["var"]),
              "sam_var": Checkbutton(root, text="sample variance", variable=variables["sam_var"]),
              "stdev": Checkbutton(root, text="standard deviation", variable=variables["stdev"]),
              "sam_stdev": Checkbutton(root, text="sample standard deviation", variable=variables["sam_stdev"]),
              "coef_var": Checkbutton(root, text="coefficient", variable=variables["coef_var"]),
              "mdev": Checkbutton(root, text="mean deviation", variable=variables["mdev"]),
              "mad": Checkbutton(root, text="median absolute deviation", variable=variables["mad"]),
              "ari_mean": Checkbutton(root, text="arithmetic mian", variable=variables["ari_mean"]),
              "har_mean": Checkbutton(root, text="harminic mean", variable=variables["har_mean"]),
              "geo_mean": Checkbutton(root, text="geometry mean", variable=variables["geo_mean"]),
              "med": Checkbutton(root, text="median", variable=variables["med"]),
              "max": Checkbutton(root, text="max", variable=variables["max"]),
              "min": Checkbutton(root, text="min", variable=variables["min"])}
    checkers = checks.values()
    confirm = Button(root, text="submit", command=submit)
    tip.pack(side=TOP)
    entry.pack(side=TOP)
    for checker in checkers:
        checker.pack(side=TOP)
    confirm.pack(side=TOP)
    root.title("输入")
    root.mainloop()
