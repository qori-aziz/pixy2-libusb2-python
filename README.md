# pixy2-libusb2-python
Python library source code for Pixy2 camera libpixyusb2 library.

This is an implementation of C++ Pixy2 CMUCam as a Python library.

You need Pixy Camera to run this library.
(while probably you are searching this repo because you had hit your head on how to stream video from Pixy2 cam using python, just like me before)

How to build:

````
cmake .
make
````
 After the build success, you can use it like this:

````
$ python3
>> import pixy2_raw_frame as p
>> p.initializing()
````

Test program:
````
$ python3 opencv_test.py
````

Credits:
1. [Pybind11 CMake Example](https://github.com/pybind/cmake_example)
2. [Pixy2 official libpixyusb2 library](https://github.com/charmedlabs/pixy2/tree/master/src/host/libpixyusb2)
