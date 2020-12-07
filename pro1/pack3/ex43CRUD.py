# CRUD 연습

import wx
import wx.xrc
import ast
import MySQLdb

with open('mariadb.txt', mode='r') as f:
    config = ast.literal_eval(f.read())

class MyFrame (wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"CRUD Test", pos=wx.DefaultPosition, size=wx.Size(310, 416), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)
        
        self.txtNo = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.txtNo, 0, wx.ALL, 5)
        
        self.btnInsert = wx.Button(self.m_panel1, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.Size(110, -1), 0)
        bSizer2.Add(self.btnInsert, 0, wx.ALL, 5)
        
        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)
        
        self.txtName = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.txtName, 0, wx.ALL, 5)
        
        self.btnUpdate = wx.Button(self.m_panel2, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer3.Add(self.btnUpdate, 0, wx.ALL, 5)
        
        self.btnConfirm = wx.Button(self.m_panel2, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer3.Add(self.btnConfirm, 0, wx.ALL, 5)
        
        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText3 = wx.StaticText(self.m_panel3, wx.ID_ANY, u"전화 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)
        
        self.txtTel = wx.TextCtrl(self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.txtTel, 0, wx.ALL, 5)
        
        self.btnDel = wx.Button(self.m_panel3, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.Size(110, -1), 0)
        bSizer4.Add(self.btnDel, 0, wx.ALL, 5)
        
        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 0, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)
        
        self.lstMember = wx.ListCtrl(self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer5.Add(self.lstMember, 1, wx.ALL | wx.EXPAND, 5)
        
        self.m_panel4.SetSizer(bSizer5)
        self.m_panel4.Layout()
        bSizer5.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)
        
        self.m_panel5 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.m_staticText4 = wx.StaticText(self.m_panel5, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer6.Add(self.m_staticText4, 0, wx.ALL, 5)
        
        self.staCount = wx.StaticText(self.m_panel5, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCount.Wrap(-1)
        bSizer6.Add(self.staCount, 0, wx.ALL, 5)
        
        self.m_panel5.SetSizer(bSizer6)
        self.m_panel5.Layout()
        bSizer6.Fit(self.m_panel5)
        bSizer1.Add(self.m_panel5, 0, wx.EXPAND | wx.ALL, 5)
        
        self.SetSizer(bSizer1)
        self.Layout()
        
        self.Centre(wx.BOTH)
        
        # 리스트 컴포넌트에 제목 표시
        self.lstMember.InsertColumn(0, '번호', width = 50)
        self.lstMember.InsertColumn(1, '이름', width = 100)
        self.lstMember.InsertColumn(2, '전화', width = 100)        
        
        # Connect Events
        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4
        
        
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnUpdate.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        
        self.btnConfirm.Enable(enable=False)  # 수정 확인 버튼 비활성화
        
        self.ViewListData() # 화면 로딩후 pymem 자료를 읽어 출력
        
        
        
    def __del__(self):
        pass
    
    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select * from pymem"
            cursor.execute(sql)
            
            self.lstMember.DeleteAllItems() # 초기화
            count = 0
            for data in cursor:
                i = self.lstMember.InsertItem(65535, 0)
                self.lstMember.SetItem(i, 0, str(data[0]))
                self.lstMember.SetItem(i, 1, data[1])
                self.lstMember.SetItem(i, 2, data[2])
                count += 1            
            
            self.staCount.SetLabel(str(count) + '명')
            
        except Exception as e:
            wx.MessageBox('읽기 오류: ' + str(e))
        finally:
            cursor.close()
            conn.close()
        
    # Virtual event handlers, overide them in your derived class
    def OnBtnClick(self, event):
        id = event.GetEventObject().id
        
        if id == 1: 
            self.MemInsertFunc()   
        elif id == 2: # 수정
            self.MemUpdateFunc()         
        elif id == 3: # 수정확인
            self.MemUpdateFuncOk()         
        elif id == 4: # 삭제
            self.MemDeleteFunc()           
        elif id == 5: # 수정 취소
            self.MemUpdateFuncCancel()
            
    def MemInsertFunc(self): # 등록
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if no == '' or name == '' or tel == '':
            wx.MessageBox('입력 자료를 채우세요', '알림', wx.OK)
            return
        # ... 검사
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            data = self.SelectData(no) # 해당 번호의 자료가 등록 되어있는지 확인함
            if data != None:
                wx.MessageBox('이미 사용중인 번호입니다', '알림', wx.OK)
                self.txtNo.SetFocus()
                return
            
            # 등록 계속
            
            sql = "insert into pymem values(%s, %s, %s)"
            cursor.execute(sql, (no, name, tel))
            conn.commit()
            
            self.ViewListData() # 등록 후 자료 보기
            
            self.txtNo.SetValue('') # 입력자료 초기화
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            
        except Exception as e:
            wx.MessageBox('추가 오류 ', '알림', wx.OK)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    
    def MemUpdateFunc(self): # 수정
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력!', '수정')
        #dlg.ShowModal()
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            upno = dlg.GetValue()
            #print('upno: ', upno)
            
            
            
            # 수정 자료 읽기
            data = self.SelectData(upno)
            if data == None:
                wx.MessageBox(upno + " 번은 등록된 자료가 아닙니다", '알림', wx.OK)
                return
            
            # 수정 계속 - 화면에 표시
            self.txtNo.SetValue(str(data[0]))
            self.txtName.SetValue(data[1])
            self.txtTel.SetValue(data[2])
            
            self.txtNo.SetEditable(False) # 번호는 pk이므로 수정에서 제외하고자 함
            self.btnConfirm.Enable(True) # 수정확인 활성화
            self.btnUpdate.SetLabel('취소')
            self.btnUpdate.id = 5
            
        else:
            return
        
        dlg.Destroy() # TextEntryDialog를 메모리 해제
        
    def MemUpdateFuncOk(self): # 수정 확인
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()
        
        if name == '' or tel == '':
            wx.MessageBox('수정 자료를 입력하세요', '알림', wx.OK)
            return
        
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "update pymem set irum=%s, junhwa=%s where bun=%s"
            cursor.execute(sql, (name, tel, no))
            conn.commit()
            
            self.ViewListData() # 수정 후 자료보기
            
            self.txtNo.SetValue('') # 입력자료 초기화
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            
            self.txtNo.SetEditable(True) # 다시 텍스트칸 입력가능하게
            self.btnUpdate.SetLabel('수정') # 버튼 이름 수정으로 다시 바꾸고
            self.btnUpdate.id = 2 # id값 2
            self.btnConfirm.Enable(False) # 다시 확인버튼 못누르게
            
            
            
        except Exception as e:
            wx.MessageBox('수정 오류 : ' + str(e), wx.OK)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def MemDeleteFunc(self): # 삭제
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력하세요!', '알림')
        
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue() == '':
                return
            delno = dlg.GetValue()
            
            data = self.SelectData(delno)
            
            if data == None:
                wx.MessageBox(delno + ' 번은 등록된 번호가 아닙니다.', '알림', wx.OK)
                return
            
            # 삭제 계속
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                
                sql = "delete from pymem where bun={0}".format(delno)
                cursor.execute(sql)
                conn.commit()
                
                self.ViewListData() #삭제 완료 후 목록 보기
                
            except Exception as e:
                wx.MessageBox('수정 오류 : ' + str(e), wx.OK)
                conn.rollback()
                
            finally:
                cursor.close()
                conn.close()

        else:
            return
        
        dlg.Destroy()
    
    def MemUpdateFuncCancel(self): # 수정 취소
        self.txtNo.SetValue('') # 입력자료 초기화
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        
        self.txtNo.SetEditable(True) # 다시 텍스트칸 입력가능하게
        self.btnUpdate.SetLabel('수정') # 버튼 이름 수정으로 다시 바꾸고
        self.btnUpdate.id = 2 # id값 2
        self.btnConfirm.Enable(False) # 다시 확인버튼 못누르게

    def SelectData(self, no): # 해당번호 자료읽기
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            
            sql = "select * from pymem where bun={}".format(no)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data
            
        except Exception as e:
            wx.MessageBox('읽기 오류 : ' + str(e), '알림', wx.OK)
        finally:
            cursor.close()
            conn.close()
            
if __name__ == "__main__":
    app = wx.App()
    MyFrame(None).Show()
    app.MainLoop()    

