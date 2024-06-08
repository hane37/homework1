
def dfs(v, graph, state, dfs_num, in_on_stack, Ostack, Rstack):
    global dfs_counter
    state[v] = 1
    dfs_num[v] = dfs_counter
dfs_counter += 1

    Ostack.append(v)
    in_on_stack[v] = True
    Rstack.append(v)

    for w in graph[v]:
        if state[w] == -1:
            dfs(w, graph, state, dfs_num, in_on_stack, Ostack, Rstack)
        elif in_on_stack[w]:
            while dfs_num[w] < dfs_num[Rstack[-1]]:
                Rstack.pop()

    state[v] = 0

    if v == Rstack[-1]:
        Rstack.pop()

        while True:
            w = Ostack.pop()
            in_on_stack[w] = False
            comp[w] = v
            connected_components[v].append(w)

            if w == v:
                break


def cheriyan_mehlhorn_gabow():
    global n, m, graph, connected_components, state, comp, dfs_num, in_on_stack, dfs_counter
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    connected_components = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    dfs_counter = 1

    state = [-1] * (n + 1)
    comp = [-1] * (n + 1)
    dfs_num = [-1] * (n + 1)
    in_on_stack = [False] * (n + 1)
    Ostack = []
    Rstack = []

    for i in range(1, n + 1):
        if state[i] == -1:
            dfs(i, graph, state, dfs_num, in_on_stack, Ostack, Rstack)

    knt = 1

    for i in range(1, n + 1):
        if comp[i] == i:
            print("component number", knt)
            print(*connected_components[i])
            knt += 1


cheriyan_mehlhorn_gabow()