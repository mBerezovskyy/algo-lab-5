def compute_lps_array(substring, len_of_substring, lps):
    len = 0
    index = 1
    lps[0] = 0

    while index < len_of_substring:
        if substring[index] == substring[len]:
            len += 1
            lps[index] = len
            index += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[index] = 0
                index += 1


def KMP(substring, string):
    len_of_substring = len(substring)
    len_of_string = len(string)
    lps = [0] * len_of_substring
    compute_lps_array(substring, len_of_substring, lps)

    string_index = 0
    substring_index = 0

    while string_index < len_of_string:
        if substring[substring_index] == string[string_index]:
            string_index += 1
            substring_index += 1
        else:
            if substring_index != 0:
                substring_index = lps[substring_index - 1]
            else:
                string_index += 1

        if substring_index == len_of_substring:
            return string_index - substring_index
    return -1

