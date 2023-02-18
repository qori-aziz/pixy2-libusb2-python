cmake_minimum_required(VERSION 3.4...3.18)
project(test)

ADD_EXECUTABLE(test tes.cpp)
target_link_libraries(test PRIVATE ${CMAKE_BINARY_DIR}/libpixy2.a -lusb-1.0) 
target_include_directories(test PUBLIC /usr/include/libusb-1.0)
target_include_directories(test PRIVATE arduino/libraries/Pixy2)

# add_library(MyExternalLib SHARED IMPORTED)
# # Provide the full path to the library, so CMake knows where to find it.
# set_target_properties(MyExternalLib PROPERTIES IMPORTED_LOCATION /home/qori/pixy2/build/libpixyusb2/libpixy2.a)
# target_link_libraries(test PRIVATE MyExternalLib)

# EXAMPLE_VERSION_INFO is defined by setup.py and passed into the C++ code as a
# define (VERSION_INFO) here.
# target_compile_definitions(pixy2_raw_frame
#                            PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})
