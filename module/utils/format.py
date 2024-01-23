PERCENT_FORMAT = '%'
PERCENT_2_FORMAT = '.2%'

def decimal_format(decimals):
    return f'.{decimals}f'

def decimal_format_2(decimals):
    return f',.{decimals}f'

def roundUp_format(decimals):
    return f'>10.{decimals}'

def roundDown_format(decimals):
    return f'<10.{decimals}'

def fomatWithDecimals(num, type):
    return format(num, type)