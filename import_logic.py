import ctypes

lib = ctypes.CDLL("/Users/illiriabalog/CLionProjects/library_check/cmake-build-debug/liblibrary_check.dylib")

lib.convert_SI.restype = ctypes.c_double