# Write your solution here
import re
def find_words(st: str )->list:
    # wildcard chars -> "." ex. ca. -> car, cat
    # "*" ca* -> california, cat ,caring  #### *ane -> crane, insane, aeroplane
    words_lst = []
    with open("words.txt") as my_file:
        for wrd in my_file:
            wr = wrd.strip()
            words_lst.append(wr)
    
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    result = []
    if st.startswith(".") :   
        for el in alph:
            if el + st[1:]  in words_lst:
                result.append(el+st[1:])

    elif st.endswith(".") and st.count(".")==1:
        for el in alph:
            if st[:-1] + el in words_lst:
                result.append(st[:-1] + el)
    
    elif st.startswith("*"):
        for wrd in words_lst:
            if wrd.endswith(st[1:]):
                result.append(wrd)

    elif st.endswith("*"):
        for wrd in words_lst:
            if wrd.startswith(st[:-1]):
                result.append(wrd)

    elif "." in st:
        regex = re.compile(st)
        result = [s for s in words_lst if re.match(regex, s) and len(s)== len(st)]


    elif "." not in st or "*" not in st:
        if st in words_lst:
            result.append(st)

    return result

if __name__=="__main__":
    print(find_words("c.d."))
