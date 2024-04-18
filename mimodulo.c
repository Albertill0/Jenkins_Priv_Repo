#include <Python.h>

static PyObject *
mimodulo_repr(PyObject *self, PyObject *args)
{
    PyObject *obj;
    if (!PyArg_ParseTuple(args, "O", &obj)) {
        return NULL;
    }

    return PyCArg_repr(obj);
}

static PyMethodDef MiModuloMethods[] = {
    {"mimodulo_repr",  mimodulo_repr, METH_VARARGS, "Devuelve la representación de cadena del argumento usando PyCArg_repr()."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef mimodulo = {
    PyModuleDef_HEAD_INIT,
    "mimodulo",   /* name of module */
    NULL, /* module documentation, may be NULL */
    -1,
    MiModuloMethods
};

PyMODINIT_FUNC
PyInit_mimodulo(void)
{
    return PyModule_Create(&mimodulo);
}
