# Modelo ARMA

El nombre ARMA es la abreviatura de Modelos Autorregresivos de Media Móvil. Proviene de la fusión de dos modelos más simples: 
  1) **_El autorregresivo o AR:_** Es una representación de un proceso aleatorio, en el que la variable de interés depende de sus observaciones pasadas. La forma genérica de representar un AR sería la siguiente.
     - _C_: Es la posición inicial, o el último valor leido de la serie. 
     - _θ_: Algún factor multiplicativo.
     - _Y_<sub>t-1</sub>: El valor leído anteriormente
     - _ε_<sub>t</sub>: Termino de error 
      <p align="center">
          <img src=https://economipedia.com/wp-content/uploads/Modelo-AR-1-formula.png />
      </p>
      
     _NOTA: Nótese que una regresión puede estar compuesto por un conjunto de valores pasados._


  2) **_El promedio móvil o MA:_** Es un promedio de valores que se va modificando a lo largo del tiempo. La media móvil es un indicador de tendencia que nunca se anticipa a la tendencia de las cotizaciones, es decir, simplemente sigue a la curva de cotizaciones confirmando la tendencia en cada momento.
  <br><br>Existen varios modelos:
      - **Media Móvil Simple:** Recoge el dato que se genera en la última sesión, y a su vez, descarta el dato más antiguo de la serie temporal. La duda que existe es ¿Cuántos términos considerar? <br>
      
        <p align="center">
          <img src=https://user-images.githubusercontent.com/63267942/149024008-9cab5989-be52-4655-a84f-e013cec55b21.png />
        </p>

        - Si elegimos un **_n_** bajo, nuestra predicción tendrá una alta capacidad para responder rápidamente ante fluctuaciones, ya que la pendiente no se ve influenciada por muchos datos. En contraparte, se vé muy influenciada por los factores aleatorios por la misma razón.<br><br>
        - Si elegimos un **_n_** alto, nuestra predicción filtra o anula los factores aleatorios, ya que no influyen mucho en un promedio de datos grandes, pero presenta cierta inflexibilidad para adaptarse a cambios drásticos válidos en el corto plazo.<br>
        
          _NOTA: Un problema con esta serie es que cambia 2 veces al leer un nuevo dato, primero por leer un dato nuevo, y segundo por sacar un dato viejo_ 

      - **Media Móvil Ponderada:** Para evitar que los datos viejos afecten significativamente a la predicción de la serie, se utilizan las medias móviles ponderadas, donde a medida que los datos se vuelven viejos, pierden valor. La idea atrás de este método es que como los datos ya son muy antiguos, no son rendundates para los valores actuales. Esto permite que la serie pueda adaptarse con mayor facilidad a los cambios abruptos en el corto plazo, ya que las ultimas lecturas toman mayor redundancia.
         <p align="center">
            <img src=https://user-images.githubusercontent.com/63267942/149025788-1fd63a1a-df6e-49c6-9dc0-0a4b12e575e2.png />
          </p>
      

      - **Media Móvil Exponencial:** Es un tipo particular de Media Móvil Ponderada que responde a un crecimiento o decrecimiento exponencial, donde los datos antiguos influyen, pero es casi insignificante.
     
<br>     
<br>     
<br>    
Luego de esta introducción podemos definir matemáticamente a los modelos ARMA. El modelo general de series temporales autorregresivo con media móvil de _p_ términos autorregresivos y _q_ términos de media móvil se expresa como:
<p align="center">
  <img src=https://economipedia.com/wp-content/uploads/Modelo-ARMA.jpg />
</p>

