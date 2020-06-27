"""
Using getopt

Syntax: getopt.getopt(args, options, [long_options])
Parameters:
    args: List of arguments passed.
    short_options: String of short_options letters that the script want to recognize. Options that require an argument should be followed by a colon (:).
    long_options: List of string with the name of long_options. Options that require arguments should be followed by an equal sign (=).

Return Type: Returns value consisting of two elements: the first is a list of (option, value) pairs.
The second is the list of program arguments left after the option list was stripped.
"""

import getopt, sys

# Using short_options
# only the short options with colon (:) are parsed
print(getopt.getopt(['-a', '-bb_val', '-c', 'c_val'], 'ab:c:'))

# Using long_options
# Only the long options with equal (=) are parsed
print(getopt.getopt(['--noarg', '--arg_1', 'arg_1_value', '--arg_2=arg_2_value'], "", ['noarg', 'arg_1=', 'arg_2=']))

# Example
arg_list = sys.argv[1:]
options = "h:i:o:"
long_options = ["in_file=", "out_file=", "output="]

usage = """Usage:
<python_interpreter> <file_name> -i <input_file> -o <output_file>
<python_interpreter> <file_name> -in_file <input_file> -out_file=<output_file>
"""
try:
    options, values = getopt.getopt(arg_list, options, long_options)
except:
    print(usage)
    sys.exit()

for opt, val in options:
    if opt in '-h':
        print(usage)
        sys.exit()
    elif opt in ('-i', '--in_file'):
        input_file = val
        print("Input File: ", input_file)
    elif opt in ('-o', '--out_file'):
        output_file = val
        print("Output File: ", output_file)

# Special case
# <python_interpreter> <file_name> -i -- -o <output_file>
# argv: <file_name> -i -- -o <output_file>
# options: [('-i', '--')]
# if getopt encounters -- in the input arguments, it stops processing the remaining arguments as options.
