import tkinter as t
from tkinter.ttk import Progressbar
import requests
from requests.exceptions import ConnectionError

top=t.Tk()
top.title('Downloader')

bv=t.StringVar()
bv.set('Ready')

def getit():
    url=E.get()
    fname=url.split('/')[-1]
    if fname=='':
        fname=url.split('/')[-2]

    if '.' not in fname:
        fname=fname+'.html'

    try:
        r=requests.get(url,stream=True)
        fsize=int(r.headers['Content-Length'])
        #fsize=len(r.content)
        dl=0
        with open(fname,'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                dl=dl+len(chunk)
                f.write(chunk)
                done=int((100*dl)/fsize)
                bar['value']=done
                bv.set('%d %%' %done)
                top.update_idletasks()

            f.close()
            bv.set('Download Completed !!')

    except ConnectionError:
        print('No Internet Connection !')


L=t.Label(top,text='Link').grid(row=0,column=0)
E=t.Entry(top)
E.grid(row=0,column=1)
E.focus_set()

B=t.Button(top,text='Get',command=getit)
B.grid(row=0,column=2)

bar = Progressbar(top)
bar.grid(row=1,column=0,columnspan=3,sticky='w'+'e')

stat=t.Label(top,textvariable=bv)
stat.grid(row=2,column=0,columnspan=3,sticky='w'+'e')

top.mainloop()
