import urllib.request

url = 'https://www.daelim.ac.kr/ajaxfile/CmnFileCpnt/fileView.do?gbn=x01&SITE_GROUP_NO=2&SITE_NO=2'
urllib.request.urlretrieve(url, filename='daelim.png')
print('저장완료')