import ctypes

lib = ctypes.CDLL("./file.dylib")

print(lib.m.argtypes)

lib.m()