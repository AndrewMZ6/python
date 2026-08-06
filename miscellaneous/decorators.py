# define outer function
def outerfunc(inputfunc):
    """
    documentation string
    """
    print("this is outer function")
    outerVar = "outerVar"

    def innerfunc():
        print("this is executed before input function")
        inputfunc()
        print("this is inner function")
        innerVar = "innerVar"

    return innerfunc


# the function will be passed to outer function as an argument
def inputfunc():
    print("Hi I am input function")


# the function decoratedFunc is "decorated" with the outer function
print("----- decorator declaration ------------", end="\n\n")


@outerfunc
def decoratedFunc():
    print("Hi I am decorated function")


print("------ someVar = outerfunc(somefunc) -------", end="\n\n")
someVar = outerfunc(inputfunc)
print("\n")
print("------ someVar() -------", end="\n\n")
someVar()
print("\n")
print("------ outerfunc(somefunc) -------", end="\n\n")
outerfunc(inputfunc)
print("\n")
print("------ decoratedFunc() -------", end="\n\n")
decoratedFunc()

############## Cosole Output ########################

# ----- decorator declaration ------------

# this is outer function
# ------ someVar = outerfunc(somefunc) -------

# this is outer function


# ------ someVar() -------

# this is executed before input function
# Hi I am input function
# this is inner function


# ------ outerfunc(somefunc) -------

# this is outer function


# ------ decoratedFunc() -------

# this is executed before input function
# Hi I am decorated function
# this is inner function

# [Finished in 136ms]
