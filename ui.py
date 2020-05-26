import tkinter as tk
from tkinter import ttk
import threading
import requests
import json
import os
from tkinter import filedialog
from tkinter import messagebox as msg
import base64

tamp=False
def download_bcmc(url):
        global name
        name = url.split('/')[-1]
    #    root_insert(name)
        net_file = requests.get(url).content.decode()
        return net_file
        
def download_image(url,path,name):
    image_name = name+'.jpg'
    with open(path +'\\图片\\'+image_name,'wb') as f:
        r = requests.get(url).content
        f.write(r)
        
def download_audio(url,path,name):
    audio_name = name +'.mp3'
    with open(path +'\\音乐\\'+audio_name,'wb') as f:
        r = requests.get(url).content
        f.write(r)


        
def main(wid,_path):
    try:
            global tamp
            tamp=True
            #本应用作者by啊不嘟，转载请申明原作
            #本作品github开源地址：https://github.com/am-abudu/codemaospider
            #此应用仅供交流和学习使用，通过此应用获取的资源请在二十四小时内删除

            root_insert('本应用作者by啊不嘟，星辰工作室版权所有')
            编辑框4.see(tk.END)
            root_insert('本项目github开源地址：https://github.com/am-abudu/codemaospider')
            编辑框4.see(tk.END)
            root_insert('此应用仅供交流和学习使用，通过此应用获取的资源请在二十四小时内删除')
            编辑框4.see(tk.END)
            root_insert('\n')
            编辑框4.see(tk.END)
            root_insert('###开始运行###')
            编辑框4.see(tk.END)
            path = _path.replace('\\','/')+'/'+wid
            error_code = '0'
            w_id = wid
            error_code = '1'
            ###获取带有素材ID的BCMC文件###
            api = 'https://api.codemao.cn/tiger/work/source/public/'+w_id
            _json = requests.get(api).json()
            base_url = _json['source_urls'][0]
            #root_insert(base_url)
            error_code = '2'
            root_insert('BCMC文件获取成功！')
            编辑框4.see(tk.END)
            

            ###从带有素材ID的BCMC文件中获取图片素材ID###
            bcmc = download_bcmc(base_url)
            bcmcjson=json.loads(bcmc)
            try:
                styles = bcmcjson['theatre']["styles"]
            except:
                styles = bcmcjson['resources']
            #root_insert(styles)
            error_code = '3'
            root_insert('图片素材ID获取成功！')
            编辑框4.see(tk.END)
              ###从带有素材ID的BCMC文件中获取音乐素材ID###
            try:
                audio = bcmcjson['audio']
            except:
                pass
            error_code = '4'
            root_insert('音乐素材ID获取成功')
            编辑框4.see(tk.END)

            ###下载图片素材###
            root_insert('开始下载图片！')
            编辑框4.see(tk.END)
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
            if os.path.exists(path +'\\图片\\'):
                pass
            else:
                os.mkdir(path +'\\图片\\')
            count_max = len(styles)
            count = 1

            try:
                for i in styles:
                    #    root_insert(styles[i]['url'])
                    styles[i]['url']
                    root_insert('图片下载中({}/{})......'.format(str(count),str(count_max)))
                    编辑框4.see(tk.END)
                    download_image(styles[i]['url'],path,styles[i]['name'])
                    count+=1
            except:
                custom_sprites = styles['custom_sprites']
                count_max = 0
                for i in custom_sprites:
                    count_max+=len(custom_sprites[i])
                for i in custom_sprites:
                    for i1 in custom_sprites[i]:
                        root_insert('图片下载中({}/{})......'.format(str(count),str(count_max)))
                        编辑框4.see(tk.END)
                        download_image(custom_sprites[i][i1]['img'],path,i1)
                        count+=1
                root_insert('开始下载背景！') #旧平台背景和角色图片是分开放的，这里要注意
                编辑框4.see(tk.END)
                count_max = 0
                count = 1
                custom_scenes = styles['custom_scenes']
                for i in custom_scenes:
                    count_max+=len(custom_scenes[i])
                for i in custom_scenes:
                    for i1 in custom_scenes[i]:
                        root_insert('背景下载中({}/{})......'.format(str(count),str(count_max)))
                        编辑框4.see(tk.END)
                        download_image(custom_scenes[i][i1]['img'],path,i1)
                        count+=1
            error_code = '5'
            ###下载音乐素材###
            root_insert('开始下载音乐！')
            编辑框4.see(tk.END)
            if os.path.exists(path +'\\音乐\\'):
                pass
            else:
                os.mkdir(path +'\\音乐\\')
            try:
                count_max = len(audio)
                count = 1
                for i in audio:
                    root_insert('音乐下载中({}/{})......'.format(str(count),str(count_max)))
                    编辑框4.see(tk.END)
                #    root_insert(audio[i]['url'])
                    download_audio(audio[i]['url'],path,audio[i]['name'])
                    count+=1
            except:
                audio = styles['custom_audio']
                count = 1
                count_max = 0
                for i in audio:
                    count_max+=len(audio[i])
                for i in audio:
                    for i1 in audio[i]:
                        root_insert('音乐下载中({}/{})......'.format(str(count),str(count_max)))
                        编辑框4.see(tk.END)
                        download_audio(i1[1],path,i1[0])
            root_insert('下载完毕！已保存至{}，欢迎下次使用！'.format(path))
            编辑框4.see(tk.END)
            tamp=False
    ###错误码解析###
    except:
        root_insert('错误！Error code:{}'.format(error_code))
        if error_code == '0':
            root_insert('请输入正确的ID！')
        elif error_code == '1':
            root_insert('BCMC文件获取失败,请输入正确的ID，或检查网络设置！')
        elif error_code == '2':
            root_insert('图片ID获取失败！')
            root_insert(bcmc)
        elif error_code == '3':
            root_insert('音乐ID获取失败！')
        elif error_code == '4':
            root_insert('图片下载失败，请检查保存路径、网络设置，或尝试管理员模式运行！')
        elif error_code == '5':
            root_insert('音乐下载失败，请检查网络设置，或尝试管理员模式运行！')
            编辑框4.see(tk.END)
        tamp=False


def run(_id,_path):
        if tamp==False:
                main_thread = threading.Thread(target=lambda: main(_id,_path))
                main_thread.start()
        else:
                msg.showerror('提示','请等待当前任务完成')
        

def root_insert(words):
        编辑框4.insert('end',words+'\n')

def get_path():
        编辑框2.delete('0.0','end')
        编辑框2.insert('end',filedialog.askdirectory())

def ui(启动窗口):
        icon_b64='''AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABJ6LgMgg1gdOZGDNFWip0xtsMNlhL3RdJPG13yby9l9m8vZdpXH12eGv9NNbrHBNVWhmxMwjGgAFHssAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFHw+KEiZlV55ts+JptL9tNDq/87q+P/f9///6P////H////x////7////+/////v////6////+b+///h+v//xeHx/4qm0fs6VKGxABB6RAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJdQIBHoJgQF+nv5iy1v/N5/f/5v///+v////k/f//3vf//9/5///P7Pv/t9Tu/63L5/+uy+j/sM7p/7jW7v/F4/f/1/P//9z2///g+f//7v///9z4//+WrtP/HjeQmwAHcxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFn1WUmqs0bbR6P/p////6f///9jy/v/R6/v/z+n5/9Ls+//S7vz/psHi/56z1/+0wN3/xM3j/8jR5v/EzuT/vsri/67B3v+ku9z/u9bu/9Xv/f/N5/n/1vD9/+7////Z8vr/Wna04wAJdToAAAAAAAAAAAAAAAAACXUIFy+Ml6C52f/o////6P///9Ps+//M5vj/z+n5/8/p+f/P6fn/1fH9/6a/4P+3vtr/8PD2////////////////////////////+Pf6/9/f7P+dsdX/y+f5/9Tt/P/O6Pn/y+b5/+H6///v////Y3+86wALdi4AAAAAABF5CjtVor/P6vb/7v///9Ls/P/N5/j/z+n5/8/p+f/P6fn/z+n5/9Ls+/+92vH/sL/c/////////////////////////////////////////////////8nQ5f+tyuj/2vT//8/p+f/P6fn/zOf4/9rz/v/q////UHGy1wANeAwAAAAARmes1en////U7/3/0uz6/9Ls+v/Q6/n/z+n5/87o+f/P6fn/0+38/7TR7P+/y+P/////////////////////////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'''
        启动窗口 = 启动窗口
        启动窗口.title('编程猫作品素材一键获取')
        启动窗口.resizable(width=False, height=False)
        screenwidth = 启动窗口.winfo_screenwidth()
        screenheight = 启动窗口.winfo_screenheight()
        size = '%dx%d+%d+%d' % (333, 292, (screenwidth - 333) / 2, (screenheight - 292) / 2)
        启动窗口.geometry(size)
        with open('./favicon.ico','wb') as f:
                f.write(base64.b64decode(icon_b64))
        启动窗口.iconbitmap('favicon.ico')
        os.remove('favicon.ico')
        标签2_标题 = tk.StringVar()
        标签2_标题.set('作品ID')
        标签2 = tk.Label(启动窗口,textvariable=标签2_标题,anchor=tk.W)
        标签2.place(x=39,y=28,width=54,height=23)
        
        标签3_标题 = tk.StringVar()
        标签3_标题.set('保存路径')
        标签3 = tk.Label(启动窗口,textvariable=标签3_标题,anchor=tk.W)
        标签3.place(x=39,y=57,width=54,height=23)
        
        编辑框1 = tk.Text(启动窗口,wrap=tk.NONE)
        编辑框1.insert(tk.END,'')
        编辑框1.place(x=98,y=27,width=200,height=23)
        global 编辑框2
        编辑框2 = tk.Text(启动窗口,wrap=tk.NONE)
        编辑框2.insert(tk.END,'')
        编辑框2.place(x=98,y=59,width=150,height=23)
        
        按钮2_标题 = tk.StringVar()
        按钮2_标题.set('浏览')
        按钮2 = tk.Button(启动窗口,textvariable=按钮2_标题,command=get_path)
        按钮2.place(x=254,y=57,width=44,height=26)
        
        按钮3_标题 = tk.StringVar()
        按钮3_标题.set('开始')
        按钮3 = tk.Button(启动窗口,textvariable=按钮3_标题,command=lambda: run(编辑框1.get('0.0',tk.END)[:-1],编辑框2.get('0.0','end')[:-1]))
        按钮3.place(x=39,y=85,width=51,height=26)
        
        按钮4_标题 = tk.StringVar()
        按钮4_标题.set('关于')
        按钮4 = tk.Button(启动窗口,textvariable=按钮4_标题,command=lambda: msg.showinfo('提示','本应用作者啊不都\n星辰工作室版权所有'))
        按钮4.place(x=39,y=227,width=51,height=26)
        global 编辑框4
        编辑框4 = tk.Text(启动窗口,wrap=tk.NONE)
        编辑框4.insert(tk.END,'')
        编辑框4.place(x=98,y=89,width=200,height=164)
root = tk.Tk()            
ui_thread = threading.Thread(target=lambda: ui(root))
ui_thread.start()
root.mainloop()

