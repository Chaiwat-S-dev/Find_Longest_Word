str = "this is an awesome test"
print("string : {}".format(str))
list = str.split(" ")
print("list : {}".format(list))
max = list[0]
print("max : {}" .format(max))
for i in range(len(list)) :
    if (len(list[i]) > len(max)):
        max = list[i]
print("max : {}".format(max))
max_ = list[0]
list_ = [x for x in list if len(x) > len(max_)]
print("max : {}".format(list_))