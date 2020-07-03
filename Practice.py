import json
import requests
import random
from influxdb import InfluxDBClient as IC
from datetime import datetime
from datetime import time
from datetime import date
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint



def database():
    client=IC(host="localhost", port=8086)
    client.create_database("prac")
    client.switch_database("prac")

    mass=[0,0,0,0,0,0,0,0,0,0]
    count=0
    json_body=[]
    for i in [j for j in range(10)]:
        mass[i]=random.randrange(1, 100)
        table={
                "measurement": "sec_table",
                "tags": {
                        "param": i,
                        "count" : count
                },
                "fields": {
                    "value": mass[i]

                }
            }
        json_body.append(table)
    count=1
    while count<11:
        izm=random.randrange(-1, 2)
        if izm== 0:
            while izm==0:
                izm=random.randrange(-1, 2)
        for y in [h for h in range(10)]:
            #izm=random.randrange(-1, 2)
            mass[y]=mass[y]+izm
            table={
                "measurement": "sec_table",
                "tags": {
                        "param": y,
                        "count" : count
                    },
                "fields": {
                    "value": mass[y]
                    }
            }
            json_body.append(table)
        #json_body.append(table)
        count=count+1




    client.write_points(json_body)
    results = client.query('select * from sec_table')
    points=list(results.get_points(tags={'param':'0'}))
  #  perem1=(str(points[1])[-4:-1])
   # perem1=perem1.replace(":", " ")
  #  print(perem1)
  #  print(perem1)
  #  print(perem1)
    #print(perem1)
  #  perem2=int(perem1)+20
   # print(perem2)
    count2=0
    global graf0
    graf0=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf0[count2]=perem2
        #    print(graf0[count2])
            count2=count2+1
        elif count2==2:
            graf0[10]=perem2
            count2=count2+1
        elif count2==10:
            graf0[count2-1]=perem2
        #    print(graf0[count2-1])
        #    print(graf0[count2])
            count2=count2+1
        else:
            graf0[count2-1]=perem2
        #    print(graf0[count2-1])
            count2=count2+1

    points=list(results.get_points(tags={'param':'1'}))
    count2=0
    global graf1
    graf1=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf1[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf1[10]=perem2
            count2=count2+1
        elif count2==10:
            graf1[count2-1]=perem2
            count2=count2+1
        else:
            graf1[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'2'}))
    count2=0
    global graf2
    graf2=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf2[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf2[10]=perem2
            count2=count2+1
        elif count2==10:
            graf2[count2-1]=perem2
            count2=count2+1
        else:
            graf2[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'3'}))
    count2=0
    global graf3
    graf3=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf3[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf3[10]=perem2
            count2=count2+1
        elif count2==10:
            graf3[count2-1]=perem2
            count2=count2+1
        else:
            graf3[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'4'}))
    count2=0
    global graf4
    graf4=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf4[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf4[10]=perem2
            count2=count2+1
        elif count2==10:
            graf4[count2-1]=perem2
            count2=count2+1
        else:
            graf4[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'5'}))
    count2=0
    global graf5
    graf5=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf5[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf5[10]=perem2
            count2=count2+1
        elif count2==10:
            graf5[count2-1]=perem2
            count2=count2+1
        else:
            graf5[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'6'}))
    count2=0
    global graf6
    graf6=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf6[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf6[10]=perem2
            count2=count2+1
        elif count2==10:
            graf6[count2-1]=perem2
            count2=count2+1
        else:
            graf6[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'7'}))
    count2=0
    global graf7
    graf7=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf7[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf7[10]=perem2
            count2=count2+1
        elif count2==10:
            graf7[count2-1]=perem2
            count2=count2+1
        else:
            graf7[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'8'}))
    count2=0
    global graf8
    graf8=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf8[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf8[10]=perem2
            count2=count2+1
        elif count2==10:
            graf8[count2-1]=perem2
            count2=count2+1
        else:
            graf8[count2-1]=perem2
            count2=count2+1

    points=list(results.get_points(tags={'param':'9'}))
    count2=0
    global graf9
    graf9=[0,0,0,0,0,0,0,0,0,0,0]
    while count2<11:
        perem1=(str(points[count2])[-4:-1])
        perem1=perem1.replace(":", " ")
        perem2=int(perem1)
        if count2<2:
            graf9[count2]=perem2
            count2=count2+1
        elif count2==2:
            graf9[10]=perem2
            count2=count2+1
        elif count2==10:
            graf9[count2-1]=perem2
            count2=count2+1
        else:
            graf9[count2-1]=perem2
            count2=count2+1

    print(graf0)
    print(graf1)
    print(graf2)
    print(graf3)
    print(graf4)
    print(graf5)
    print(graf6)
    print(graf7)
    print(graf8)
    print(graf9)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(11))
        self.y0 = graf0 
        self.y1 = graf1
        self.y2 = graf2
        self.y3 = graf3
        self.y4 = graf4
        self.y5 = graf5
        self.y6 = graf6
        self.y7 = graf7
        self.y8 = graf8
        self.y9 = graf9

        self.graphWidget.setBackground('w')
        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Значения', **styles)
        self.graphWidget.setLabel('bottom', 'Номер измерения', **styles)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y0, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y1, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y2, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y3, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y4, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y5, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y6, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y7, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y8, pen=pen)
        self.data_line =  self.graphWidget.plot(self.x, self.y9, pen=pen)



def main():
    database()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()