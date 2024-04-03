# helloworld-gpp

This sample is showing you how you can use g++ to compile and run your c++ application.

## Environment Setup

Make sure *g++* installed by running following command:

```
g++ --version
zsh: command not found: g++
```

if you see *command not found: g++*, you need to install *g++*. *g++* compiler is a part of gcc package in some operating systems, but in some you need to install it separately. I prefer to keep both of them

### Installing gcc

  - MacOS
    ```
    $ brew install gcc
    ```
  - Linux
    - Debian/Ubuntu
      ```
      $ sudo apt install gcc
      $ sudo apt install g++
      ```

## Building hello shared library (including hello.cpp and hello.h files)

Using -c you can compile your shared library that typically it shouldn't be executable and having main method. Here is an example:
```
$ g++ -c hello.cpp
```
After running above list, you should be able to find a hello.o in the same folder

## Building greet executable file

Use following g++ with -o option to specify the executable file name you want to run and also add hello.o shared library file, so that g++ compiler link all files into one executable file called greet.

```
$ g++ -o greet main.cpp hello.o
```

## Run greet application

Now you can run your compile greet app using following command:

```
$ ./greet
Hello World!
```
