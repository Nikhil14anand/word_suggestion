import csv   #importing csv module
import enchant  #importing enchant module

word=input("ENTER THE WORD")   #word to be found or suggested

f = open('dictionary.csv','r')   #open and read the csv file

reader = csv.reader(f)

people = {}   #creating a empty dictionary

for row in reader:     #loop for filling the dictionary with the data of csv file
    people[row[0]] = {'':row[0]}


d = enchant.Dict(people)  # using people dictionary

d.check(word)

print(d.suggest(word))   # word will be suggested from the given dictionary


