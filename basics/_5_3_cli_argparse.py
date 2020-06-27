import argparse
my_parser = argparse.ArgumentParser(description='This is a simple argparse example')
my_parser.add_argument('-o', '--out_file', help="Prints output to a file")


# my_parser.version = '1.0'
# my_parser.add_argument('-a', action='store')
# my_parser.add_argument('-b', action='store_const', const=42)
# my_parser.add_argument('-c', action='store_true')
# my_parser.add_argument('-d', action='store_false')
# my_parser.add_argument('-e', action='append')
# my_parser.add_argument('-f', action='append_const', const=42)
# my_parser.add_argument('-g', action='count')
# my_parser.add_argument('-i', action='help')
# my_parser.add_argument('-j', action='version')


# Read arguments from command line
args = my_parser.parse_args()
