# (a) 将字符串格式的列表转为列表格式
lib = "<ul><li>matplotlib</li><li>numpy</li><li>pandas</li><li>bs4</li><li>requests</li><li>selenium</li></ul>"
lib_list = []
start = "<li>"
end = "</li>"
index = 0
while index < len(lib):
    start_index = lib.find(start, index)
    end_index = lib.find(end, start_index)
    if start_index != -1 and end_index != -1:
        lib_list.append(lib[start_index+len(start):end_index])
        index = end_index + len(end)
    else:
        break
print(lib_list)


# (b) 在 requests 之后插入 scipy 和 jieba
lib_list.insert(lib_list.index("requests")+1, "scipy")
lib_list.insert(lib_list.index("requests")+2, "jieba")
print(lib_list)


# (c) 删除 bs4
lib_list.remove("bs4")
print(lib_list)


# (d) 按字符长度对 lib_list 中各项进行降序排序
lib_list.sort(key=lambda x: len(x), reverse=True)
print(lib_list)
