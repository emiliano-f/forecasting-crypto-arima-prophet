# Modelo Prophet
Este modelo surge por las limitaciones que presentan los modelos SARIMAX, como estacionariedad y valores igualmente espaciados en el tiempo (siendo que esto puede variar mucho en la realidad).

La idea de este algoritmo es plantear a la serie temporal como la suma de 4 componentes: 

<p align="center">
  <img src=https://user-images.githubusercontent.com/63267942/153080718-4034613d-5540-4f7f-8aad-c58d5300b46d.png />
</p>

  1) **_g(t):_** Describe la tendencia lineal o de crecimiento logístico de largo plazo, creando una función definida por partes en los puntos de cambio (simplificando la predicción).<br>
  <br>_NOTA: Los puntos de cambio son momentos en los datos donde los datos cambian de dirección._ 

  2) **_s(t):_** Función que define la estacionalidad (anual, mensual, semanal, etc.)
  3) **_h(t):_** Hechos concretos que pueden alterar los valores de la serie (vacaciones, feriados, paros, etc.), a definirse por el usuario
  4) **_ε<sub>t</sub>:_** Termino de error 

Prophet intenta ajustar las funciones (lineales o no) a los datos dando más o menos importancia a los distintos efectos, es decir, un modelo muy parametrizable:

1) El primer término se modela como una curva de crecimiento logístico (curva sigmoidea). Estos casos corresponden a situaciones en donde se da una saturación que no permite el crecimiento más allá de un límite determinado. Se aplica una sigmoide pero un poco cambiada.

<p align="center">
  <img src=https://user-images.githubusercontent.com/63267942/153085439-b7207149-8b2d-4f00-a7fb-b2c69e2cb5b8.png />
</p>


<p align="center">
  <img src=https://miro.medium.com/max/724/1*Y7bCUzRTaKsdPc1JGgdb2A.png />
</p>
<ul>
  <ul>
    <li>
      C: Capacidad de Carga. Define la carga máxima que puede llegar a tomar la curva. Nótese que este valor puede no ser fijo y depender de otro parámetro externo C(t). <br>
Por ejemplo: Al aumentar la cantidad de dispositivos con capacidad de conexión, aumentará la cantidad de conexiones en una red.<br>
    </li>
    <li>
      k: Es la tasa de crecimiento. Define qué tan rápido pasará de 0 a la capacidad de carga o viceversa.<br>
    </li>
    <li>
      m: Es un parámetro de compensación. Define el punto de inflexión de la función, es decir, cuando cambia de concavidad. <br>
    </li>
  </ul>
</ul>
  

2) La curva de tendencia g(t) se determina por tramos. Prophet detecta automáticamente los puntos de quiebre, pero tambien los puede determinar el usuario para anticiparse a algún envento.

3) El ajuste estacional h(t) se hace utilizando series de Fourier. Fourier demostró que cualquier función periódica puede formarse a partir de una suma infinita de senos y cosenos.
<p align="center">
  <img src=https://user-images.githubusercontent.com/63267942/153087454-c07d69ab-8ef3-4233-891b-a025ad3adac9.png />
</p>

4) El término h(t) queda definido por el usuario, y son aquellos valores que pueden llegar a alterar la serie temporal. Por ejemplo: La llegada del verano altera las ventas de una heladería, los hechos históricos importantes, los fin de semana largos en la venta de vuelos, etc.

5) El término ε<sub>t</sub> se estima por diferencia




