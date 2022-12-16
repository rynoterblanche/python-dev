## Custom Metaclass

Customizing `issubclass` and `isinstance` requires careful consideration to ensure consistent semantics in your code.

This is an awkward technique that retrospectively introduces subclass relations on unknowing classes. It is used in 
many protocols in the Python Standard Library.

Overriding `__instancecheck__` & `__subclasscheck__` via a metaclass can quickly become tricky. Metaclasses are also 
not very widely understood. There is a much better alternative in the standard library support for ABC.