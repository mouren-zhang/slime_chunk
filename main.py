import os
import csv
import time
import glob


def main():
    while True:
        print('=' * 20)
        print('输入序号，选择功能')
        print_data = {
            '0': '退出当前脚本',
            '1': '运行计算脚本',
            '2': '查看配置文件',
            '3': '修改配置文件',
            '4': '查史莱姆个数'
        }
        for k, v in print_data.items():
            print(k, v)

        a = input('$:')
        # 退出
        if a == '0':
            return 'ok'
        # 运行java
        elif a == '1':
            Run_Java()

        # 查看ini
        elif a == '2':
            Print_Ini()

        # 修改ini
        elif a == '3':
            Revise_Ini()

        # 查史莱姆
        elif a == '4':
            Csv_Slime()

        else:
            print('输入错误，请重新选择')


def Csv_Slime():
    '''
    查指定个数的
    :return:
    '''

    while True:
        print('=' * 20)
        print('输入序号，选择功能')
        print_data = {
            '0': '回到主菜单',
            '1': '列出最大所有',
            '2': '列出最小所有',
            '3': '列出指定个数',
            '4': '列出指定范围'
        }
        for k, v in print_data.items():
            print(k, v)
        a = input('$:')
        # 回主菜单
        if a == '0':
            return 'ok'
        # 列出最大所有
        elif a == '1':
            Csv_All_Max()
        # 列出最小所有
        elif a == '2':
            Csv_All_Min()
        # 列出指定个数
        elif a == '3':
            Csv_X()
        elif a == '4':
            csv_scope()
        else:
            print('输入有误')


def Csv_All_Max():
    # 文件名列表
    csv_name_list = glob.glob(r'Slime*.csv')

    # 获取csv文件名
    if len(csv_name_list) == 1:
        csv_name = csv_name_list[0]
    elif len(csv_name_list) == 0:
        print('未识别到数据文件')
        return 'nocsv'
    else:
        for i in range(0, len(csv_name_list), 2):
            if i + 1 >= len(csv_name_list):
                print(csv_name_list[i])
            else:
                print(csv_name_list[i], csv_name_list[i + 1])
        print('检测到数据文件有{}个'.format(len(csv_name_list)))
        print('请手动输入文件名')
        csv_name = input('输入csv文件名')
        if csv_name[:4] != '.csv':
            csv_name = csv_name + '.csv'

    time_start = time.time()
    # 输出全部最大值
    max_yes = 0
    max_list = []
    with open(csv_name, 'r') as f:
        read = csv.reader(f)
        for line in read:
            # 取最大值
            if int(line[2]) > max_yes:
                max_yes = int(line[2])
                # 最大值改变就清空列表
                max_list = []
            # 最大值加入列表
            if int(line[2]) == max_yes:
                max_list.append(line)
    time_stop = time.time()
    print('本次查询耗时约{}秒'.format(time_stop - time_start))
    print('最大值为{}，共查询到{}个'.format(max_yes, len(max_list)))
    save_csv('max.csv', max_list)
    print('已经保存到[max.csv]文件')


def Csv_All_Min():
    # 文件名列表
    csv_name_list = glob.glob(r'Slime*  .csv')

    # 获取csv文件名
    if len(csv_name_list) == 1:
        csv_name = csv_name_list[0]
    elif len(csv_name_list) == 0:
        print('未识别到数据文件')
        return 'nocsv'
    else:
        for i in range(0, len(csv_name_list), 2):
            if i + 1 >= len(csv_name_list):
                print(csv_name_list[i])
            else:
                print(csv_name_list[i], csv_name_list[i + 1])
        print('检测到数据文件有{}个'.format(len(csv_name_list)))
        print('请手动输入文件名')
        csv_name = input('输入csv文件名')
        if csv_name[:4] != '.csv':
            csv_name = csv_name + '.csv'

    time_start = time.time()
    # 输出全部最小值
    min_yes = 12 * 12
    min_list = []
    with open(csv_name, 'r') as f:
        read = csv.reader(f)
        for line in read:
            # 取最大值
            if int(line[2]) < min_yes:
                min_yes = int(line[2])
                # 最大值改变就清空列表
                min_list = []
            # 最大值加入列表
            if int(line[2]) == min_yes:
                min_list.append(line)
    time_stop = time.time()
    print('本次查询耗时约{}秒'.format(time_stop - time_start))
    print('最小值为{}，共查询到{}个'.format(min_yes, len(min_list)))
    save_csv('min.csv', min_list)
    print('已经保存到[min.csv]文件')


def Csv_X():
    # 文件名列表
    csv_name_list = glob.glob(r'Slime*.csv')

    # 获取csv文件名
    if len(csv_name_list) == 1:
        csv_name = csv_name_list[0]
    elif len(csv_name_list) == 0:
        print('未识别到数据文件')
        return 'nocsv'
    else:
        for i in range(0, len(csv_name_list), 2):
            if i + 1 >= len(csv_name_list):
                print(csv_name_list[i])
            else:
                print(csv_name_list[i], csv_name_list[i + 1])
        print('检测到数据文件有{}个'.format(len(csv_name_list)))
        print('请手动输入文件名')
        csv_name = input('输入csv文件名')
        if csv_name[:4] != '.csv':
            csv_name = csv_name + '.csv'

    time_start = time.time()
    # 输出全部
    min_yes = int(input('输入指定值'))
    yes_list = []
    with open(csv_name, 'r') as f:
        read = csv.reader(f)
        for line in read:
            # 取指定值
            if int(line[2]) == min_yes:
                yes_list.append(line)

    time_stop = time.time()
    print('本次查询耗时约{}秒'.format(time_stop - time_start))
    print('指定值为{}，共查询到{}个'.format(min_yes, len(yes_list)))
    save_csv('X.csv', yes_list)
    print('已经保存到[X.csv]文件')


def csv_scope():
    # 文件名列表
    csv_name_list = glob.glob(r'Slime*.csv')

    # 获取csv文件名
    if len(csv_name_list) == 1:
        csv_name = csv_name_list[0]
    elif len(csv_name_list) == 0:
        print('未识别到数据文件')
        return 'nocsv'
    else:
        for i in range(0, len(csv_name_list), 2):
            if i + 1 >= len(csv_name_list):
                print(csv_name_list[i])
            else:
                print(csv_name_list[i], csv_name_list[i + 1])
        print('检测到数据文件有{}个'.format(len(csv_name_list)))
        print('请手动输入文件名')
        csv_name = input('输入csv文件名')
        if csv_name[:4] != '.csv':
            csv_name = csv_name + '.csv'

    time_start = time.time()
    # 输出全部最小值
    min_yes = int(input('输入范围最小值'))
    max_yes = int(input('输入范围最大值'))
    yes_list = []
    with open(csv_name, 'r') as f:
        read = csv.reader(f)
        for line in read:
            # 取指定值
            if min_yes <= int(line[2]) <= max_yes:
                yes_list.append(line)

    time_stop = time.time()
    print('本次查询耗时约{}秒'.format(time_stop - time_start))
    print('范围值为{}~{}，共查询到{}个'.format(min_yes, max_yes, len(yes_list)))
    save_csv('scope.csv', yes_list)
    print('已经保存到[scope.csv]文件')


def save_csv(name, list):
    '''
    写csv文件
    :param name: name.csv
    :param list:
    :return:
    '''
    with open(name, 'w') as f:
        for i in list:
            f.write('{},{},{}\n'.format(i[0], i[1], i[2]))


def Run_Java():
    '''
    运行java
    :return:
    '''

    time_start = time.time()
    os.system('java ./src/slimepk.java')
    time_stop = time.time()
    print('################################')
    print('# 以上只是1/500，具体以csv文件为准 #')
    print('# 本次耗时约{}秒                 #'.format(time_stop - time_start))
    print('################################')


def Print_Ini():
    '''
    读ini然后打印
    :return:
    '''
    with open('./src/config.ini', 'r') as f:
        print(f.read())


def Revise_Ini():
    '''
    修改配置文件
    :return:
    '''
    seed = input('种子：')
    x_min = input('X轴最小值：')
    z_min = input('Z轴最小值：')
    x_max = input('X轴最大值')
    z_max = input('Z轴最大值')

    txt = '''[data]
seed = {}
x_min = {}
z_min = {}
x_max = {}
z_max ={}'''.format(seed, x_min, z_min, x_max, z_max)

    with open('./src/config.ini', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    main()
