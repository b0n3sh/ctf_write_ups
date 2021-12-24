<h1>INICIO DEL RETO</h1> 
<img src="images/init.png" alt="init" title="" />
<p>Empezamos con un .pcap en el cual se encuentra la traza de un actor malicioso que exfiltró un fichero de un servidor.</p>

<p>Abrimos el .pcap con el WireShark y nos encontramos lo siguiente:</p>

<p><img src="images/1.png" alt="wireshark_pcap" title="" /></p>

<p>A continuación vemos que el fichero se ha enviado usando <a href="http://www.columbia.edu/kermit/ck90.html">Kermit</a> el cual es un software de comunicación de los 80 que permite transferir archivos entre terminales.</p>

<p>Por lo tanto tendremos que "deshacer" lo que el protocolo del Kermit haga a la hora de enviar los paquetes y poder extraer el archivo.</p>

<p>Además, si nos fijamos, el archivo está codeado en base64, lo que nos será de utilidad más adelante:</p>

<img src="images/2.png" alt="base64" title="" /><

<h2>Hora de leer la documentación</h2>

<p>Lo primero es entender cómo funciona el protocolo antes de darse cabezazos contra la pared (no sigáis mis pasos...), por lo que acudimos a <a href="https://www.kermitproject.org/kproto.pdf">Kermit Protocol Manual</a> en el que se nos explica con todo tipo de detalles su funcionamiento.</p>

<p>Resumiendo un poco, lo que hace el Kermit es pasar a ASCII-friendly todos los bytes que se van a enviar por la línea, de manera que sea "universal" y no haya confusiones a la hora de interpretar paquetes.</p>

<p>Las 3 claves que nos conciernene a la hora de deconstruir nuestro archivo son:</p>

<ul>
<li>Negociación previa al envio de datos</li>

<li>Qué estructura tendrá cada paquete?</li>

<li>Repeat Count Prefixing</li>

<li> Window size </li>
</ul>

<h2>Analizando la negociación</h2>

<p>Todos los paquetes de Kermit se componen de lo siguiente: <p>
<img src="images/3.png" alt="kpackets" title="" />
<ul>
<li> Mark especifica el principio del paquete (generalmente, SOH 0x01)</li>
<li> LEN la longitud del paquete (este parámetro es uncontrollified, es decir, tenemos que restarle 32, ya que es lo que lo convierte en ASCII friendly.</li>
<li> SEQ es para el ACK, también es uncontrollified, por lo que tenemos que restarle 32.</li>
<li> TYPE nos indicará qué tipo de paquete es, data, ack, nack, init, end of file....</li>
<li> DATA lo que nos interesa</li>
<li> CHECK para comprobación de errores</li>
</p>
</ul>

<p>Visto esto, sabemos que tenemos que encontrar un paquete en el cual tenga en su campo TYPE, el valor S ( de Send initiate): </p>

<img src="images/4.png" alt="type" title="" /></p>

<p>Si nos vamos al WireShark, conociendo ahora cómo se componen los paquetes de Kermit, encontramos el send initiation: </p>

<img src="images/5.png" alt="pcap_initation" title="" /></p>

<p>Por lo tanto tenemos, el inicio del paquete en rojo, en amarillo el LEN, en azul la SEQ, en verde el TYPE, que como podemos ver, tiene el valor 0x53, que en ASCII es una "S" (lo podemos ver en la representación de la derecha), en morado la negociación y 0d 00 en marrón, el final del paquete.</p>

<p>De la negociación, los paquetes que nos interesan son:
<ul>
<li> CHKT</li>
<li> REPT</li>
<li> QCTL</li>
<li> CAPAS </li>
</ul>
</p>

<p>En la documentación está bien detallado, pero para hacer un breve resumen:</p>

<h3> CHKT </h3>

<p>El type de check que se va a realizar, en nuestra negotiation tenemos el valor 3, lo que hace un CRC-CCIIT (3 bytes) esto es importante a la hora de extraer el fichero.</p>

<h3> REPT </h3>

<p> Cuando un carácter se repite, Kermit no printa "AAAA" por ejemplo, usa la siguiente notación ~$A , ~(tilde) indica que el siguiente valor va a ser el cuantificador del número de repeticiones (este carácter es ascii-friendly, por lo que en realidad tenemos que restarle -32 para saber el valor numérico real, es decir $ tiene el valor 36 en ascii, le quitamos 32, 36-32 = 4  repeticiones) y el siguiente valor, la A, se repetirá 4 veces.</p>

<h3> QCTL </h3> 

<p> Nos indica el carácter que va a preceder los escapes de CTRL, por ejemplo si Kermite envía un CTRL+J, simplemente enviará #J.</p>

<h3> CAPAS </h3> 

<p> Aquí podemos ver que el bitmask de "Extended packet" está marcado, lo que le permite a Kermit enviar varios paquetes sin esperar los ACKS, además de esto se incrementa el header el paquete, por lo que tenemos que tenerlo en cuenta. </p>

<p>Bien, ya hemos avanzado un poco más.</p>
<p> Estos flags y configuraciones que hemos visto en la negociación del Kermit, nos van a cambiar un poco la estructura de cómo van a ser los paquetes, veamos como quedarían: </p>

<img src="images/ext.png" alt="extende" title="" /><br>

<p> Solo nos interesan los paquetes de data, tendremos que borrar los 3 primeros bytes antes de cada "0x0d 0x00" y los 7 bytes siguientes, 3+2+7 = 12 bytes. </p>

<p>A continuación buscamos el/los paquetes que haya envíado Kermit con el TYPE D de data, para trabajar más cómodamente nos lo llevamos a la terminal, la parte amarilla es de kermit (MARK, LEN, SEQ, TYPE, LENX1, LENX2, HCHECK) y la verde es nuestra data, he marcado a modo de ejemplo un par de count repeaters (en azul) y un par de escaped CTRL, en rojo, que indicarían LINE FEED un salto de página: </p>
<img src="images/6.png" alt="packs" title="" /></p>

<p>Una vez en el terminal extraemos solo la parte hexadecimal que será con la que trabajemos, y escribí un pequeño programa para realizar la limpieza de forma automática, el programa se encarga de: 
<ol>
<li> Quita todos los bytes que inician el paquete, teniendo en cuanta que lleva headers extendidos, su checksum y el final, lo que se traduciría en un simple regex de (0xXX 0xXX 0xXX 0d 00 01 0xXX 0xXX 0xXX 0xXX 0xXX 0xXX)</li>
<li> Para los hex a su representación en ASCII</li>
<li> para #J, sustituye por \n y para las repeticiones, haz la lógica pertinente</li>
</ol>
</p>

<img src="images/script.png" alt="script" title="" />
<p>Y con esto ya tendríamos nuestra imagen en b64, con uudecode extraemos la imagen: </p>

<p><img src="images/7.png" alt="first" title="" /></p>

<p>Con binwalk extraemos de la imagen un .ogg, el cual si abrimos se rie de nosotros.</p>

<p>Después de mirar el espectograma del archivo, los LSB, vemos que si pasamos le binwalk (fail), nos muestra que detecta un 7z (pero no es un 7z, o sí?): </p>
<img src="images/8.png" alt="7z" title="" />

<p>Tras leer bastante, vemos que es un binary polyglot (archivos que son válidos para varios formatos), por lo que simplemente extraemos como si fuera un 7z.</p>

<p>Lo cual abrimos el .cpio y encontramos 2 archivos, un txt y un html cifrado: </p>
<img src="images/9.png" alt="ll" title="" /><br>
<img src="images/10.png" alt="ssl" title="" />

<p>Abrimos el .txt y encontramos un villancico donde nos dice que puede que la contraseña esté ahí: </p>
<img src="images/11.png" alt="chant" title="" /></p>

<p>A continuación hacemos bruteforce con las keywords del txt, hasta que damos con la buena, que es Christmas: </p>
<img src="images/12.png" alt="bf" title="" /></p>

<p>Abrimos el html y...</p>

<img src="images/13.png" alt="final" title="" />

<p>Felices fiestas a todos! Y muchas gracias <a href="https://twitter.com/NN2ed_s4ur0n/">@s4ur0n</a> por el reto!</p>
<img class="logo_footer" src="images/s4u_grinch.png" alt-"s4u grinch.png" title="" />
</body>
</html>

