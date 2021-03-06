#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import uuid
import platform
from qframer.qt.QtCore import *
from qframer.qt.QtGui import *
from qframer.qt import QtCore
from qframer import FSplashScreen, QSingleApplication

from gui import MainWindow
from gui.uiconfig import windowsoptions

from log import logger

logger.info('using %s(%s)' % (os.environ['QT_API'], QtCore.__version__))

if __name__ == '__main__':
    if sys.platform == "linux2":
        if platform.architecture()[0] == "32bit":
            QApplication.addLibraryPath(
                '/usr/lib/%s-linux-gnu/qt5/plugins/' % 'i386')
        else:
            QApplication.addLibraryPath(
                '/usr/lib/%s-linux-gnu/qt5/plugins/' % platform.machine())
    applicationName = 'PFramer'
    app = QSingleApplication(applicationName, sys.argv)

    app.setApplicationVersion("1.0")
    app.setOrganizationName("dragondjf.github.io")
    app.setApplicationName(applicationName)

    if app.isRunning():
        sys.exit(0)
    if windowsoptions['splashflag']:
        splash = FSplashScreen(1, windowsoptions['splashimg'])
        mainwindow = MainWindow()
        mainwindow.show()
        splash.finish(mainwindow)
    else:
        mainwindow = MainWindow()
        mainwindow.show()

    app.setActivationWindow(mainwindow)

    mainwindow.guimanger.globals = globals()
    mainwindow.guimanger.locals = locals()

    print(app.desktop().availableGeometry())
    mainwindow.setGeometry(app.desktop().screen().geometry())

    exitCode = app.exec_()
    sys.exit(exitCode)
