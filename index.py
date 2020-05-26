#!/usr/bin/env python3
# index.py
# 2020-05-25 21時22分  Rev:13
# manontanto

import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import re

dbname = 'index.db'
bold = ('', 12, 'bold')
win = tk.Tk()
win.title("索引")
win.geometry("600x400")

def record_word():
    def quit_button():
        win.destroy()
    def search_button():
        label1.pack_forget()
        frame.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame3.pack_forget()
        button4.pack_forget()
        search_word()
    def create_sql():
        conn = sqlite3.connect(dbname)
        c = conn.cursor() 
        rem = entry3.get('1.0', 'end -1c')
        rem = re.sub('\n', '/', rem)
        try:
            c.execute('''
                    INSERT INTO list VALUES(null,'{}',{},'{}');
                    '''.format(entry1.get(), entry2.get(), rem))
            conn.commit()
            print('1件登録済み')
            clear_entrys()
        except sqlite3.Error as e:
#            print('エラーにより登録できませんでした')
            print('sqlite3.Error occurred:', e.args[0])
    def clear_entrys():
        entry1.delete(0,'end')
        entry2.delete(0,'end')
        entry3.delete('1.0', 'end')
        entry1.focus_set()

    #メニューFrame # 縁は2pt,形状はridge
    frame = tk.LabelFrame(win, bd=2, relief='ridge', text='menu')
    frame.pack(fill='x', padx=10, pady=10) # 横方向に余白を拡張
    button1 = tk.Button(frame, text='検索', command=search_button)
    button1.pack(side='left', padx=3)
    button2 = tk.Button(frame, font=bold, text='入力')
    button2.pack(side='left')
    button3 = tk.Button(frame, text='終了', command=quit_button)
    button3.pack(side='right', padx=3)

    #登録語入力Frame
    label1 = tk.Label(win, font=('', 18), text="入力画面")
    label1.pack(fill="x", pady=20)

    frame1 = tk.Frame(win)
    frame1.pack(anchor=tk.W, padx=60, pady=5)
    label2 = tk.Label(frame1,font=("",14),text="登録語:")
    label2.pack(side='left')
    entry1 = tk.Entry(frame1, width=40, bg='#f0f0f0')
    entry1.pack(side='left')

    frame2 = tk.Frame(win)
    frame2.pack(anchor=tk.W, padx=60, pady=5)
    label3 = tk.Label(frame2,text="ページ:")
    label3.pack(side='left')
    entry2 = tk.Entry(frame2,width=8, bg='#f0f0f0')
    entry2.pack(side='left')

    frame3 = tk.Frame(win)
    frame3.pack(anchor=tk.W, padx=60)
    label4 = tk.Label(frame3,text="備　考:")
    label4.pack(side='left')
    entry3 = tk.Text(frame3, width=40, height=5, bg='#f0f0f0')
    entry3.pack(side='left')

    button4 = tk.Button(win, text="登録", width=10, bg="gray",command=create_sql)
    button4.pack(anchor=tk.S, pady=40)

    win.mainloop()

def search_word():
    def quit_button():
        win.destroy()
    def record_button():
        frame.pack_forget()
        frameWord.pack_forget()
        frameResult.pack_forget()
        record_word()
    def select_sql(w):    
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        sql = 'SELECT * FROM list WHERE word LIKE ?'

        tree.delete(*tree.get_children())
        for r in c.execute(sql, (w,)):
            tree.insert("","end",values=r)
        tree.pack()
        textWord.delete(0, 'end')
        textWord.focus_set()

    #メニューFrame # 縁は2pt,形状はridge
    frame = tk.LabelFrame(win, bd=2, relief='ridge', text='menu')
    frame.pack(fill='x', padx=10, pady=10) # 横方向に余白を拡張
    button1 = tk.Button(frame, text='検索', font=bold)
#    button1 = Button(frame, text='検索', bg='gray')
    button1.pack(side='left', padx=3)
    button2 = tk.Button(frame, text='入力', command=record_button)
    button2.pack(side='left')
    button3 = tk.Button(frame, text='終了', command=quit_button)
    button3.pack(side='right', padx=3)

    #検索語入力Frame
    frameWord = tk.Frame(win)
    frameWord.pack(anchor=tk.W, pady=10) #左寄せで配置したい
    labelWord = tk.Label(frameWord, text='検索語:')
    labelWord.pack(side='left', padx=10)
    textWord = tk.Entry(frameWord, width=30)
    textWord.pack(side='left', padx=5)

    #検索開始ボタン
    #w = re.sub(r"[\0-\037]", '', textWord.get())
    #入力中の半角コンマを全角にし，先頭の不要文字を削除する。
    #入力窓の先頭でカタカナ入力にするためにコマンドキーを押すと、
    #それが不可視文字として文字列中に含まれてしまうための処置.
    calcButton = tk.Button(frameWord, text='Go', bg='gray')
    calcButton['command'] = lambda:select_sql(re.sub(r"[\0-\037]",'',textWord.get()))
    calcButton.pack(side='left')

    #結果表示ツリー
    frameResult = tk.Frame(win)
    frameResult.pack(padx=10, pady=10)
    tree = ttk.Treeview(frameResult)
    tree["columns"] = (1,2,3,4)
    tree["show"] = "headings"
    tree.column(1,width=30)
    tree.column(2,width=300)
    tree.column(3,width=75)
    tree.column(4,width=200)
    tree.heading(1,text="id")
    tree.heading(2,text="人名")
    tree.heading(3,text="ページ")
    tree.heading(4,text="備考")
    tree.pack()

    win.mainloop()


search_word()
