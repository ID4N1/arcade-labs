class habitacion:
        def __init__(self, descripcion, norte, sur, este, oeste):
                self.descripcion = descripcion
                self.norte= norte
                self.este = este
                self.oeste = oeste
                self.sur = sur

def run():
        lista_habitaciones=[]
        pasillo = habitacion("Despiertas en un pasillo alargado. No tiene luz y solo huele a hierro. Parece que tiene una puerta al fondo (este)", None, None, 1, None)
        lista_habitaciones.append(pasillo)
        room = habitacion("Tras avanzar hacia el este, te encuentras en una habitación totalmente cuadrada, llena de marcas de uñas en las paredes. Una sensación extraña te invita a irte. Tras una puerta en el este, una escena horrible te deja sin aliento, aún así, puedes pasar por dicha puerta. Hacia el norte hay una puerta totalmente normal.", 2, None, 4, None)
        lista_habitaciones.append(room)
        pasad_norte = habitacion("Decides ir por la ruta amable, solo ves una especie de trampilla con una cuerda hacia el oeste", None, None, None, 3)
        lista_habitaciones.append(pasad_norte)
        cuerda = habitacion("Bajas la cuerda y apareces en una sala extraña, ves otra entrada que procede del techo", None, 4, None, None)
        lista_habitaciones.append(cuerda)
        pasad_este = habitacion("Pasas por aquella escena no sin antes pararte a mirar, una amalgama de restos, aparentemente humanos, te abrazan ya hasta la altura del tobillo. Sales corriendo, siguiendo tu camino y te encuentras con una escalera que baja por el techo de un habitación.", None, None, None, None)
        lista_habitaciones.append(pasad_este)
        
        habitacion_actual = 0
        completado = False
        
        while completado != True:
                print("\n")
                print(lista_habitaciones[habitacion_actual].descripcion)
                print("\n")
                
                decision = input("Dónde quieres ir?: ").lower()


                
                if decision == "norte" or decision == "n":
                        siguiente_hab = lista_habitaciones[habitacion_actual].norte
                        if siguiente_hab == None:
                                
                                print("Te has topado con una pared.")
                        else:
                                habitacion_actual = siguiente_hab
                                
                if decision == "sur" or decision == "s" :
                        siguiente_hab = lista_habitaciones[habitacion_actual].sur
                        if siguiente_hab == None:
                                print("Te has topado con una pared.")
                        else:
                                habitacion_actual = siguiente_hab
                                
                if decision == "este" or decision == "e":
                        siguiente_hab = lista_habitaciones[habitacion_actual].este
                        if siguiente_hab == None:
                                print("Te has topado con una pared.")
                        else:
                                habitacion_actual = siguiente_hab
                                
                if decision == "oeste" or decision == "o" :
                        siguiente_hab = lista_habitaciones[habitacion_actual].oeste 
                        if siguiente_hab == None:
                                print("Te has topado con una pared.")
                        else:
                                habitacion_actual = siguiente_hab
                if decision == "salir" or decision == "q":
                    completado = True



run()