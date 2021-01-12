import requests
from requests.exceptions import ConnectionError
from time import sleep

url=input('Enter site: ')
print()

fname=url.split('/')[-1]
if fname=='':
    fname=url.split('/')[-2]

if '.' not in fname:
    fname=fname+'.html'

try:
    r=requests.get(url,stream=True)
    fsize=len(r.content)
    dl=0
    with open(fname,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            dl=dl+len(chunk)
            f.write(chunk)
            done=(100*dl)/fsize
            print('%d %% done' %done)

        f.close()
        print('\n\nDownload Completed !!')

except ConnectionError:
    print('No Internet Connection !')

sleep(1)
