# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sellalert.ui'
#
# Created: Mon Jul 07 02:01:26 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SellAlert(object):
    def setupUi(self, SellAlert):
        SellAlert.setObjectName(_fromUtf8("SellAlert"))
        SellAlert.resize(822, 484)
        SellAlert.setStyleSheet(_fromUtf8("QDoubleSpinBox{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-left-color: rgba(47, 53, 64, 255);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"border-right-color: rgba(47, 53, 64, 255);\n"
"border-right-style: solid;\n"
"border-right-width:1px;\n"
"\n"
"border-radius: 3px;\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"\n"
"}\n"
"QDoubleSpinBox::up-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"QDoubleSpinBox::down-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"QDoubleSpinBox::up-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QDoubleSpinBox::down-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QDoubleSpinBox::down-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(55, 64, 73), stop:0.917522 rgb(73, 82, 97), stop:0.978056 rgb(90, 100, 112));\n"
"}\n"
"\n"
" QMenuBar::item {\n"
"     spacing: 3px; /* spacing between menu bar items */\n"
"     padding: 1px 4px;\n"
"     background: transparent;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background: #a8a8a8;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"     background: #888888;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"     background: #a8a8a8;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"     background: #888888;\n"
" }\n"
"\n"
"\n"
"QTabBar::tab {width: 130px; }\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QWidget ---- */\n"
"QWidget {\n"
"    background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:2, fx:0.5, fy:0.5, stop:0 rgba(76, 88, 102, 255), stop:1 rgba(65, 73, 86, 255));\n"
"    }\n"
"\n"
"/* ----- QDialogButtonBox ---- */\n"
"QDialogButtonBox\n"
"{\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"\n"
"    }\n"
"QDialogButtonBox:hover {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"}\n"
"QDialogButtonBox:pressed {\n"
"color:#acb3bd;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"/* ----- QSpinBox ---- */\n"
"\n"
"QSpinBox{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"\n"
"border-radius: 3px;\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"\n"
"}\n"
"QSpinBox::up-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"QSpinBox::down-arrow\n"
"{\n"
"   image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QSpinBox::up-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"QSpinBox::up-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QSpinBox::down-button:pressed\n"
"{\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-left-color: rgb(90, 100, 112);\n"
"border-left-style: solid;\n"
"border-left-width:1px;\n"
"}\n"
"QSpinBox::down-button\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(55, 64, 73), stop:0.917522 rgb(73, 82, 97), stop:0.978056 rgb(90, 100, 112));\n"
"}\n"
"\n"
"/* ----- QProgressBar ---- */\n"
"\n"
"QProgressBar {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    text-align: center;\n"
"    border-radius: 3px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QLineEdit ---- */\n"
"\n"
"QLineEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QTextBrowser ---- */\n"
"\n"
"QTextBrowser {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* -----  QTextBrowser - QScrollBar:vertical  ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QTextBrowser - QScrollBar:horizontal  ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QPlainTextEdit ---- */\n"
"\n"
"QPlainTextEdit {\n"
"    border-radius: 3px;\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    color:#fff;\n"
"}\n"
"\n"
"/* ----- QCheckBox ---- */\n"
"\n"
"QCheckBox {\n"
"    spacing: 10px;\n"
"     color:#fff;\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    border-radius: 3px;\n"
"width:16px;\n"
"height:16px;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/newPrefix/images/check.png);\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"    border-radius: 3px;\n"
"    width:16px;\n"
"    height:16px;\n"
"}\n"
"\n"
"/* ----- QTabWidget ---- */\n"
"\n"
"QTabWidget::pane{\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"}\n"
"QTabBar::tab {\n"
"     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    min-width:100px;\n"
"    min-height:25px;\n"
"    padding-left:5px;\n"
" }\n"
"\n"
" QTabBar::tab:selected,  QTabBar::tab:!selected:hover {\n"
" background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
" color:#fff;\n"
" }\n"
" QTabBar::tab:!selected:hover\n"
" {\n"
" color:#fff;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"\n"
"    border-left-color: rgba(47, 53, 64, 255);\n"
"    border-left-style: solid;\n"
"    border-left-width:1px;\n"
"    border-top-color: rgba(47, 53, 64, 255);\n"
"    border-top-style: solid;\n"
"    border-top-width:1px;\n"
"    border-right-color: rgba(47, 53, 64, 255);\n"
"    border-right-style: solid;\n"
"    border-right-width:1px;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 2px;\n"
"     color:#acb3bd;\n"
"     background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"\n"
" }\n"
"\n"
"/* ----- QComboBox editable and !editable ---- */\n"
"\n"
"\n"
" QComboBox:editable {\n"
"\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"    border-bottom-color: rgb(90, 100, 112);\n"
"    border-bottom-style: solid;\n"
"    border-bottom-width:1px;\n"
"   border-radius: 3px;\n"
"     padding: 1px 18px 1px 13px;\n"
"     min-width: 6em;\n"
"     min-height:28px;\n"
"\n"
"    color:#fff;\n"
"    margin-bottom:3px;\n"
" }\n"
"\n"
" QComboBox:!editable {\n"
"  border-radius: 10px;\n"
"  padding: 1px 18px 1px 3px;\n"
"  min-width: 6em;\n"
"  background: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow-combo.png);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down:!editable {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"\n"
"    border-left-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:1, stop:0 rgb(0, 40, 65), stop:0.319716 rgba(127, 204, 255, 255), stop:0.803987 rgba(0, 0, 0, 255), stop:0.994318 rgba(0, 0, 0, 255));\n"
"\n"
"    border-left-style: solid;\n"
"    border-left-width:2px;\n"
"\n"
"    padding:9px 5px 7px 5px;\n"
"    width:17px;\n"
"}\n"
"\n"
"QComboBox::drop-down:editable {\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
" padding:6px;\n"
" width:16px;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down:hover:editable {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"\n"
" QComboBox::drop-down:editable:on {\n"
" color:#acb3bd;\n"
" background-color:  rgba(47, 53, 64, 255);\n"
"border:0 solid transparent;\n"
" }\n"
"\n"
"\n"
"QComboBox QListView\n"
"{\n"
"margin:5px;\n"
"background-color:  rgb(47, 53, 64);\n"
"}\n"
"\n"
"\n"
"QComboBox QListView:on::item {\n"
"    border-left: 1px solid transparent;\n"
"    color:#acb3bd;\n"
"padding-left:5px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    selection-background-color: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"    selection-color:#fff;\n"
"}\n"
"\n"
"/* ----- QScrollBar:vertical ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QScrollBar:horizontal ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QRadioButton ---- */\n"
"\n"
"QRadioButton\n"
"{\n"
"color:#fff;\n"
"\n"
"}\n"
" QRadioButton::indicator::unchecked {\n"
"    background-color:  rgba(47, 53, 64, 255);\n"
"\n"
"    border-radius:8px;\n"
"    width:16px;\n"
"    height:16px;\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
" QRadioButton::indicator::checked {\n"
" background-color:  rgba(47, 53, 64, 255);\n"
" border-radius: 8px;\n"
" width:16px;\n"
" height:16px;\n"
"     image: url(:/newPrefix/images/radio.png);\n"
" }\n"
"\n"
"\n"
" QRadioButton::indicator:checked:pressed {\n"
"    image: url(:/newPrefix/images/radio.png);\n"
" }\n"
"\n"
"/* ----- QTableView ---- */\n"
"\n"
"QTableView\n"
"{\n"
"color:#fff;\n"
"background-color:  rgba(47, 53, 64, 255);\n"
"border-bottom-color: rgb(90, 100, 112);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"border-radius: 3px;\n"
"gridline-color:rgb(90, 100, 112);\n"
"selection-background-color: qlineargradient(spread:pad, x1:0, y1:0.955, x2:0, y2:0, stop:0 rgba(63, 109, 184, 255), stop:1 rgba(90, 155, 209, 255));\n"
"}\n"
"QHeaderView::section, QTableView QTableCornerButton::section {\n"
"color:#fff;\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
"border-radius: 3px;\n"
"padding:5px;\n"
" }\n"
"\n"
" QHeaderView::section:checked, QTableView QTableCornerButton::section:checked\n"
" {\n"
" background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
" border-color: rgba(47, 53, 64, 255);\n"
" border-style: solid;\n"
" border-width:1px;\n"
"  border-radius: 3px;\n"
" }\n"
"\n"
"/* ----- QScrollBar:vertical ---- */\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 15px;\n"
"      margin: 22px 0 22px 0;\n"
"  }\n"
"QScrollBar::handle:vertical {\n"
"      background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"      border-color: rgba(47, 53, 64, 255);\n"
"      border-style: solid;\n"
"      border-width:1px;\n"
"      border-radius: 3px;\n"
"      min-height: 20px;\n"
"  }\n"
"QScrollBar::add-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 20px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/up-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::up-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::down-button:vertical\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"image: url(:/newPrefix/images/down-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"background: none;\n"
"}\n"
"\n"
"/* ----- QScrollBar:horizontal ---- */\n"
"\n"
"QScrollBar:horizontal {\n"
"      border: 1px solid rgba(47, 53, 64, 255);\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      height: 15px;\n"
"      margin: 0 22px 0 22px;\n"
"  }\n"
"QScrollBar::handle:horizontal {\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1.5, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(92, 104, 120), stop:0.958056 rgb(110, 120, 132));\n"
"border-color: rgba(47, 53, 64, 255);\n"
"border-style: solid;\n"
"border-width:1px;\n"
" border-radius: 3px;\n"
"      min-width: 20px;\n"
"  }\n"
"QScrollBar::add-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      background-color:  rgba(47, 53, 64, 255);\n"
"      width: 20px;\n"
"      subcontrol-position: left;\n"
"      subcontrol-origin: margin;\n"
"  }\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/left-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::left-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:3, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-bottom-color: rgba(47, 53, 64, 255);\n"
"border-bottom-style: solid;\n"
"border-bottom-width:1px;\n"
"}\n"
"\n"
"QScrollBar::right-button:horizontal\n"
"{\n"
"background-color: qlineargradient(spread:pad, x2:0.0001, y1:1, x2:0.0001, y2:0, stop:0.0709427 rgb(60, 68, 79), stop:0.947522 rgb(73, 82, 97), stop:0.958056 rgb(90, 100, 112));\n"
"border-top-color: rgba(47, 53, 64, 255);\n"
"border-top-style: solid;\n"
"border-top-width:1px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"image: url(:/newPrefix/images/right-arrow.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"background: none;\n"
"}\n"
""))
        SellAlert.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        self.central2Widget = QtGui.QWidget(SellAlert)
        self.central2Widget.setGeometry(QtCore.QRect(10, 30, 851, 451))
        self.central2Widget.setLocale(QtCore.QLocale(QtCore.QLocale.Cherokee, QtCore.QLocale.UnitedStates))
        self.central2Widget.setObjectName(_fromUtf8("central2Widget"))
        self.smthwrong = QtGui.QLabel(self.central2Widget)
        self.smthwrong.setGeometry(QtCore.QRect(270, 395, 331, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 0, 3))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QRadialGradient(0.5, 0.5, 2.0, 0.5, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(76, 88, 102))
        gradient.setColorAt(1.0, QtGui.QColor(65, 73, 86))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.smthwrong.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.smthwrong.setFont(font)
        self.smthwrong.setText(_fromUtf8(""))
        self.smthwrong.setObjectName(_fromUtf8("smthwrong"))
        self.label = QtGui.QLabel(self.central2Widget)
        self.label.setGeometry(QtCore.QRect(130, -10, 681, 451))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.menuBar = QtGui.QMenuBar(SellAlert)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 822, 18))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.mainToolBar = QtGui.QToolBar(SellAlert)
        self.mainToolBar.setGeometry(QtCore.QRect(0, 0, 4, 12))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.statusBar = QtGui.QStatusBar(SellAlert)
        self.statusBar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))

        self.retranslateUi(SellAlert)
        QtCore.QMetaObject.connectSlotsByName(SellAlert)

    def retranslateUi(self, SellAlert):
        SellAlert.setWindowTitle(_translate("SellAlert", "Sell", None))
        self.label.setText(_translate("SellAlert", "Now your message in the process of sending to the network, \n"
"please wait until it is sent, if necessary, click resend.\n"
" The message is usually sent for 20-40 minutes.", None))

