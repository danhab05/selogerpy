# open txt file
f = open("a.txt", "r")
# add the data in the file the a var
data = f.readlines()
# remove unwanted \n for new lines and '' left over by the code above
# readlines() returns a list so we need to convert data to str
# in data[] add the line you wish to read from
info = str(data[0]).strip("\n").strip("'")
# run the code
exec(info)