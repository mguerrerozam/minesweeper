#PUNTO DE ENTRADA DE LA APLICACIÓN, INICIALIZACIÓN Y BUCLE PRINCIPAL
import pygame
import sys
from game.utils import COLORES, ANCHO, ALTO #IMPORTA EL DICCIONARIO CON LOS RGB DE LOS COLORES A UTILIZAR EN LA UI. EJEMPLO DE SINTAXIS: AZUL=COLORES['AZUL']

def main(): #SE DEFINE LA FUNCIÓN MAIN POR MODULARIDAD Y FACILIDAD PARA EL TESTEO

    pygame.init() #INICIALIZACIÓN DE PYGAME

    #CONFIGURACIÓN DE LA PANTALLA
    pantalla=pygame.display.set_mode((ANCHO,ALTO)) #DEFINE LA VARIABLE PANTALLA Y ESTABLECE SU ANCHO Y ALTO (EN PÍXELES)
    pygame.display.set_caption('Buscaminas') #SE AGREGA EL TÍTULO A LA VENTANA
    reloj=pygame.time.Clock() #ESTA VARIABLE SE UTILIZARÁ MÁS ADELANTE PARA LIMITAR LA FRECUENCIA DE ACTUALIZACIÓN DE LA PANTALLA 

    #BUCLE PRINCIPAL
    ejecutando=True #VARIABLE QUE PERMITE QUE EL PROGRAMA SIGA EJECUTÁNDOSE HASTA QUE SE CIERRE LA VENTANA
    while ejecutando: #BUCLE QUE SE REPITE MIENTRAS LA VARIABLE EJECUTANDO SEA VERDADERA
        eventos=pygame.event.get() #VARIABLE QUE AL ESTAR DENTRO DEL BUCLE PRINCIPAL, SE REDEFINE CONSTANTEMENTE CON LOS EVENTOS DEL JUEGO (ENTIÉNDASE EVENTO POR CADA COSA QUE HACE EL USUARIO)
        for evento in eventos:
            if evento.type==pygame.QUIT: #SI EL EVENTO ES HACER CLICK EN LA "X" PARA CERRAR EL PROGRAMA, EL BUCLE SE CORTA
                ejecutando=False

if __name__=='__main__': #ESTAS LÍNEAS PERMITEN QUE LA FUNCIÓN MAIN SOLO SEA LLAMADA SI ESTE ARCHIVO ES EJECUTADO DIRECTAMENTE, NO SI ES IMPORTADO COMO MÓDULO EN OTRO ARCHIVO
    main()