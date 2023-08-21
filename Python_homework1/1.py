# (a) 计算该文本由几个段落构成。
text = "Python is a widely used general purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an emphasis on code readability, and it allows programmers to express their concepts in fewer lines of code.\nPython is a programming language that lets you work quickly and integrate systems more efficiently.\nThere are two major Python versions: Python 2 and Python 3. Both are quite different.\nBefore we start Python programming, we need to have an interpreter to interpret and run our programs."
paragraphs = text.split('\n')
count_paragraphs = len(paragraphs)
print(f"该文本由{count_paragraphs}个段落构成。")

# (b) 提取出第一段的内容。
first_paragraph = paragraphs[0]
print(f"第一段的内容是：\n{first_paragraph}")

# (c) 统计第一段中包括哪些单词（不重复）。
words = set(first_paragraph.split())
print(f"第一段中包括的单词有：\n{words}")

# (d) 计算第一段中 Python 出现的次数，并利用字符串格式化操作打印输出
count_python = first_paragraph.count('Python')
print(f"第一段中Python出现了{count_python}次")
