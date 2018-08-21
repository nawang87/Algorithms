def compress(self, chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    inilen = len(chars)
    curr = 0
    i = 0
    while i < len(chars):
        currchar = chars[i]
        count = 1
        j = i + 1
        while j < len(chars) and chars[j] == currchar:
            count += 1
            j += 1
        i = j
        chars[curr] = currchar
        curr += 1
        if count > 1:
            for k in str(count):
                chars[curr] = k
                curr += 1

    return min(inilen, len(chars[:curr]))
