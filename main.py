from subprocess import Popen, PIPE

p = Popen(["a.exe"], shell=True, stdout=PIPE, stdin=PIPE)
# p = Popen(["dstar.exe"], shell=True, stdout=PIPE, stdin=PIPE)

for i in range(10):
    value = str(i + 1) + '\n'

    # writes input
    p.stdin.write(bytes(value, "UTF-8"))

    # flushes input
    p.stdin.flush()

    # receives output
    result = p.stdout.readline().strip()

    print(result.decode("UTF-8"))
