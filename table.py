# Form implementation generated from reading ui file 'table.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_table_window(object):
    def setupUi(self, table_window):
        table_window.setObjectName("table_window")
        table_window.resize(1920, 1080)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/ProgrammIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        table_window.setWindowIcon(icon)
        table_window.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(parent=table_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 30, 160, 621))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.faculty_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.faculty_layout.setContentsMargins(0, 0, 0, 0)
        self.faculty_layout.setObjectName("faculty_layout")
        self.faculty_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.faculty_label.setFont(font)
        self.faculty_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.faculty_label.setObjectName("faculty_label")
        self.faculty_layout.addWidget(self.faculty_label)
        self.faculty_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.faculty_list.setFont(font)
        self.faculty_list.setObjectName("faculty_list")
        self.faculty_layout.addWidget(self.faculty_list)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 30, 160, 621))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.year_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.year_layout.setContentsMargins(0, 0, 0, 0)
        self.year_layout.setObjectName("year_layout")
        self.year_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.year_label.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.year_label.setFont(font)
        self.year_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year_label.setObjectName("year_label")
        self.year_layout.addWidget(self.year_label)
        self.year_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.year_list.setFont(font)
        self.year_list.setObjectName("year_list")
        self.year_layout.addWidget(self.year_list)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(420, 30, 160, 621))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.group_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.group_layout.setContentsMargins(0, 0, 0, 0)
        self.group_layout.setObjectName("group_layout")
        self.groupe_label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupe_label.setFont(font)
        self.groupe_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.groupe_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupe_label.setObjectName("groupe_label")
        self.group_layout.addWidget(self.groupe_label)
        self.group_list = QtWidgets.QListWidget(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.group_list.setFont(font)
        self.group_list.setObjectName("group_list")
        self.group_layout.addWidget(self.group_list)
        self.group_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.group_table.setGeometry(QtCore.QRect(630, 70, 1241, 751))
        self.group_table.setMouseTracking(True)
        self.group_table.setAutoFillBackground(False)
        self.group_table.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.group_table.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.group_table.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.group_table.setLineWidth(1)
        self.group_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.group_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.group_table.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.group_table.setObjectName("group_table")
        self.group_table.setColumnCount(16)
        self.group_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.group_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.group_table.setHorizontalHeaderItem(15, item)
        self.group_table.horizontalHeader().setCascadingSectionResizes(False)
        self.group_table.horizontalHeader().setStretchLastSection(False)
        self.group_table.verticalHeader().setCascadingSectionResizes(False)
        self.calendar_Widget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendar_Widget.setGeometry(QtCore.QRect(30, 680, 551, 351))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calendar_Widget.setFont(font)
        self.calendar_Widget.setGridVisible(True)
        self.calendar_Widget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendar_Widget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.ISOWeekNumbers)
        self.calendar_Widget.setNavigationBarVisible(True)
        self.calendar_Widget.setDateEditEnabled(False)
        self.calendar_Widget.setObjectName("calendar_Widget")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(1780, 910, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        table_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=table_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        table_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=table_window)
        self.statusbar.setObjectName("statusbar")
        table_window.setStatusBar(self.statusbar)

        self.retranslateUi(table_window)
        QtCore.QMetaObject.connectSlotsByName(table_window)

    def retranslateUi(self, table_window):
        _translate = QtCore.QCoreApplication.translate
        table_window.setWindowTitle(_translate("table_window", "Voice journal"))
        self.faculty_label.setText(_translate("table_window", "Факультет"))
        self.year_label.setText(_translate("table_window", "Курс"))
        self.groupe_label.setText(_translate("table_window", "Группа"))
        self.group_table.setSortingEnabled(True)
        item = self.group_table.horizontalHeaderItem(0)
        item.setText(_translate("table_window", "14.01.2023"))
        item = self.group_table.horizontalHeaderItem(1)
        item.setText(_translate("table_window", "21.01.2023"))
        item = self.group_table.horizontalHeaderItem(2)
        item.setText(_translate("table_window", "28.01.2023"))
        item = self.group_table.horizontalHeaderItem(3)
        item.setText(_translate("table_window", "04.02.2023"))
        item = self.group_table.horizontalHeaderItem(4)
        item.setText(_translate("table_window", "11.02.2023"))
        item = self.group_table.horizontalHeaderItem(5)
        item.setText(_translate("table_window", "18.02.2023"))
        item = self.group_table.horizontalHeaderItem(6)
        item.setText(_translate("table_window", "25.02.2023"))
        item = self.group_table.horizontalHeaderItem(7)
        item.setText(_translate("table_window", "04.03.2023"))
        item = self.group_table.horizontalHeaderItem(8)
        item.setText(_translate("table_window", "11.03.2023"))
        item = self.group_table.horizontalHeaderItem(9)
        item.setText(_translate("table_window", "18.03.2023"))
        item = self.group_table.horizontalHeaderItem(10)
        item.setText(_translate("table_window", "25.03.2023"))
        item = self.group_table.horizontalHeaderItem(11)
        item.setText(_translate("table_window", "01.04.2023"))
        item = self.group_table.horizontalHeaderItem(12)
        item.setText(_translate("table_window", "08.04.2023"))
        item = self.group_table.horizontalHeaderItem(13)
        item.setText(_translate("table_window", "15.04.2023"))
        item = self.group_table.horizontalHeaderItem(14)
        item.setText(_translate("table_window", "22.04.2023"))
        item = self.group_table.horizontalHeaderItem(15)
        item.setText(_translate("table_window", "29.05.2023"))
        self.exit_button.setText(_translate("table_window", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    table_window = QtWidgets.QMainWindow()
    ui = Ui_table_window()
    ui.setupUi(table_window)
    table_window.show()
    sys.exit(app.exec())
