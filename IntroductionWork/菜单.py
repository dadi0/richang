import Fibonacci as one
import Qsort as two
import Graham as three
import Prim as four
import Dynamic as five

def hengxian():
    for i in range(40):
        print('-', end='')
    return ''

def main():
    print(hengxian())
    print('          《算法设计与分析》')
    print(hengxian())
    print('1. 算法分析基础——Fibonacci序列问题')
    print('2. 分治策略的应用——快速排序')
    print('3. 计算几何——凸包问题')
    print('4. Prim算法求最小生成树')
    print('5. 动态规划法在图问题中的应用——子段和问题')
    print('6. 退出本实验')
    print(hengxian())
    print('请输入您所要执行的操作（1，2，3，4，5，6）')

tag = '0'
while tag != '6':
    main()
    tag = input()
    if tag == '1':
        print('利用迭代算法找到的最大正整数n为：%d执行时间为：%f'
              % one.MaxIntAndTime(2**31))
        print('当n为35时迭代执行次数为：%d,花费的时间为：%f'
              % one.DieDaiCountAndTime(35))
        print('当n为35时递归执行次数为：%d,花费的时间为：%f'
              % one.DiGuiCountAndTime(35))
    elif tag == '2':
        print('请以空格为分界符输入需要排序的数组')
        list1 = list(map(eval, input().split()))
        two.qsort(list1, 0, len(list1)-1)
        print('排序后的结果为：', end='')
        for i in list1:
            print('%s' % i, end=' ')
        print()
    elif tag == '3':
        print('请以,为x与y的分界符空格为点与点的分界符输入树的坐标')
        list2 = list(map(eval, input().split()))
        print('请输入每头牛的占地大小')
        number = eval(input())
        print('最多能养%d头牛' % int(three.psort(list2)/number))
    elif tag == '4':
        print('请输入城市个数')
        n = eval(input())
        print('请输入各个城市之间距离的邻接矩阵(,为各个距离的分界符无穷大用float(\'inf\'))')
        g = []
        for i in range(1, n+1):
            print('请输入第%d行：' % i, end='')
            row = eval(input())
            g.append(row)
        print('请输入每个单位长度的价格')
        money_one = eval(input())
        money = four.prim(g, money_one)
        print('最低费用为%d' % money)
    elif tag == '5':
        print('请输入需要求的数列以空格为分界符')
        list3 = list(map(eval, input().split()))
        MaxNumber = five.dynamic(list3)
        print('最大和为%d' % MaxNumber)
    elif tag == '6':
        break
    else:
        print('请输入正确的序号')
    print('是否返回到主菜单 Y(是)/N(否)')
    tag = input()
    if tag == 'N':
        break
