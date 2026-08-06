# tThe idea of the unique_list class
# is to add functionality to build-in class list
# that removes duplicates but saves the order of the
# elements

# The first step is to create algorithm of how to
# filter duplicates and keep order

import sys


class unique_list(list):
    def __init__(self, x):
        super().__init__(x)
        # print(f"""x:\n
        # 		  {super()}\n
        # 		  type:\n
        # 		  {type(super())}\n
        # 		  dir:\n
        # 		  {dir(super())}\n""")
        # print(f"""x:\n
        # 		  {x}\n
        # 		  type:\n
        # 		  {type(x)}\n
        # 		  dir:\n
        # 		  {dir(x)}\n""")
        # print(f"""self:\n
        # 		  {self}\n
        # 		  type:\n
        # 		  {type(self)}\n
        # 		  dir:\n
        # 		  {dir(self)}\n""")

    def make_unique(self: list) -> list:
        S1 = set(self)
        new_list = list(S1)

        order = dict()
        for element in new_list:
            if element not in order:
                order[element] = L1.index(element)

        corrected_list = ["x"] * len(L1)

        for value, index in order.items():
            corrected_list[index] = value

        # the problem with this filter is that if original list L1 contains str values
        # then they will be filtered. That's not good. Yes
        corrected_list = list(filter(lambda x: not isinstance(x, str), corrected_list))

        # check if the correction is right:
        # to make sure that corrected list didn't remove some elements from the original
        #     if all unique elements of the original list
        # 	  are present in corrected list then the correction
        # 	  made right
        #
        # 	OR
        #
        # 	if set of original list and set of corrected list are equal

        assert set(self) == set(corrected_list), (
            "The number of unique elements does not match"
        )

        return corrected_list


L1 = [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14]

print(f"orginal list:\n{L1}")
print(f"Uniquefied list:\n{unique_list(L1).make_unique()}")


# OUTPUT:
# orginal list:
# [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 52.3, 3.14, 3.14]
# Uniquefied list:
# [1, 8.1, 9, 52.3, -6.1, 0, -90, 4, 3.14]
# [Finished in 234ms]
