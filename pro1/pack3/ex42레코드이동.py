import wx
import wx.xrc
import ast
import MySQLdb

with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())
# print(config)

datas = []
rec_r = 0

class MyFrame (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"레코드이동", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        
        self.txtCode = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtCode, 0, wx.ALL, 5)
        
        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"상품명 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)
        
        self.txtSang = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtSang, 0, wx.ALL, 5)
        
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.btn1 = wx.Button(self.m_panel2, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btn1, 0, wx.ALL, 5)
        
        self.btn2 = wx.Button(self.m_panel2, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btn2, 0, wx.ALL, 5)
        
        self.btn3 = wx.Button(self.m_panel2, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btn3, 0, wx.ALL, 5)
        
        self.btn4 = wx.Button(self.m_panel2, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.btn4, 0, wx.ALL, 5)
        
        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # self.txtCode.SetEditable(False) # read-only인데 커서는 위치시킬수 있고 복사는 가능할듯?
        # self.txtSang.SetEditable(False)
        self.txtCode.Enable(enable=False)  # 보기만 가능 커서 안됨
        self.txtSang.Enable(enable=False)
        
        # 버튼의 이벤트 핸들러 장착
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
        
        self.btn1.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn2.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn3.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        self.btn4.Bind(wx.EVT_BUTTON, self.ButtonProcess)
        
        self.DataLoad()
        
    def __del__(self):
        pass
    
    def DataLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from sangdata"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall() # datas의 수준이 전역변수로 바뀜 
            #print(datas)
            #print(datas[0]) # (1, '장갑', 3, 10000)
            #print(datas[0][0], datas[0][1]) # 1 장갑
            
            self.ShowData()
            
            
        except Exception as e:
            print("DataLoad err : " + str(e))
        finally:
            cursor.close()
            conn.close()
    def ShowData(self):
        self.txtCode.SetLabel(str(datas[rec_r][0]))
        self.txtSang.SetLabel(datas[rec_r][1])
                
    def ButtonProcess(self, event):
        id = event.GetEventObject().id
        global rec_r
        if id == 1: # 처음으로
            rec_r = 0
        elif id == 2: # 이전으로
            rec_r -= 1
            if rec_r < 0: rec_r = 0
        elif id == 3: # 다음으로
            rec_r += 1
            if rec_r > (len(datas) - 1): rec_r = (len(datas) - 1) 
        elif id == 4: # 맨끝으로
            rec_r = (len(datas) - 1)
            
        self.ShowData()
        
if __name__ == "__main__":
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()
