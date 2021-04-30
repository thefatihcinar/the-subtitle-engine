"""
	coded by Fatih Cinar
	in July 2018

	This algorithm clears up the time information
	in subtitles
"""

fileName = input("Enter the file name: ")

newFileName = input("Enter the file name for the new file: ")

with open (fileName,"r") as file:
    all_data =file.readlines()
    
length = len(all_data)

index_data = []


for (J,M) in zip(all_data,range(0,length)):
    if J == "\n":
        index_data.append(M)

who_to_pass = []
who_to_pass.append(0);who_to_pass.append(1)

for R in index_data:
    who_to_pass.append(R+1);who_to_pass.append(R+2)

with open (newFileName,"w") as file:
    # FIRST FEW LINES
    for U,Y in zip(all_data,range(0,length)):
        if Y in who_to_pass:
            pass
        else:
            file.writelines(U)
