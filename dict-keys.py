name = input("Enter file:") #input file name
if len(name) < 1 : name = "mbox-short.txt" #if the file name is less than 1 character then it will default to the name listed.
handle = open(name) # variable to open the file name

lins = dict() # empty dict we'll need to use this later to store our data
for lin in handle: #First loop to go through each line and split the content
    lin = lin.rstrip()
    words = lin.split()
    for w in words: #Loop that reads through each word
        print(w) #Print statement to check that all words are printed in a separate line
