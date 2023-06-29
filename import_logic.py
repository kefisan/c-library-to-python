import ctypes
import os
from os.path import dirname, abspath

path = str(dirname(abspath(__file__)) + "/liblibrary_check.dylib")

lib = ctypes.CDLL(path)
lib.convert_SI.restype = ctypes.c_double