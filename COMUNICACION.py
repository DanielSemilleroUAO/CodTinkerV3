# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:21:21 2018

@author: Daniel Delgado Rodrìguez
         Juan Fernando Guerrero F.  
"""
###############################################################################
###############################################################################
        #########           ###########                ###########            
        #        #      @        #                          # 
        #        #               #                          #
        #        #      #        #         #########        #
        #########       #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #########       #   ###########    #########        #
###############################################################################
###############################################################################
        
#-------------------------IMPORTAR LÌBRERIAS-----------------------------------
import urllib.request
import paho.mqtt.client as mqtt
#------------------------CLASE COMUNICACION------------------------------------
class comunicacion(object):
    #-----------------------CONSTRUCTOR----------------------------------------
    def __init__(self):
        self.dato = ""
        self.client = mqtt.Client()
    def conectar_server(self):
        self.client.connect("192.168.4.1",1883,60)
        self.client.on_connect = self.on_connect
    def on_connect(self,client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    def publicar(self,topic):
        try:
            self.client.connect("192.168.4.1",1883,1)
            self.client.on_connect = self.on_connect
            self.client.publish(topic,"*")
            return True
        except:
            return False
    #-------------------------VERIFICACIÒN CONEXIÒN INTERNET-------------------
    def sondeo(self):
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False
#-------------------------FIN DEL PROGRAMA-------------------------------------
###############################################################################
###############################################################################
        #########           ###########                ###########            
        #        #      @        #                          # 
        #        #               #                          #
        #        #      #        #         #########        #
        #########       #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #        #      #        #        #         #       #
        #########       #   ###########    #########        #
###############################################################################
###############################################################################