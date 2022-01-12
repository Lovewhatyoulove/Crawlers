import pandas as pd
import time
import datetime

def firstWrite(tb_len, datDict):
    """
    将数据首次写入csv文件，并且向对照字典tb_len中添加数据
    datDict为URL与文件名对照字典
    """
    for page in datDict.keys():
        url = "http://www.96369.net/indices/" + page
        tb = pd.read_html(url)[0]
        tb_len[datDict[page]] = len(tb)
        tb.to_csv(datDict[page]+".csv", mode = "w", header = 1, index = 0)

def update(tb_len, datDict):
    """
    获取数据更新时间、更新数据写入文件、更新对照字典
    tb_len表示所需的表格行数对照字典
    datDict表示URL与文件名对照字典
    """
    count = 0
    while True:
        for page in datDict.keys():
            url = "http://www.96369.net/indices/" + page
            tb = pd.read_html(url)[0]
            length = len(tb)
            if tb_len[datDict[page]] == length - 1:
                #打印更新时间
                now = datetime.datetime.now()
                print("%s数据已更新，更新时间为：%d时%d分" % (datDict[page], now.hour, now.minute))
                #更新数据写入文件
                tb.to_csv(datDict[page]+".csv", mode = "w", header = 1, index = 0)
                #更新对照字典
                tb_len[datDict[page]] = length - 1
                #计数加一
                count += 1
        if count == 7:
            break
        time.sleep(60) #获取频率为1分钟
    
    
def main():
    """
    首先将程序开始运行时的网页数据写入文件，后续检测更新时间并更新文件，判断数据是否更新
    的依据是表格行数是否加一
    """
    datDict = {"72":"沪螺纹钢社会库存", "67":"国内螺纹钢社会库存量",
               "68":"国内线材社会库存量", "69":"国内主要城市热轧卷板库存",
               "70":"国内主要城市冷轧卷板库存", "73":"国内主要城市中厚板库存",
               "117":"全国主要钢材品种库存总量"}

    tb_len = {} #存放各表格行数，用于后续判断数据是否更新
    
    firstWrite(tb_len, datDict)
    update(tb_len, datDict)  
        
if __name__ == "__main__":
    main()






