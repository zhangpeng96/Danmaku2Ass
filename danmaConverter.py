import time, datetime
import html, os

xml_header_str = '''<?xml version="1.0" encoding="utf-8"?>
<i>
  <chatserver>chat.bilibili.com</chatserver>  
  <chatid>77764929</chatid>
  <mission>0</mission>
  <maxlimit>8000</maxlimit>
  <state>0</state>
  <real_name>0</real_name>
  <source>e-r</source>
'''
xml_footer_str = '''</i>
'''

def calcSecondGap(time_str):
    # begin_time_str = '0:05:00'
    begin_time_str =  time_str
    delta_now_time = datetime.datetime.strptime(begin_time_str,'%H:%M:%S')
    delta_zero_time = datetime.datetime(delta_now_time.year, delta_now_time.month, delta_now_time.day, 0, 0, 0)
    gap = (delta_now_time - delta_zero_time).seconds
    return gap

def converter(origin_path, des_path, gap):
    data = []
    record = open(origin_path, encoding = 'utf-8')
    # 数据处理
    for r in record.readlines():
        ts = r.split('\t')[0]
        text = html.escape(r.split('\t')[1].strip('\n').strip('\r'))
        ts = format(calcSecondGap(ts) - gap, '.5f')
        data.append('  <d p="%s,1,25,16777215,1551154567,0,adcd879c,12589409055014916">%s</d>\n' % (ts, text))
    # 文件写入
    with open(des_path, 'a', encoding = 'utf-8') as f:
        f.write(xml_header_str)
        for d in data:
            f.write(d)
        f.write(xml_footer_str)
    print('成功输出弹幕文件 %s' % des)
    return True

if __name__ == '__main__':
    # gap = calcSecondGap('19:28:17')
    # orig = '2019-06-30.txt'
    # des = 'nnnn.xml'
    print('弹幕文件临时转换器')
    orig = input('待处理弹幕文件名:')
    des = input('输出弹幕文件名:')
    gap = calcSecondGap(input('弹幕开始时间:'))
    converter(orig, des, gap)
    command_str = 'dass\\dass.exe -bottom 12 -S %s' % des
    os.system(command_str)
    print('弹幕已转换为ass文件')
