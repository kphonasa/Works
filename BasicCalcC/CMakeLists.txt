cmake_minimum_required(VERSION 2.6)
project(hw01)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(hw01 main.cpp)

install(TARGETS hw01 RUNTIME DESTINATION bin)
