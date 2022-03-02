#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        res = [i / j for i , j in zip(my_list_1, my_list_2)]
    except ZeroDivisionError:
        i / j == 0
        print("division by 0")
    except TypeError:
        i / j == 0
        print("wrong type")
    except ValueError:
        i / j == 0
        print("out of range")
    finally:
        return res

    
        
