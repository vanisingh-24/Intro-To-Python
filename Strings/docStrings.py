## Python DocStrings

# Using triple single quotes
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''

    return None

print(my_function.__doc__)
help(my_function)

# Using triple double quotes

def my_function():
    """Demonstrates triple double quotes
    docstrings and does nothing really."""

    return None

print(my_function.__doc__)
help(my_function)

# One-line Docstrings

def power(a,b):
    """Returns arg1 raised to power arg2."""

    return a**b

print(power.__doc__)

# Multi-line Docstrings

def my_function(arg1):
    """
    Summary line.
  
    Extended description of function.
  
    Parameters:
    arg1 (int): Description of arg1
  
    Returns:
    int: Description of return value
  
    """

    return arg1

print(my_function.__doc__)

# Docstrings in Classes

class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """

    def __init__(self,real,imag):
        """
        The constructor for ComplexNumber class.
  
        Parameters:
           real (int): The real part of complex number.
           imag (int): The imaginary part of complex number.   
        """

    def add(self, num):
        """
        The function to add two Complex Numbers.
  
        Parameters:
            num (ComplexNumber): The complex number to be added.
          
        Returns:
            ComplexNumber: A complex number which contains the sum.
        """

        re = self.real + num.real
        im = self.imag + num.imag

        return ComplexNumber(re,im)

help(ComplexNumber)
help(ComplexNumber.add)
