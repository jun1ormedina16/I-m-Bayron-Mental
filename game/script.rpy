# Definición del personaje
define sis = Character('Conciencia', color="#4DFF00")
define j = Character("Jefecito", color="#FF5733")
define b = Character("Byron", color="#2d7af1")
define a = Character("Compañeros", color="#37f12d")


# Variables
default puntos = 10

# Canales de audio adicionales

init python:
    renpy.music.register_channel('bateria','music')
    renpy.music.register_channel('comping','music')
    renpy.music.register_channel('bongos','music')
    renpy.music.register_channel('rainstick','music')
    renpy.music.register_channel('flauta','music')
    renpy.music.register_channel('synthDark','music')

# Inicio del juego
label start:

#en la mañana
    play music "audio/Despertador.wav" fadein 1
    
    image dormitorio = "cuarto.jpg"
    scene dormitorio
    play music "audio/Despertador.wav" fadein 4
    image alarma = "aaaa.png"
    show alarma at truecenter
    "OUAAH! Creo que es hora de despertarse"
    hide alarma
    image reloj = "reloj.png"
    show reloj at truecenter
    sis "Ya son las 7 debería levantarme"
    
    #Inician los 6 canales 

    play bateria "audio/1 Batería.wav" fadein 1
    play comping "audio/2 Comping.wav" fadein 1
    play bongos "audio/3 bongos.wav" fadein 1
    play rainstick "audio/4 rainstick.wav" fadein 1
    play flauta "audio/5 Flauta.wav" fadein 1
    play flauta "6 synth darks.wav" fadein 1


    stop music fadeout 3
    play music "audio/Apartamento día_Ambiente.wav"
    sis "Será mejor que revise mi celular"
    hide reloj
    menu:
        "Coger el celular":
            jump decision  

        "No coger el celular":
            jump decision2  
    stop music
    return

label decision:
    play music "audio/Revisar el celular_Decisión Mala.wav"
    image celular = "celular.png"
    show celular at truecenter
    sis "¡WOW! Me han escrito varias personas y mis redes están a estallar, vamos a responder los mensajes"
    $ puntos -= 1
    hide celular
    image reloj2 = "reloj2.png"
    show reloj2 at truecenter
    sis "¡OOH NOOO! se me hizo tarde, me tengo que bañar"
    hide reloj2
    stop music
    jump escena2
    return

label decision2:
    play music "audio/No revisar y levantarse_decisión buena.wav"
    image reloj = "reloj.png"
    show reloj at truecenter
    sis "Mejor no, no es buena idea"
    sis "Será mejor que me levante"
    $ puntos += 1
    hide reloj
    stop music
    jump escena2
    return

label escena2:
#en la ducha
    play music "audio/musica.mp3"
    image ducha = "baño.jpg"
    scene ducha

    sis "Me voy a bañar"
    menu:
        "Bañarse con agua caliente":
            jump decision5  

        "Bañarse con agua fría":
            jump decision6  
    stop music
    return

label decision5:
    play music "audio/Ducha Caliente_Decisión mala.wav"
    image acaliente = "caliente.png"
    show acaliente at truecenter
    sis "Que delicia el agua caliente"
    b "AgGhH me quemo !!!"
    $ puntos -= 1
    hide acaliente
    image tiempo = "reloj3" 
    show tiempo at truecenter
    sis "¡OH NOOO! Me cogio la tarde, ya son las 8:00"
    stop music
    jump escena3
    return

label decision6:
    play music "audio/Ducha Fria_Decisión Buena.wav"
    image afria = "frio.png"
    show afria at truecenter
    sis "Mejor me baño con agua fría, quiero ahorrar tiempo"
    $ puntos += 1
    hide afria
    stop music
    jump escena3 
    return

stop music

label escena3:
#en el cuarto arreglandose
    play music "audio/musica.mp3"
    image dormitorio = "cuarto.jpg"
    scene dormitorio
    sis "Bueno me voy a arreglar y salgo a trabajar"
    menu:
        "Coger carro":
            jump decision7  

        "Ir en bicicleta":
            jump decision8  
    stop music
    return

label decision7:
    play music "audio/Auto_Decisión mala.wav"
    image carro = "carro.png"
    show carro at truecenter
    sis "Si me voy en carro me demoro menos"
    $ puntos -= 1
    hide acaliente
    stop music
    jump escena4
    return

label decision8:
    play music "audio/Bicicleta_Decisión buena.wav"
    image bicicleta = "bici.png"
    show bicicleta at truecenter
    sis "Mejor me voy en bicicleta, hago un poco de ejercicio"
    $ puntos += 1
    hide afria
    stop music
    jump escena4
    return

label escena4:
#en la oficina
    play music "audio/Trabajo_Ambiente.wav"
    image cuarto = "oficina.png"
    scene cuarto 
     
    "En el trabajo"
    b "He llegado justo a tiempo al trabajo !!"
    sis "Que es lo que tenia que hacer??"
    j "Buenos dias, ya me tiene listo el informe?"
    j "Lo estoy esperando"
    b "Si Jefe, ya se lo entrego *glup*…"
    
    #show yo at right
    #with move  
    
    sis "Como entrego el informe?"
  
    menu:
        #renpy.music.set_volume(volume, delay=0.5, channel='music') 
        #music at 0.5
        #renpy.music.set_volume(0.5)
       # config.music_volume = 0.5
        "Imprimir el informe":
            jump imprimo

        "Lo envialo por correo":
            jump correo
    #hide yo
    #with dissolve
    stop music
    return

label imprimo:

    play sound "audio/Imprimir_Desición mala.wav"
    sis "Apreciará mas que se lo lleve en fisico"
    b "Jefe !! Aquí el informe"
    j "Gracias, la proxima vez no demore tanto"
    sis "fiu, por un pelo"
    $ puntos -= 1
    stop sound
    jump almuerzo
    return


label correo:
    play sound "audio/Enviar digital_Decisión buena.wav"
    #j "Ya me llego, lo leere de una vez"
    sis "Veo que lo necesita con urgencia"
    sis "Será por correo"
    $ puntos += 1
    stop sound
    jump almuerzo

    return


# LA HORA DEL ALMUERZO

label almuerzo:
    sis "Por fin, hora de comer"
    #"glu glu glu"
    a "Hey amigo !! Ya tenemos hambre, quieres ir por unas hamburguesas?"
    sis "Que deberia hacer?"
    menu:
        "Comer lo que traje de casa":
            jump comidaCasa
        "Ir a almorzar con los compañeros":
            jump comidaCompas
    return

label comidaCasa:

    play sound "audio/Traer comida_decisión buena.wav"
    sis "No, gracias, traje mi propia comida, nos vemos en el café"
    a "jajaj como quieras, tu te lo pierdes"
    sis "Quien lo diría? Cada dia cocino mejor"

    $ puntos += 1
    jump finDia

    return
label comidaCompas:

    play sound "audio/Almorzar fuera_Decisión mala.wav"
    sis "SI, por que no?"
    a "Excelente !! No te tardes"

    $ puntos -= 1
    jump finDia

    return

#ES LA HORA DE DORMIR


label finDia:
    image tiempo = "tiempo.jpg"
    scene tiempo at center
    with fade
    "ya son las 5pm"
    b "Es todo por hoy, que dia tan agotador…"
    b "Será mejor volver a casa"

    play music "audio/Apartamento noche_Ambiente.wav"
    
    image sala = "IMG_2998.png"
    scene sala at center
    with fade
    "por fin en casa"
    sis "Salió un nuevo capitulo de la serie que me gusta, ¿Qué debería hacer?"

    menu:
        "Ver television":
            jump television
        "Ir a dormir":
            jump dormir



label television:
    play sound "audio/Ver TV_Desición mala.wav"
    sis "Es la ultima temporada"
    sis "Otra vez me trasnoché, maldición"
    $ puntos -= 1
    jump store
    return

label dormir:
    play sound "audio/Irse a dormir_Decisión buena.wav"
    sis "Creo que mejór descansaré"
    sis "Dormir es el mejor placer que hay"
    $ puntos += 1
    jump store
    return
    
label store:
    $ puntosT = str(puntos)
    "tu puntaje del día es [puntosT]" 

    return
