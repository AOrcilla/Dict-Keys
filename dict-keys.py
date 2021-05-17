name = input("Enter file:") #input file name
if len(name) < 1 : name = "mbox-short.txt" #if the file name is less than 1 character then it will default to the name listed.
handle = open(name) #variable to open the file name

di = dict() #empty dict we'll need to use this later to store our data

# Count the number of sent emails from each User
for lin in handle: #First loop to go through each line and split the content
    lin = lin.strip()
    words = lin.split()
    for wrd in words: #Loop that reads through each word
        if wrd == "From": #Reads through split words to identify if the line starts with 'From:'
            wrd = lin.strip() #strips whitespace
            email = words[1] #if first word begins with 'From' then store the User's email since the email always comes right after 'From'
            di[email] = di.get(email, 0) + 1 #idiom: retrieve data / create / update counter

# Find the User with the most sent emails
largest = -1 #declare int variable for # of emails sent
most = None #declare string variable for the User

for k,v in di.items(): #Looks at every user in the dictionary .items gives you all key value pairs
    if v > largest: #checks if the user's # of sent emails is larger than previous maximum
        largest = v #if so, then override maximum value with # of emails sent
        most = k #and store corresponding user
print(di)
print(most,largest) #print the User with most sent emails
#End
