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


1) **Tendencia lineal g(t):** Para calcular el termino _g(t)_, Prophet ofrece 2 alternativas
   - *Crecimiento Logístico:* Estos casos corresponden a situaciones en donde se da una saturación que no permite el crecimiento más allá de un límite determinado. Se aplica una sigmoide pero un poco cambiada.

     - C: Capacidad de Carga. Define la carga máxima que puede llegar a tomar la curva. Nótese que este valor puede no ser fijo y depender de otro parámetro externo C(t). <br>
     - k: Es la tasa de crecimiento. Define qué tan rápido pasará de 0 a la capacidad de carga o viceversa.<br>
     - m: Es un parámetro de compensación. Define el punto de inflexión de la función, es decir, cuando cambia de concavidad. <br>

<p align="center">
  <img src=https://user-images.githubusercontent.com/63267942/153085439-b7207149-8b2d-4f00-a7fb-b2c69e2cb5b8.png />
</p>


<p align="center">
  <img src=https://miro.medium.com/max/724/1*Y7bCUzRTaKsdPc1JGgdb2A.png />
</p>

<ul>
  <ul>
    <li>
      <i>Modelo Lineal por Partes:</i> Para pronosticar problemas que no muestran un crecimiento saturado, existe una tasa de crecimiento constante por partes.
    </li>
    <ul>
      <li>
        δ: tiene los ajustes de tarifas
      </li>
      <li>
        k: es la tasa de crecimiento
      </li>
      <li>
        m: es el parámetro de compensación, en estos casos, los puntos de quiebre. Los puede definir el usuario o los puede calcular Prophet.
      </li>
    </ul>
<p align="center">
  <img src=https://miro.medium.com/max/724/1*vxQNbfVATdzjNUtCm5mNUw.png />
</p>
      

  </ul>
</ul>





2) **Ajuste estacional h(t):** Se hace utilizando series de Fourier. Fourier demostró que cualquier función periódica puede formarse a partir de una suma infinita de senos y cosenos.
<p align="center">
  <img src=https://user-images.githubusercontent.com/63267942/153087454-c07d69ab-8ef3-4233-891b-a025ad3adac9.png />
</p>

3) **Término h(t):** Queda definido por el usuario, y son aquellos valores que pueden llegar a alterar la serie temporal. Por ejemplo: La llegada del verano altera las ventas de una heladería, los hechos históricos importantes, los fin de semana largos en la venta de vuelos, etc.

4) **Error ε<sub>t</sub>**: Se estima por diferencia




