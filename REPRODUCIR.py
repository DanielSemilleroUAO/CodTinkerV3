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
import playsound

class Reproducir(object):
    def __init__(self):
        self.VOZ = ["background", "Organico.mp3", "Plastico.mp3", "Vidrio.mp3", "PapelCarton.mp3","PapelCarton.mp3", "Metal.mp3", "PapelCarton.mp3", "Organico.mp3", "Organico.mp3", "Organico.mp3", "Organico.mp3","Otros.mp3","Contenedorlleno.mp3"]
        self.ruta = "/home/linaro/CodTinkerV1/"
        #self.ruta = ""
    def reproducir(self):
        f = open(self.ruta+"SONIDOS/REPRODUCIR.txt")
        linea = f.readline()
        f.close()
        if(int(linea) != 0):
            playsound.playsound(self.ruta+"SONIDOS/"+self.VOZ[int(linea)], True)
            f = open(self.ruta+"SONIDOS/REPRODUCIR.txt",'w+')
            f.write(str(0))
            f.close()
sonidos = Reproducir()
while True:
    sonidos.reproducir()
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