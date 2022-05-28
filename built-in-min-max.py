def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print("maximum(12, 27, 36) :",maximum(12, 27, 36))

print("maximum(12.3, 45.6, 9.7) :",maximum(12.3, 45.6, 9.7))



def minimum(value1, value2, value3, value4, value5):
    """Return the minimum of five values."""
    min_value = value1
    if value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    if value4 < min_value:
        min_value = value4
    if value5 < min_value:
        min_value = value5
    return min_value

print("minimum(12, 27, 36, 67, 0) :", minimum(12, 27, 36, 67, 0))

print("minimum(12.3, 45.6, 9.7, 0.9, 1.0) :",minimum(12.3, 45.6, 9.7, 0.9, 1.0))


""" Built- In Functions of Min and Max """

print("max(12, 27, 36) :",max(12, 27, 36))
print("min(15, 9, 27, 14) :",min(15, 9, 27, 14))