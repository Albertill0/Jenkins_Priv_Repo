# Especifica la versión mínima de CMake requerida
cmake_minimum_required(VERSION 3.5)

# Define el nombre del proyecto
project(Jenkins_Priv_Repo)

# Agrega los archivos fuente a la variable sources
set(SOURCES
    hello.cpp
    hello.h
    main.cpp
)

# Crea el ejecutable utilizando los archivos fuente
add_executable(${PROJECT_NAME} ${SOURCES})
