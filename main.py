"""
Created on Sat Sep  2 21:32:23 2023

@author: Julián Calderón Almendros
"""

from NthOrderFiniteDifferences import findiff_nth as findiff

if __name__ == "__main__":
    # sys.set_int_max_str_digits(1_000_000)
    #
    # limit: int = 10
    #
    # print("Series de diferencias finitas de tercer orden [comienzo]")
    # print("")
    # print("")
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # for index in range(2 * limit):
    #     if index != 0:
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         series3rd: tuple = tuple(findiff_3rd(1, -1, 2, 2, 1, 1, index))
    #         print(f"3RD ORDER número de índice:{index-1} es {series3rd[0]}")
    #         print(f"3RD ORDER número de índice:{index} es {series3rd[1]}")
    #         print(f"3RD ORDER número de índice:{index+1} es {series3rd[2]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print("")
    #         series3rd_p: tuple = tuple(findiff((1, -1, 2), (2, 1, 1), index))
    #         print(f"GENERAL   número de índice:{index-1} es {series3rd_p[0]}")
    #         print(f"GENERAL   número de índice:{index} es {series3rd_p[1]}")
    #         print(f"GENERAL   número de índice:{index+1} es {series3rd_p[2]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # print("")
    # print("")
    # print("Series de diferencias finitas de tercer orden [final]")
    # print("")
    # print("")
    # print("")
    # print("")
    # print("Series de diferencias finitas de segundo orden [comienzo]")
    # print("")
    # print("")
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # for index in range(limit):
    #     if index != 0:
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         series2nd: tuple = tuple(findiff_2nd(1, 1, 1, 1, index))
    #         print(f"2ND ORDER número de índice:{index-1} es {series2nd[0]}")
    #         print(f"2ND ORDER número de índice:{index} es {series2nd[1]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print("")
    #         series2nd_p: tuple = tuple(findiff((1, 1), (1, 1), index))
    #         print(f"GENERAL   número de índice:{index-1} es {series2nd_p[0]}")
    #         print(f"GENERAL   número de índice:{index} es {series2nd_p[1]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # print("")
    # print("")
    # print("Series de diferencias finitas de segundo orden [final]")
    # print("")
    # print("")
    # print("")
    # print("")
    # print("Series de diferencias finitas de primer orden [comienzo]")
    # print("")
    # print("")
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # for index in range(limit):
    #     if index != 0:
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         series1st: tuple = tuple(findiff_1st(1, 1, index))
    #         print(f"1ST ORDER número de índice:{index-1} es {series1st[0]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print("")
    #         series1st_p: tuple = tuple(findiff((1,), (1,), index))
    #         print(f"GENERAL   número de índice:{index-1} es {series1st_p[0]}")
    #         print(
    #             f"{index}     -------------------------------------------------------------------------------"
    #         )
    #         print(
    #             "--------------------------------------------------------------------------------------"
    #         )
    # print(
    #     "--------------------------------------------------------------------------------------"
    # )
    # print("")
    # print("")
    # print("Series de diferencias finitas de primer orden [final]")

    """
    The argument coeffs   is a tuple[int] such as nth_order == len(coeffs)
    The argument initdata is a tuple[int] such as nth_order == len(initdata)
    The argument index    is a int        such as index >= 0
    """

    limit: int = 3 * 5

    coeffs: tuple[int] = (1, 2, -1, 1, 2)
    initdata: tuple[int] = (1, 1, 1, 2, 1)

    for index in range(1, limit + 2, 4):
        print(
            f"findiff({coeffs}, {initdata}, {index})"
            + f"  ==  {findiff(coeffs, initdata, index)}"
        )
        print(
            f"findiff({coeffs}, {initdata}, {index + 1})"
            + f"  ==  {findiff(coeffs, initdata, index + 1)}"
        )
