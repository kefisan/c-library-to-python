import ctypes

lib = ctypes.CDLL("/Users/illiriabalog/CLionProjects/library_check/cmake-build-debug/liblibrary_check.dylib")

lib.convert_SI.restype = ctypes.c_double

val = ctypes.c_double(1.0)
unit_in = ctypes.c_char_p(b"yard")
unit_out = ctypes.c_char_p(b"cm")

result = lib.convert_SI(val, unit_in, unit_out)
print(result)