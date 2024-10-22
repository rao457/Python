haystack = "zohaib"
needle = "haib"
i = 0
substr = ""
result = -1
while i < len(haystack):
    for j in range(len(needle)):
        if haystack[i] == needle[j]:
            substr += haystack[i]
            result += 1
            i += 1
if substr == needle:
    print(result)
else:
    print(-1)
