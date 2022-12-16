### Using the ABC class

Prefer using `ABC` and `@abstractmethod` when defining and structuring base classes. It is a clearer, more intuitive
and better understood over using `ABCMeta`, `metaclass` and `__subclasshook__`, and definitely over using custom
metaclasses.

Only consider using `__subclasshook__` if you have absolutely no other choice, for example if you are somehow forced to
add methods to virtual bases in third party libraries.

[ABC - Python Docs](https://docs.python.org/3/library/abc.html#abc.ABC)

[ABCMeta - Python Docs](https://docs.python.org/3/library/abc.html#abc.ABCMeta)
