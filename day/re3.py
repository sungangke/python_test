#计算器作业
#说明：开始不会，去网上看的思路，听老师讲的后，又改进的。原来40多行，现在除去注释也就20多行。
import re
def multiply_divide(s):
    '''乘除'''
    ret = float(s.split('*')[0]) * float(s.split('*')[1]) if '*' in s else float(s.split('/')[0]) / float(s.split('/')[1])
    print(ret)
    return ret

def remove_md(s):
    '''迭代去括号并调用乘除'''
    if '*' not in s and '/' not in s:return s
    else:
        k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
        s = s.replace(k, '+' + str(multiply_divide(k))) if len(re.findall(r'-', k)) == 2 else s.replace(k, str(multiply_divide(k)))
        return remove_md(s)
def add_sub(s):
    '''
    修正符号
    加减
    '''
    s = s.replace('--','+').replace('-+','-').replace('-+','-').replace('+-','-').replace('++','+')
    l = re.findall(r'[+\-]?\d+\.?\d*', s)   #['-60', '+30', '+40']
    total = sum([i for i in map(lambda n:float(n),l)])
    return total
def basic_operation(s):
    '''去空格'''
    s = s.replace(' ', '')
    return add_sub(remove_md(s))

def calculate(expression):
    '''计算'''
    if not re.search(r'\([^()]+\)', expression):
        return basic_operation(expression)
    k = re.search(r'\([^()]+\)', expression).group()
    expression = expression.replace(k, str(basic_operation(k[1:len(k) - 1])))
    return calculate(expression)

s = '1 - 2 * ( (-60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# expression = '1 - 2 * ( (-60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
#s="-60--30--40"
print('用eval计算出来的值为：{}\n计算器计算出来的值为：{}'.format(eval(s), calculate(s)))



# def add_sub(s):
#     s = s.replace('--','+').replace('-+','-').replace('-+','-').replace('+-','-').replace('++','+')
#     l = re.findall(r'[+\-]?\d+\.?\d*', s)   #['-60', '+30', '+40']
# #法一
#     total = sum([i for i in map(lambda n:float(n),l)])
#     return total
# #法二
#     # if l:
#     #     total = 0
#     #     for item in l:
#     #         total += float(item)
#     #     return total