# -*- encoding: utf-8 -*-
from pprint import pprint
from PySide2.QtCore import *
from PySide2.QtCore import Qt
from PySide2.QtGui import *
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QObject, QUrl, Slot
import csv
import sys
import json
 
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QInputDialog, QWidget, QTableWidget,QTableWidgetItem,QPushButton,QListView,QAbstractItemView,QTreeView,QMessageBox
from PySide2.QtWebEngineWidgets import QWebEngineView





# from PySide2.QtWebKit import *

#=SI(IZQUIERDA(E2;1)="9";CONCATENAR("0";E2);E2)
import controlador
import ventanitaPro 
import os
from os.path import isfile
import csv
import math
#from PySide2.phonon import Phonon
import time
import itertools

#http://dev.openlayers.org/examples/sld.html
#http://localhost/geoserver/wfs?service=WFS&version=1.1.0&request=GetFeature&typename=megadapt:infra&outputFormat=application/json&srsname=EPSG:4326


#pyside-uic.exe -o controlador.py controlador.ui
#pyside-uic.exe -o dialog.py dialog.ui


class tiempoItem(QStandardItem):
    def __init__(self, parent=None):
        super(tiempoItem, self).__init__(parent)
        self.arrayDeSettings=[]
    def setArrayDeSettings(self,settings):
        self.arrayDeSettings=[]
        for diccionario in settings:
            self.arrayDeSettings.append(diccionario.copy())
            
    def getArrayDeSettings(self):
        return(self.arrayDeSettings)
    def clickEvent(self, evt):
        print("auch!!")
        return super(tiempoItem, self).dropEvent(evt)
        
    def onclick(self):
        print("aqui pondre la cofiguracion de las 6 pantallas")

class Ui_MainWindow(QMainWindow, controlador.Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)
        estaImagen = QImage("Logotipos_Tablero_de_Control_Megadapt.png") 
        sample_palette = QPalette() 
        sample_palette.setColor(QPalette.Window, Qt.white)
        sample_palette.setColor(QPalette.WindowText, Qt.blue)
        
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setPalette(sample_palette)
        
        
        try:   
            self.logos.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
        self.pantallaActivaIndex=0
        self.fechaSlider.valueChanged.connect(self.ponFecha)
        self.fpSlider.valueChanged.connect(self.ponFp)
        self.groupsOfTimeSisters = []
        self.groupsOfSpaceSisters = []
        
        self.satellite.clicked.connect(self.ponSatelite)
        self.calles.clicked.connect(self.ponCalles)
        
        self.P1.clicked.connect(lambda: self.activaPantalla(0))
        self.P2.clicked.connect(lambda: self.activaPantalla(1))
        self.P3.clicked.connect(lambda: self.activaPantalla(2))
        self.P4.clicked.connect(lambda: self.activaPantalla(3))
        self.P5.clicked.connect(lambda: self.activaPantalla(4))
        self.P6.clicked.connect(lambda: self.activaPantalla(5))
        
        
        self.P1.setChecked(True)
        
        
        self.guardaPantallas.clicked.connect(self.guardaPantallasEnArchivo)
        self.guardaGuion.clicked.connect(self.guardaGuionEnArchivo)
        self.cargaGuion.clicked.connect(self.cargaGuionDeArchivo)
        self.borrar.clicked.connect(self.borraTiempo)
        self.model = QStandardItemModel(self.listView)
        self.listView.setModel(self.model)
        self.cualRow=0
        self.listView.clicked.connect(self.ponTiempo)
        self.contador=0
        
        
        
        self.addImage.clicked.connect(self.agregaCustomImage)
        self.addVideo.clicked.connect(self.agregaCustomVideo)
        self.addSerie.clicked.connect(self.agregaSerie)
        self.addSerieWeb.clicked.connect(self.agregaSerieWeb)
        self.addWeb.clicked.connect(self.agregaWeb)
        
        self.vincularPorEspacio.clicked.connect(self.setSpaceSisters)
        self.vincularPorTiempo.clicked.connect(self.setTimeSisters)
        self.desvincularTiempo.clicked.connect(self.removeTimeSisterhood)
        self.desvincularEspacio.clicked.connect(self.removeSpaceSisterhood)
        
        self.x1.clicked.connect(lambda: self.extiendePantalla(1))
        self.x2.clicked.connect(lambda: self.extiendePantalla(2))
        self.x3.clicked.connect(lambda: self.extiendePantalla(3))
        self.x4.clicked.connect(lambda: self.extiendePantalla(4))
        
        
        
        self.play.clicked.connect(self.hasPlay)
        self.stop.clicked.connect(self.hasStop)
        self.pause.clicked.connect(self.hasPause)
        #self.loop.clicked.connect(self.pantallaX4)
        
        self.playGuion.setEnabled(False)
        self.stopGuion.setEnabled(False)
        
        self.playGuion.clicked.connect(self.playGuionConDelay)
        self.stopGuion.clicked.connect(self.stopGuionConDelay)
        
        alpha  = 255
        color  = QtGui.QColor(237,248,251)
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c1.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        color  = QtGui.QColor(179,205,227)
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c2.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        color  = QtGui.QColor(140,150,198)
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c3.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        color  = QtGui.QColor(136,86,167)
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c4.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        color  = QtGui.QColor(129,15,124)
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c5.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
#      
        
    def ponFp(self,valor):
        fp = float(valor) / 10.0
        cuts = self.bojorquezSerrano(fp,maximo=self.pantallaActiva.api.maximo)##aqui esta mal
        print(str(cuts))
        self.pantallaActiva.webFrame.evaluateJavaScript("setIntervals("+str(cuts)+");") 
        self.pantallaActiva.currentFp = valor
        labelCuts = self.bojorquezSerrano(fp,maximo=330.0)
        self.c1.setGeometry(10,10,labelCuts[1],24)
        self.c2.setGeometry(10+labelCuts[1],10,labelCuts[2]-labelCuts[1],24)
        self.c3.setGeometry(10+labelCuts[2],10,labelCuts[3]-labelCuts[2],24)
        self.c4.setGeometry(10+labelCuts[3],10,labelCuts[4]-labelCuts[3],24)
        self.c5.setGeometry(10+labelCuts[4],10,labelCuts[5]-labelCuts[4],24)
        
        
        
    def bojorquezSerrano(self,fp,numcats=5,maximo=1.0,minimo=0.0):
        laSuma = 0
        for i in range(numcats) :
            laSuma += ((fp) ** i)
        
        cachito = (maximo-minimo) / laSuma
        cut = []
        cut.append(minimo)
        for i in range(numcats):
            anterior = cut[i]
            corte = anterior + fp ** i * cachito
            cut.append(corte)
    
        return cut 
    
    def setSpaceSisterhood(self,listaDeHermanas):
        for hermana in listaDeHermanas:
            susHermanasEnNumero = self.settingsPantallas[int(hermana)-1]['spaceSisters']
            susHermanas = []
            for hermanaNumero in susHermanasEnNumero:
                susHermanas.append(self.pantalla[hermanaNumero].webFrame)
                
            self.pantalla[int(hermana)-1].api.addSpacialSisters(susHermanas)   
        
    def setSpaceSisters(self):
        print ("vinculando pantallas " + self.hermanasDeEspacio.text() + " espacialmente")
        listaDeHermanas = self.hermanasDeEspacio.text().split(",")
        for hermana in listaDeHermanas:
            self.settingsPantallas[int(hermana)-1]['spaceSisters'] = []
            for sister in listaDeHermanas:
                if not sister == hermana:
                    self.settingsPantallas[int(hermana)-1]['spaceSisters'].append(int(sister)-1)
                    
        self.setSpaceSisterhood(listaDeHermanas)
        
                    
        
        
        print (self.settingsPantallas)
    
    def setTimeSisterhood(self, listaDeHermanas):
        for hermana in listaDeHermanas:
            susHermanasEnNumero = self.settingsPantallas[int(hermana)-1]['timeSisters']
            susHermanas = []
            for hermanaNumero in susHermanasEnNumero:
                susHermanas.append(self.pantalla[hermanaNumero].webFrame)
                
            self.pantalla[int(hermana)-1].api.addTemporalSisters(susHermanas)
    
    def setTimeSisters(self):
        print ("vinculando pantallas " + self.hermanasDeTiempo.text() + " temporalmente")
        listaDeHermanas = self.hermanasDeTiempo.text().split(",")
        for hermana in listaDeHermanas:
            self.settingsPantallas[int(hermana)-1]['timeSisters'] = []
            for sister in listaDeHermanas:
                if not sister == hermana:
                    self.settingsPantallas[int(hermana)-1]['timeSisters'].append(int(sister)-1)
                    
        self.setTimeSisterhood(listaDeHermanas)
        
                    
        
        
        print (self.settingsPantallas)
        
    
    def removeSpaceSisterhood(self):
        self.hermanasDeEspacio.setText("")
        print ("desvinculando pantallas")
        for i in range(0, self.numeroDePantallas):
            self.pantalla[i].api.spatial_sisters = []
            self.settingsPantallas[i]['spaceSisters'] = []
    
    def removeTimeSisterhood(self):
        self.hermanasDeTiempo.setText("")
        print ("desvinculando pantallas")
        for i in range(0, self.numeroDePantallas):
            self.pantalla[i].api.temporal_sisters = []
            self.settingsPantallas[i]['timeSisters'] = []
    
    def ponGeometria(self,p,offsetX,offsetY):
        self.pantalla[p].setGeometry(1920+(p*1920)+offsetX,offsetY,1920,1080)
        
    def setSisterhoods(self):
#  esto es para reestablecer los sisterhoods                
        print(self.groupsOfTimeSisters) 
        print(self.groupsOfSpaceSisters)     
         
        for groupOfSisters in self.groupsOfTimeSisters:
            self.setTimeSisterhood(groupOfSisters)  
        for groupOfSisters in self.groupsOfSpaceSisters:
            self.setSpaceSisterhood(groupOfSisters)
    
    def ajustaSliders(self, sender, earg):##esta es la funcion handler del evento del api de cada pantalla que se activa cuando se carga para obtener informacion de la serie web (nFrames y paleta)
        print ('foo! '+str(sender.numberOfFrames))
        nFrames = sender.numberOfFrames
        self.settingsPantallas[earg]['numberOfFrames'] = nFrames
        self.fechaSlider.setMaximum (nFrames)
        self.fechaSlider.setMinimum(1) 
        self.fechaSlider.setValue(1)
        self.pantalla[earg].paleta = sender.paleta#si la paleta es vacia??
        if len(sender.paleta) > 0:
            #print (str(sender.paleta))
            self.setWebberPaleta(earg)
        self.cargando[earg] = False
        if self.guion == True:
            self.ponSiguienteSerieWeb()
        
        if True in self.cargando:
            print(str(earg)+" ya, pero faltan")
        else:
            print("todos ya")
            self.setSisterhoods()

            
    def setWebberPaleta(self, p):
        alpha  = 255
        p_chunk = self.pantalla[p].paleta[0].split("(")[1].split(",")
        color  = QtGui.QColor(int(p_chunk[0]),int(p_chunk[1]),int(p_chunk[2]))
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c1.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        p_chunk = self.pantalla[p].paleta[1].split("(")[1].split(",")
        color  = QtGui.QColor(int(p_chunk[0]),int(p_chunk[1]),int(p_chunk[2]))
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c2.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        p_chunk = self.pantalla[p].paleta[2].split("(")[1].split(",")
        color  = QtGui.QColor(int(p_chunk[0]),int(p_chunk[1]),int(p_chunk[2]))
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c3.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        p_chunk = self.pantalla[p].paleta[3].split("(")[1].split(",")
        color  = QtGui.QColor(int(p_chunk[0]),int(p_chunk[1]),int(p_chunk[2]))
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c4.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        p_chunk = self.pantalla[p].paleta[4].split("(")[1].split(",")
        color  = QtGui.QColor(int(p_chunk[0]),int(p_chunk[1]),int(p_chunk[2]))
        values = "{r}, {g}, {b}, {a}".format(r = color.red(), g = color.green(), b = color.blue(), a = alpha)
        self.c5.setStyleSheet("QLabel { background-color: rgba("+values+"); }")
        
    def ensamblaPantallas(self, numeroDePantallas):
        self.numeroDePantallas=numeroDePantallas
        self.pantalla=[]
        self.settingsPantallas=[]
        self.cargando = []
        for p in range(0,numeroDePantallas):
            self.settingsPantallas.append({'type' : None,'path' : None,'numberOfFrames' : 1,'initialFrame' : 1,'timeSisters' : [],'spaceSisters' : [],'multiplicador': 1})
            self.pantalla.append(Wind())
            self.ponGeometria(p,0,0)
            self.pantalla[p].show()
            self.cargando.append(False)
        
        self.pantallaActiva=self.pantalla[0]
        
        self.P1.setEnabled(True if (self.numeroDePantallas>0) else False)
        self.P2.setEnabled(True if (self.numeroDePantallas>1) else False)
        self.P3.setEnabled(True if (self.numeroDePantallas>2) else False)
        self.P4.setEnabled(True if (self.numeroDePantallas>3) else False)
        self.P5.setEnabled(True if (self.numeroDePantallas>4) else False)
        self.P6.setEnabled(True if (self.numeroDePantallas>5) else False)
        
        
    def playGuionConDelay(self):
        print("aqui se activa el modo de reproduccion automatica del guion")  
        print(str(self.elGuion))
        for tiempo in self.elGuion:
            time.sleep(14)
            self.settingsPantallas=[]
            for row in tiempo:
                self.settingsPantallas.append(row[:])
            
            self.ponPantallasAsi()
            
        
        
    def stopGuionConDelay(self):
        print("aqui se detiene el modo de reproduccion automatica del guion")  
          
    def hasPlay(self):
        print("aqui se reproduce el video")
        self.pantallaActiva.media_obj.play()
    def hasStop(self):
        print("aqui se detiene el video")
        self.pantallaActiva.media_obj.stop()
    def hasPause(self):
        print("aqui se pausa el video")
        self.pantallaActiva.media_obj.pause()    

        
    def extiendePantalla(self,multiplicador):
        
        elPunto = self.pantallaActiva.pos()
        self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=multiplicador
        largo = 1920 * multiplicador
        self.pantallaActiva.setGeometry(elPunto.x(),0,largo,1080) 
        self.pantallaActiva.frame.setGeometry(0,0,largo,1080)
        self.pantallaActiva.imageCanvas.setGeometry(0,0,largo,1080) 
        
        if multiplicador>1:
        
            for i in range(self.pantallaActivaIndex+1,self.pantallaActivaIndex+multiplicador):
                self.pantalla[i].hide()
                self.settingsPantallas[i]['type']=None
        
        self.pantallaActiva.show()
        
    def extiendePantallaNoActiva(self,p,multiplicador):
        
        elPunto = self.pantalla[p].pos()
        self.settingsPantallas[p]['multiplicador']=multiplicador
        largo = 1920 * multiplicador
        self.pantalla[p].setGeometry(elPunto.x(),0,largo,1080) 
        self.pantalla[p].frame.setGeometry(0,0,largo,1080)
        self.pantalla[p].imageCanvas.setGeometry(0,0,largo,1080) 
        
        if multiplicador>1:
        
            for i in range(p+1,p+multiplicador):
                self.pantalla[i].hide()
                self.settingsPantallas[i]['type']=None
        
        self.pantalla[p].show()      
        
  
       
        
    def pantallasX1(self):
        print("todas x1")
        for p in range(0,self.numeroDePantallas):
            self.settingsPantallas[p]['multiplicador']=1
            self.pantalla[p].ponGeometria(p)
            self.pantalla[p].show() 
       
    def agregaSerie(self):
        self.guion = False
        print("aqui agregare una serie de imagenes") 
        imageSerie, _ = QFileDialog.getOpenFileNames(self, 'Selecciona serie de imágenes') 
        
        prefijo=imageSerie[0].split(".")[0][:-2]
        print(prefijo,len(imageSerie))
        image0 = imageSerie[0]
        estaImagen = QImage(image0) 
        
        if self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']==None:
            self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=1
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']
        self.extiendePantalla(multiplicador)
        self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames']=len(imageSerie)
        self.settingsPantallas[self.pantallaActivaIndex]['path']=prefijo
        self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=multiplicador
        self.settingsPantallas[self.pantallaActivaIndex]['initialFrame']=1
        self.fechaSlider.setMaximum(len(imageSerie))
        self.sliderObservados.setVisible(True)
        
        self.fechaSlider.setFocus()
        try:   
            if self.pantallaActiva.video_widget:     
                self.pantallaActiva.video_widget.resize(0, 0)
            self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
        
    def agregaCustomImage(self):
        self.guion = False
        customImage, _ = QFileDialog.getOpenFileName(self, 'Cargar imagen')
        estaImagen = QImage(customImage) 
    
        if self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']==None:
            self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=1
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']
        self.extiendePantalla(multiplicador) 
        
        
        self.settingsPantallas[self.pantallaActivaIndex]['type']="customImage"
        self.settingsPantallas[self.pantallaActivaIndex]['path']=customImage
        self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=multiplicador
        try:   
            if self.pantallaActiva.video_widget:
                self.pantallaActiva.video_widget.resize(0, 0)
            
            self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
            self.pantallaActiva.view.hide()
        except:
            print("no pude") 
        
    def agregaCustomVideo(self):
        self.guion = False
        if self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']==None:
            self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=1
        
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']
        self.extiendePantalla(multiplicador)
        largo = 1920 *multiplicador
        customVideo, _ = QFileDialog.getOpenFileName(self, 'Cargar video')
        
        #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
        
        
        
        self.controlesVideo.setVisible(True)
        #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
        
        media_src = Phonon.MediaSource(customVideo)
        self.pantallaActiva.media_obj = Phonon.MediaObject(self.pantallaActiva.frame)
        self.pantallaActiva.media_obj.setCurrentSource(media_src)
        
        self.pantallaActiva.video_widget = Phonon.VideoWidget(self.pantallaActiva.frame)
   
        self.pantallaActiva.video_widget.setGeometry(0,0,largo,1080)
        Phonon.createPath(self.pantallaActiva.media_obj, self.pantallaActiva.video_widget)
        
        audio_out = Phonon.AudioOutput(Phonon.VideoCategory)
        Phonon.createPath(self.pantallaActiva.media_obj, audio_out)
        
      
        self.pantallaActiva.video_widget.show()
        

        self.pantallaActiva.media_obj.play()
        
        
        self.settingsPantallas[self.pantallaActivaIndex]['type']="customVideo"
        self.settingsPantallas[self.pantallaActivaIndex]['path']=customVideo
        self.settingsPantallas[self.pantallaActivaIndex]['multiplicador']=multiplicador
        

    def agregaSerieWeb(self):
        self.guion = False
        url, ok = QInputDialog.getText(self, 'Input Dialog', 
            'url:')
        if ok:
            self.settingsPantallas[self.pantallaActivaIndex]['path'] = str(url)
            self.settingsPantallas[self.pantallaActivaIndex]['type'] = 'serieWeb'
                        
            self.pantallaActiva.setWebKit(url)
            self.pantallaActiva.api.setEvent(self.pantallaActivaIndex)
           
            
            self.pantallaActiva.api.evt_foo += self.ajustaSliders
            
                  
    
    def agregaWeb(self):
        self.guion = False
        url, ok = QInputDialog.getText(self, 'Input Dialog', 
            'url:')
        if ok:
            
            self.settingsPantallas[self.pantallaActivaIndex]['path'] = str(url)
            self.settingsPantallas[self.pantallaActivaIndex]['type'] = 'webPage'
            self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'] = 1 
            self.pantallaActiva.numberOfFrames = 1           
            self.pantallaActiva.setSimpleWebKit(url)
        
        
    def borraTiempo(self):
        self.model.removeRow(self.cualRow)
    def cargaGuionDeArchivo(self):
        proyectoFileName, _ = QFileDialog.getOpenFileName(self, 'Cargar guión')
        #proyectoFile= open(proyectoFileName,"r")
        

        with open(proyectoFileName) as data_file:
            self.elGuion = json.load(data_file)
        
        
        
        
        self.model.clear()
#         proyectoFile
        contador = 0
        for i in range(1,len(self.elGuion)+1):
            k = 'tiempo'+str(i)
            tiempo = self.elGuion[k][:]
            pixpathFoto = "screens30.png"
         
            elIcon = QImage(pixpathFoto) 
     
            contador += 1
             
             
            textual_item = tiempoItem() 
            textual_item.setData(elIcon,Qt.DecorationRole) 
            textual_item.setText(str(contador))
            textual_item.setArrayDeSettings(tiempo) 
            #textual_item = QStandardItem('Item text'+str(self.contador))    
            self.model.appendRow(textual_item)
            
        self.playGuion.setEnabled(True)
        self.stopGuion.setEnabled(True)
        
    def guardaGuionEnArchivo(self):
        print("Salvando...")
        
        proyectoFileName, _ = QFileDialog.getSaveFileName(self, 'Guardar guión')
        
        proyectoFile= open(proyectoFileName,"w")
        #proyectoFile = asksaveasfile(title="Donde guardo?", mode='w')
        #self.listView
        losItems = self.model.findItems('', Qt.MatchContains)
        print(str(losItems))
        contador = 0
        proyectoFile.write("{")
        for item in losItems:
            contador += 1
            if contador > 1:
                proyectoFile.write(",\n")
            
            proyectoFile.write('"tiempo'+str(contador)+'" :\n') 
            contador2 = 0
            proyectoFile.write("[")
            for diccionario in item.arrayDeSettings:
                contador2 += 1
                if contador2 > 1:
                    proyectoFile.write(",\n") 
                proyectoFile.write(json.dumps(diccionario, sort_keys=False,))
            proyectoFile.write("]") 
            
        proyectoFile.write("}")    
        
        proyectoFile.close()
   
    def ponTiempo(self,evnt):
        print(str(evnt.row()))
        print(str(self.model.item(evnt.row()).getArrayDeSettings()))
        self.cualRow=evnt.row()
        array = self.model.item(evnt.row()).getArrayDeSettings()
        self.settingsPantallas=array[:]
        self.ponPantallasAsi()
    
    def ponPantallasAsi(self):
        print(str(self.settingsPantallas))
        self.guion = True
        estabaEnLaPantalla = self.pantallaActivaIndex
        self.groupsOfTimeSisters = []
        self.groupsOfSpaceSisters = []
        self.cargando = [False for i in range(0, self.numeroDePantallas)]
        for x in range(0,self.numeroDePantallas):
            if self.settingsPantallas[x]['type']=="serieWeb":
                self.cargando[x] = True
        for p in range(0,self.numeroDePantallas):
            
            ya = False
            for i in range(0, len(self.groupsOfTimeSisters)):
                if p in self.groupsOfTimeSisters[i]:
                    ya = True
            
            if not ya and len(self.settingsPantallas[p]['timeSisters']) > 0:
                lista = self.settingsPantallas[p]['timeSisters'][:]
                lista.append(p)
                self.groupsOfTimeSisters.append(lista)
                
            ya = False    
            for i in range(0, len(self.groupsOfSpaceSisters)):
                if p in self.groupsOfSpaceSisters[i]:
                    ya = True
            
            if not ya and len(self.settingsPantallas[p]['spaceSisters']) > 0:
                lista = self.settingsPantallas[p]['spaceSisters'][:]
                lista.append(p)
                self.groupsOfSpaceSisters.append(lista)
            
            
            if self.settingsPantallas[p]['type']=="imageSerie":
                print("imageSerie")
                print(str(self.settingsPantallas[p]))
                
                
                
                print("poniendo el slider en "+ str(self.settingsPantallas[p]['initialFrame']))
                
                self.sliderObservados.setVisible(True)
                self.fechaSlider.setFocus()
                
                self.extiendePantallaNoActiva(p,self.settingsPantallas[p]['multiplicador'])

                if self.pantalla[p].video_widget:     
                    self.pantalla[p].video_widget.resize(0, 0)
                    
                print(str(self.settingsPantallas[p]))
                #self.fechaSlider.setMaximum(self.settingsPantallas[self.pantallaActivaIndex][0])
                self.ponFecha(self.settingsPantallas[p]['initialFrame'])
                    
            elif self.settingsPantallas[p]['type']=="customVideo":
                largo = self.settingsPantallas[p]['multiplicador']*1920
                self.extiendePantallaNoActiva(p,self.settingsPantallas[p]['multiplicador'])
                
                
                self.pantalla[p].frame.setGeometry(0,0,largo,1080)
                
                self.controlesVideo.setVisible(True)
                #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
                customVideo= self.settingsPantallas[p]['path']
                media_src = Phonon.MediaSource(customVideo)
                self.pantalla[p].media_obj = Phonon.MediaObject(self.pantalla[p].frame)
                self.pantalla[p].media_obj.setCurrentSource(media_src)
                
                self.pantalla[p].video_widget = Phonon.VideoWidget(self.pantalla[p].frame)
           
                self.pantalla[p].video_widget.setGeometry(0,0,largo,1050)
                Phonon.createPath(self.pantalla[p].media_obj, self.pantalla[p].video_widget)
                
                audio_out = Phonon.AudioOutput(Phonon.VideoCategory)
                Phonon.createPath(self.pantalla[p].media_obj, audio_out)
                
                self.pantalla[p].video_widget.show()
                self.pantalla[p].media_obj.play()
                
                
            elif self.settingsPantallas[p]['type']=="customImage":
                print("aqui se agrega una imagen custom " + self.settingsPantallas[p]['path']+ " en la pantalla " + str(p))
                customImage= str(self.settingsPantallas[p]['path'])
                estaImagen = QImage(customImage)
                multiplicador = self.settingsPantallas[p]['multiplicador']
                
                self.extiendePantallaNoActiva(p,multiplicador)
            
                
                try: 
                    
                        
                    if self.pantalla[p].video_widget:
                        self.pantalla[p].video_widget.resize(0, 0)
                    self.pantalla[p].imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
                    self.pantalla[p].view.hide()
                
                except:
                    print("no pude") 
                        
            
            elif self.settingsPantallas[p]['type']=="webPage":
                
                print("webPage")
                print(str(self.settingsPantallas[p]))
                self.extiendePantallaNoActiva(p,self.settingsPantallas[p]['multiplicador'])
                self.settingsPantallas[p]['numberOfFrames'] = 1 
                self.pantalla[p].numberOfFrames = 1  
                self.pantalla[p].setSimpleWebKit(self.settingsPantallas[p]['path']) 
                if self.pantalla[p].video_widget:     
                    self.pantalla[p].video_widget.resize(0, 0)  
              
                
                
                #self.ponFecha(self.settingsPantallas[self.pantallaActivaIndex]['initialFrame'])
            else:
                print("no es nada") 
                
        if True in self.cargando:        
        #elif self.settingsPantallas[p]['type']=="serieWeb":
                self.ponSiguienteSerieWeb()
                
         
                    
                
        self.pantallaActiva=self.pantalla[estabaEnLaPantalla]              
        self.pantallaActivaIndex = estabaEnLaPantalla

    def ponSiguienteSerieWeb(self):
        print("serieWeb")
        
        if True in self.cargando:
            p = self.cargando.index(True)
            
           
            print(str(self.settingsPantallas[p]))
            print("poniendo el slider en "+ str(self.settingsPantallas[p]['initialFrame']))
            
            
            self.sliderObservados.setVisible(True)
            
            self.extiendePantallaNoActiva(p,self.settingsPantallas[p]['multiplicador'])
            self.pantalla[p].setWebKit(self.settingsPantallas[p]['path']) 
            if self.pantalla[p].video_widget:     
                self.pantalla[p].video_widget.resize(0, 0)  
                
            
            print(str(self.settingsPantallas[p]))
            #self.fechaSlider.setMaximum(self.settingsPantallas[self.pantallaActivaIndex][0])
            
            
            self.pantalla[p].api.setEvent(p)
            
            self.pantalla[p].api.evt_foo += self.ajustaSliders    
    
    def guardaPantallasEnArchivo(self):
        
    
        
        elIcon = QImage("screens30.png") 

        
        
        
        textual_item = tiempoItem() 
        textual_item.setData(elIcon,Qt.DecorationRole)  
        textual_item.setArrayDeSettings(self.settingsPantallas[:]) 
        #textual_item = QStandardItem('Item text'+str(self.contador))    
        self.model.appendRow(textual_item)
        print(str(self.model.item(0).getArrayDeSettings()))
        self.contador+=1
        
        #self.listView.show()
        
    def ponSatelite(self):
        self.pantallaActiva.webFrame.evaluateJavaScript("setSatelite();")
    
    
    def ponCalles(self):
        self.pantallaActiva.webFrame.evaluateJavaScript("setCalles();")
        
    
        


    def ponFecha(self,valor):
        #self.pantallaActiva.webFrame.evaluateJavaScript("setup();")
        #print str(self.settingsPantallas[self.pantallaActivaIndex])
        if self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'] > 1:
            if valor>9:
                valorStr = str(valor)
            else:
                valorStr = "0"+str(valor)
            
            if self.settingsPantallas[self.pantallaActivaIndex]['type']=="serieWeb":
                self.pantallaActiva.webFrame.evaluateJavaScript("setStep("+str(valor-1)+");")
                self.pantallaActiva.currentFrame = valor
                for i in self.settingsPantallas[self.pantallaActivaIndex]['timeSisters']:
                    self.pantalla[i].webFrame.evaluateJavaScript("setStep("+str(valor-1)+");")   
                    self.pantalla[i].currentFrame = valor         
                
                
            else:
                print("aqui va el slider de serie de imagenes custom "+str(valor))    
                #self.settingsPantallas[self.pantallaActivaIndex][3]=valor
                #if self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'] > 1: ##esto es para saber si es una serie,cuando settingsPantallas sea un diccionario bien parido esto se escribira mejor           
                pixpath = os.path.join(self.settingsPantallas[self.pantallaActivaIndex]['path']+valorStr+".png")
                print(pixpath) 
                laImagen = QImage(pixpath) 
                try:   
                    self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(laImagen))    
                except:
                    print("no hay") 
        
    

    def ponFechaSliderCustom(self, valor):   
        if valor>9:
            valorStr = str(valor)
        else:
            valorStr = "0"+str(valor)
            
        #self.settingsPantallas[self.pantallaActivaIndex][3]=valor
        if self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'] > 1: ##esto es para saber si es una serie,cuando settingsPantallas sea un diccionario bien parido esto se escribira mejor           
            pixpath = os.path.join(self.settingsPantallas[self.pantallaActivaIndex]['path']+valorStr+".png")
            print(pixpath) 
            laImagen = QImage(pixpath) 
            try:   
                self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(laImagen))    
            except:
                print("no hay") 
            
              
    def recuperaPantalla(self):
        
        if self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'] > 1:##esto es para saber si es una serie,cuando settingsPantallas sea un diccionario bien parido esto se escribira mejor
            #self.quitaSliders()
            self.fpSlider.setValue(self.pantallaActiva.currentFp)
            self.fechaSlider.setValue(self.pantallaActiva.currentFrame)
            self.fechaSlider.setMaximum (self.settingsPantallas[self.pantallaActivaIndex]['numberOfFrames'])
            self.fechaSlider.setMinimum(1) 
            if len(self.pantallaActiva.api.paleta) > 0:
                self.setWebberPaleta(self.pantallaActivaIndex)
            
            self.sliderObservados.setVisible(True)
            self.fechaSlider.setFocus()
            
        if self.settingsPantallas[self.pantallaActivaIndex]['type']=="customVideo":
            #self.quitaSliders()
            self.controlesVideo.setVisible(True)
            

                         
       
    def activaPantalla(self,pantallaIndex):
        print(str(self.settingsPantallas[pantallaIndex]))
        self.pantallaActiva=self.pantalla[pantallaIndex]
        self.pantallaActivaIndex=pantallaIndex

        self.recuperaPantalla()
        
        self.x2.setEnabled(True if (pantallaIndex<self.numeroDePantallas-2) else False)
        self.x3.setEnabled(True if (pantallaIndex<self.numeroDePantallas-3) else False)
        self.x4.setEnabled(True if (pantallaIndex<self.numeroDePantallas-4) else False)
        
        if self.settingsPantallas[pantallaIndex]['numberOfFrames'] == 1:
            print("pantalla "+str(pantallaIndex+1)+" activa")
        else:
            print("pantalla "+str(pantallaIndex+1)+" activa en el frame " + str(self.pantallaActiva.currentFrame))
        



# turn on developer tools in webkit so we can get at the javascript console for debugging
#QWebSettings.globalSettings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

# not required, used for example javascript->python calls
import json
import event

# any QObject can be added to the javascript window object
# slots are then callable from javascript
class PythonAPI(QObject):
    
    def setEvent(self,p):
        if p==0:
            self.evt_foo = event.Event0()
        if p==1:
            self.evt_foo = event.Event1()
        if p==2:
            self.evt_foo = event.Event2()
        if p==3:
            self.evt_foo = event.Event3()
        if p==4:
            self.evt_foo = event.Event4()
        if p==5:
            self.evt_foo = event.Event5()
        
    def addSpacialSisters(self, hermanas):
        self.spatial_sisters = []
        for hermana in hermanas:
            self.spatial_sisters.append(hermana)
            
    def addTemporalSisters(self, hermanas):
        self.temporal_sisters = []
        for hermana in hermanas:
            self.temporal_sisters.append(hermana)
            
    @Slot(float, float, float, float, float)        
    def setWebberCuts(self, c1,c2,c3,c4,c5):
        self.webberCuts = [c1,c2,c3,c4,c5]
        print (str(self.webberCuts))
    
    @Slot('QStringList')     
    def setPaleta(self, paleta):
        #print (str(paleta))
        self.paleta = paleta
    
    @Slot(str)     
    def setBorde(self,borde):
        self.borde = borde
    
    @Slot(float)        
    def setMaximum(self, m):
        self.maximo = m
        
    @Slot(int)        
    def setNumberOfFrames(self, n):
        self.numberOfFrames = n
        self.evt_foo(self)
            
    @Slot(float, float)        
    def rePanSisters(self, x,y):
        for sister in self.spatial_sisters:
            sister.evaluateJavaScript("rePan("+str(x)+","+str(y)+");")   
                 
    
    @Slot(float)        
    def reZoomSisters(self, res):
        for sister in self.spatial_sisters:
            sister.evaluateJavaScript("reZoom("+str(res)+");")
    # take two integers and return an integer
    @Slot(int, int, result=int)
    def add(self, a, b):
        return a + b

    # take a list of strings and return a string
    # because of setapi line above, we get a list of python strings as input
    @Slot('QStringList', result=str)
    def concat(self, strlist):
        return ''.join(strlist)

    # take a javascript object and return string
    # javascript objects come into python as dictionaries
    # functions are represented by an empty dictionary
    @Slot('QVariantMap', result=str)
    def json_encode(self, jsobj):
        # import is here to keep it separate from 'required' import
        return json.dumps(jsobj)

    # take a string and return an object (which is represented in python
    # by a dictionary
    @Slot(str, result='QVariantMap')
    def json_decode(self, jsstr):
        return json.loads(jsstr)
    
class Wind(QMainWindow, ventanitaPro.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Wind, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint);
        self.video_widget=None
        self.view = QWebEngineView(self)
        self.api = PythonAPI()
        self.currentFrame = 1
        self.currentFp = 1.0
        
        
    def setWebKit(self, url):
        #print("estoy intentando abrir una pagina web")
        #self.titleFrame.setVisible(False)
        #self.graphFrame.setVisible(False)
        #self.fotosFrame.setVisible(False)
        #cualUrl = 
        self.view = QWebEngineView(self)
        #self.view.settings().setAttribute(QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
        self.api = PythonAPI()
        self.currentFrame = 1
        self.currentFp = 1.0
        self.view.setGeometry(0,0,1920,1080)
        #self.view.load(QtCore.QUrl('http://localhost/~fidel/testMegadapt2.html'))
        self.view.load(QtCore.QUrl(url))
        self.view.show()
        self.view.setFocus()
        
        self.webFrame = self.view.page().mainFrame()
        
        self.webFrame.javaScriptWindowObjectCleared.connect(self.load_api)
        
        self.show()
        
        #self.webFrame.javaScriptWindowObjectCleared.connect(self.setopea)
        

        self.webFrame.loadFinished.connect(self.setopea)
        #self.pushButton.clicked.connect(self.call_js)
    def setSimpleWebKit(self, url):
        self.view = QWebEngineView(self)  
        #self.view.settings().setAttribute(QWebSettings.WebAttribute.DeveloperExtrasEnabled, True)
        self.view.setGeometry(0,0,1920,1080)  
        self.view.load(QtCore.QUrl(url))
        self.view.show()
        self.view.setFocus()
        self.show()
        
    def setopea(self):
        self.webFrame.evaluateJavaScript("setup();")
        
        
        
    def load_api(self):
        # add pyapi to javascript window object
        # slots can be accessed in either of the following ways -
        #   1.  var obj = window.pyapi.json_decode(json);
        #   2.  var obj = pyapi.json_decode(json)
        self.webFrame.addToJavaScriptWindowObject('pyapi', self.api)
        self.api.spatial_sisters = []
        self.api.temporal_sisters = []
 

        
        
app = QApplication(sys.argv)
form = Ui_MainWindow()
form.ensamblaPantallas(1)
form.show()

# form2.show()
app.exec_()