import pandas as pd
import numpy as np


class Main:
    def __init__(self):
        기상데이터 = pd.read_csv("OBS_ASOS_MNH_20220526044109월별.csv",encoding='cp949')

        한강공원 = pd.read_csv("test.csv",encoding='cp949')
        기간리스트원본 = list(set(한강공원['기간'].to_list()))
        한강공원 = 한강공원[한강공원['구분'] =='합계']
        한강공원 = 한강공원.reset_index()
        한강공원 = 한강공원['합계'].to_frame()

        기상데이터 = 기상데이터[(기상데이터['지점명']=='서울') & (기상데이터['일시']>='2013-01')  & (기상데이터['일시']<='2020-12')]
        날짜리스트 = list(set(기상데이터['일시']))
        기상데이터 = 기상데이터.reset_index()

        기상데이터 = 기상데이터['평균기온(°C)'].to_frame()




        print(한강공원)
        print(기상데이터)
        총 = pd.concat([한강공원,기상데이터],axis=1)
        
        print("총",총)

        기상데이터.corr(method='pearson')
        A = 기상데이터['평균기온(°C)'].corr(한강공원['합계'])

        print(A)




        


if __name__ == "__main__":
    Main()