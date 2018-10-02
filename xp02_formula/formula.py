import re

regex_a = "(([+-]\s)?\d*)x2([^0-9]|$)"
regex_b = "(([+-]\s)?\d*)x([^2-9]|$)"
regex_c = "(?<![x(x2)(x1)])(([+-]\s)?\d+((?!(x|[0-9]))|$))"

# Maybe include the excluding any numbers after regex b's 1.
# Also add that it excludes plus when there is a plus

if __name__ == '__main__':

    def print_regex_results(regex, f):
        for match in re.finditer(regex, f):
            if match != "aaaaaaaaa":
                print(match.group(1))



    f = "3x2 - 4x + 1"

    #print_regex_results(regex_a, f)  # 3
    #print_regex_results(regex_b, f)  # - 4
    #print_regex_results(regex_c, f)  # 1

    #f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"

    #print("x2")
    #print_regex_results(regex_a, f2)  # 3, - 2
    #print("x")
    #print_regex_results(regex_b, f2)  # 4, - 7
    #print("c")
    #print_regex_results(regex_c, f2)  # 5, 4


    f = "1 - x2 + 48587x1"
    print_regex_results(regex_b, f)

    print("end")
