import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QStyle
from PyQt5.QtGui import QPixmap, QIcon
import sqlite3
##################################################################################
#Homepage Window Loading
###################################################################################
class Homepage(QMainWindow):
    def __init__(self):
        super(Homepage,self).__init__()
        loadUi("Homepage.ui",self)
        logobg=QPixmap('WhatsApp Image 2022-03-22 at 5.44.11 PM.jpeg')
        self.label_4.setPixmap(logobg)
        homimg=QPixmap('WhatsApp Image 2022-03-22 at 5.44.09 PM.jpeg')
        self.label_2.setPixmap(homimg)
        loginimg=QIcon('WhatsApp Image 2022-03-16 at 3.47.24 PM.jpeg')
        self.LoginButton.setIcon(loginimg)
        infoimg=QPixmap('WhatsApp Image 2022-03-22 at 5.44.10 PM.jpeg')
        self.label_3.setPixmap(infoimg)
        self.AdminLogin.clicked.connect(self.gotoadminlogin)
        self.LoginButton.clicked.connect(self.gotouserlogin)
        self.Register.clicked.connect(self.gotouserreg)
    def gotoadminlogin(self):
        adlogin=AdminLogin()
        widget.addWidget(adlogin)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotouserlogin(self):
        uslogin = Userlogin()
        widget.addWidget(uslogin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotouserreg(self):
        usreg = userregister()
        widget.addWidget(usreg)
        widget.setCurrentIndex(widget.currentIndex() + 1)
#####################################################################
#Admin Login Window Loading
######################################################################
class AdminLogin(QMainWindow):
    def __init__(self):
        super(AdminLogin,self).__init__()
        loadUi("FinalAdminLogin.ui",self)
        Adminphoto=QPixmap('1.jpg')
        self.label_2.setPixmap(Adminphoto)
        self.LoginButton.clicked.connect(self.gotoadmindashboard)
        self.BackButton.clicked.connect(self.gotohomepage)
    def gotohomepage(self):
        gohom=Homepage()
        widget.addWidget(gohom)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoadmindashboard(self):
        user=self.usernamefield.text()
        password=self.passfield.text()
        if len(user)==0 or len(password)==0:
            self.label_3.setText("Please input all the fields")
        else:
            connection = sqlite3.connect("ADMINLOGIN1.db")
            result = connection.execute("SELECT * FROM admintable WHERE Username =?  AND Password =? ",(user, password))
            if(len(result.fetchall())>0):
                print("Succesfully logined")
                self.label_3.setText("")
                admindash=AdminDashboard()
                widget.addWidget(admindash)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.label_3.setText("Invalid Username or Password")
##################################################################################
#Admin Dashboard Window Loading
##################################################################################
class AdminDashboard(QMainWindow):
    def __init__(self):
        super(AdminDashboard,self).__init__()
        loadUi("FinalDashboard.ui",self)
        logobg1 = QPixmap('WhatsApp Image 2022-03-22 at 5.44.11 PM.jpeg')
        self.label_22.setPixmap(logobg1)
        dashicon = QIcon('WhatsApp Image 2022-03-16 at 3.47.21 PM.jpeg')
        self.pushButton.setIcon(dashicon)
        searchlogo = QPixmap('WhatsApp Image 2022-03-16 at 3.47.20 PM.jpeg')
        self.label_2.setPixmap(searchlogo)
        heartbg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.13 PM.jpeg')
        self.label_5.setPixmap(heartbg)
        bedlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.18 PM.jpeg')
        self.label_8.setPixmap(bedlogobg)
        ventlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.23 PM.jpeg')
        self.label_11.setPixmap(ventlogobg)
        revlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.20 PM (1).jpeg')
        self.label_14.setPixmap(revlogobg)
        declogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.15 PM.jpeg')
        self.label_16.setPixmap(declogobg)
        addlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.12 PM.jpeg')
        self.label_20.setPixmap(addlogobg)
        self.pushButton_4.clicked.connect(self.gotoho)
        self.pushButton_3.clicked.connect(self.gotot)
        self.pushButton_6.clicked.connect(self.gotoht)
    def gotoht(self):
        gotoht = hostable()
        widget.addWidget(gotoht)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotoho(self):
        gohom = Homepage()
        widget.addWidget(gohom)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotot(self):
        gotot=patable()
        widget.addWidget(gotot)
        widget.setCurrentIndex(widget.currentIndex() + 1)
#########################################################################
#User Login Window Loading
##########################################################################
class Userlogin(QMainWindow):
    def __init__(self):
        super(Userlogin,self).__init__()
        loadUi("FinalLogin.ui",self)
        loginphoto=QPixmap('1.jpg')
        self.label_2.setPixmap(loginphoto)
        self.backButton.clicked.connect(self.gotohomepage1)
        self.LoginButton1.clicked.connect(self.gotouserdashboard)
        self.createbutton.clicked.connect(self.gotoregis)
    def gotohomepage1(self):
        gohom=Homepage()
        widget.addWidget(gohom)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotouserdashboard(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(user) == 0 or len(password) == 0:
            self.label_3.setText("Please input all the fields")
        else:
            connection = sqlite3.connect("userdata1.db")
            result = connection.execute("SELECT * FROM logintable WHERE username =?  AND password =? ",(user, password))
            if (len(result.fetchall()) > 0):
                print("Succesfully logined")
                self.label_3.setText("")
                userdash = Userdashboard()
                widget.addWidget(userdash)
                widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                self.label_3.setText("Invalid Username or Password")
    def gotoregis(self):
        usregis = userregister()
        widget.addWidget(usregis)
        widget.setCurrentIndex(widget.currentIndex() + 1)
####################################################################################################
#User Registeratiion Login Window
#####################################################################################################
class userregister(QMainWindow):
    def __init__(self):
        super(userregister,self).__init__()
        loadUi("FinalRegister.ui",self)
        regphoto=QPixmap('1.jpg')
        self.label_2.setPixmap(regphoto)
        self.bacButton.clicked.connect(self.gotohomepage2)
        self.SubmitButton.clicked.connect(self.userregdone)
        self.GotoLogin.clicked.connect(self.gotouslogin)
    def gotohomepage2(self):
        gohom=Homepage()
        widget.addWidget(gohom)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def userregdone(self):
        firstandlastname=self.lineEdit_fname.text()
        username=self.lineEdit_username.text()
        middlename=self.lineEdit_Mname.text()
        email=self.lineEdit_Email.text()
        mobile=self.lineEdit_Mobile.text()
        password=self.lineEdit_pass.text()
        gender=self.lineEdit_Gender.text()
        confirmpass=self.lineEdit_8.text()
        if len(firstandlastname) == 0 or len(username) == 0 or len(middlename) == 0 or len(email)==0 or len(mobile)==0 or len(password)==0 or len(gender)==0 or len(confirmpass)==0:
            self.label_3.setText("Please fill in all inputs.")
        elif password != confirmpass:
            self.label_3.setText("Passwords do not match.")
        else:
            con = sqlite3.connect("userdata1.db")
            query = "insert into userdata(firstandlastname,username,middlename,email,mobile,password,gender,confirmpass) values ('" + firstandlastname + "','" + username + "','" + middlename + "','" + email + "','" + mobile + "','" + password + "','" + gender + "','" + confirmpass + "' )"
            query1 = "insert into logintable(username,password) values ('" + username + "','" + password + "')"
            con.execute(query)
            con.execute(query1)
            con.commit()
            con.close()
            print("register successfully")
            self.label_3.setText("")
            userlogin=Userlogin()
            widget.addWidget(userlogin)
            widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotouslogin(self):
        uselogin = Userlogin()
        widget.addWidget(uselogin)
        widget.setCurrentIndex(widget.currentIndex() + 1)
################################################################################################
#UserDashboard Window Loading
################################################################################################
class Userdashboard(QMainWindow):
    def __init__(self):
        super(Userdashboard,self).__init__()
        loadUi("FinalUserdashboard.ui",self)
        logobg12 = QPixmap('WhatsApp Image 2022-03-22 at 5.44.11 PM.jpeg')
        self.label_22.setPixmap(logobg12)
        dashicon = QIcon('WhatsApp Image 2022-03-16 at 3.47.21 PM.jpeg')
        self.pushButton.setIcon(dashicon)
        searchlogo = QPixmap('WhatsApp Image 2022-03-16 at 3.47.20 PM.jpeg')
        self.label_2.setPixmap(searchlogo)
        heartbg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.13 PM.jpeg')
        self.label_5.setPixmap(heartbg)
        bedlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.18 PM.jpeg')
        self.label_8.setPixmap(bedlogobg)
        ventlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.23 PM.jpeg')
        self.label_11.setPixmap(ventlogobg)
        revlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.20 PM (1).jpeg')
        self.label_14.setPixmap(revlogobg)
        declogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.15 PM.jpeg')
        self.label_16.setPixmap(declogobg)
        addlogobg = QPixmap('WhatsApp Image 2022-03-16 at 3.47.12 PM.jpeg')
        self.label_20.setPixmap(addlogobg)
        self.pushButton_4.clicked.connect(self.gotoho)
        self.pushButton_5.clicked.connect(self.gotobed)
        self.pushButton_3.clicked.connect(self.bedavail)
    def gotoho(self):
        gohom = Homepage()
        widget.addWidget(gohom)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def gotobed(self):
        gotobed = Bookbed()
        widget.addWidget(gotobed)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def bedavail(self):
        gotoavail = bedavail()
        widget.addWidget(gotoavail)
        widget.setCurrentIndex(widget.currentIndex() + 1)
############################################################
####Book Bed Window Loading
#############################################################
class Bookbed(QMainWindow):
    def __init__(self):
        super(Bookbed, self).__init__()
        loadUi("bb.ui", self)
        logodoc12 = QPixmap('Doctor.jpeg')
        self.label_2.setPixmap(logodoc12)
        self.pushButton_2.clicked.connect(self.gtodash)
        self.pushButton.clicked.connect(self.confirm)
    def gtodash(self):
        gotdash = Userdashboard()
        widget.addWidget(gotdash)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def confirm(self):
        name=self.lineEdit.text()
        email = self.lineEdit_2.text()
        date =self.lineEdit_3.text()
        gender = self.lineEdit_5.text()
        mobile = self.lineEdit_6.text()
        bed=self.lineEdit_4.text()
        if len(name) == 0  or len(email) == 0 or len(date) == 0 or len(gender) == 0 or len(mobile) == 0 or len(bed) == 0:
            self.label_9.setText("Please fill in all inputs.")
        else:
            con = sqlite3.connect("ADMINLOGIN1.db")
            query = "insert into confrim(name,email,date,gender,mobile,bed) values ('" + name + "','" + email + "','" + date + "','" + gender + "','" + mobile + "','" + bed + "' )"
            con.execute(query)
            con.commit()
            con.close()
            print("bed confirm successfully")
            self.label_9.setText("Your Bed is Succesfully booked")
            conmess = success()
            widget.addWidget(conmess)
            widget.setCurrentIndex(widget.currentIndex() + 1)
######################################################
#Bed Booking Confqrimation Window
######################################################
class success(QMainWindow):
    def __init__(self):
        super(success, self).__init__()
        loadUi("success.ui", self)
        logodoc12 = QPixmap('WhatsApp Image 2022-03-22 at 5.44.11 PM.jpeg')
        self.label.setPixmap(logodoc12)
        logodoc123= QPixmap('WhatsApp Image 2022-04-07 at 7.30.21 PM.jpeg')
        self.label_2.setPixmap(logodoc123)
        self.pushButton.clicked.connect(self.gotous)
    def gotous(self):
        gotdash = Userdashboard()
        widget.addWidget(gotdash)
        widget.setCurrentIndex(widget.currentIndex() + 1)
############################################################
#Loading patient list
############################################################
class patable(QDialog):
    def __init__(self):
        super(patable, self).__init__()
        loadUi("tabletutorial.ui", self)
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 350)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 350)
        self.tableWidget.setColumnWidth(4, 350)
        self.tableWidget.setColumnWidth(5, 350)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Email", "Date", "Gender", "Mobile", "Bed"])
        self.pushButton.clicked.connect(self.gotodash)
        self.loaddata()
    def loaddata(self):
        connection = sqlite3.connect('ADMINLOGIN1.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM confrim LIMIT 40'
        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1
    def gotodash(self):
        admindash = AdminDashboard()
        widget.addWidget(admindash)
        widget.setCurrentIndex(widget.currentIndex() + 1)
######################################################
#Loading haspital adding table
###########################################################
class hostable(QDialog):
    def __init__(self):
        super(hostable, self).__init__()
        loadUi("Hopitaltable.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 500)
        self.tableWidget.setColumnWidth(3, 500)
        self.tableWidget.setHorizontalHeaderLabels(["Hospital Name", "Address", "Count of the Single Beds", "Count of the ICU Beds"])
        self.pushButton_2.clicked.connect(self.addhos)
        self.pushButton_4.clicked.connect(self.loadda)
        self.pushButton.clicked.connect(self.gotoadmindashboarded)
    def addhos(self):
        name = self.lineEdit.text()
        address = self.lineEdit_2.text()
        sbeds = self.lineEdit_3.text()
        ibeds = self.lineEdit_4.text()
        if len(name) == 0 or len(address) == 0 or len(sbeds) == 0 or len(ibeds) == 0:
            self.label_2.setText("Please fill in all inputs.")
        else:
            con = sqlite3.connect("ADMINLOGIN1.db")
            query = "insert into hosdata (name,address,sbeds,ibeds) values ('" + name + "','" + address + "','" + sbeds + "','" + ibeds + "')"
            con.execute(query)
            con.commit()
            con.close()
            print("Hopital added succesfully")
            self.label_3.setText("Hopital added succesfully")
    def loadda(self):
        connection = sqlite3.connect('ADMINLOGIN1.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM hosdata LIMIT 100'
        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(100)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1
    def gotoadmindashboarded(self):
        addash = AdminDashboard()
        widget.addWidget(addash)
        widget.setCurrentIndex(widget.currentIndex() + 1)
########################################################
#Loading bed availablity window
#########################################################
class bedavail(QDialog):
    def __init__(self):
        super(bedavail, self).__init__()
        loadUi("bedavail.ui", self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 500)
        self.tableWidget.setColumnWidth(3, 500)
        self.tableWidget.setHorizontalHeaderLabels(["Hospital Name", "Address", "Count of the Single Beds", "Count of the ICU Beds"])
        self.pushButton.clicked.connect(self.gotouserdash)
        self.loadbed()
    def loadbed(self):
        connection = sqlite3.connect('ADMINLOGIN1.db')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM hosdata LIMIT 100'
        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(100)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            tablerow += 1
    def gotouserdash(self):
        userdash = Userdashboard()
        widget.addWidget(userdash)
        widget.setCurrentIndex(widget.currentIndex() + 1)
################################################################
#loading and exiting the window
#main
app=QApplication(sys.argv)
Homepag=Homepage()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Homepag)
widget.show()
widget.setFixedWidth(1150)
widget.setFixedHeight(700)
try:
    sys.exit(app.exec())
except:
    print("Exiting")