"""
7.2 Write a program that prompts for a file name, then opens that file and reads 
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and 
compute the average of those values and produce an output as shown below. Do 
not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

# check if file exists
try:
	fh = open(fname)
except:
    quit()

# initialize
count = 0
total = 0
# handle line by line
for line in fh:
    # handle two newlines case:
    line = line.rstrip()
    # find lines of the form
    if not line.startswith("X-DSPAM-Confidence:"):
    	continue
    else:
        idx = line.find(':')
        substr = line[idx+1:]
        total = total + float(substr)
        count = count + 1
    # print(line)
#print("Done")
print('Average spam confidence:', total/count)