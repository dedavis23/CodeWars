
def comp(array1, array2):
    if type(array) != list or type(array2) != list:
        return False
    result = []
    for integer in array1:
        result.append(integer * integer)
    return sorted(result)  == sorted(array2)

