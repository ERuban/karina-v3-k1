## FLASHEO de las radios Quansheng UV-K5V3 y K1

### y trabajo con CHIRP

**ANTES DE HACER NADA EN ABSOLUTO:**

**1.**
**¡¡¡Asegúrate de que tienes una versión K1 o K5V3!!!**

**La versión V1 no lleva ninguna marca.**
**Las versiones V2 y V3 suelen llevar la marca correspondiente en la etiqueta**
**que hay bajo la batería.**

![screenshot](images/p01_3.png)

![screenshot](images/p01_1.png)

**El firmware NO es intercambiable entre versiones. Si intentas flashear una radio**
**con firmware destinado a otra versión, acabarás con una radio inutilizada (brickeada).**

Las versiones V1 tienen un bootloader que empieza por 2, 3, 4 o 5
Las versiones V2 tienen un bootloader que empieza por 1
Las versiones V3 tienen un bootloader que empieza por 7

Puedes comprobarlo en k5prog-win con la radio conectada en modo flasheo:

![screenshot](images/p01_2.png)

**Haz una COPIA DE SEGURIDAD de las calibraciones de fábrica**

**CONTENIDO:**

**1. BREVE RESUMEN DE LA INSTALACIÓN DEL FIRMWARE KARINA (Autumn rain)**
**en las radios Quansheng UV-K5(V3) y UV-K1.**

**2. Procedimiento detallado de instalación del firmware.**

**3. USO DE CHIRP.**
3.1. Descarga del módulo
3.2. Uso del módulo con CHIRP (Karina)
3.3. Copiar frecuencias desde el fichero de otra persona.

**4. PREGUNTAS FRECUENTES, POSIBLES PROBLEMAS Y CÓMO RESOLVERLOS.**

## 1. BREVE RESUMEN DE LA INSTALACIÓN DEL FIRMWARE KARINA (Autumn rain)

**en las radios Quansheng UV-K5(V3) y UV-K1:**

**Estas instrucciones sirven únicamente para flashear la K5(V3) o la K1.**
**Intentar cargar firmware de K5V3 (o de K1) en una radio K5V1 = radio inutilizada.**

**Si ya tienes experiencia flasheando, este procedimiento breve es para ti.**
**Si no la tienes, más abajo encontrarás un procedimiento más detallado con explicaciones e imágenes.**

**Antes de flashear, CARGA LA BATERÍA POR COMPLETO.**

**BREVE RESUMEN DE LA COPIA DE SEGURIDAD Y DEL FLASHEO**

**1.** Enciende la radio y conéctala por USB Type-C (o con un cable Kenwood).

**2.** Haz una copia de seguridad de las calibraciones de fábrica y de la configuración.

**3.** Apaga la radio y vuelve a encenderla manteniendo pulsada la tecla PTT.

**4.** Instala el firmware con la herramienta de flasheo que prefieras
(el fichero con el índice `packed` – para la herramienta de flasheo de fábrica **qpscps** / el fichero SIN el
índice `packed` – para cualquier otra herramienta de flasheo).

**5.** **¡¡¡DESCONECTA EL CABLE DEL ORDENADOR!!!** Apaga la radio y vuelve a encenderla manteniendo
pulsadas **PTT+EXIT** (mantenlas unos 2 segundos) – la memoria se borra.

**6.** Abre de nuevo la herramienta de flasheo y vuelve a escribir las calibraciones de fábrica.

**7.** Escribe las calibraciones que se suministran con el firmware **Karina**.

**8.** Vuelve a escribir la configuración (si es necesario).
Como alternativa, configúralo todo a mano desde el menú de la radio o mediante CHIRP
*(solo funcionarán las configuraciones de versiones anteriores; los ficheros de configuración de otros*
*firmware*
*no funcionarán).*

**¡¡¡ATENCIÓN!!!**
**Si configuras los 3 presets por separado (ver el punto 35 del menú de ajustes), debes**
**realizar los pasos 5-8 por separado para cada uno de ellos, seleccionando previamente el preset**
**necesario en el punto 35. ¡¡¡!!!**

**Recordatorio:**

**Las calibraciones y la configuración se leen y se escriben** con la radio encendida
en modo normal.

**El flasheo** se hace con la radio encendida en modo flasheo (con la radio apagada, mantén pulsado PTT y,
sin soltarlo, enciende la radio). La pantalla permanecerá apagada y el LED de la linterna
se encenderá para indicar que la radio está en modo flasheo.

## 2. PROCEDIMIENTO DETALLADO DE INSTALACIÓN DEL FIRMWARE

**Antes de flashear, CARGA LA BATERÍA POR COMPLETO.**

**1.** Enciende la radio y conéctala por USB Type-C (o con un cable Kenwood).

**¡¡¡ Las radios Quansheng UV-K1 fabricadas para el mercado chino** tienen problemas con la
conexión USB Type-C; con ellas es mejor usar un cable Kenwood.

![screenshot](images/p03_1.png)

Versión para el mercado europeo

Versión
para el
mercado
chino

**2.** **HAZ UNA COPIA DE SEGURIDAD DE LAS CALIBRACIONES Y DE LA CONFIGURACIÓN**

Para ello, abre **k5prog-win** (se recomienda la versión v0.1.26) y haz la
copia de seguridad:

Calibraciones: pulsa **read calibration** y guarda las calibraciones de fábrica.
Configuración: pulsa **read configuration** y guarda la configuración de fábrica.

![screenshot](images/p03_2.png)

**3.** Apaga la radio y vuelve a encenderla manteniendo pulsada la tecla PTT.

**4.** Abre el programa nativo **qpscps** ( https://en.qsfj.com/support/downloads/8740 ),
selecciona el puerto COM y el menú de flasheo (alt+D, el tercer elemento).

![screenshot](images/p04_1.png)

Indica la ruta al fichero **packed** y flashea la radio pulsando **Update**.

![screenshot](images/p04_2.png)

*(Si vas a flashear en línea a través del sitio https://armel.github.io/uvtools2/, en la pestaña* ***Flash***
***Firmware*** *pulsa* ***Choose file*** *y selecciona el firmware sin el índice* ***packed****,*

![screenshot](images/p04_4.png)

![screenshot](images/p04_3.png)

*pulsa* ***Flash firmware****, selecciona el* ***COM port*** *y flashea la radio.)*

**5.** **¡¡¡DESCONECTA EL CABLE DEL ORDENADOR!!!** Apaga la radio y vuelve a encenderla manteniendo
pulsadas **PTT+EXIT** durante unos 2 segundos – la memoria se borra.

**6.** Abre de nuevo **k5prog-win** y vuelve a escribir las calibraciones de fábrica con el
botón **Write calibration**.

![screenshot](images/p05_1.png)

*(Esto también se puede hacer a través del sitio https://armel.github.io/uvtools2/ (si guardaste las calibraciones*
*con* ***k5prog-win****, debes cambiar la extensión del fichero de* ***bin*** *a* ***dat****). Para ello, en la pestaña*
***Restore Calib*** *selecciona el fichero necesario con el botón* ***Choose file****, pulsa* ***Restore***
***Calibration Data****, selecciona el* ***COM port*** *y escribe las calibraciones.)*

![screenshot](images/p05_3.png)

![screenshot](images/p05_2.png)

**7.** Escribe las calibraciones una vez más, seleccionando esta vez las calibraciones de Karina (en el momento de
escribir estas instrucciones es **calib5**) – siguiendo el mismo procedimiento que en el paso 6.

**8.** Vuelve a escribir la configuración usando **k5prog-win** y el botón **Write configuration**.
*(Solo funcionarán las configuraciones de versiones anteriores; los ficheros de configuración de otros firmware*
*no funcionarán.)*

![screenshot](images/p05_4.png)

## SI NECESITAS ABANDONAR EL FIRMWARE KARINA

(dado que su distribución de memoria difiere de la de otros firmware)
debes hacer lo siguiente:

**1. Borra la memoria** (apaga la radio y vuelve a encenderla manteniendo pulsadas las teclas PTT+EXIT (mantenlas unos 2 segundos))

**2. Instala cualquier otro FIRMWARE MODIFICADO** (el firmware de fábrica no sirve, porque no permite escribir los datos de calibración)

**3. Vuelve a escribir tus datos de calibración originales de fábrica.**

**4. Usa la radio**, o instala lo que quieras (incluido el firmware de fábrica), según prefieras.

## 3. USO DE CHIRP

### 3.1. Carga del módulo

**¡¡¡IMPORTANTE!!!** Por el momento no existe un módulo de CHIRP dedicado al firmware Karina. Hay módulos escritos para otros firmware que son más o menos compatibles con Karina. El módulo que se indica a continuación se escribió originalmente para el firmware F4 y se ha adaptado a Karina en algunos puntos. Aun así, no deberías cambiar todo lo que veas desde CHIRP, porque la compatibilidad no es completa.

Al usar CHIRP tienes que cargar un módulo en él (*para Karina usa el módulo del archivo comprimido*; **para otros firmware debes elegir el módulo que les corresponda**). Para ello, inicia CHIRP, haz clic en "HELP" y activa el modo desarrollador. Después reinicia CHIRP, abre el menú "File", selecciona "Load module" y elige el fichero del archivo comprimido.

![screenshot](images/p07_1.png)

![screenshot](images/p07_2.png)

**¡¡¡ IMPORTANTE:** el módulo se descarga al cerrar CHIRP, así que hay que volver a cargarlo cada vez que inicies CHIRP.

**A continuación:** Radio -> Download from radio -> selecciona el puerto COM -> Vendor (Quansheng) -> en el campo Model, el módulo correspondiente a tu firmware.

![screenshot](images/p07_4.png)

![screenshot](images/p07_3.png)

### 3.2. Uso del módulo con CHIRP (Karina)

Como se ha dicho antes, no es aconsejable cambiar todas las funciones en CHIRP, porque el módulo no es totalmente compatible. A continuación hay un ejemplo de lo que se puede editar con seguridad (**marcado en verde**) y lo que se recomienda encarecidamente no tocar (**marcado en rojo**):

**En la primera pestaña**, la de los canales de memoria, todo se puede editar con seguridad.

**En la segunda pestaña, Basic Settings**, puedes cambiar libremente las siguientes funciones (todas ellas, salvo el mensaje de bienvenida, también se pueden cambiar desde el menú de la radio):

![screenshot](images/p08_1.png)

**En la segunda pestaña, Programmable Keys**, puedes cambiar los ajustes de las teclas laterales FN1 y FN2. Estos ajustes solo se pueden cambiar desde el software; no se pueden cambiar desde el menú de la radio:

![screenshot](images/p08_2.png)

Asegúrate de que a las teclas laterales se les asignan valores tanto para la pulsación corta como para la pulsación larga (si se deja NONE, ¡la radio se bloquea y pide un código!).

**En la segunda pestaña, ScanList**, puedes establecer la lista de escaneo predeterminada y elegir los canales prioritarios para el escaneo en las listas de escaneo 1 y 2 (estos ajustes están disponibles tanto desde CHIRP como desde el menú de la radio):

![screenshot](images/p09_1.png)

**En la segunda pestaña, Unlock Settings**, puedes seleccionar el bloqueo de transmisión para el plan de frecuencias (estos ajustes están disponibles tanto desde CHIRP como desde el menú oculto de la radio):

![screenshot](images/p09_2.png)

**En la segunda pestaña, FM Broadcast Receiver**, puedes asignar las frecuencias de las emisoras de radiodifusión FM guardadas en memoria (estos ajustes están disponibles tanto desde CHIRP como desde el menú oculto de la radio):

![screenshot](images/p09_3.png)

### 3.3. Copiar frecuencias desde el fichero de otra persona

No es aconsejable cargar en tu radio el fichero de frecuencias de otra persona, ni un fichero de un firmware distinto. CHIRP y PSCPS cargan esencialmente una Configuración (los ajustes de la radio), y su estructura puede diferir entre versiones de firmware (e incluso entre distintas versiones del firmware de un mismo desarrollador).

Cargar un fichero de configuración ajeno de ese tipo puede volver inestable la radio (sin recepción, mala recepción, problemas con la transmisión o la modulación, etc.).

**Si necesitas copiar frecuencias desde el fichero de otra persona a una radio con Karina, haz lo**
**siguiente:**

- Ábrelo en CHIRP (cargando antes el módulo necesario, si hace falta — los módulos pueden diferir de un firmware a otro)
- carga el módulo de Karina
- conecta la radio al ordenador y elige Radio -> Download From Radio; en el menú que se abre, selecciona el puerto, el fabricante de la radio y el módulo necesario

![screenshot](images/p10_1.png)

![screenshot](images/p10_2.png)

Entonces tendrás dos pestañas abiertas: el fichero "donante" y tu propia radio.

- en la pestaña del "donante", selecciona las frecuencias que necesites y elige Copy; después cambia a la pestaña de tu propia radio, selecciona la primera fila a partir de la cual quieras empezar y pega las frecuencias. *(abajo hay un ejemplo de copia de datos entre dos radios incompatibles, una Baofeng y una Quansheng)* - **este tipo de copia es seguro, porque copia únicamente los canales (sus frecuencias, nombres y ajustes) y no afecta a los ajustes generales de la radio**

![screenshot](images/p10_4.png)

![screenshot](images/p10_3.png)

## 4. PREGUNTAS FRECUENTES, POSIBLES PROBLEMAS Y SOLUCIONES

**Problemas y preguntas — posibles soluciones, comentarios y respuestas.**

### Después de instalar y configurar el firmware, no se puede introducir una frecuencia en modo VFO

Al instalar el firmware, el cable DEBE estar desconectado del ordenador antes de realizar el borrado de memoria con PTT+EXIT. Hay que ejecutar de nuevo el borrado, después escribir los datos de calibración y configurar la radio.

### 1. ¿En qué frecuencias se me permite transmitir?

Existen frecuencias de radio civiles cuyo uso está permitido sin licencia. Por regla general son:

- CB (25.165 – 29.445 MHz) con una potencia de transmisión de 4.0-12.0 W
- LPD (433.075 – 434.775 MHz) con una potencia de transmisión de 0.01 W
- PMR (446.00625 – 446.19375) con una potencia de transmisión de 0.5 W

En algunos países se usan además las bandas FRS y GMRS.

### 2. ¿En qué frecuencias no se me permite transmitir?

Sin permisos especiales, transmitir fuera de las bandas civiles está prohibido por ley. Todas las demás bandas de frecuencia las utilizan otros servicios, desde radioaficionados hasta servicios gubernamentales, incluyendo satélites, redes de telefonía móvil, controladores aéreos y aeronaves, estaciones meteorológicas, comunicaciones fluviales y marítimas, el ejército y otros. Si interfieres en el funcionamiento de alguno de estos servicios, puedes incurrir en responsabilidad conforme a la legislación de tu país.

### 3. ¿En qué frecuencias recibe y transmite la Quansheng UV-K5?

En el firmware Karina, la recepción y la transmisión están abiertas en todas las bandas (ver la sección 2.2, Bandas de frecuencia de trabajo).

En radios sin modificación de hardware, solo se puede transmitir sin riesgo de quemar la radio dentro de las bandas declaradas por el fabricante: 136-174 MHz / 400-470 MHz.

### 4. ¿Qué pasa si transmito sin antena?

Transmitir sin antena, y también con una antena sintonizada para otra banda de frecuencia, quema la etapa de salida de la radio.

### 5. ¿La radio transmite en la banda CB? ¿Puedo hablar con camioneros?

En el firmware Karina la banda de 27 MHz está abierta por defecto tanto para recepción como para transmisión.

Para recibir, necesitas una antena sintonizada para esta banda.

Sin embargo, transmitir en esta banda con una radio que no ha sido modificada a nivel de hardware no proporciona una comunicación utilizable (la potencia de salida es muchísimo más baja de lo necesario). Al mismo tiempo, debido a las características físicas de la radio, un intento de transmitir en esta banda genera interferencias en la banda aérea y además quema la etapa de salida de la radio.

### 6. ¿Por qué nadie me oye en CB?

De fábrica, la potencia de transmisión de la radio en la banda CB no supera los 0.01 W. En consecuencia, sin una modificación física, transmitir en esta banda no solo es inútil, sino también peligroso para la propia radio.

### 7. ¿Por qué la comunicación es mala dentro de un coche?

La carrocería del coche apantalla las señales de radio. Para una comunicación estable se recomienda montar una antena externa fuera de la carrocería.

### 8. ¿Para qué flashear la radio?

Una radio de fábrica, recién sacada de la caja, funciona de forma fiable y cumple sus funciones.

El firmware modificado amplía la funcionalidad de la radio, ofreciendo ajustes adicionales y más flexibles (profesionales), mayor velocidad de escaneo, escaneo con representación gráfica (modo analizador de espectro), etc.

### 9. ¿Cuál es el mejor firmware?

El que mejor se adapte a tus necesidades.

### 10. ¿Cómo guardo el firmware de fábrica?

No tiene sentido guardar el firmware de fábrica, porque está disponible libremente en internet y en la web del fabricante. Es mucho más importante guardar los datos de calibración originales (que pueden ser únicos de tu radio) y el fichero de configuración. Esto se hace con el programa k5prog.

### 11. El ordenador no ve la radio cuando se conecta por el puerto Type-C integrado

El puerto Type-C integrado en la radio está pensado únicamente para cargar la batería.

El flasheo se hace con un cable de programación especial con conector de tipo KENWOOD (sirve un cable de radios Baofeng analógicas y similares).

### 12. ¿Sirve un cable de Baofeng para flashear y programar?

Sí, sirve (uno de radios analógicas).

### 13. ¿Por dónde empiezo el flasheo?

Cualquier flasheo debe empezar comprobando la carga de la batería. Si la batería está cargada por debajo del 50% (~7.2 V), el proceso de flasheo puede resultar defectuoso o incompleto.

Para flashear necesitas comprar o fabricar un cable de flasheo con conector de tipo Kenwood e instalar el driver de ese cable en el PC.

Prepara la herramienta de flasheo. Prepara el propio fichero de firmware. Conecta la radio encendida al PC con el cable que has comprado y usa el programa para hacer una copia de seguridad de tus datos de calibración y del fichero de configuración. Después conecta la radio en modo flasheo y usa el programa para escribir el fichero de firmware.

### 14. ¿Dónde puedo encontrar instrucciones detalladas de flasheo?

Consulta la sección GUÍA RÁPIDA DE FLASHEO PARA LA QUANSHENG UV-K5 Y SUS VARIANTES.

### 15. El ordenador no ve la radio

- El cable no está insertado hasta el fondo en la radio (la primera vez entra muy apretado, a menudo hasta que se oye un clic).
- El driver del cable no está instalado, o está instalado el driver equivocado.

### 16. ¿Qué programa debo usar para flashear?

El firmware modificado debe flashearse así:

- las versiones UV-K5, K5(8) y K5+ deben flashearse con k5prog-win — se recomienda la versión 1.26;
- la versión UV-K5+ (con puerto Type-C) debe flashearse con k5tools.

### 17. He flasheado la radio, pero al encenderla pide una especie de contraseña

Prueba con todos los dígitos iguales — 000000 o 111111 — o con 123400, o mantén pulsadas MENU+EXIT con la radio apagada y enciéndela sin soltarlas.

Además, si al configurar mediante CHIRP o PSCPS pusiste las teclas laterales FN1 y/o FN2 en NONE (sin asignar), la radio puede bloquearse y pedir un código al encenderse.

Si eso no ayuda, borra la memoria de la radio con el firmware REBORN — ver la sección 6 de esta guía.

### 18. ¿Qué programa debo usar para programar (configurar) la radio?

CHIRP o PSCPS. Para usar CHIRP necesitas cargar el módulo.

### 19. ¿Qué es CHIRP y qué puede hacer?

Es un programa para programar radios. Edita canales y activa y desactiva diversas funciones, incluidas las que no están disponibles desde el propio menú de la radio.

### 20. He escrito mis frecuencias guardadas (de un firmware distinto) o el fichero de frecuencias de otra persona, y la radio se comporta de forma extraña

Los ficheros de configuración de versiones de firmware distintas pueden hacer que la radio funcione incorrectamente, por eso no se recomienda escribirlos. Tampoco se recomienda escribir ficheros de configuración y ajustes de otras personas.

Si necesitas escribir frecuencias del fichero de otra persona (o de un fichero tuyo, pero hecho con un firmware distinto), usa CHIRP: abre el otro fichero, lee tu radio — aparecerá una segunda pestaña — y después copia las frecuencias que necesites desde la pestaña del otro fichero y pégalas en la pestaña de tu radio. No olvides cargar el módulo adecuado antes de leer los ficheros.

### 21. ¿Tiene la radio cifrado?

La radio no tiene cifrado de la señal, pero sí dispone de una función de scrambler (enmascaramiento de voz). Ten en cuenta que en muchos países el uso de cifrado, scramblers y otras funciones de enmascaramiento de la señal en la radiocomunicación civil está prohibido por ley.

### 22. ¿Por qué se enciende el LED verde en recepción mientras el altavoz permanece en silencio?

- comprueba si tienes configurados subtonos de recepción (R-DCS y R-CTCS);
- comprueba que ambas radios usan la misma modulación (en particular FM).

### 23. ¿Qué es un subtono?

Un subtono es una señal adicional, inaudible para el oído humano, que se transmite junto con la voz. Actúa como una especie de identificador "amigo o enemigo" (filtrando la señal entrante). Si hay un subtono configurado, tu radio rechazará todas las señales en esa frecuencia y solo abrirá la recepción cuando detecte una señal con el mismo subtono.

Una radio sin subtono, en cambio, oirá en recepción a todas las demás radios, tanto a las que usan subtono como a las que no.

### 24. ¿Qué es el subtono no estándar de 55 Hz que detecta el escáner?

Consulta la descripción en el manual del firmware Karina, punto 22, página 5.

### 25. ¿Por qué oigo a un corresponsal y al otro no?

Significa que la señal de un operador es lo bastante fuerte para que lo oigas, mientras que la del otro es demasiado débil.

Esto puede deberse a que tu antena no es muy eficiente, a que uno de los operadores está más cerca de ti, o simplemente a que la señal del segundo operador es demasiado débil.

También es posible el caso contrario: la señal de uno de los corresponsales es tan fuerte que satura tu receptor, que entonces se "atraganta" con la señal excesivamente fuerte y permanece en silencio.

### 26. He puesto la radio a escanear frecuencias, ¿por qué no oigo a nadie?

Para oír a alguien, primero hay que decidir dónde escanear. Escanear "todo a la vez" no te llevará a ninguna parte.

Por ejemplo, quieres escanear el rango de 100-200 MHz con un paso de 25 kHz (la velocidad de escaneo en modo frecuencia (VFO) es de unas 15 frecuencias por segundo), lo que da:

100/((0.025)*15)=266 segundos (o casi 5 minutos) por cada pasada de escaneo. Es mucho más eficiente estrechar el rango de búsqueda o iniciar el escaneo en modo analizador de espectro usando los presets configurados.

### 27. ¿Puedo pedir ayuda con la radio?

En casos excepcionales, y únicamente **cuando exista una amenaza directa para la vida y la salud de las personas y no haya forma de pedir ayuda por otros medios técnicos de comunicación**, puedes enviar una señal de socorro SOS o MAYDAY.

### 28. ¿En qué frecuencias es mejor pedir ayuda para que me oigan?

No existen frecuencias de socorro universalmente aceptadas. Hay frecuencias marítimas, fluviales, de emergencia en montaña, etc. Estas frecuencias también pueden variar de una región a otra y de un país a otro. Cuando planifiques un viaje a una región concreta, es aconsejable informarse al menos de qué frecuencias de comunicación de emergencia se usan allí.

Sin embargo, sí existen frecuencias de llamada de uso común en las que tienes más posibilidades de ser oído:

- 433.500 — la frecuencia general de llamada de la banda de 70 cm
- 446.09375 — la frecuencia general de llamada de la banda PMR
- 145.500 — la frecuencia general de llamada de los radioaficionados (para comunicación entre radioaficionados con licencias y permisos)

Estas frecuencias también pueden variar según la región. No se recomienda ocuparlas con conversaciones largas. Siempre puedes establecer el contacto y después pasar a otras frecuencias de común acuerdo.

### 29. ¿Qué es el símbolo S que se enciende de vez en cuando en la esquina superior izquierda?

Consulta la descripción en el manual del firmware Karina, punto 14, página 5.

### 30. ¿Por qué, cuando cambio la potencia de transmisión (o el ancho de banda, o la modulación, o el subtono, o el desplazamiento de frecuencia), los cambios no se guardan al pasar a otro canal y volver, o al apagar y encender la radio?

Consulta la descripción en el manual del firmware Karina, punto 13, página 5.

### 31. Cuando pulso PTT la pantalla muestra DISABLE, ¿qué hago?

Consulta la descripción en el manual del firmware Karina, puntos 36 y 37, página 7.

### 32. He conectado un cable Type-C a la radio, pero no carga

La carga por Type-C es una opción adicional. Comienza a una tensión de batería más baja y no carga la batería hasta su valor nominal. Si puedes cargar la radio en la base de carga, usa la base de carga.

### 33. Mi radio muestra la tensión de la batería de forma incorrecta, ¿qué hago?

Si la tensión de la batería en la pantalla de la radio es inverosímilmente baja (~0.25 V) o inverosímilmente alta (600 V), esa es la primera señal de que tus datos de calibración están corruptos: tienes que escribir primero la calibración de fábrica y solo después la calibración de Karina.

Si eso no ayuda, realiza el borrado de memoria tal como se describe en el manual del firmware, y después instala de nuevo el firmware y los datos de calibración.

Si la tensión se muestra más o menos correctamente, con una desviación de unos 0.2-0.5 V respecto al valor medido con un multímetro, esta es la situación normal con la calibración de fábrica. Se puede ajustar en un editor HEX cambiando el valor de la celda 140/6 del fichero de calibración (en mi caso este valor es B0, pero el tuyo puede ser distinto).

### 34. ¿Por qué la pantalla muestra 6.0 V mientras la radio ya se está apagando?

El rango de tensión de trabajo de la batería es ~6.0 V - 8.4 V:

- ~8.4 V = 100%
- ~7.2 V = 50%
- ~6.0 V = 0%

Descargar la batería por debajo de 4 V provoca su degradación.
