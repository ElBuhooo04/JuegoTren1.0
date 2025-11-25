define l = Character("Layla", image="Layla", color="#FFFFFF")
define h = Character("Hombre de taquilla", image="Layla", color="#FFFFFF")
define s = Character("Sirius", image="Layla", color="#FFFFFF")
define m = Character("Mujer molesta", image="Layla", color="#FFFFFF")
define u = Character("???", image="Layla", color="#FFFFFF")
define uu = Character("???", color="#FFFFFF")
define c = Character("Celia", image="Layla", color="#FFFFFF")
define t = Character("Mathias", image="Layla", color="#FFFFFF")
define a = Character("Arnold", image="Layla", color="#FFFFFF")


# ==========================IMAGES==========================

init: 
    image Tren medio dia = "images/bgs/Tren medio dia.PNG"
    image Vagon 2 medio dia = "images/bgs/Vagon 2 medio dia.PNG"
    image Vagon 1 noche = "images/bgs/Vagon 1 noche.PNG"
    image Vagon 1 Morning = "images/bgs/Vagon 1 manana.PNG"
    image Negro = "images/bgs/negro.png"
    image CorredorNoche = "images/bgs/Corredor noche.PNG"
    image CorredorMorning = "images/bgs/Corredor manana.PNG"
    image bg = "images/bgs/Corredor noche.PNG"

    image side Layla = "Side Layla Seria.PNG"
    image side Layla Seria = "Side Layla Seria.PNG"
    image side Layla SeriaSonrojo = "Side Layla Seriasonrojo.PNG"
    image side Layla Sonrisa = "Side Layla Sonrisa.PNG"
    image side Layla Sorpresa = "Side Layla Sorpresa.PNG"
    image side Layla OjosCerradosSonrisa = "Side Layla Ojoscerradossonrisa.PNG"
    image side Layla Enojo = "Side Layla Enojo.PNG"
    image side Layla Triste = "Side Layla Tristeza.PNG"

    image Sirius Normal = "images/Sirius/Sirius Normal.PNG"
    image Sirius Feliz = "images/Sirius/Sirius Feliz.PNG"
    image Sirius FelizOjosCerrados = "images/Sirius/Sirius Felizojoscerrados.PNG"
    image Sirius Preocupacion = "images/Sirius/Sirius Preocupado.PNG"
    image Sirius Muy Feliz = "images/Sirius/Sirius Muyfelizojoscerradossonrojado.PNG"

    image Celia Disconforme = "images/Celia/celia disconforme.PNG"
    image Celia Enojada = "images/Celia/Celia enojada.PNG"
    image Celia Risa = "images/Celia/celia ojoscerradosbocaabierta.PNG"
    image Celia Seria = "images/Celia/Celia seria.PNG"
    image Celia Feliz = "images/Celia/Celia feliz.PNG"

    image Mathias Normal = "images/Mathias/Mathias Normal.PNG"
    image Mathias CerradoSerio = "images/Mathias/Mathias ojoscerradosserio.PNG"
    image Mathias Sonrisa = "images/Mathias/Mathias sonrisa.PNG"
    image Mathias OjoCerrados = "images/Mathias/Mathias ojoscerrados.PNG"

    image Nadia Normal = "images/Nadia/Nadia Normal.PNG"

init:
    transform my_shake:
        linear 0.1 xoffset -2 yoffset 2 
        linear 0.1 xoffset 3 yoffset -3 
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat


# ==========================OPCIONES==========================

default checked_op1A = False
default checked_op1B = False
default checked_op1C = False
default checked_op1D = False



label start:

    $ Bad = 0
    $ Neutral = 0 
    $ Good = 0

    scene Tren medio dia with dissolve

    play music "audio/music/Murmullos gente.mp3" fadein 1.5 volume 0.5 loop

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    l "(La estación está oscura, llena de murmullos y pasos.)"

    play sound "audio/sfx/Sonido de pasos rapidos.mp3" fadein 0.5 loop

    l "(Corro apresurada entre la multitud, es una costumbre mía siempre llegar tarde.)"

    l "(No se realmente hacia donde voy, solo camino entre la multitud y siento que habia un lugar donde tenía que estar hoy...)"

    l "(Trato de apurarme pero la multitud me empuja.)"

    l "(Después de un largo rato batallando por llegar a la taquilla, al fin logro llegar.)"

    play music "audio/music/ES_Valse triste Nicoise - Magnus Ludvigsson.mp3" fadein 1.5 loop

    play sound "audio/sfx/Murmullos gente.mp3" volume 0.5 loop

    l "Buenas tardes?"
    
    h "Bienvenida a {color=#818589}{i}.... .. . ....{/i}{/color}"

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

    show Sirius Normal with dissolve

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

    hide Sirius with dissolve

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

    l Sorpresa "(La voz de una persona desconocida me saca de mis pensamientos. Es un muchacho no mucho mayor que yo.)"

    l Seria "(Parece algo tímido, y su cara se me hace conocida, aunque prefiero no decir nada, ya que al parecer incluso confundir al conductor con otra persona.)"

    l "(Lo miro fijamente esperando a que hable.)"

    u "¿De casualidad eres Layla?"

    l Sorpresa "(Sorprendentemente sí era una persona conocida, asiento con la cabeza y me sonríe.)"

    u "¡Lo sabía! Te vi desde que estábamos abordando. No esperaba verte aquí, Soy..."

    l Seria "(Antes de que el muchacho terminara de hablar, empezó a sonar el altavoz.)"

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

    show Celia Disconforme with dissolve

    m "Necesitas algo?"

    l SeriaSonrojo "(Que incomodo, parece que me vio mirarla. Niego con la cabeza y me volteo por mi propia ventana.)"

    hide Celia Disconforme with dissolve

    jump op1

label op1B:
    $ checked_op1B = True
    l Seria "(Del otro lado del pasillo hay un hombre leyendo un libro.)"

    show Mathias Normal with dissolve

    play sound "audio/sfx/paginas pasando final.mp3"

    l "(Parece muy concentrado y esta totalmente ajeno a que yo lo vea, no parece importarle otra cosa que no sea su libro.)"

    hide Mathias with dissolve

    stop sound

    jump op1

label op1C: 
    $ checked_op1C = True

    show Nadia Normal with dissolve

    l Seria "(La niña a la que le hablé hace un rato, está en su lugar jugando con lo que parece ser una muñeca.)"

    l "(Parece ser muy retraída y tímida. Está concentrada en su juguete y tampoco hace mucho ruido.)"

    l "(Por un segundo me mira y me siento incómoda.)"

    hide Nadia with dissolve

    jump op1

label op1D: 
    $ checked_op1D = True

    l Seria "(De reojo veo al muchacho sentado enfrente de mi.)"

    l "(Parece concentrado en la ventana, pero se ve algo nervioso. No se si deberia sacarle platica y preguntarle qué quería decirme.)"

    jump op1

label op1F: 

    l OjosCerradosSonrisa "(Después de tanto pensar y mirar el paisaje sin darme cuenta, se ha hecho de noche.)"

    l "(Me relajo en mi lugar y poco a poco siento los ojos pesados hasta que me quedo dormida en tan solo un momento.)"

    stop music fadeout 1.5

    scene Negro with dissolve

    "..."

    "..."

    "..."

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    uu "{i}No deberías de dormir en el tren...{/i}"

    scene Vagon 1 noche with hpunch

    stop sound

    l Seria "(Abro los ojos de golpe, parece que estaba teniendo una pesadilla.)"

    l "(Pero me doy cuenta de un detalle importante:)"

    play music "audio/music/ES_The Cost of Fear - Jon Bjork.mp3" fadein 1.5 loop

    l Sorpresa "Donde están todos..."

    l Seria "(El vagón está completamente vacío, además de que no estamos moviéndonos.)"

    l "(Miro hacia la ventana y me doy cuenta de que está muy empañada como para mirar afuera.)"

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    l "(Termino tomando la decisión de caminar por los vagones para ver si hay alguien.)"

    l "(Conforme avanzó. Me doy cuenta de que no hay nadie.)"

    l "(Será que estamos en algún medio tiempo para ir al baño?)"

    stop sound

    play music "audio/music/ES_Candy Clown - Enigmanic.mp3" fadein 1.5 loop

    l Sorpresa "¡Hola! ¿Hay alguien aquí? ¡Conductor!"

    l Seria "(No hay ninguna respuesta, solo el eco de mi voz.)"

    l "(Mientras camino me doy cuenta de que en el cristal parece escribirse la palabra “BAJA”.)"

    l "(A decir verdad me da un poco de miedo... Puede que esté soñando todavía.)"

    l Enojo "(Empieza a dolerme la cabeza. No me da un buen presentimiento lo que está pasando.)"

    l "¡Conductor!"

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    l Seria "(Sigo caminando hacia la salida, pero solo porque no se que otra cosa hacer.)"

    l Enojo "¡Sirius!"

    l Seria "(En medio de la desesperación lo llamó por su nombre...)"

    l "(Unos segundos después el altavoz empieza a sonar y veo que algo brilla en mi bolsillo.)"

    l Sorpresa "(Al sacar el objeto veo que es el boleto, el cual tiene el sello brillando.)"

    l "(Lo toco, y siento como si me quemara.)"

    l "Esto no... esto no puede ser real."

    s "{color=#818589}{i}Un, dos, tres{/i}{/color}"

    l Seria "(Empiezo a escuchar la voz de Sirius en el altavoz.)"

    s "{color=#818589}{i}Llegamos a la primera parada, por favor deben descender.{/i}{/color}"

    l "(Pero esta no es mi parada, supongo que puedo quedarme en mi lugar, y solo es una coincidencia muy rara que todos se bajaran ahora.)"

    s "{color=#818589}{i}Repito, todos deben descender.{/i}{/color}"

    l "(Su voz suena más seria que en el mensaje anterior. Será que es un mensaje solo para mi.)"

    l "(Me quedo parada en la puerta, sin atreverme a bajar, sigo sin tener un buen presentimiento.)"

    show Sirius FelizOjosCerrados with dissolve

    s "Bienvenida al verdadero viaje."

    l "(Escucho la voz del conductor y siento cómo me empuja.)"

    hide Sirius

    scene CorredorNoche with hpunch

    l "(Al momento de caer al piso, volteo para reclamar, pero solo veo como las puertas se cierran atrás de mi.)"

    scene CorredorNoche with hpunch

    l "(Intento volver a subir, pero las puertas no se abren y sin previo aviso, el tren arranca. Por instinto me hago para atrás...)"

    l "(Con pánico y sin saber que hacer veo como el tren se pierde entre las sombras y me quedo en la primera estación sintiéndome sola.)"

    stop music

    scene CorredorNoche with dissolve

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    l "(Camino sola por el corredor. El tren ya se ha ido.)"

    l "(No hay viento, no hay voces, no hay movimiento.)"

    l "(Solo una banca vieja, faroles parpadeando y neblina cubriendo el suelo como un velo espeso.)"

    l "¿Por qué me dejó aquí…?"

    l "(No entiendo qué está pasando, miro mis manos. Están temblando.)"

    l "(Siento un peso en el pecho, como si algo dentro de mí quisiera hundirme.)"

    l "(Al fondo, veo una silueta femenina sentada en la banca. Inmóvil. Elegante. Distante...)"

    l "(Me tranquiliza darme cuenta que es la misma mujer del tren, que estaba en el tren.)"

    stop sound 

    play music "audio/music/ES_Valse triste Nicoise - Magnus Ludvigsson.mp3" fadein 1.5 loop

    l "Disculpe... ¿Sabe qué está pasando? ¿Dónde está la gente?"

    l "(La mujer gira lentamente la cabeza. Sus ojos son fríos, calculadores.)"

    play sound "audio/sfx/mujer enojada final.mp3"

    show Celia Enojada with dissolve

    m "Le hablas a toda la gente así, ¿sin respeto?"

    l "(Desde el tren se nota que es una persona con muy mala actitud, muy bonita pero pésima actitud.)"

    l Enojo "Disculpe señora... yo..."

    c "Me llamo Celia, no soy cualquier señora niña igualada."

    l Seria "(El estómago se me revuelve: su postura, la línea de su cuello, la forma de cruzar los brazos...)"

    l "(Me recuerda a ella. Si fuera otra circunstancia evitará hablar totalmente con una persona así...)"

    l "(Pero no tengo ni idea de por que se fue el tren y posiblemente esta mujer tenga una respuesta.)"

    l Enojo "Disculpe señorita Celia... ¿Sabe qué está pasando? ¿Dónde está la gente?"

    l "(La mujer gira lentamente la cabeza. Sus ojos son fríos, calculadores.)"

    c "Qué pregunta tan ingenua."

    c "Incluso aquí sigues sin entender lo que ocurre. Qué decepción."

    l "(Layla frunce el ceño. Un escalofrío le recorre la espalda.)"

    l Seria "Ni siquiera me conoce. No tiene derecho a hablarme así."

    show Celia Risa

    l "(Celia sonríe con desprecio.)"

    c "No necesito conocerte. Se nota a simple vista: frágil, confundida, inútil."

    c "No sabes a dónde vas, ni quién eres, ni qué esperas."

    c "Una niña perdida esperando que alguien la salve... y nadie lo hará."

    l Enojo "(Sus palabras hacen que me duela la cabeza.)"

    show Celia Risa at left with move

    c "Eres una niña tonta y pérdida que espera que alguien la salve y nadie lo hará nunca."
    
    show Celia Risa at center with move

    l "(Celia se pone de pie, caminando lentamente alrededor de mí, examinándose como si fuera un objeto defectuoso.)"

    show Celia Risa at right with move
    
    l "Retrocedo un paso enfurecida, lista para responderle."

    show Celia Risa at center with move

    label op2:
        menu:
            "Confrontar con Miedo":
                $ Bad += 1
                jump op2A
            "Callar":
                $ Neutral += 1
                jump op2B
            "Confrontar con Firmeza":
                $ Good += 1
                jump op2C

label op2A:
    l "(Sin pensar mucho las cosas la confronto.)"

    with hpunch

    show Celia Disconforme

    l "¡Cállese! ¡No sabe nada de mí!"

    c "Te aterra escuchar la verdad, igual que antes. Patética, por eso siempre me dejas ser la villana."

    l Seria "(Me quedo fría escuchándola. Ya no se que mas decirle.)"

    jump OP2CONTI

label op2B: 
    l Seria "(Le bajó la mirada sin responder, no se que tiene esa mujer que me paraliza.)"

    l "..."

    show Celia Seria 

    c "Claro... guarda silencio. Es lo único que sabes hacer."

    l "..."

    jump OP2CONTI

label op2C: 
    l Seria "(Podrá ser una mujer mayor, y me intimida un poco, pero no voy a dejarla opacarme.)"

    show Celia Disconforme
    
    l Enojo "No tiene derecho a hablarme así. No voy a aceptar sus palabras."

    l "(La veo entornar los ojos, parece fastidiada de que le responda.)"

    show Celia Risa 

    c "Que linda, jugando a ser fuerte."

    jump OP2CONTI

label OP2CONTI:

    l Seria "(La siento poco a poco molestarse más, pareciera que mi presencia es una total molestia para ella. No tengo idea del porqué.)"

    show Celia Enojada 

    c "Dime, ¿alguna vez alguien te ha elegido? ¿Alguien te ha esperado? ¿Alguien te quiere? No. Por eso terminaste aquí. Invisible. Desechable."

    l "(Siento un golpe horrible en el pecho, esta mujer me recuerda mucho a mi madre… las mismas palabras hirientes, el mismo desprecio.)"

    play music "audio/music/Nebula - Myuu.mp3" fadein 1.5 loop

    l "(La neblina aumenta. El ambiente se vuelve asfixiante para mi. No se que hacer.)"

    label op3:
        menu: 
            "Perdonar.":
                $ Good += 1
                jump op3A
            "Indiferencia.":
                $ Neutral += 1
                jump op3B
            "Rencor.":
                $ Bad += 1
                jump op3C

label op3A:
    l Triste "No sé quién es usted... pero ya no voy a cargar con esto."

    l "Lo que me hicieron… lo que me dijo… ya no voy a vivir a través de ese daño. Lo suelto."

    l "(Celia me observa con repulsión, pero la veo luego respirar… me mira con molestia.)"

    hide Celia with dissolve

    l "(Y luego frente a mis ojos desaparece.)"

    jump OP3CONTI

label op3B: 
    l Enojo "Ya no me importa."

    l "(Doy media vuelta, trato de evitar su mirada.)"

    l "Tus palabras no tienen poder sobre mí Celia. No más."

    l "(Celia se queda ahí, rígida, como una estatua, incapaz de decir otra cosa… ni de irse.)"

    jump OP3CONTI

label op3C: 
    with hpunch

    l Enojo "¡Ojalá nunca hubiera conocido a nadie como usted!"

    l "(Mi boca habla antes de que pueda controlarme... me miro en un reflejo...)"

    l "(Tengo los ojos llenos de rencor, pero no puedo detenerme.)"

    with hpunch

    l "Me voy a encargar de no sentir esto nunca más. Juro que nunca volveré a ser débil."

    show Celia Feliz

    l "(Celia para mi sorpresa, sonríe, satisfecha, como si hubiera ganado,-)"

    hide Celia with dissolve

    l "(-antes de  terminar desapareciendo frente a mi.)"

    jump OP3CONTI

label OP3CONTI:

    play music "audio/music/Murmullos gente.mp3" fadein 1.5 volume 0.5 loop

    l "(Me siento mareada, la vista se me pone borrosa. y empiezo a escuchar mucho ruido.)"

    l "(Me tambaleo. Y antes de darme cuenta… pierdo la conciencia.)"

    hide Celia with dissolve

    stop music

    scene Negro with hpunch

    "..."

    "..."

    "Mamá."

    uu "Ahora no, estoy ocupada."

    "Necesito que vayas a un evento de la escuela... todos los padres irán y..."

    uu "Ya te dije que estoy ocupada, igual no es como si fuesen a darte un premio, siempre eres tan inutil."

    "...."

    "......"
    
    play music "audio/music/ES_Lost Years - Luella Gren.mp3" fadein 1.5 volume 0.5 loop

    scene Vagon 1 Morning with hpunch

    l Seria "(Me despierto después de un momento, me doy cuenta que estoy de regreso en mi asiento del tren.)"

    l Enojo "(Me duele mucho la cabeza.)"

    l Seria "(Todo está a la normalidad. Mi compañero está al frente de mi parece estar durmiendo.)"

    l "(Veo que los otros pasajeros están en sus asuntos.)"

    show Mathias Normal at right with dissolve

    l "(El intelectual sigue leyendo un libro...)"

    show Nadia Normal at left with dissolve

    l "(La niña está mirando a la ventana...)"

    hide Nadia with dissolve

    hide Mathias with dissolve

    l "???"

    l Sorpresa "(Me doy cuenta de que la mujer no está.)"

    l "(Me levanto de mi asiento y revisó todo el vagón...)"

    l "(No está por ningún lado.)"

    l Seria "(Voy a otros compartimentos, reviso uno por uno, después de ese sueño tan raro… quiero saber donde está ella.)"

    l "(Término en la cabina del capitán.)"

    l "(Sin saber por qué, decidió tocarle la puerta.)"

    show Sirius Feliz with dissolve

    s "Hola Layla! ¿Necesitas algo?"

    if Good >= 2:
        jump BONUS1
    else:
        jump NOBONUS1

label BONUS1: 
    l "Perdón por molestarte… tenía curiosidad por la mu... Celia."

    l "(Ni siquiera sabía con certeza si ese era su nombre, pero recordar su actitud me hizo llamarla de esa manera.)"

    show Sirius FelizOjosCerrados

    l "(Sirius me sonrió.)"

    s "Su viaje era uno corto, se bajó en la parada anterior."

    l "Ya veo..."

    show Sirius Normal

    s "Es bueno que se bajara, es una mujer difícil… nada le parecía cuando llegó."

    l "No está mal que hables así de tus pasajeros?"

    show Sirius Preocupacion

    s "Solo hablo así de los que no me agradan."

    l "Ya veo… volvere a mi lugar."

    show Sirius Normal 

    s "Layla..."

    l "(Volteo a mirarlo con curiosidad.)"

    show Sirius Muy Feliz 

    s "Fue bueno que la perdonaras."

    jump CONTI1

label NOBONUS1:
    show Sirius Normal

    l "¿Y la mujer?"

    s "Celia? Se bajó hace una parada."

    l "Parecía algo enojada."

    s "Hay personas no muy satisfechas con su vida que necesitan lastimar a los demás."

    l "No me agradan esas personas..."

    s "A mí tampoco... a veces son tan horribles que no merecen perdón."

    jump CONTI1

label CONTI1: 
    l "(No entiendo su comentario, pero el me mira como si supiera mas que yo.)"

    l "(Me despido de Sirius y regreso a mi compartimento.)"

    hide Sirius with dissolve

    l "(Sigue pareciendo extraño que ya no esté esa mujer... pero trato de ignorar el sentimiento.)"

    l "(El viaje prosigue. Veo a mi compañero aún dormido.)"

    scene Negro with dissolve

    l OjosCerradosSonrisa "(Lentamente, cierro los ojos....)"

    stop music

    l "...."

    l "(A decir verdad estoy muy agotada emocionalmente.)"

    l "(Y el tren avanza con un suave vaivén, como si buscara volver a arrullarme para hundirme otra vez en la inconsciencia.)"

    l "..."

    l "......"

    scene Vagon 1 noche with dissolve

    play music "audio/music/ES_Valse triste Nicoise - Magnus Ludvigsson.mp3" fadein 1.5 loop

    l "(Al despertar el tren está vacío de nuevo. Y antes de que suenen las indicaciones ya sé que es lo que me espera.)"

    l "(Dejo salir un suspiro.)"

    l Enojo "No otra vez..."

    l "(Escucho otra vez el ruido del altavoz.)"

    s "{color=#818589}{i} Llegamos a la segunda parada, por favor deben descender.{/i}{/color}"

    l "...."

    l Seria "(Yo no soy la clase de persona que sueña la misma cosa 2 veces, Y el anterior fue extremadamente agotador.)"

    l "(Sin embargo... la experiencia de ser empujada nuevamente de un tren prefiero saltarla...)"

    l "(Así que terminó bajando por voluntad.)"

    scene CorredorNoche with dissolve

    play music "audio/music/ES_Going Back - John Barzetti.mp3" fadein 1.5 loop

    l "(La puerta del tren se abre sola. Ya ni siquiera me sorprende.)"

    play sound "audio/sfx/Sonido de pasos.mp3" fadein 1.5 loop

    l "(Bajo... Aunque no quiero.)"

    l "(Me pregunto qué es lo que me está esperando aquí.)"

    l "(El aire de esta estación se siente distinto.)"

    l "(Más denso. Más caliente.)"

    l "(Como si hubiera un incendio invisible bajo el suelo.)"

    l "Genial... otro sueño raro."

    l "(Camino por el andén. Las losas están agrietadas, como si algo las hubiera golpeado muchas veces.)"

    l "(El cielo sobre mí es de un azul apagado que parece suplicar por una segunda oportunidad de amanecer.)"

    stop sound

    show Mathias Normal at right with dissolve

    l Sorpresa "(Entonces lo veo. Un hombre parado al final del pasillo.)"

    l "(Me doy cuenta que es el intelectual del tren. Parece más intimidante ahora.)"

    l "(No es nadie que recuerde de mi vida. Y no entiendo porque me da esta sensación de molestia en el pecho.)"

    l "¿Por qué... siento esto?"

    show Mathias Normal at center with move

    l Seria "(Doy un paso. El hombre inclina la cabeza hacia un lado, como si supiera que estoy ahí.)"

    u "Tarde otra vez."

    l "(Mi respiración se corta. Siento algo de deja vu.)"

    l "(Ese tono autoritario.)"

    l "(Ese desprecio escondido.)"

    l "(Ese aliento que siempre hacía temblar mis rodillas.)"

    l "N-no sé quién es usted."

    show Mathias CerradoSerio

    t "Mi nombre es Mathias, Y aunque no me conoces… aquí estás."

    t "Como siempre. Llegando tarde. Sin prepararte."

    l "(Mis manos se cierran en puños sin que yo lo note.)"

    l Enojo "(Me intimida su actitud de buscar mis fallas, y de clavar su mirada en mí como si fuese insignificante.)"

    show Mathias Sonrisa 

    t "¿Te vas a quedar ahí parada como una inútil?"

    l "(Mi garganta arde.)"

    l "...¿Qué dijo?"

    show Mathias OjoCerrados

    t "Lo que eres. Un caso perdido."

    label op4:
        menu: 
            "Explotar":
                $ Bad += 1
                jump op4A
            "Evitarlo":
                $ Neutral += 1
                jump op4B
            "Mantengo la calma":
                $ Good += 1
                jump op4C

label op4A:
    l "¡No me hable así! ¡Usted no me conoce!"

    show Mathias Sonrisa

    t "Claro que sí. Siempre fuiste sencilla de leer."

    t "Llorona, insegura, débil."

    jump op4CONTI

label op4B:
    l Seria "(No respondo.)"

    l "(No puedo.)"

    show Mathias Sonrisa

    t " ¿Nada? Típico. Te callas y esperas a que alguien te salve."

    jump op4CONTI

label op4C:
    l Seria "(Mantengo la calma.)"

    l "(Levantó la cabeza.)"
    
    l "No sé quién es usted, pero no voy a dejar que me humille."

    show Mathias Sonrisa

    t "¿Ah, no? Hace un minuto estabas temblando."

    l "(El hombre da un paso hacia mí.)"

    l "(Luego otro. Su presencia pesa.)"

    l "(Pesa como cuando tenía ocho años y estaba sola frente a un adulto que disfrutaba verme fallar.)"

    jump op4CONTI

label op4CONTI: 
    show Mathias Normal 

    t "Dime, Layla... ¿Cuántas veces te lo han dicho? Esforzarte no sirve de nada si eres mediocre."

    l "(Mi corazón retumba en mi pecho.)"

    l Triste "D-Deje de decir eso..."

    t "¿Por qué? ¿Acaso no es verdad?"

    l "(Algo dentro de mí se quiebra.)"

    l "(No tengo miedo. Es más ese sentimiento de ira que siempre tengo.)"

    l "(La que nunca tengo que mostrar porque siempre tengo que ser amable.)"

    l "(Esta persona no debería de afectarme pero me hace recordar cosas que pensé que ya tenía enterradas.)"

    l "(Las luces explotan en un destello breve.)"

    l "(Mi respiración se acelera.)"

    label op5: 
        menu:
            "Perdonar":
                $ Good += 1
                jump op5A
            "Indiferencia":
                $ Neutral += 1
                jump op5B
            "Rencor":
                $ Bad += 1
                jump op5C

label op5A:
    hide Mathias

    scene Negro with dissolve

    l "(Cierro los ojos, tragándome el orgullo y el rencor.)"

    l Triste "Ya no voy a vivir con miedo a alguien como usted. Se acabó."

    scene CorredorNoche

    show Mathias Normal

    l "(Cuando abro los ojos, el hombre me mira con una expresión que no entiendo.)"

    l "(Confusión. Molestia.)"

    l "(Luego su figura se deshace en humo oscuro.)"

    jump op5CONTI

label op5B: 
    l Enojo "No me importa. Nada de lo que tenga que decir me importa."

    l "(Me doy la vuelta. Camino sin verlo más.)"

    l "(Evadiendo la situación como lo he hecho siempre.)"

    l "(El hombre queda rígido, como una sombra sin dueño.)"

    jump op5CONTI

label op5C: 
    l Enojo "(Mi voz se rompe. Pero no en tristeza. En furia.)"

    with vpunch

    l "¡Lo odio! ¡Odio a los hombres como usted!"

    show Mathias Sonrisa

    l "(El hombre sonríe. Una sonrisa torcida.)"

    l "(De esas que parecen condescendientes y solo molestan.)"

    t "Al parecer nunca aprendes y si eres tan mediocre como pensaba."

    scene bg at my_shake

    l Sorpresa "(El suelo vibra como si algo respondiera a mis emociones.)"

    jump op5CONTI

label op5CONTI:

    l Seria "(Sin poder hacer otra cosa, siento como mis ojos se ponen pesados, y pierdo el conocimiento.)"

    stop music

    hide Mathias 
    
    scene Negro

    "...."

    "...."

    uu "Si no puedes hacer esto, Layla... ¿Para qué estás aquí?"

    uu "No entiendo porque prefiere a todos mis compañeros."

    uu "Ellos no muestran mediocridad, si realmente te interesara harías las cosas mejor."

    scene Vagon 1 noche with dissolve

    play music "audio/music/ES_Valse triste Nicoise - Magnus Ludvigsson.mp3" fadein 1.5 loop

    l "(Me despierto como recién salida de una pesadilla.)"

    l "(Siento los ojos pesados y me siento incluso más agotada que la última vez.)"

    with vpunch

    l Sorpresa "(Siento que me tocan el hombro y me sobresalto.)"

    show Sirius Preocupacion with dissolve

    l "(Veo a Sirius parado al lado de mi, mirándome con sorpresa.)"

    s "Lo siento, estaba revisando a los pasajeros, y no te veías muy bien."

    l Seria "No es nada, solo tuve una pesadilla. ¿No deberías estar conduciendo?"

    show Sirius Normal 

    s "Acaba de bajarse un pasajero."

    if Good >= 3:
        jump GOODEND
    else: 
        jump NOGOOD

label GOODEND: 
    l "Miro a mi alrededor y me doy cuenta que el intelectual ya no va sentado al lado de la niña."

    s "Iba de muy mal humor a decir verdad, parece que no tuvo la respuesta que quería."

    l Sorpresa "A que te refieres?"

    show Sirius Feliz 

    l Seria "(Sirius solo me sonrio como si no fuera la gran cosa.)"

    s "Nada que deba preocuparte."

    jump FINALEND

label NOGOOD: 
    l "Miro a mi alrededor y me doy cuenta que el intelectual ya no va sentado al lado de la niña."

    s "Iba de excelente humor, dijo que le encantaba tener la razon."

    l Sorpresa "A que te refieres?"

    l "(Sirius solo me mira con un poco de desaprobación.)"

    s "No te preocupes, solo hablo a la nada, pero si me lo permites, considero que deberias de cuidar un poco más tus asuntos."

    jump FINALEND

label FINALEND: 
    show Sirius FelizOjosCerrados

    s " Bueno, me despido, tengo que volver a manejar este tren."

    hide Sirius with dissolve 

    l Seria "(Sirius se va y me quedo pensando en las cosas mirando a la ventana. Ya es muy tarde de todos modos.)"

    u "Disculpa..."

    l "(El pasajero sentado enfrente de mi habla, y recuerdo desde hace un tiempo ha estado queriendo hablarme.)"

    l "¿Pasa algo?"

    u "No se si me recuerdas... íbamos juntos a la escuela,"

    a "Me llamo Arnold."

    l "Lo miro de arriba a abajo, a decir verdad si se me hacía bastante familiar."

    l "A decir verdad no recuerdo mucho, pero igual pensaba que eras bastante familiar."

    a "Es muy curioso volverte a encontrar justo aquí."

    a "Este viaje esta siendo muy raro, he estado teniendo unos sueños extraños y..."

    l "(Nuestra platica se ve detenida por el ruido del altavoz.)"

    s "{color=#818589}{i}Lamentamos las demoras, seguiremos avanzando.{/i}{/color}"

    s "{color=#818589}{i}Les agradecemos su preferencia{/i}{/color}"

    s "{color=#818589}{i}y recuerden que este puede ser su viaje final... así que usen sus cinturones en todo momento.{/i}{/color}"

    l Sorpresa "(Este anuncio es raro, es la primera vez en todo el viaje que Sirius realiza un comentario así.)"

    scene Negro with dissolve

    play music "audio/music/ES_Hidden Beneath - Rikard From.mp3" fadein 1.5 loop

    "HAS LLEGADO AL FINAL DE LA DEMO DE EL ÚLTIMO PASAJERO"

    "Este es solo el comienzo del viaje de Layla."

    "Aún quedan verdades que enfrentar… y heridas que sanar."

    "Gracias por jugar."

    return
