import math


def addComplex(a, b):
    """
    This function returns the sum of two complex numbers
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :param b: List of two numbers, first one the real part and second one the imaginary part
    :return: Addition list of a and b
    """
    return [a[0] + b[0], a[1] + b[1]]


def subtComplex(a, b):
    """
    This function returns the subtract of two complex numbers
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :param b: List of two numbers, first one the real part and second one the imaginary part
    :return: Subtraction list of a and b
    """
    return [a[0] - b[0], a[1] - b[1]]


def multComplex(a, b):
    """
    This function returns the multiplication of two complex numbers
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :param b: List of two numbers, first one the real part and second one the imaginary part
    :return: Multiplication list of a and b
    """
    entero = a[0] * b[0] + ((-1) * (a[1] * b[1]))
    imgani = a[1] * b[0] + a[0] * b[1]
    return [entero, imgani]


def divComplex(a, b):
    """
    This function returns the division  of two complex numbers
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :param b: List of two numbers, first one the real part and second one the imaginary part
    :return: Division list of a and b
    """
    den = b[0] ** 2 + b[1] ** 2
    num = multComplex(a, [b[0], b[1] * -1])
    return [round(num[0] / den, 2), round(num[1] / den, 2)]


def conjuComplex(a):
    """
    This function returns the conjugate of a complex number
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :return: List of two numbers, first one the real part and second one the imaginary part
    """
    return [a[0], a[1] * -1]


def modComplex(a):
    """
    This function returns the modulus of a complex number
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :return: Real number
    """
    return round(math.sqrt(a[0] ** 2 + a[1] ** 2), 2)


def phaseComplex(a):
    """
    This function returns the phase of a complex number
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :return: Real number
    """
    return round(math.atan2(a[1], a[0]), 2)


def polarCarteComplex(a):
    """
    This function returns the coonversion between polar and cartesian
    :param a: List of two items
    :return: List of two numbers, first one the real part and second one the imaginary part
    """
    return [round(a[0] * math.cos(a[1]), 2), round(a[0] * math.sin(a[1]), 2)]


def cartePolarComplex(a):
    """
    This function returns the coonversion between cartesian and polar
    :param a: List of two numbers, first one the real part and second one the imaginary part
    :return: List of two items
    """
    if a[0] > 0:
        return [modComplex(a), round(math.atan(a[1] / a[0]), 2)]
    elif a[0] < 0:
        return [modComplex(a), phaseComplex(a)]
    elif a == 0 and b > 0:
        return [modComplex(a), round(math.pi / 2, 2)]
    elif a == 0 and b < 0:
        return [modComplex(a), round(3 * math.pi / 2, 2)]
