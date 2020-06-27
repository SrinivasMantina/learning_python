"""
Using sys.argv
"""
import sys

num_of_arguments = len(sys.argv)                        # including file_name
# By default the zeroth argument is file name. so the sys.argv has at least one argument.
print("file_name: ", sys.argv[0])
print("other arguments", end=": ")
for arg in range(1, num_of_arguments):
    print(sys.argv[arg], end=" ")
print("\nnumber of arguments passed: ", num_of_arguments-1)