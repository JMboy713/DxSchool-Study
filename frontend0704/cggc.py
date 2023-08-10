# origin="ABCDECGGCDKEDCGGCGGCDDDD";
# count=0
# i=0
# while i<=len(origin):
#     if origin[i:i+4]=='CGGC':
#         count+=1
#         i+=4
#     else:
#         i+=1
#         continue
# print(count)


def select(origin, main):
    count = 0
    i = 0
    while i <= len(origin):
        if origin[i : i + len(main)] == main:
            count += 1
            i += len(main)
        else:
            i += 1
            continue
    return count


print(select("ABCDECGGCDKEDCGGCGGCDDDD", "CGGC"))
