cmake_minimum_required(VERSION 3.4...3.18)
project(pixy2_raw_frame)

add_subdirectory(pybind11)
# add_executable(pixy2_raw_frame src/main.cpp)
pybind11_add_module(pixy2_raw_frame src/main.cpp)
set_property(TARGET pixy2_raw_frame PROPERTY POSITION_INDEPENDENT_CODE ON)

# link_directories(${CMAKE_BINARY_DIR}/lib)
target_include_directories(pixy2_raw_frame PRIVATE /usr/include/libusb-1.0)
target_include_directories(pixy2_raw_frame PRIVATE ${CMAKE_BINARY_DIR}/lib)
target_include_directories(pixy2_raw_frame PRIVATE ${CMAKE_BINARY_DIR}/lib/arduino/libraries/Pixy2)
target_link_libraries(pixy2_raw_frame PRIVATE ${CMAKE_BINARY_DIR}/lib/libpixy2.so -lusb-1.0)

# add_library(MyExternalLib SHARED IMPORTED)
# set_target_properties(MyExternalLib PROPERTIES IMPORTED_LOCATION ${CMAKE_BINARY_DIR}/lib/libpixy2.so)
# target_link_libraries(pixy2_raw_frame PRIVATE MyExternalLib -lusb-1.0)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
# target_compile_definitions(pixy2_raw_frame
#                            PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
