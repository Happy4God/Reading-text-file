# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file(filename):
    open_file = open("./story.txt","r")
    read_file = open_file.read()


    boy = read_file.split()

    count = {}
    for x in boy:
        if x in count:
            count[x] += 1
        else:
            count[x] =1
    return count
print(read_file("./story.txt"))


    #text = read_file_content("./story.txt")
    # [assignment] Add your code here

    #return {"as": 10, "would": 20}

