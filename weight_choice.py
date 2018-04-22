# coding:utf-8
import random

#把序列按权重值扩展成:lists=[A,A,A,A,A,B,B,C,C,D],然后random.choice(lists)随机选一个就行。
# 虽然这样选取的时间复杂度是O(1)，但是数据量一大，空间消耗就太大了。
def weight_choice1(list, weight):
    """
    :param list: 待选取序列
    :param weight: list对应的权重序列
    :return:选取的值
    """
    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)
#复杂度o(n)
def windex(weight):
    t = random.randint(0, sum(weight) - 1)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i


if __name__ == "__main__":
    for i in range(10):
        print(weight_choice1(['A', 'B', 'C', 'D'], [5, 2, 2, 1]))
        print(windex([5, 2, 2, 1]))