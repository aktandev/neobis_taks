class List:
    def remove_(self, integer_list, values_list):
        for v_element in values_list:
            while v_element in integer_list:
                integer_list.remove(values_list)
        return integer_list


l = List()
integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
values_list  = [1, 3, 4, 2]
print(l.remove_(integer_list, values_list))