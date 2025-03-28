# 编写一个程序来计算输入中单词的频率。 按字母顺序进行排序后输出。
# 假设为程序提供了以下输入：
#
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
#
# 然后，输出应该是：
#
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:

def task(input):
    word=""
    freq={}
    for i in input:
        if i.isalnum():
            word += i
        else:
            if word:
                freq.get(word, 0)+1
            word=""

        if word:
            freq[word] = freq.get(word, 0)+1

    sort = sorted(freq.items(), key = lambda x: x[0])

    return dict(sort)

output = task("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3")

print(output)