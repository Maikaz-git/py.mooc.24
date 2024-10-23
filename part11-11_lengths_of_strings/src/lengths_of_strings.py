# WRITE YOUR SOLUTION HER
def lengths(strings: list):
    return {el:len(el) for el in strings}


if __name__=="__main__":
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)