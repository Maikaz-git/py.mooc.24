# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int) -> dict:
    import string

    with open(filename, "r") as f:

        data = f.read()
        words = data.split() ## lst
        #print(string.punctuation) 
        
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in words]

        return {w:stripped.count(w) for w in stripped if stripped.count(w) >= lower_limit}



if __name__=="__main__":
    print(most_common_words("comprehensions.txt", 3) )