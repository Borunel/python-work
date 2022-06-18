import sys # import module sys
script, encoding, error  = sys.argv #allocate script, encoding, errors to argv(from sys)


def main(language_file, encoding, errors): #define function main with arguments language_file, encoding,errors
    line = language_file#.readline() # line is declared to be the string read from 'language_file' (which is declared in the arguments) each line automatically has \n at the end so after finished, readline() will click to next line

    #if line: # if line is what? exists? has a value? what? - If there is a line.... i.e tests for empty string.
    print_line(line, encoding, errors) # print the line from 'language_file' in 6 + encoding and errors from argv
        #return main(language_file, encoding, errors) # function returns a re-run of function main()


def print_line(line, encoding, errors): #defines function print_line to take arguments line, encoding and errors
    next_lang = line#.strip() #next lang is line, with all extraneous characters stipped from beginning and end - in this case \n from end
    cooked_string = next_lang.decode(encoding, errors=errors)
    raw_bytes = cooked_string.encode(encoding, errors=errors) # raw_bytes is next_lang operated on by the encode function with the arguments encoding and 'errors=errors'
    # so errors = errors is an argument whuch can take different values - in this case it takes errors from print_line which takes errors from line 9 in main() which takes errors from the arguments of the function which are provided when the function is called on line 24 as error - one of the arguments of argv
     #cooked_string is raw_bytes operated on by decode with arguments encoding and error=errors

    print(cooked_string, "<===>", raw_bytes) # output result raw_bytes turns into (or is equivalent to) cooked_string

languages = b'\xd0\xa3\xd0\xba\xd1\x80\xd0\xd1\x97\xd0\xbd\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0' # declare languages to be the contents when opening languages.txt encoded as utf-8



main(languages, encoding, error)  # calls function main with arguments languages, encoding, error
