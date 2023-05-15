from subprocess import Popen, PIPE

# rows = 5
# cols = 4
# grid = np.zeros((rows, cols), dtype=int)
#
# gridStr = "00011101000100110000"
# # gridStr = "000000000"
# # gridStr = "111111111"
# index = 0
#
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         grid[i][j] = int(gridStr[index])
#         index += 1


def find_path(nodes):
    p = Popen(["dstar.exe"], shell=True, stdout=PIPE, stdin=PIPE)

    rows = len(nodes)
    cols = len(nodes[0])

    # defines grid dimensions
    inputStr = f"{rows} {cols}\n"

    # adds grid
    for i in range(len(nodes)):
        row = nodes[i]
        for node in row:
            inputStr += f"{node.value} "
        if i < len(nodes) - 1:
            inputStr += "\n"
    # print(inputStr)

    # writes input
    p.stdin.write(bytes(inputStr, "UTF-8"))

    # flushes input
    p.stdin.flush()

    # decodes output
    byteLines = p.stdout.readlines()
    output = "\n".join([line.decode("UTF-8").strip() for line in byteLines])
    # print("Output: " + output)

    noPossiblePath = output == "No possible path"
    if noPossiblePath:
        return []

    # extracts path from output
    path = []
    points = output.split("\n")
    for i in range(1, len(points) - 1):
        # print("Point: " + points[i])
        x, y = points[i].split(" ")
        path.append((int(x), int(y)))

    return path

