# -*- encoding: utf-8 -*-
from pprint import pprint
from PySide.QtCore import *
from PySide.QtCore import Qt
from PySide.QtGui import *
from PySide import QtWebKit, QtCore, QtGui
from PySide.QtCore import QObject, QUrl, Slot
import csv
import sys
import json

#=SI(IZQUIERDA(E2;1)="9";CONCATENAR("0";E2);E2)
import controlador
import ventanitaPro 
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
        self.pantallaActivaIndex=0
        self.fechaSlider.valueChanged.connect(self.ponFecha)
        
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
        
        
    def setSpaceSisters(self):
        print "vinculando pantallas " + self.hermanasDeEspacio.text() + " espacialmente"
        listaDeHermanas = self.hermanasDeEspacio.text().split(",")
        for hermana in listaDeHermanas:
            self.settingsPantallas[int(hermana)-1][4] = []
            for sister in listaDeHermanas:
                if not sister == hermana:
                    self.settingsPantallas[int(hermana)-1][4].append(int(sister)-1)
                    
        for hermana in listaDeHermanas:
            susHermanasEnNumero = self.settingsPantallas[int(hermana)-1][4]
            susHermanas = []
            for hermanaNumero in susHermanasEnNumero:
                susHermanas.append(self.pantalla[hermanaNumero].webFrame)
                
            self.pantalla[int(hermana)-1].api.addSisters(susHermanas)
        
                    
        
        
        print self.settingsPantallas
    
    
    def setTimeSisters(self):
        print "vinculando pantallas " + self.hermanasDeTiempo.text() + " temporalmente"
        
    
    def removeSpaceSisterhood(self):
        self.hermanasDeEspacio.setText("")
        print "desvinculando pantallas"
        for i in range(0, self.numeroDePantallas):
            self.pantalla[i].api.sisters = []
            self.settingsPantallas[i][4] = []
    
    def removeTimeSisterhood(self):
        self.hermanasDeTiempo.setText("")
        print "desvinculando pantallas"
    
    
    def ponGeometria(self,p,offsetX,offsetY):
        self.pantalla[p].setGeometry(1920+(p*1920)+offsetX,offsetY,1920,1080)
        
    def ensamblaPantallas(self, numeroDePantallas):
        self.numeroDePantallas=numeroDePantallas
        self.pantalla=[]
        self.settingsPantallas=[]
        for p in range(0,numeroDePantallas):
            self.settingsPantallas.append([None,None,None,1,[],[]])
            self.pantalla.append(Wind())
            self.ponGeometria(p,11,13)
            self.pantalla[p].show()
        
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
        self.settingsPantallas[self.pantallaActivaIndex][2]=multiplicador
        largo = 1920 * multiplicador
        self.pantallaActiva.setGeometry(elPunto.x()+8,13,largo,1080) 
        self.pantallaActiva.imageCanvas.setGeometry(0,0,largo,1080) 
        
        if multiplicador>1:
        
            for i in range(self.pantallaActivaIndex+1,self.pantallaActivaIndex+multiplicador):
                self.pantalla[i].hide()
                self.settingsPantallas[i][0]=None
        
        self.pantallaActiva.show()
        
          
        
  
       
        
    def pantallasX1(self):
        print("todas x1")
        for p in range(0,self.numeroDePantallas):
            self.settingsPantallas[p][2]=1
            self.pantalla[p].ponGeometria(p)
            self.pantalla[p].show() 
       
    def agregaSerie(self):
        print("aqui agregare una serie de imagenes") 
        imageSerie, _ = QFileDialog.getOpenFileNames(self, 'Selecciona serie de imágenes') 
        
        prefijo=imageSerie[0].split(".")[0][:-2]
        print(prefijo,len(imageSerie))
        image0 = imageSerie[0]
        estaImagen = QImage(image0) 
        
        if self.settingsPantallas[self.pantallaActivaIndex][2]==None:
            self.settingsPantallas[self.pantallaActivaIndex][2]=1
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex][2]
        self.extiendePantalla(multiplicador)
        self.settingsPantallas[self.pantallaActivaIndex][0]=len(imageSerie)
        self.settingsPantallas[self.pantallaActivaIndex][1]=prefijo
        self.settingsPantallas[self.pantallaActivaIndex][2]=multiplicador
        self.settingsPantallas[self.pantallaActivaIndex][3]=1
        self.fechaSlider.setMaximum(len(imageSerie))
        self.sliderObservados.setVisible(True)
        
        self.fechaSlider.setFocus()
        try:   
            if self.pantallaActiva.video_widget:     
                size = self.pantallaActiva.video_widget.size()
                self.pantallaActiva.video_widget.resize(0, 0)
            self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
        
    def agregaCustomImage(self):
        customImage, _ = QFileDialog.getOpenFileName(self, 'Cargar imagen')
        estaImagen = QImage(customImage) 
    
        if self.settingsPantallas[self.pantallaActivaIndex][2]==None:
            self.settingsPantallas[self.pantallaActivaIndex][2]=1
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex][2]
        self.extiendePantalla(multiplicador) 
        
        
        self.settingsPantallas[self.pantallaActivaIndex][0]="customImage"
        self.settingsPantallas[self.pantallaActivaIndex][1]=customImage
        self.settingsPantallas[self.pantallaActivaIndex][2]=multiplicador
        try:   
            if self.pantallaActiva.video_widget:
                self.pantallaActiva.video_widget.resize(0, 0)
            self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
        
        except:
            print("no pude") 
        
    def agregaCustomVideo(self):
        
        if self.settingsPantallas[self.pantallaActivaIndex][2]==None:
            self.settingsPantallas[self.pantallaActivaIndex][2]=1
        
        multiplicador = self.settingsPantallas[self.pantallaActivaIndex][2]
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
        
        
        self.settingsPantallas[self.pantallaActivaIndex][0]="customVideo"
        self.settingsPantallas[self.pantallaActivaIndex][1]=customVideo
        self.settingsPantallas[self.pantallaActivaIndex][2]=multiplicador
        

    def agregaSerieWeb(self):
        pass        
    
    def agregaWeb(self):
        self.pantallaActiva.setWebKit()
        
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
        estabaEnLaPantalla = self.pantallaActivaIndex
        for p in range(0,self.numeroDePantallas):
            
            self.pantallaActiva=self.pantalla[p]   
            self.pantallaActivaIndex = p
            
            
            if ("custom" in str(self.settingsPantallas[self.pantallaActivaIndex][0])) or (str(self.settingsPantallas[self.pantallaActivaIndex][0]).isdigit()):
                if str(self.settingsPantallas[self.pantallaActivaIndex][0]).isdigit():
                    print("serie")
                    print(str(self.settingsPantallas[self.pantallaActivaIndex]))
                    
                    
                    
                    print("poniendo el slider en "+ str(self.settingsPantallas[self.pantallaActivaIndex][3]))
                    
                    self.sliderObservados.setVisible(True)
                    self.fechaSlider.setFocus()
                    
                    self.extiendePantalla(self.settingsPantallas[self.pantallaActivaIndex][2])

                    if self.pantallaActiva.video_widget:     
                        self.pantallaActiva.video_widget.resize(0, 0)
                        
                    print(str(self.settingsPantallas[self.pantallaActivaIndex]))
                    #self.fechaSlider.setMaximum(self.settingsPantallas[self.pantallaActivaIndex][0])
                    self.ponFecha(self.settingsPantallas[self.pantallaActivaIndex][3])
                    
                if self.settingsPantallas[self.pantallaActivaIndex][0]=="customVideo":
                    largo = self.settingsPantallas[self.pantallaActivaIndex][2]*1920
                    self.extiendePantalla(self.settingsPantallas[self.pantallaActivaIndex][2])
                    
                    
                    self.pantallaActiva.frame.setGeometry(0,0,largo,1080)
                    
                    self.controlesVideo.setVisible(True)
                    #self.pantallaActiva.mapFrame.setGeometry(0,0,1900,1050)
                    customVideo= self.settingsPantallas[self.pantallaActivaIndex][1]
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
                
                
                if self.settingsPantallas[self.pantallaActivaIndex][0]=="customImage":
                    print("aqui se agrega una imagen custom")
                    customImage= self.settingsPantallas[self.pantallaActivaIndex][1]
                    estaImagen = QImage(customImage)
                    multiplicador = self.settingsPantallas[self.pantallaActivaIndex][2]
                    
                    self.extiendePantalla(multiplicador)
                
                    
                    try: 
                        if self.pantallaActiva.video_widget:
                              
                            size = self.pantallaActiva.video_widget.size()
                            self.pantallaActiva.video_widget.resize(0, 0)
                            #self.pantallaActiva.video_widget.resize(size)
                        self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(estaImagen)) 
                    
                    except:
                        print("no pude") 
            else:
                print("no es nada") 
                
        self.pantallaActiva=self.pantalla[estabaEnLaPantalla]              
        self.pantallaActivaIndex = estabaEnLaPantalla

        
        
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
        if str(self.settingsPantallas[self.pantallaActivaIndex][0]).isdigit():
            print("aqui va el slider de serie de imagenes custom"+str(valor))
            self.ponFechaSliderCustom(valor)
        
    

    def ponFechaSliderCustom(self, valor):   
        
        if valor>9:
            valorStr = str(valor)
        else:
            valorStr = "0"+str(valor)
        
        self.settingsPantallas[self.pantallaActivaIndex][3]=valor
        
        if str(self.settingsPantallas[self.pantallaActivaIndex][0]).isdigit():
            
            pixpath = os.path.join(self.settingsPantallas[self.pantallaActivaIndex][1]+valorStr+".png")
            print(pixpath) 
           
            

            laImagen = QImage(pixpath) 
            
            
   
            try:   
                
                self.pantallaActiva.imageCanvas.setPixmap(QPixmap.fromImage(laImagen))
                 
                
            except:
                    print("no hay") 
            
              
    def recuperaPantalla(self):###################################################################################### aqui falta poner todos los componentes
        print(str(self.settingsPantallas))
        if str(self.settingsPantallas[self.pantallaActivaIndex][0]).isdigit():
            self.quitaSliders()
            
            self.sliderObservados.setVisible(True)
            self.fechaSlider.setFocus()
            
        if self.settingsPantallas[self.pantallaActivaIndex][0]=="customVideo":
            self.quitaSliders()
            self.controlesVideo.setVisible(True)
            

                         
       
    def activaPantalla(self,pantallaIndex):
        self.pantallaActiva=self.pantalla[pantallaIndex]
        self.pantallaActivaIndex=pantallaIndex

        self.recuperaPantalla()
        
        self.x2.setEnabled(True if (pantallaIndex<self.numeroDePantallas-2) else False)
        self.x3.setEnabled(True if (pantallaIndex<self.numeroDePantallas-3) else False)
        self.x4.setEnabled(True if (pantallaIndex<self.numeroDePantallas-4) else False)
            
        print("pantalla "+str(pantallaIndex)+" activa")
        



# turn on developer tools in webkit so we can get at the javascript console for debugging
#QWebSettings.globalSettings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

# not required, used for example javascript->python calls
import json

# any QObject can be added to the javascript window object
# slots are then callable from javascript
class PythonAPI(QObject):
        
    def addSisters(self, hermanas):
        self.sisters = []
        for hermana in hermanas:
            self.sisters.append(hermana)
            
    @Slot(float, float)        
    def rePanSisters(self, x,y):
        for sister in self.sisters:
            sister.evaluateJavaScript("rePan("+str(x)+","+str(y)+");")          
    
    @Slot(float)        
    def reZoomSisters(self, res):
        for sister in self.sisters:
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
        self.video_widget=None
        self.view = QtWebKit.QWebView(self)
        self.api = PythonAPI()
        
    def setWebKit(self):
        print("estoy intentando abrir una pagina web")
        #self.titleFrame.setVisible(False)
        #self.graphFrame.setVisible(False)
        #self.fotosFrame.setVisible(False)
        #cualUrl = 
        self.view.setGeometry(0,0,1920,1080)
        self.view.load(QtCore.QUrl('http://localhost/~fidel/testMegadapt2.html'))
        self.view.show()
        self.view.setFocus()
        
        self.webFrame = self.view.page().mainFrame()
        
        self.webFrame.javaScriptWindowObjectCleared.connect(self.load_api)
        self.show()
        print("y no puedo")
        #self.pushButton.clicked.connect(self.call_js)
    
    def load_api(self):
        # add pyapi to javascript window object
        # slots can be accessed in either of the following ways -
        #   1.  var obj = window.pyapi.json_decode(json);
        #   2.  var obj = pyapi.json_decode(json)
        self.webFrame.addToJavaScriptWindowObject('pyapi', self.api)
        self.api.sisters = []
        
       
    


        
        
app = QApplication(sys.argv)
form = Ui_MainWindow()
form.ensamblaPantallas(4)
form.show()

# form2.show()
app.exec_()