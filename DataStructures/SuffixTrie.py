def xyz(t):
    """ Make suffix trie from t """
    t += '$'  # terminator symbol
    root = {}
    for i in range(len(t)):  # for each suffix
        cur = root
        print("i = ", i)
        print(t[i:])
        for c in t[i:]:  # for each character in i'th suffix
            print("c = ",c)
            if c not in cur:
                cur[c] = {}  # add outgoing edge if necessary
            cur = cur[c]

    print("cur =", root)

xyz('ABCD')