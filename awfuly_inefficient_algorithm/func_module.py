# the module contains function my_gen
# which generates x fake emails.
# To generate just 5 emails it takes almost 1 second
# well that's a result would never expect!
# This function is going to be imported to main.py module
# and used to generate 100 emails that takes 10 second


def my_gen(x):
    from faker import Faker

    while x:
        x -= 1
        yield Faker().email()


if __name__ == "__main__":
    g = my_gen(5)
    for i in g:
        print(i)

# output:
# lbell@example.net
# codysmith@example.net
# tiffany82@example.net
# alan77@example.net
# samantha41@example.net
# [Finished in 854ms]
