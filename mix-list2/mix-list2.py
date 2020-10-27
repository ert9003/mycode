#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.extend('dns') # this line will add
                    # 'd', 'n', and 's' to
                    # the end of our list
print(proto)
#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)
proto.append('dns') # this line will add 'dns' to the end of our list
protoa.append('dns') # this line will add 'dns' to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print (proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- then print result
print (protoa)

#!/usr/bin/env python3
"""using csv data"""
import csv

def main():
    # open the CSV data set
    with open("vendor.csv", "r") as vendorfile:
        vendata = csv.reader(vendorfile, delimiter=",")
        # The CSV data is now nicely prepared.
        # Each new row is a Python list.
        # We can reference the items we want to print
        # as we loop over the data.
        for row in vendata:
            print("The IP address " + row[2] + \
              " requires the driver " + row[3])

main()











