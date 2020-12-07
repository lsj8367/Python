import MySQLdb
import wx
import wx.xrc
import sys

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,435 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"사번 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNo = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNo, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"직원명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtName = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtName, 0, wx.ALL, 5 )
        
        self.btnLogin = wx.Button( self.m_panel1, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.btnLogin, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.txtNum = wx.StaticText( self.m_panel2, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.txtNum.Wrap( -1 )
        bSizer3.Add( self.txtNum, 0, wx.ALL, 5 )
        
        self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"번 직원의 관리 고객", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer3.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )
        
        self.lstGogek = wx.ListCtrl( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.lstGogek.InsertColumn(0, '고객번호') # 칼럼 추가
        self.lstGogek.InsertColumn(1, '고객명')
        self.lstGogek.InsertColumn(2, '고객전화')
        bSizer4.Add( self.lstGogek, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer6.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.staCount = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staCount.Wrap( -1 )
        bSizer6.Add( self.staCount, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnLogin.Bind( wx.EVT_BUTTON, self.LoginClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def LoginClick( self, event ):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        
        if(no == '' and name == ''):
            wx.MessageBox('비었음', '에러', wx.OK)
            self.txtNo.SetFocus()
            return
        
        self.txtNum.SetLabel(no)
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select gogek_no, gogek_name, gogek_tel from gogek inner join jikwon on gogek_damsano = jikwon_no where jikwon_no = %s and jikwon_name=%s"
            a = cursor.execute(sql, (no, name))
            if a == False:
                wx.MessageBox('사번,이름 불일치!', '에러', wx.OK)
                self.txtNo.SetFocus()
                return

            datas = cursor.fetchall()
            
            
            self.lstGogek.DeleteAllItems() # listctrl 자료 초기화
            for d in datas:
                i = self.lstGogek.InsertItem(50, 0)
                self.lstGogek.SetItem(i, 0, str(d[0]))
                self.lstGogek.SetItem(i, 1, d[1])
                self.lstGogek.SetItem(i, 2, d[2])
                
            self.staCount.SetLabel(str(len(datas)))
            self.txtNo.SetLabel('')
            self.txtName.SetLabel('')
            self.txtNo.SetFocus()
            
        except Exception as e:
            print("err : " + str(e))
        finally:
            conn.close()
        
if __name__ == "__main__":
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
