a = 10
b = 20
c = 0

c = a
a = b
b = c

print("var A: ", a)
print("var B: ", b)

a2 = 30
b2 = 40

a2, b2 = b2, a2
print("var A2: ", a2)
print("var B2: ", b2)