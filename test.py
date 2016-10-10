fhand = open("/tmp/test")
for line in fhand:
    if line.startswith("From: "): continue
    print(line.rstrip())

