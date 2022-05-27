
# #range(5) ------->[0, 1, 2, 3, 4]

# def userCountMsg(num):
#     for i in range(num):
#         print(f"Hello World! {i}")

# option = input("How many times do you want to print 'Hello World'?")

# userCountMsg(int(option))

#List  (Same as array in javaScript)
elements = ["a", "b", "c", "a"]

for e in elements:
    print(e)

# using range (Slower form)
for i in range(4):
    print(elements[i])

# Dictionary - key/value store -  cannot duplicate keys

me = {
    "first": "Chris",
    "last": "Finster",
    "age": 34
}

print(me)
# access with the key instead of index
print(me["age"])

