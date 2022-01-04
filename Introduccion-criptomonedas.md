# INFORME FINAL INTELIGENCIA ARTIFICIAL I - PREDICCIÓN DEL BITCOIN

## INTRODUCCIÓN

### ¿Qué son las criptomonedas?
Una criptomoneda es un activo digital que emplea un cifrado para garantizar integridad, autenticidad y confidencialidad de las transacciones, es decir, funcionan como moneda de cambio y solucionan los problemas que las monedas de cambio tradicionales presentan.

### ¿Cuál es su origen?
Lo que necesitamos para entender esta idea es que el dinero viene a solucionar los problemas del mercado, es decir, determinar cuánto de mi producto vale el tuyo. Por ejemplo: cuántas gallinas vale tu vaca (en palabras poco formales y en un contexto muy simple), o cuanto capital valen mis horas de servicio.
(...)"El dinero es válido en la medida que otro lo acepte"(...)

Una vez que entendemos ese concepto, podemos abstraer a la moneda como cualquier objeto (real o no) que resuelva estos aspectos.

Pero para que nuestra monera sea válida, debe cumplir ciertos aspectos: 
 - Debe servir como moneda de cambio, es decir, quien aporta el capital recibe un bien o servicio a cambio.
 - Debe servir de referencia de valor, es decir, poder determinar, a través de dicha moneda, cuánto vale un bien o servicio.
 - Debe servir como reserva de valor, es decir, que su valor no se vea moficado con el paso del tiempo.

Estos 3 parametros son determinados por la sociedad, según el uso y confianza que le tengan a la moneda.

### ¿Cómo funcionan?
Las criptomonedas no son diferentes a las monedas corrientes, con algunas salvedades:
 - No hay un ente central del que dependamos (como el banco) que regule las transacciones. 
 - Mantiene total privacidad, ya que toda la información está encriptada y nadie sabe la información del dueño del dinero.
 - Evita problemas de "devaluación" de la moneda, ya que no depende de factores socio-económicos (como la emisión monetaria)

Este sistema funciona bajo el modelo Peer-To-Peer (2p2) (como Torrent, por ejemplo), donde cada usuario funciona como cliente o servidor de otro, según corresponda. Es decir, si queremos saber cuanto dinero tiene una persona, debemos mantener un registro global, que incluye a todas las transacciones que han ocurrido desde el origen de una determina criptomoneda. Este registro debe ser público, para que cualquier persona pueda consultarlo en cualquier momento.

Pero si existe este registro ¿Cómo puede existir la privacidad?
La privacidad se sigue respetando, ya que realmente no se sabe a quien pertenece el dinero que figura en dichas transacciones. Esta cadena de transacciones se conoce como **_BLOCKCHAIN_** (cadena de bloques). La idea aquí es formar una LinkedList, donde cada bloque apunta al anterior.
Las personas encargadas de añadir los bloques al registro de transacciones se conocen como **mineros**.

Supongamos que Pepe le quiere transferir dinero a Pedro, entonces, la tarea del minero es crear un bloque con los datos (encriptados) de Pepe y Pedro y añadirlos a la cadena de bloque. Este registro esta almacenado en cada uno de los usuarios de la red. Una vez que se añade el bloque a la cadena, se avisa al resto de los mineros que añadan dicho en su registro.
Nótese que un bloque puede contener muchas transacciones.

![Captura de pantalla de 2022-01-04 18-51-26](https://user-images.githubusercontent.com/63267942/148128644-24016ab7-d877-47fb-ba4d-23a4dd8702f3.png)

Para poder mantener esto de manera estable, las criptomonedas se rigen bajo ciertas reglas. Por ejemplon en el caso del Bitcoin:
 - Cada bloque está hecho de un fichero de texto, que contiene los datos de las transacciones.
 - Cada bloque tiene aproximadamente 1 MB
 - El minero que inserte el bloque recibirá una recompensa. Esta recompensa disminuye a medida que se inserten más bloques en la cadena.
 - El bloque debe ser aceptado por la mayoria de los mineros antes de insertarse en la cadena.
 - Por cada bloque se genera un Hash, que los identifica. Para hashear un bloque, se necesita: Hash anterior + Fecha y Hora de creación del bloque + Transaccion de recompensa para el minero + Todas las transacciones que quepan hasta completar 1 MB + Prueba de trabajo (detallaremos mas adelante).
 
 LINK: https://www.blockchain.com/btc/blocks?page=1
 
_Recordemos que los Hash tienen la propiedad de que si conocemos la formula, es muy facil, a partir de los datos, obtener ese hash, pero teniendo el hash es muy dificil saber cuales son los datos iniciales_

Esta particularidad, hace que sea muy dificil o imposible la falsificación de nuevos bloques, ya que al cambiar algún dato de la transacción, cambiaría completamente su hash, el cual debe cumplir con ciertos requisitos.

Posibles problemas:
 1- Supongamos que tenemos un amigo minero con el cual queremos hacer un pacto para que él se lleve la recompensa haciendo una transacción con un bitcoin y luego otra con el mismo bitcoin, realizando una estafa. Para evitar estos problemas, cada transacción debe estar aprobada por la comunidad de mineros, que no lo aprobarían. Como la recompensa es muy alta, si el bloque está mal, aún pueden llevarse ellos la recompensa.

 2- Supongamos que un usuario malicioso tiene máquinas bots mineras para garantizar la mayor cantidad de votos a favor en sus transacciones. Este es el problema más grande que tenemos, ya que no se puede validar si son bots o votos autenticos. Para solucionar esto, se introduce el concepto de **_Proof of works_**. En este caso, la prueba de trabajo es que los hash inicien con cierta cantidad de 0's, el cual es modificado cada cierta cantidad de bloques. 
Como el hash cambia con cada minima modificación, la idea es que si se quiere falsificar una transacción, el minero deba buscar un número de forma tal que el hash empiece con la cantidad de 0's correspondientes. Esta cantidad de 0's se ajusta de acuerdo a la capacidad de cómputo de mineria que haya en la red.
Esto significa que para poder falsificar una transacción, se debe superar, en potencia informática, a más de la mitad de los mineros en toda la red.

### ¿De dónde salen las criptomonetas? 
Las criptomonedas se generan cada vez que se crea un bloque, es decir, la recompensa de los mineros. En un principio, fue muy incentivada por especuladores y personas que evitaban mantener un registro de sus monedas.

### ¿Qué determina el precio de las criptomonedas?
El precio se determina por la oferta y la demanda. Cuando se incrementa la demanda, el precio sube, y cuando cae la demanda, el precio baja. Hay un número limitado de criptomonedas en circulación y las nuevas son creadas a una velocidad predecible y decreciente, esto significa que la demanda debe seguir este nivel de inflación para mantener un precio estable.
