from collections import Counter

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        self.integers_list = integers_list
        self.digits_list = digits_list
        my_list = []
        integers_list = str(integers_list)
        c = Counter(integers_list)
        for i in digits_list:
            if c[str(i)]:
                my_list.append((i, c[str(i)]))
            else:
                my_list.append((i, 0))

        return my_list

l1 = List()
integers_list1 =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list1 = [1, 3]
print(l1.count_spec_digits(integers_list1, digits_list1)) # [(1, 3), (3, 2)]

l2 = List()
integers_list2 = [-18, -31, 81, -19, 111, -888]
digits_list2 = [1, 8, 4]
print(l2.count_spec_digits(integers_list2, digits_list2)) # [(1, 7), (8, 5), (4, 0)]

l3 = List()
integers_list3 = [-77, -65, 56, -79, 6666, 222]
digits_list3 = [1, 8, 4]
print(l3.count_spec_digits(integers_list3, digits_list3)) # [(1, 0), (8, 0), (4, 0)]
