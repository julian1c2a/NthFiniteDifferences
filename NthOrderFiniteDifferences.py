"""
    Module to calculate finite differences
    given an n_th order formula.

    Calculates the relation
    f(n+1) / f(n) as numpy.longdouble.

    Owner of repository: julian1c2a at GitHub

    The formula to calculate the result is given by the expression:
    — f(1) = v_1
    — f(2) = v_2
    — …
    — f(n) = v_n
    — …
    — f(i+n+1) = c_1*f(i+1) + c_2*f(i+2) + … + c_n*f(i+n)

    Entries will be:
    — The coefficients of the formula (n for n_th order) as a list or tuple in general.
    — The initial values for the series (n for n_th order) as a list or tuple in general.
    — The index of required value at the series.

    Returned values will be:
    — As a tuple with the n (as n_th order) values
    referenced by the index.
    — Add some important relations between the successive terms of the series that it be
    enough to verify the right calcul.
    (For example, the golden ratio or geometric sum).
"""


def findiff_1st(coef_first: int, first: int, idx: int) -> tuple:
    result_list: list = [None]
    ix: int = 0
    while 0 <= ix < idx+1:
        if ix > 0:
            if ix == 1:
                result_list[0] = first
            elif ix == 2:
                result_list[0] += coef_first*first
            elif ix == 3:
                result_list[0] += (coef_first**2)*first
            elif ix == 4:
                result_list[0] += (coef_first**3)*first
            else:
                result_list[0] += coef_first*result_list[0]
        ix += 1
    return tuple(result_list)


def findiff_2nd(coef_first: int, coef_second: int,
                first: int, second: int,
                idx: int) -> tuple:
    result_list: list = [None, None]
    ix: int = 0
    while 0 <= ix < idx+1:
        if ix > 0:
            if ix == 1:
                result_list[0] = first
                result_list[1] = second
            elif ix == 2:
                result_list[0] = second
                result_list[1] = coef_first*first + coef_second*second
            elif ix == 3:
                result_list[0] = coef_first*first + coef_second*second
                result_list[1] = ((coef_first+coef_second**2)*second +
                                  (coef_second*coef_first)*first)
            elif ix == 4:
                result_list[0] = ((coef_first+coef_second**2)*second +
                                  (coef_second*coef_first)*first)
                result_list[1] = (((coef_first**2)+(coef_first*coef_second**2))*first +
                                  ((2*coef_first*coef_second)+(coef_second**3))*second)
            else:
                temp: int = result_list[0]
                result_list[0] = result_list[1]
                result_list[1] = coef_first*temp + coef_second*result_list[1]
        ix += 1
    return tuple(result_list)


def findiff_3rd(coef_first: int, coef_second: int, coef_third: int,
                first: int, second: int, third: int,
                idx: int) -> tuple:
    result_list: list = [None, None, None]
    ix: int = 0
    while 0 <= ix < idx+1:
        if ix > 0:
            if ix == 1:
                result_list[0] = first
                result_list[1] = second
                result_list[2] = third
            elif ix == 2:
                result_list[0] = second
                result_list[1] = third
                result_list[2] = coef_first*first + coef_second*second + coef_third*third
            elif ix == 3:
                temp_1: int = result_list[1]
                result_list[0] = third
                result_list[1] = result_list[2]
                result_list[2] = coef_first*third + coef_second*temp_1 + coef_third*result_list[2]
            else:
                temp_1: int = result_list[0]
                temp_2: int = result_list[1]
                result_list[0] = temp_2
                result_list[1] = result_list[2]
                result_list[2] = coef_first*temp_1 + coef_second*temp_2 + coef_third*result_list[2]

        ix += 1
    return tuple(result_list)


def findiff_nth(coeffs: tuple,
                initdata: tuple,
                index: int) -> tuple:

    nth_order: int = len(coeffs)

    if (nth_order != len(initdata)) or (nth_order < 1) or (index < 0):
        return tuple([None]*nth_order)

    if nth_order == 1:
        return findiff_1st(coeffs[0], initdata[0], index)

    result_list: list = list(initdata)
    for idx in range(1, index):
        # GUARDAMOS EL HEAD DE LA LISTA (SE VA A PERDER)
        first_item_list: int = result_list[0]
        # COGEMOS EL TAIL DE LA LISTA
        result_list = result_list[1:]
        # CALCULAMOS EL PRIMER SUMANDO DEL NUEVO TÉRMINO
        temp: int = coeffs[0]*first_item_list
        for ix in range(1, nth_order):
            temp += coeffs[ix]*result_list[ix-1]
        # EL TÉRMINO A ANEXAR ESTÁ YA CALCULADO
        # HACEMOS EL APPEND AL FINAL DE LA LISTA
        result_list.append(temp)
    return tuple(result_list)
