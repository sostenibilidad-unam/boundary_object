# -*- encoding: utf-8 -*-
from pprint import pprint
from PySide.QtCore import *
from PySide.QtCore import Qt
from PySide.QtGui import *
#from PySide import QtWebKit
import csv
import sys
import json

#=SI(IZQUIERDA(E2;1)="9";CONCATENAR("0";E2);E2)
import controlador
import dialog
import os
from os.path import isfile
import csv
import math
from PySide.phonon import Phonon
import time
import itertools




#pyside-uic.exe -o controlador.py controlador.ui
#pyside-uic.exe -o dialog.py dialog.ui


class tiempoItem(QStandardItem):
    def __init__(self, parent=None):
        super(tiempoItem, self).__init__(parent)
        self.arrayDeSettings=[]
    def setArrayDeSettings(self,settings):
        self.arrayDeSettings=[]
        for row in settings:
            self.arrayDeSettings.append(row[:])
            
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
        
        self.CarpetaMapas="Z:/PlataformaAbril/"
        
       
        self.pantalla=0
        self.settingsPantallas=[]
        self.settingsPantallas.append([None,None,None,1])
        self.settingsPantallas.append([None,None,None,1])
        self.settingsPantallas.append([None,None,None,1])
        self.settingsPantallas.append([None,None,None,1])
        self.settingsPantallas.append([None,None,None,1])
        self.settingsPantallas.append([None,None,None,1])
        
       
        self.fechaSlider.valueChanged.connect(self.ponFecha)
        
        self.Pantalla1 = Wind() 
        self.Pantalla1.video_widget=None
        self.Pantalla1.setGeometry(1931,13,1904,1055)
        self.Pantalla1.show()
        self.Pantalla2 = Wind() 
        self.Pantalla2.video_widget=None
        self.Pantalla2.setGeometry(3851,13,1904,1055)   
        self.Pantalla2.show()
        self.Pantalla3 = Wind() 
        self.Pantalla3.video_widget=None
        self.Pantalla3.setGeometry(5771,13,1904,1055)      
        self.Pantalla3.show()
        self.Pantalla4 = Wind() 
        self.Pantalla4.video_widget=None
        self.Pantalla4.setGeometry(7691,13,1904,1055)     
        self.Pantalla4.show()
        self.Pantalla5 = Wind() 
        self.Pantalla5.video_widget=None
        self.Pantalla5.setGeometry(9611,13,1904,1055)     
        self.Pantalla5.show()
        self.Pantalla6 = Wind() 
        self.Pantalla6.video_widget=None
        self.Pantalla6.setGeometry(11531,13,1904,1055)     
        self.Pantalla6.show()
        self.pantalla1Componente=None
        self.pantalla1Elemento=None
        self.pantalla1Slider=None
        self.pantalla2Componente=None
        self.pantalla2Elemento=None
        self.pantalla2Slider=None
        self.pantalla3Componente=None
        self.pantalla3Elemento=None
        self.pantalla3Slider=None
        
        self.pantallaActiva=self.Pantalla1
        
        self.P1.clicked.connect(self.activaPantalla1)
        self.P2.clicked.connect(self.activaPantalla2)
        self.P3.clicked.connect(self.activaPantalla3)
        self.P4.clicked.connect(self.activaPantalla4)
        self.P5.clicked.connect(self.activaPantalla5)
        self.P6.clicked.connect(self.activaPantalla6)
        
        
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
        self.x1.clicked.connect(self.pantallaX1)
        self.x2.clicked.connect(self.pantallaX2)
        self.x3.clicked.connect(self.pantallaX3)
        self.x4.clicked.connect(self.pantallaX4)
        
        
        
        self.play.clicked.connect(self.hasPlay)
        self.stop.clicked.connect(self.hasStop)
        self.pause.clicked.connect(self.hasPause)
        #self.loop.clicked.connect(self.pantallaX4)
        
        self.playGuion.setEnabled(False)
        self.stopGuion.setEnabled(False)
        
        self.playGuion.clicked.connect(self.playGuionConDelay)
        self.stopGuion.clicked.connect(self.stopGuionConDelay)
    
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
    def pantallaX1(self):
        print("x1")
        elPunto = self.pantallaActiva.pos()
        if str(self.settingsPantallas[self.pantalla][2]).isdigit():
            self.settingsPantallas[self.pantalla][2]=1 
        self.pantallaActiva.setGeometry(elPunto.x()+8,13,1904,1055)   
        if self.pantalla==0:
            self.Pantalla2.show() 
        if self.pantalla==1:
            self.Pantalla3.show() 
        if self.pantalla==2:
            self.Pantalla4.show() 
        if self.pantalla==3:
            self.Pantalla5.show() 
        if self.pantalla==4:
            self.Pantalla6.show() 
        
    def pantallaX2(self):
        print("x2")
        elPunto = self.pantallaActiva.pos()
        #if str(self.settingsPantallas[self.pantalla][2]).isdigit():
        self.settingsPantallas[self.pantalla][2]=2
        self.pantallaActiva.setGeometry(elPunto.x()+8,13,3820,1055) 
        largo=3820
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False)
        if self.pantalla==0:
            self.Pantalla2.hide()
            self.settingsPantallas[1][0]=None
            print("ocultando la pantalla 2")
            self.Pantalla3.show()
        if self.pantalla==1:
            self.Pantalla3.hide()
            self.settingsPantallas[2][0]=None
            self.Pantalla4.show()
        if self.pantalla==2:
            self.Pantalla4.hide()
            self.settingsPantallas[3][0]=None
            self.Pantalla5.show()
        if self.pantalla==3:
            self.Pantalla5.hide()
            self.settingsPantallas[4][0]=None
            self.Pantalla6.show()
        if self.pantalla==4:
            self.Pantalla6.hide()
            self.settingsPantallas[5][0]=None
          
        
    def pantallaX3(self):
        print("x3")
        elPunto = self.pantallaActiva.pos()
        self.settingsPantallas[self.pantalla][2]=3
        self.pantallaActiva.setGeometry(elPunto.x()+8,13,5740,1055) 
        largo=5740
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False) 
        if self.pantalla==0:
            self.Pantalla2.hide()
            self.Pantalla3.hide()
            self.settingsPantallas[1][0]=None
            self.settingsPantallas[2][0]=None
            self.Pantalla4.show()
        if self.pantalla==1:
            self.Pantalla3.hide()
            self.Pantalla4.hide()
            self.settingsPantallas[2][0]=None
            self.settingsPantallas[3][0]=None
            self.Pantalla5.show()
        if self.pantalla==2:
            self.Pantalla4.hide()
            self.Pantalla5.hide()
            self.settingsPantallas[3][0]=None
            self.settingsPantallas[4][0]=None
            self.Pantalla6.show()
        if self.pantalla==3:
            self.Pantalla5.hide()
            self.Pantalla6.hide()
            self.settingsPantallas[4][0]=None
            self.settingsPantallas[5][0]=None
        
        
    def pantallaX4(self):
        print("x4")
        elPunto = self.pantallaActiva.pos()
        self.settingsPantallas[self.pantalla][2]=4
        self.pantallaActiva.setGeometry(elPunto.x()+8,13,7660,1055)  
        largo=7660
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False)
        if self.pantalla==0:
            self.Pantalla2.hide()
            self.Pantalla3.hide()
            self.Pantalla4.hide()
            self.settingsPantallas[1][0]=None
            self.settingsPantallas[2][0]=None
            self.settingsPantallas[3][0]=None
            self.Pantalla5.show()
        if self.pantalla==1:
            self.Pantalla3.hide()
            self.Pantalla4.hide()
            self.Pantalla5.hide()
            self.settingsPantallas[2][0]=None
            self.settingsPantallas[3][0]=None
            self.settingsPantallas[4][0]=None
            self.Pantalla6.show()
        if self.pantalla==2:
            self.Pantalla4.hide()
            self.Pantalla5.hide()
            self.Pantalla6.hide()
            self.settingsPantallas[3][0]=None
            self.settingsPantallas[4][0]=None
            self.settingsPantallas[5][0]=None
        
        
    def pantallasX1(self):
        print("todas x1")
        self.settingsPantallas[0][2]=1
        self.settingsPantallas[1][2]=1
        self.settingsPantallas[2][2]=1
        self.settingsPantallas[3][2]=1
        self.settingsPantallas[4][2]=1
        self.settingsPantallas[5][2]=1
        
        self.Pantalla1.setGeometry(1931,13,1904,1055)
        self.Pantalla1.show()
        self.Pantalla2.setGeometry(3851,13,1904,1055)   
        self.Pantalla2.show()
        self.Pantalla3.setGeometry(5771,13,1904,1055)      
        self.Pantalla3.show()
        self.Pantalla4.setGeometry(7691,13,1904,1055)     
        self.Pantalla4.show()
        self.Pantalla5.setGeometry(9611,13,1904,1055)     
        self.Pantalla5.show()
        self.Pantalla6.setGeometry(11531,13,1904,1055) 
        self.Pantalla5.show() 
    def agregaSerie(self):
        print("aqui agregare una serie de imagenes") 
        imageSerie, _ = QFileDialog.getOpenFileNames(self, 'Selecciona serie de imágenes') 
        
        prefijo=imageSerie[0].split(".")[0][:-2]
        print(prefijo,len(imageSerie))
        image0 = imageSerie[0]
        estaImagen = QImage(image0) 
        largo=1904
        if self.settingsPantallas[self.pantalla][2]==None:
            self.settingsPantallas[self.pantalla][2]=1
        multiplicador = self.settingsPantallas[self.pantalla][2]
        if multiplicador==2:
            largo = 3820
        if multiplicador==3:
            largo = 5740
        if multiplicador==4:
            largo = 7660
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False)
        self.settingsPantallas[self.pantalla][0]=len(imageSerie)
        self.settingsPantallas[self.pantalla][1]=prefijo
        self.settingsPantallas[self.pantalla][2]=multiplicador
        self.settingsPantallas[self.pantalla][3]=1
        self.fechaSlider.setMaximum(len(imageSerie))
        self.sliderObservados.setVisible(True)
        
        self.fechaSlider.setFocus()
        try:   
            if self.pantallaActiva.video_widget:     
                size = self.pantallaActiva.video_widget.size()
                self.pantallaActiva.video_widget.resize(0, 0)
            self.pantallaActiva.mapFrame.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
        
    def agregaCustomImage(self):
        customImage, _ = QFileDialog.getOpenFileName(self, 'Cargar imagen')
        estaImagen = QImage(customImage) 
        largo=1904
        if self.settingsPantallas[self.pantalla][2]==None:
            self.settingsPantallas[self.pantalla][2]=1
        multiplicador = self.settingsPantallas[self.pantalla][2]
        
        if multiplicador==2:
            largo = 3820
        if multiplicador==3:
            largo = 5740
        if multiplicador==4:
            largo = 7660
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False)
        self.settingsPantallas[self.pantalla][0]="customImage"
        self.settingsPantallas[self.pantalla][1]=customImage
        self.settingsPantallas[self.pantalla][2]=multiplicador
        try:   
            if self.pantallaActiva.video_widget:
                              
                size = self.pantallaActiva.video_widget.size()
                self.pantallaActiva.video_widget.resize(0, 0)
            self.pantallaActiva.mapFrame.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
    def agregaCustomVideo(self):
        largo=1904
        if self.settingsPantallas[self.pantalla][2]==None:
            self.settingsPantallas[self.pantalla][2]=1
        multiplicador = self.settingsPantallas[self.pantalla][2]
        if multiplicador==2:
            largo = 3820
        if multiplicador==3:
            largo = 5740
        if multiplicador==4:
            largo = 7660
        customVideo, _ = QFileDialog.getOpenFileName(self, 'Cargar video')
        self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
        self.pantallaActiva.titleFrame.setVisible(False)
        self.pantallaActiva.graphFrame.setVisible(False)
        self.pantallaActiva.fotosFrame.setVisible(False)
        #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
        
        
        
        self.controlesVideo.setVisible(True)
        #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
        
        media_src = Phonon.MediaSource(customVideo)
        self.pantallaActiva.media_obj = Phonon.MediaObject(self.pantallaActiva.frame)
        self.pantallaActiva.media_obj.setCurrentSource(media_src)
        
        self.pantallaActiva.video_widget = Phonon.VideoWidget(self.pantallaActiva.frame)
   
        self.pantallaActiva.video_widget.setGeometry(0,0,largo,1050)
        Phonon.createPath(self.pantallaActiva.media_obj, self.pantallaActiva.video_widget)
        
        audio_out = Phonon.AudioOutput(Phonon.VideoCategory)
        Phonon.createPath(self.pantallaActiva.media_obj, audio_out)
        
      
        self.pantallaActiva.video_widget.show()
        

        self.pantallaActiva.media_obj.play()
        
        
        self.settingsPantallas[self.pantalla][0]="customVideo"
        self.settingsPantallas[self.pantalla][1]=customVideo
        self.settingsPantallas[self.pantalla][2]=multiplicador
        

               
        
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
        for tiempo in self.elGuion:
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
        arrayDeArays = []
        for item in losItems:
            arrayDeArays.append(item.arrayDeSettings)
            
        proyectoFile.write(json.dumps(arrayDeArays, sort_keys=True))
     
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
        estabaEnLaPantalla = self.pantalla
        for panta in range(0,6):
            
            print("pantalla "+str(panta+1))
            if panta == 0:
                self.pantallaActiva=self.Pantalla1
            if panta == 1:
                self.pantallaActiva=self.Pantalla2
            if panta == 2:
                self.pantallaActiva=self.Pantalla3
            if panta == 3:
                self.pantallaActiva=self.Pantalla4
            if panta == 4:
                self.pantallaActiva=self.Pantalla5
            if panta == 5:
                self.pantallaActiva=self.Pantalla6
                
            self.pantalla = panta
            
            
            if ("custom" in str(self.settingsPantallas[self.pantalla][0])) or (str(self.settingsPantallas[self.pantalla][0]).isdigit()):
                if str(self.settingsPantallas[self.pantalla][0]).isdigit():
                    print("serie")
                    print(str(self.settingsPantallas[self.pantalla]))
                    
                    
                    
                    print("poniendo el slider en "+ str(self.settingsPantallas[self.pantalla][3]))
                    
                    self.sliderObservados.setVisible(True)
                    self.fechaSlider.setFocus()
                    largo = 1904
                    if self.settingsPantallas[self.pantalla][2]==2:
                        largo = 3820
                        self.pantallaX2()
                    if self.settingsPantallas[self.pantalla][2]==3:
                        largo = 5740
                        self.pantallaX3()
                    if self.settingsPantallas[self.pantalla][2]==4:
                        largo = 7660 
                        self.pantallaX4()  
                    if largo == 1904:
                        self.pantallaX1()
                    self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
                    self.pantallaActiva.titleFrame.setVisible(False)
                    self.pantallaActiva.graphFrame.setVisible(False)
                    self.pantallaActiva.fotosFrame.setVisible(False)
                    #self.fechaSlider.setValue(self.settingsPantallas[self.pantalla][3])
                    #self.ponFecha(self.settingsPantallas[self.pantalla][3])
                    #self.fechaSlider.setValue(self.settingsPantallas[self.pantalla][3])
                    if self.pantallaActiva.video_widget:     
                        size = self.pantallaActiva.video_widget.size()
                        self.pantallaActiva.video_widget.resize(0, 0)
                        
                    print(str(self.settingsPantallas[self.pantalla]))
                    #self.fechaSlider.setMaximum(self.settingsPantallas[self.pantalla][0])
                    self.ponFecha(self.settingsPantallas[self.pantalla][3])
                    
                if self.settingsPantallas[self.pantalla][0]=="customVideo":
                    largo = 1904
                    if self.settingsPantallas[self.pantalla][2]==2:
                        largo = 3820
                        self.pantallaX2()
                    if self.settingsPantallas[self.pantalla][2]==3:
                        largo = 5740
                        self.pantallaX3()
                    if self.settingsPantallas[self.pantalla][2]==4:
                        largo = 7660 
                        self.pantallaX4()  
                    if largo == 1904:
                        self.pantallaX1()
                    self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
                    self.pantallaActiva.titleFrame.setVisible(False)
                    self.pantallaActiva.graphFrame.setVisible(False)
                    self.pantallaActiva.fotosFrame.setVisible(False)
                    
                    self.controlesVideo.setVisible(True)
                    #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
                    customVideo= self.settingsPantallas[self.pantalla][1]
                    media_src = Phonon.MediaSource(customVideo)
                    self.pantallaActiva.media_obj = Phonon.MediaObject(self.pantallaActiva.frame)
                    self.pantallaActiva.media_obj.setCurrentSource(media_src)
                    
                    self.pantallaActiva.video_widget = Phonon.VideoWidget(self.pantallaActiva.frame)
               
                    self.pantallaActiva.video_widget.setGeometry(0,0,largo,1050)
                    Phonon.createPath(self.pantallaActiva.media_obj, self.pantallaActiva.video_widget)
                    
                    audio_out = Phonon.AudioOutput(Phonon.VideoCategory)
                    Phonon.createPath(self.pantallaActiva.media_obj, audio_out)
                    
                    self.pantallaActiva.video_widget.show()
                    self.pantallaActiva.media_obj.play()
                
                
                if self.settingsPantallas[self.pantalla][0]=="customImage":
                    print("aqui se agrega una imagen custom")
                    customImage= self.settingsPantallas[self.pantalla][1]
                    estaImagen = QImage(customImage) 
                    largo = 1904
                    if self.settingsPantallas[self.pantalla][2]==2:
                        largo = 3820
                        self.pantallaX2()
                    if self.settingsPantallas[self.pantalla][2]==3:
                        largo = 5740
                        self.pantallaX3()
                    if self.settingsPantallas[self.pantalla][2]==4:
                        largo = 7660  
                        self.pantallaX4() 
                        
                    if largo == 1904:
                        self.pantallaX1()
                    self.pantallaActiva.frame.setGeometry(0,0,largo,1050)
                    self.pantallaActiva.mapFrame.setGeometry(0,0,largo,1050)
                    self.pantallaActiva.titleFrame.setVisible(False)
                    self.pantallaActiva.graphFrame.setVisible(False)
                    self.pantallaActiva.fotosFrame.setVisible(False)
                    
                    try: 
                        if self.pantallaActiva.video_widget:
                              
                            size = self.pantallaActiva.video_widget.size()
                            self.pantallaActiva.video_widget.resize(0, 0)
                            #self.pantallaActiva.video_widget.resize(size)
                        self.pantallaActiva.mapFrame.setPixmap(QPixmap.fromImage(estaImagen)) 
                    
                    except:
                        print("no pude") 
            else:
                print("no es nada") 
        if estabaEnLaPantalla == 0:
            self.pantallaActiva=self.Pantalla1
        if estabaEnLaPantalla == 1:
            self.pantallaActiva=self.Pantalla2
        if estabaEnLaPantalla == 2:
            self.pantallaActiva=self.Pantalla3
        if estabaEnLaPantalla == 3:
            self.pantallaActiva=self.Pantalla4
        if estabaEnLaPantalla == 4:
            self.pantallaActiva=self.Pantalla5
        if estabaEnLaPantalla == 5:
            self.pantallaActiva=self.Pantalla6
                    
        self.pantalla = estabaEnLaPantalla

        
        
    def guardaPantallasEnArchivo(self):
        
        
            
        pixpathFoto = os.path.join(self.CarpetaMapas,"inocuidad/screens30.png")
        
        elIcon = QImage(pixpathFoto) 

        
        
        
        textual_item = tiempoItem() 
        textual_item.setData(elIcon,Qt.DecorationRole)  
        textual_item.setArrayDeSettings(self.settingsPantallas[:]) 
        #textual_item = QStandardItem('Item text'+str(self.contador))    
        self.model.appendRow(textual_item)
        print(str(self.model.item(0).getArrayDeSettings()))
        self.contador+=1
        
        #self.listView.show()
        

        


    def ponFecha(self,valor):
        if str(self.settingsPantallas[self.pantalla][0]).isdigit():
            print("aqui va el slider de serie de imagenes custom"+str(valor))
            self.ponFechaSliderCustom(valor)
        
    def ponFechaSlider(self, valor):

        
        if valor>9:
            valorStr = str(valor)
        else:
            valorStr = "0"+str(valor)
        
        self.settingsPantallas[self.pantalla][3]=valor
        
        if self.settingsPantallas[self.pantalla][0]=="Derrame":
            pixpath = os.path.join(self.CarpetaMapas,"fase_aguda/superficial_muestreo/M_SUP_M_"+self.settingsPantallas[self.pantalla][2]+valorStr+".png")
            print(pixpath) 
            pixpathGraph = os.path.join(self.CarpetaMapas,"fase_aguda/superficial_muestreo/G_SUP_M_"+self.settingsPantallas[self.pantalla][2]+valorStr+".png")
            pixpathGraph2 = os.path.join(self.CarpetaMapas,"fase_aguda/superficial_muestreo/G_SOL_M_"+self.settingsPantallas[self.pantalla][2]+valorStr+".png")
            
            
            
            elMapa = QImage(pixpath) 
            laGrafica = QImage(pixpathGraph) 
            laGrafica2 = QImage(pixpathGraph2) 
    #         elPixOverlay = QImage(pixpath)
    #         painter = QPainter()
    #         painter.begin(elPixBase) 
    #         painter.drawImage(10, 0, elPixOverlay)
    #         painter.end() 
            try:   
                self.pantallaActiva.fotosFrame.setVisible(True)
                self.pantallaActiva.graphFrame.setVisible(True)
                self.pantallaActiva.mapFrame.setPixmap(QPixmap.fromImage(elMapa))
                self.pantallaActiva.graphFrame.setPixmap(QPixmap.fromImage(laGrafica))  
                self.pantallaActiva.fotosFrame.setPixmap(QPixmap.fromImage(laGrafica2)) 
            except:
                print("no hay") 
        
            self.ponTitulo()


    def ponFechaSliderCustom(self, valor):   
        
        if valor>9:
            valorStr = str(valor)
        else:
            valorStr = "0"+str(valor)
        
        self.settingsPantallas[self.pantalla][3]=valor
        
        if str(self.settingsPantallas[self.pantalla][0]).isdigit():
            
            pixpath = os.path.join(self.settingsPantallas[self.pantalla][1]+valorStr+".png")
            print(pixpath) 
           
            

            laImagen = QImage(pixpath) 
            
            
   
            try:   
                
                self.pantallaActiva.mapFrame.setPixmap(QPixmap.fromImage(laImagen))
                 
                
            except:
                    print("no hay") 
            
              
    def recuperaPantalla(self):###################################################################################### aqui falta poner todos los componentes
        print(str(self.settingsPantallas))
        if str(self.settingsPantallas[self.pantalla][0]).isdigit():
            self.quitaSliders()
            
            self.sliderObservados.setVisible(True)
            self.fechaSlider.setFocus()
            
        if self.settingsPantallas[self.pantalla][0]=="customVideo":
            self.quitaSliders()
            self.controlesVideo.setVisible(True)
            

                         
       
    def activaPantalla1(self):
        self.pantallaActiva=self.Pantalla1
        self.pantalla=0

        self.recuperaPantalla()
        self.x2.setEnabled(True)
        self.x3.setEnabled(True)
        self.x4.setEnabled(True)
            
        print("pantalla 1 activa")
        
            
    def activaPantalla2(self):
        self.pantallaActiva=self.Pantalla2
        self.pantalla=1
        
        self.recuperaPantalla()
        self.x2.setEnabled(True)
        self.x3.setEnabled(True)
        self.x4.setEnabled(True)
        print("pantalla 2 activa")        
        
    def activaPantalla3(self):
        self.pantallaActiva=self.Pantalla3
        self.pantalla=2
        
        self.recuperaPantalla()
        self.x2.setEnabled(True)
        self.x3.setEnabled(True)
        self.x4.setEnabled(True)
        
        print("pantalla 3 activa")     
        
    def activaPantalla4(self):
        self.pantallaActiva=self.Pantalla4
        self.pantalla=3
        
        self.recuperaPantalla()
        self.x2.setEnabled(True)
        self.x3.setEnabled(True)
        self.x4.setEnabled(False)
        print("pantalla 4 activa")     
        
    def activaPantalla5(self):
        self.pantallaActiva=self.Pantalla5
        self.pantalla=4
        
        self.recuperaPantalla()
        self.x2.setEnabled(True)
        self.x4.setEnabled(False)
        self.x3.setEnabled(False)
        print("pantalla 5 activa")     
        
    def activaPantalla6(self):
        self.pantallaActiva=self.Pantalla6
        self.pantalla=5
        
        self.recuperaPantalla()
        self.x4.setEnabled(False)
        self.x3.setEnabled(False)
        self.x2.setEnabled(False)
        print("pantalla 6 activa")     
    
        

class Wind(QWidget, dialog.Ui_Dialog):
    def __init__(self, parent=None):
        super(Wind, self).__init__(parent)
        self.setupUi(self)
        #self.mapFrame.clicked.connect(self.getPos)
        
       
    


        
        
app = QApplication(sys.argv)
form = Ui_MainWindow()
form.show()

# form2.show()
app.exec_()