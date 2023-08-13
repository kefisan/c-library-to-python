cmake_minimum_required(VERSION 3.23)
project(library_check C)

set(CMAKE_C_STANDARD 17)

add_library(library_check SHARED library.c)
