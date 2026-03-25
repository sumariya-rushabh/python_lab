# Open file in read mode
f = open("rushabh.txt", "r")

# ----------- readline() -----------
print("Using readline():")
lines1 = f.readline()
lines2 = f.readline()

print("Line 1:", lines1.strip())
print("Line 2:", lines2.strip())

# Reset file pointer to beginning
f.seek(0)

# ----------- readlines() -----------
print("\nUsing readlines():")
lines = f.readlines()

print("All lines:", lines)
print("Second line:", lines2.strip())

# Close file
f.close()