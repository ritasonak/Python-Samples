from math import log
import os
import msvcrt

def convert(s):
    try:
        return int(s)
        print("Conversion is succeeded!")
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)))
        raise Exception("error occurred")


def string_log(s):
    v = convert(s)
    return log(v)


def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e)
        raise
    finally:
        os.chdir(original_path)


def get_key():
    try:
        return msvcrt.getch()
    except ImportError:
        print("msvcrt is not a supported library")


