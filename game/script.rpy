define l = Character("Layla", image="Layla", color="#FFFFFF")
define h = Character("Hombre de taquilla", image="Layla", color="#FFFFFF")
define s = Character("Sirius", image="Layla", color="#FFFFFF")
define m = Character("Mujer molesta", image="Layla", color="#FFFFFF")
define u = Character("???", image="Layla", color="#FFFFFF")
define uu = Character("???", color="#FFFFFF")


# ==========================IMAGES==========================

init: 
    image Tren medio dia = "images/bgs/Tren medio dia.PNG"
    image Vagon 2 medio dia = "images/bgs/Vagon 2 medio dia.PNG"
    image Vagon 1 noche = "images/bgs/Vagon 1 noche.PNG"
    image Negro = "images/bgs/negro.png"
    image CorredorNoche = "images/bgs/Corredor noche.PNG"

    image side Layla = "Side Layla Seria.PNG"
    image side Layla Seria = "Side Layla Seria.PNG"
    image side Layla Sonrisa = "Side Layla Sonrisa.PNG"
    image side Layla Sorpresa = "Side Layla Sorpresa.PNG"
    image side Layla OjosCerradosSonrisa = "Side Layla Ojoscerradossonrisa.PNG"
    image side Layla Enojo = "Side Layla Enojo.PNG"

    image Sirius Normal = "images/Sirius/Sirius Normal.PNG"
    image Sirius Feliz = "images/Sirius/Sirius Feliz.PNG"
    image Sirius FelizOjosCerrados = "images/Sirius/Sirius Felizojoscerrados.PNG"

    image Celia Disconforme = "images/Celia/celia disconforme.PNG"


# ==========================OPCIONES==========================

default checked_op1A = False
default checked_op1B = False
default checked_op1C = False
default checked_op1D = False



label start:

    scene Tren medio dia with dissolve

    play music "audio/music/Murmullos gente.mp3" fadein 1.5 volume 0.5 loop

    play sound "audio/sfx/Sonido de pasos" fadein 1.5 loop

    l "(La estación está oscura, llena de murmullos y pasos.)"

    play sound "audio/sfx/Sonido de pasos rapidos.mp3" fadein 0.5 loop

    l "(Corro apresurada entre la multitud, es una costumbre mía siempre llegar tarde.)"

    l "(No se realmente hacia donde voy, solo camino entre la multitud y siento que habia un lugar donde tenía que estar hoy...)"

    l "(Trato de apurarme pero la multitud me empuja.)"

    l "(Después de un largo rato batallando por llegar a la taquilla, al fin logro llegar.)"

    play music "audio/music/ES_Valse triste Nicoise - Magnus Ludvigsson.mp3" fadein 1.5 loop

    play sound "audio/sfx/Murmullos gente.mp3" volume 0.5 loop

    l "Buenas tardes?"
    
    h "Bienvenida a .... .. . ...."

    h "¿Cómo puedo ayudarla?"

    l "(No escuche la mitad de lo que decía por el ruido a mi alrededor...)"
    
    l "(Igual creo que el cansancio debe de estar cobrando factura.)"

    l Sonrisa "Quisiera un boleto para el tren más próximo, ¿Todavía lo alcanzó?"

    h "Siempre puede alcanzarlo, mientras tenga con que pagar."

    l "(Sin pensar mucho, saco de mi bolsa unas monedas.)"

    l "(El taquillero me sonríe.)"

    h "Su nombre por favor."

    l Seria "Me llamo Layla."

    h "Listo, un boleto para que tenga un buen día y disfrute su viaje, debe de apurarse, el tren está a punto de salir."

    play sound "audio/sfx/Sonido de pasos rapidos.mp3" fadein 0.5 loop

    l "(Sigo corriendo por el pasillo, hasta llegar al andén que me toca, el #6. Me parece frustrante caminar entre tantas personas.)"

    stop sound

    l "(Al fin llego a la entrada del tren, donde quien parece ser el conductor está revisando a los que ingresan.)"

    l "(Me pongo en la fila a esperar mi turno.)"

    show Sirius Normal

    u "Su boleto por favor."

    show Sirius Feliz

    l "(Le entrego mi boleto, él lo inspecciona, y me mira ofreciéndome una sonrisa.)"

    l Sonrisa "Casi no llego."

    u "Que bueno que puede acompañarnos entonces."

    s "Soy el conductor: Sirius a su servicio."

    l "(El conductor Sirius, sella mi boleto, me llama la atención que utiliza un sello color sangre, además de que tiene una insignia que nunca había visto antes cuando viajo.)"

    l "(Su cara también me parece conocida.)"

    l Sorpresa "Disculpe, ¿nos conocemos?"

    show Sirius FelizOjosCerrados

    s "No lo creo, pero estaremos viéndonos seguido en este viaje."

    s "Por lo que veo va a tener un viaje muy largo... se quedará todas las 5 estaciones."

    l Sonrisa "Hay un lugar al que tengo que ir."

    show Sirius Feliz

    s "Ya veo... Disfrute estar a bordo de este tren y cualquier cosa que necesite, estaré visitando los vagones cada cierto tiempo."

    l "Gracias, con permiso."

    hide Sirius

    l "(El conductor parece una persona muy amable, incluso minutos antes de que me atendiera estuvo hablando con una mujer que parecía molesta y consiguió calmarla.)"

    scene Vagon 2 medio dia with dissolve

    play music "audio/music/ES_Coal - Arden Forest.mp3" fadein 1.5 loop
    
    l Seria "(Empiezo a caminar hacia mi vagón, en el camino veo a varias personas.)"

    l "(Me encuentro a la mujer de antes, peleando con otro pasajero que parece ser un instructor.)"

    l "(Mientras empiezo a guardar mi equipaje veo a una niña jugando en el suelo.)"

    l OjosCerradosSonrisa "¿Estas sola?"

    l "(La niña me mira un momento, y luego se voltea a seguir jugando, supongo que sus padres le han dicho que no hable con desconocidos.)"

    l Seria "(Sigo acomodando mis cosas, y me siento en mi lugar.)"

    l "(Me pongo a mirar por la ventana, todo se ve muy vacío, al parecer la multitud ya se dispersó un poco.)"

    u "Disculpa..."

    l "(La voz de una persona desconocida me saca de mis pensamientos. Es un muchacho no mucho mayor que yo.)"

    l "(Parece algo tímido, y su cara se me hace conocida, aunque prefiero no decir nada, ya que al parecer incluso confundir al conductor con otra persona.)"

    l "(Lo miro fijamente esperando a que hable.)"

    u "¿De casualidad eres Layla?"

    l "(Sorprendentemente sí era una persona conocida, asiento con la cabeza y me sonríe.)"

    u "¡Lo sabía! Te vi desde que estábamos abordando. No esperaba verte aquí, Soy..."

    l "(Antes de que el muchacho terminara de hablar, empezó a sonar el altavoz.)"

    s "{color=#818589}{i}Bienvenidos al tren #6, gracias por preferirnos por sobre otras líneas.{/i}{/color}"

    s "{color=#818589}{i}Les habla Sirius, su capitán y recuerden, si necesitan algo, estoy en la cabina.{/i}{/color}"

    s "{color=#818589}{i}Esperamos que su viaje esté lleno de recuerdos y sorpresas inolvidables.{/i}{/color}"

    l "(Después de ese anuncio empiezo a sentir que el tren se mueve, me relajo y veo como poco a poco dejamos atrás a las personas.)"

    l "(Miro a la gente a mi alrededor.)"

    label op1:
        menu:
            "La mujer que parece molesta." if checked_op1A == False:
                jump op1A
            "El hombre de lentes." if checked_op1B == False:
                jump op1B
            "La niña que está sentada sola." if checked_op1C == False:
                jump op1C
            "El muchacho que está sentado a mi lado." if checked_op1D == False:
                jump op1D
            "Continuar." if checked_op1A and checked_op1B and checked_op1C and checked_op1D == True:
                jump op1F
            
label op1A: 
    $ checked_op1A = True

    l "(Miro a la mujer, que parece estar molesta sentada en el pasillo a mi izquierda.)"

    l "(Está mirando a la ventana, y a decir verdad me intimida un poco.)"

    play sound "audio/sfx/mujer enojada final.mp3"

    show Celia Disconforme

    m "Necesitas algo?"

    l "(Que incomodo, parece que me vio mirarla. Niego con la cabeza y me volteo por mi propia ventana.)"

    hide Celia Disconforme

    jump op1

label op1B:
    $ checked_op1B = True
    l "(Del otro lado del pasillo hay un hombre leyendo un libro.)"

    play sound "audio/sfx/paginas pasando final.mp3"

    l "(Parece muy concentrado y esta totalmente ajeno a que yo lo vea, no parece importarle otra cosa que no sea su libro.)"

    stop sound

    jump op1

label op1C: 
    $ checked_op1C = True

    l "(La niña a la que le hablé hace un rato, está en su lugar jugando con lo que parece ser una muñeca.)"

    l "(Parece ser muy retraída y tímida. Está concentrada en su juguete y tampoco hace mucho ruido.)"

    l "(Por un segundo me mira y me siento incómoda.)"

    jump op1

label op1D: 
    $ checked_op1D = True

    l "(De reojo veo al muchacho sentado enfrente de mi.)"

    l "(Parece concentrado en la ventana, pero se ve algo nervioso. No se si deberia sacarle platica y preguntarle qué quería decirme.)"

    jump op1

label op1F: 

    l "(Después de tanto pensar y mirar el paisaje sin darme cuenta, se ha hecho de noche.)"

    l "(Me relajo en mi lugar y poco a poco siento los ojos pesados hasta que me quedo dormida en tan solo un momento.)"

    stop music fadeout 1.5

    scene Negro with dissolve

    "..."

    "..."

    "..."

    play sound "audio/sfx/Sonido de pasos" fadein 1.5 loop

    uu "{i}No deberías de dormir en el tren...{/i}"

    scene Vagon 1 noche with dissolve

    stop sound

    l "(Abro los ojos de golpe, parece que estaba teniendo una pesadilla.)"

    l "(Pero me doy cuenta de un detalle importante:)"

    play music "audio/music/ES_Candy Clown - Enigmanic.mp3" fadein 1.5 loop

    l Sorpresa "Donde están todos..."

    l Seria "(El vagón está completamente vacío, además de que no estamos moviéndonos.)"

    l "(Miro hacia la ventana y me doy cuenta de que está muy empañada como para mirar afuera.)"

    l "(Termino tomando la decisión de caminar por los vagones para ver si hay alguien.)"

    l "(Conforme avanzó. Me doy cuenta de que no hay nadie.)"

    l "(Será que estamos en algún medio tiempo para ir al baño?)"

    l Sorpresa "¡Hola! ¿Hay alguien aquí? ¡Conductor!"

    l Seria "(No hay ninguna respuesta, solo el eco de mi voz.)"

    l "(Mientras camino me doy cuenta de que en el cristal parece escribirse la palabra “BAJA”.)"

    l "(A decir verdad me da un poco de miedo... Puede que esté soñando todavía.)"

    l "(Empieza a dolerme la cabeza. No me da un buen presentimiento lo que está pasando.)"

    l Enojo "¡Conductor!"

    l Seria "(Sigo caminando hacia la salida, pero solo porque no se que otra cosa hacer.)"

    l Enojo "¡Sirius!"

    l Seria "(En medio de la desesperación lo llamó por su nombre...)"

    l "(Unos segundos después el altavoz empieza a sonar y veo que algo brilla en mi bolsillo.)"

    l "(Al sacar el objeto veo que es el boleto, el cual tiene el sello brillando.)"

    l "(Lo toco, y siento como si me quemara.)"

    l Sorpresa "Esto no... esto no puede ser real."

    s "{color=#818589}{i}Un, dos, tres{/i}{/color}"

    l "(Empiezo a escuchar la voz de Sirius en el altavoz.)"

    s "{color=#818589}{i}Llegamos a la primera parada, por favor deben descender.{/i}{/color}"

    l "(Pero esta no es mi parada, supongo que puedo quedarme en mi lugar, y solo es una coincidencia muy rara que todos se bajaran ahora.)"

    s "{color=#818589}{i}Repito, todos deben descender.{/i}{/color}"

    l "(Su voz suena más seria que en el mensaje anterior. Será que es un mensaje solo para mi.)"

    l "(Me quedo parada en la puerta, sin atreverme a bajar, sigo sin tener un buen presentimiento.)"

    show Sirius FelizOjosCerrados

    s "Bienvenida al verdadero viaje."

    l "(Escucho la voz del conductor y siento cómo me empuja.)"

    hide Sirius

    scene CorredorNoche with hpunch

    l "(Al momento de caer al piso, volteo para reclamar, pero solo veo como las puertas se cierran atrás de mi.)"

    scene CorredorNoche with hpunch

    l "(Intento volver a subir, pero las puertas no se abren y sin previo aviso, el tren arranca. Por instinto me hago para atrás...)"

    l "(Con pánico y sin saber que hacer veo como el tren se pierde entre las sombras y me quedo en la primera estación sintiéndome sola.)"


    return
