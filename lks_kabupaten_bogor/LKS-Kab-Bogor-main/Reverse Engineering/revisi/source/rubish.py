# from faker import Faker

# tplate = """
# void msn_{num}(){{
#  _pp("{word}\n");
#  sysnum = {num};
# }}
# """

# fake = Faker()
# for i in range(335):
#     print(tplate.format(num=i, word=fake.word()))


FLAG = "LKS{what_to_do_when_there's_nothing_in_main}"
ENV = "FIRST_STEP"

x = []

for i in range(len(ENV) - 1):
    tmp = ord(ENV[i]) ^ 0x25
    tmp ^= ord(ENV[i+1])

    x.append(tmp)
x.append(ord(ENV[-1]))

print(x)

# print(bytes(x), len(ENV), len(x))

# for i in range(len(x) - 1, 0, -1):
#     # print(x[i-1], x)
#     tmp = x[i] ^ x[i-1]
#     tmp ^= 0x25

#     x[i - 1] = tmp

# print(bytes(x), len(ENV), len(x))



ENV = "LKS{what_to_do_when_there's_nothing_in_main}\n"

x = []

for i in range(len(ENV) - 1):
    tmp = ord(ENV[i]) ^ 0x25
    tmp ^= ord(ENV[i+1])

    x.append(tmp)
x.append(ord(ENV[-1]))

print(x)

y = []
for i in x:
    y.append(i << 5 | i >> 3)

print(y)

for i in range(len(y)):
    y[i] = ((y[i] >> 5 | y[i] << 3) & 0xff)

print(y)

for i in range(len(x) - 1, 0, -1):
    # print(y[i-1], x)
    tmp = y[i] ^ y[i-1]
    tmp ^= 0x25

    y[i - 1] = tmp

print(bytes(y))