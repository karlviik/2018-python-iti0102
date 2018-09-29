import re

regex_a = "(([+-]\s)?\d*)x2"
regex_b = "(([+-]\s)?\d*)x[^2-9]"
regex_c = "(?<!x2)([+-]\s)?\d+(?=[=\s$])"
regex_c = "(?<![x(x2)(x1)])(([+-]\s)?\d+(?!x))"

if __name__ == '__main__':

    def print_regex_results(regex, f):
        for match in re.finditer(regex, f):
            if match != "":
                print(match.group(1))



    f = "3x2 - 4x + 1"

    #print_regex_results(regex_a, f)  # 3
    #print_regex_results(regex_b, f)  # - 4
    #print_regex_results(regex_c, f)  # 1

    f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"

    print("x2")
    print_regex_results(regex_a, f2)  # 3, - 2
    print("x")
    print_regex_results(regex_b, f2)  # 4, - 7
    print("c")
    print_regex_results(regex_c, f2)  # 5, 4

    print("end")
