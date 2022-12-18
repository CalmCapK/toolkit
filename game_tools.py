
import csv

def cal_shengyiwu(file_path):
    '''
    功能：计算原神圣遗物
    输入：
        file_path: 原神的圣遗物清单  格式：套装名字和ID\t爆伤\t暴击\t攻击\t圣遗物五种类型之一
    输出：
        [
            cnt, 
            d1[0], d2[0], d3[0], d4[0], d5[0], 
            juedoushi, leyuan, zhankuang, zongshi, 
            baoji, baoshang, gongji, 
            baoji+5, baoji+19.4, (baoji+5)*2, (baoji+19.4)*2, baoshang+50, baoshang+78.8, baoshang+50-(baoji+5)*2, baoshang+50-(baoji+19.4)*2, baoshang+78.8-(baoji+5)*2
        ]
    '''
    file = open(file_path, 'r', encoding='utf-8')
    data_1 = []
    data_2 = []
    data_3 = []
    data_4 = []
    data_5 = []
    for line in file.read().splitlines():
        data = line.split('\t')
        print(data)
        if data[-1] == '1':
            data_1.append(data)
        elif data[-1] == '2':
            data_2.append(data)
        elif data[-1] == '3': 
            data_3.append(data)
        elif data[-1] == '4':    
            data_4.append(data)
        elif data[-1] == '5':
            data_5.append(data)
    print(len(data_1), len(data_2), len(data_3), len(data_4), len(data_5))

    cnt = 0
    with open('res2.csv', 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['序号', 1, 2, 3, 4, 5, '角斗士', '乐园', '战狂', '宗室', '暴击', '爆伤', '攻击', '暴击实际', '暴击魈', '暴击两倍', '暴击魈两倍', '爆伤实际', '爆伤甘雨', '差距', '差距魈', '差距甘雨'])
        for d1 in data_1:
            for d2 in data_2:
                for d3 in data_3:
                    for d4 in data_4:
                        for d5 in data_5:
                            baoshang = float(d1[1]) + float(d2[1]) + float(d3[1]) + float(d4[1]) + float(d5[1]) 
                            baoji = float(d1[2]) + float(d2[2]) + float(d3[2]) + float(d4[2]) + float(d5[2]) 
                            gongji = float(d1[3]) + float(d2[3]) + float(d3[3]) + float(d4[3]) + float(d5[3])
                            zuhe = d1[0] + '_' + d2[0] + '_' + d3[0] + '_' + d4[0] + '_' + d5[0]
                            juedoushi = zuhe.count('角斗士')
                            leyuan = zuhe.count('乐园')
                            zhankuang = zuhe.count('战狂') 
                            zongshi = zuhe.count('宗室') 
                            if baoshang > 10.0 and baoji > 10.0:
                                #print('{}, jue:{}, le:{}, zhan:{}, {:.1f}, {:.1f}, {:.1f}'.format(zuhe, juedoushi, leyuan, zhankuang, baoji, baoshang, gongji))
                                cnt += 1               
                                spamwriter.writerow([cnt, d1[0], d2[0], d3[0], d4[0], d5[0], juedoushi, leyuan, zhankuang, zongshi, baoji, baoshang, gongji, baoji+5, baoji+19.4, (baoji+5)*2, (baoji+19.4)*2, baoshang+50, baoshang+78.8, baoshang+50-(baoji+5)*2, baoshang+50-(baoji+19.4)*2, baoshang+78.8-(baoji+5)*2])


if __name__=="__main__":    
    path = './yuanshen.txt'
    cal_shengyiwu(path)