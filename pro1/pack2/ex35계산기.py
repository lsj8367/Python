import wx
import wx.xrc

class MyCalc ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"미니 계산기", pos = wx.DefaultPosition, size = wx.Size( 315,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"숫자1 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        self.txtNum1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.txtNum1, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"숫자 2 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtNum2 = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.txtNum2, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer4 )
        self.m_panel2.Layout()
        bSizer4.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        rdoOpChoices = [ u"+", u"-", u"*", u"/" ]
        self.rdoOp = wx.RadioBox( self.m_panel3, wx.ID_ANY, u"연산자 선택", wx.DefaultPosition, wx.DefaultSize, rdoOpChoices, 1, wx.RA_SPECIFY_ROWS )
        self.rdoOp.SetSelection( 0 )
        bSizer5.Add( self.rdoOp, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel3.SetSizer( bSizer5 )
        self.m_panel3.Layout()
        bSizer5.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"연산결과 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer6.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.staResult = wx.StaticText( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staResult.Wrap( -1 )
        bSizer6.Add( self.staResult, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer6 )
        self.m_panel4.Layout()
        bSizer6.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btnCalc = wx.Button( self.m_panel5, wx.ID_ANY, u"계산", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.btnCalc, 0, wx.ALL, 5 )
        
        self.btnClear = wx.Button( self.m_panel5, wx.ID_ANY, u"초기화", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.btnClear, 0, wx.ALL, 5 )
        
        self.btnExit = wx.Button( self.m_panel5, wx.ID_ANY, u"종료", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.btnExit, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer1.Add( self.m_panel5, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btnCalc.id = 1
        self.btnClear.id = 2
        self.btnExit.id = 3
        
        self.btnCalc.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnClear.Bind( wx.EVT_BUTTON, self.OnProcess )
        self.btnExit.Bind( wx.EVT_BUTTON, self.OnProcess )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def OnProcess( self, event ):
        sel_id = event.GetEventObject().id
        #print(sel_id)
        if sel_id == 1: # 계산
            op = self.rdoOp.GetStringSelection()
            # print(op) # + - * /
            num1 = self.txtNum1.GetValue()
            num2 = self.txtNum2.GetValue()
            
            if num1 == '' or num2 == '':
                wx.MessageBox('값을 입력하세요', '오류', wx.OK)
                return
            
            try:
                mes = eval(num1 + op + num2) # mes = eval('5' + '-' + '2') 수식의 모양 만들어야함
                
            except Exception as e:
                wx.MessageBox('연산 오류 : '+ str(e), '에러', wx.OK)
                return
            
            self.staResult.SetLabel(str(mes))
            
        elif sel_id == 2: # 초기화
            self.txtNum1.SetLabel('')
            self.txtNum2.SetLabel('')
            self.staResult.SetLabel('')
            self.rdoOp.SetSelection(0)
            self.txtNum1.SetFocus()
        else: # 종료
            dlg = wx.MessageDialog(self, '정말 종료할까요?', '알림', wx.YES_NO)
            imsi = dlg.ShowModal()
            if imsi == wx.ID_YES: # yes버튼 눌렀을때
                dlg.Destroy() # MessageDialog 닫기
                self.Close() # 프로그램 종료
                
if __name__ == "__main__":
    app = wx.App()
    MyCalc(None).Show()
    app.MainLoop()    
   

