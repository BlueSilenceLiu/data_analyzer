"""
English(UK & USA)     Anglais(Royaume-Uni et États-Unis)     Inglés(Reino Unido y EE. UU.)

This program analyzes various parameters of a set of discrete data,
including data describing the overall nature, degree of dispersion, etc.
"""
##########################################
#         All rights reserved            #
##########################################

import numpy as np
from typing import *
from tkinter import *
import re
import os

VERSION = "1.2.0"
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
        Label(res_win, text= + str(eval(f"{calculate}({user_datas})"))).pack(side=TOP)
    res_win.title("Result")
    res_win.mainloop()


if __name__ == '__main__':
    root = Tk()
    tip = Label(root, text="Input some datas(Separated by newline, space, tab or comma)：")
    entry = Text(root)
    functions = {   # function name: description
                    "var": "variance",
                    "sam_var": "sample variance",
                    "stdev": "standard deviation",
                    "sam_stdev": "sample standard deviation",
                    "coef_var": "coefficient",
                    "mdev": "mean deviation",
                    "mad": "median absolute deviation",
                    "ari_mean": "arithmetic mean",
                    "har_mean": "harmonic mean",
                    "geo_mean": "geometry mean",
                    "med": "median",
                    "max": "max",
                    "min": "min",
                    "len": "amount",
                    "sum": "sum"
                }
    variables = {key: StringVar(value='0') for key in functions.keys()}
    checks = {key: Checkbutton(root, text=des, variable=variables[key]) for key, des in functions.items()}
    checkers = checks.values()

    confirm = Button(root, text="submit", command=submit)
    tip.pack(side=TOP)
    entry.pack(side=TOP)
    for checker in checkers:
        checker.pack(side=TOP)
    confirm.pack(side=TOP)
    root.title("input")
    root.mainloop()
