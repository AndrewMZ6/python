even_list = [x for x in range(2, 99) if x % 2 == 0]
even_list.append(99)


def check_function(func):
    def new_func(input_list, chunk_size):
        try:
            assert chunk_size >= 1
            new_list = func(input_list, chunk_size)
            return new_list
        except AssertionError:
            print(
                "The value of chunk_size must be positive integer, not %s"
                % str(chunk_size)
            )

    return new_func


def power_of_two(func):
    def new_func(input_list, chunk_size) -> list:
        input_list2 = func(input_list, chunk_size)

        chunk1, chunk2, *other_chunks = input_list2
        chunk1, chunk2 = [x**2 for x in chunk1], [x**2 for x in chunk2]
        temp = [chunk1, chunk2]

        for x in other_chunks:
            temp.append(x)
        return temp

    return new_func


# @check_function
def chunker(input_list: list, chunk_size: int) -> list:

    chunked_list = []
    left_pointer = 0
    right_pointer = chunk_size
    chunks_number = len(input_list) // chunk_size

    for i in range(chunks_number):
        chunked_list.append(input_list[left_pointer:right_pointer])
        left_pointer, right_pointer = right_pointer, right_pointer + chunk_size

    if len(input_list) % chunk_size != 0:
        chunked_list.append(input_list[chunk_size * chunks_number :])

    return chunked_list


#

chunker = check_function(chunker)
first_chunk = chunker(even_list, -7)


print(first_chunk)
