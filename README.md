**NthFiniteDifferences**

This is a Python Code project is part of a chellenge to learn self.

This primer code is a python module to calculate integer series from 
a generic formula for finite differences of any order.

The call to this method is:

    from NthFiniteDifferences import findiff_nth as findiff
    
    if __name__ == '__main__':
        
        """
        The argument coeffs   is a tuple[int] such as nth_order == len(coeffs)
        The argument initdata is a tuple[int] such as nth_order == len(initdata)
        The argument index    is a int        such as index >= 0
        """
        
        print(f'findiff({coeffs}, {initdata}, {index})'+
              f'  ==  {findiff(coeffs,initdata,index)}')