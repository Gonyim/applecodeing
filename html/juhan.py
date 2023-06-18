from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

service_key = 'Z9ge2iv8H/RXTbAHZXkbWspSk3lpMr0EGYyqX2Ao6OM='
local_codes = ['3010000', '3030000']  # 여러 지역 코드를 리스트로 입력

datas = []

for localCode in local_codes:
    url = f'http://www.localdata.go.kr/platform/rest/GR0/openDataApi?authKey={service_key}&localCode={localCode}'
    result = urlopen(url)
    house = BeautifulSoup(result, 'lxml-xml')
    te = house.find_all('row')

    for i in range(len(te)):
        개방자치단체코드 = te[i].opnSfTeamCode.string.strip()
        관리번호 = te[i].mgtNo.string.strip()
        개방서비스ID = te[i].opnSvcId.string.strip()
        사업장명 = te[i].bplcNm.string.strip()
        도로명주소 = te[i].rdnWhlAddr.string.strip()
        소재지면적 = te[i].siteArea.string.strip()
        인허가일자 = te[i].apvPermYmd.string.strip()
        영업상태명 = te[i].trdStateNm.string.strip()
        
        data = [개방자치단체코드, 관리번호, 개방서비스ID, 사업장명, 도로명주소, 소재지면적, 인허가일자, 영업상태명]
        datas.append(data)

df = pd.DataFrame(datas, columns=['개방자치단체코드', '관리번호', '개방서비스ID', '사업장명', '도로명주소', '소재지면적', '인허가일자', '영업상태명'])

df