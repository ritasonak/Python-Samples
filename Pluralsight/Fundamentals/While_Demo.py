c = 5
while c != 0:
    print c
    c -= 1

while c:
    print c
    c -= 1

# while True:
#   print("Looping")
c = 5
while True:
    response = input()
    if response == 1:
        print "break"
        break
c = 5
while c != 0:
    if c == 1:
        c -= 1
        continue
    print c
    c -= 1

