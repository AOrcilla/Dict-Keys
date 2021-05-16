name = input("Enter file:") #input file name
if len(name) < 1 : name = "mbox-short.txt" #if the file name is less than 1 character then it will default to the name listed.
handle = open(name) # variable to open the file name

lins = dict() # empty dict we'll need to use this later to store our data

# Count the number of sent emails from each User
for lin in handle: #First loop to go through each line and split the content
    lin = lin.rstrip()
    words = lin.split()
    for wrd in words: #Loop that reads through each word
        if wrd == 'From' :
            sender = words[1]   #if first word begins with 'From' then store the User's email
            if sender in lins:    #checks if the User is in the dictionary
                lins[sender] += 1 #if User is in the dictionary, then increase counter
            else:
                lins[sender] = 1  #if User is not in the dictionary, then declare new item in dictionary with starting counter of 1

# Find the User with the most sent emails
maxUser = None  #declare string variable for the User
maxEmails = 0   #declare int variable for # of emails sent

for user in lins:   #Looks at every user in the dictionary
    if lins[user] > maxEmails:  #checks if the user's # of sent emails is larger than previous maximum
        maxEmails = lins[user]    #if so, then override maximum value with # of emails sent
        maxUser = user            #and store corresponding user

print(maxUser, maxEmails)   #print the User with most sent emails
