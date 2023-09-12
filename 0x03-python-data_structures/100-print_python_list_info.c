#include <python.h>
#include <stdio.h>

/**
 * print_python_list_info - function to print python list info
 * @p: PyObject
 *
 * Return: noting to return
 */
void print_python_list_info(PyObject *p)
{
	long int size, x;
	PyListObject *list;
	PyObject *obj;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
	obj = PyList_GetItem(p, x);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
