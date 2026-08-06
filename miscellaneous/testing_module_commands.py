# the script is used for checking commands of module while reading documentation
# the scenario is to import module for example sys
import sys

# then create a name "command" to represent function of the module or attribute
# without () at the end
# for example "sys path". Since the it's an attribute it falls into category "not callable"
# and the result will be just printted without trying to call it
command = sys.path

# on the other hand if we want to test method getwindowsversion() of the module
# we also do this
command = sys.getwindowsversion

# but this time command becomes "callable" and gets called

if callable(command):
    print("callable:", end="\n\n")
    print(command("gdsg"), end="\n\n")

    print(list(filter(lambda s: not s.startswith("_"), dir(command))))
else:
    print("not callable:", end="\n\n")
    print(command, end="\n\n")
    print(list(filter(lambda s: not s.startswith("_"), dir(command))))
