BASE2 = "01"
BASE10 = "0123456789"
BASE16 = "0123456789ABCDEF"
BASE62 = "AzByCxDwEvFuGtHsIrJqKpLoMnNmOlPkQjRiShTgUfVeWdXcYbZa0123456789"
def string_to_integer(number):
    return base_convert(number, BASE62,BASE10)

def id_to_string(number):
    return base_convert(number, BASE10, BASE62)

def base_convert(number,fromradix,toradix):
    # based on http://code.activestate.com/recipes/111286/
    x=long(0)
    for digit in str(number):
       x = x*len(fromradix) + fromradix.index(digit)
    
    res=""
    while x>0:
        d = x % len(toradix)
        res = toradix[d] + res
        x /= len(toradix)
    
    return res
