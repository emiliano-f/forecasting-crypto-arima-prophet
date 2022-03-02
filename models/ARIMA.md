# Modelo ARIMA

Comencemos con una pequeña comparación.

ARMA significa "Promedio móvil autorregresivo" y ARIMA significa "Promedio móvil integrado autorregresivo".

La única diferencia, entonces, es la parte “integrada”. 
Integrado se refiere a la cantidad de veces que se necesita diferenciar una serie para lograr la estacionariedad, que se requiere para que los modelos ARMA sean válidos. Por diferenciar me refiero a formar una nueva serie restando la observación 1 de 2, 2 de 3, etc.

Entonces, un modelo ARMA es equivalente a un modelo ARIMA de las mismas órdenes MA y AR sin diferenciación.

La notación abreviada típica para ARMA es “ARMA(p,q)”, donde p es el orden AR y q es el orden MA. Para ARIMA, la notación es “ARIMA(p,d,q)” donde la d agregada es el orden de integración, o número de diferencias. Así que las siguientes dos afirmaciones lo resumen todo:
<ul>
  <li>ARMA(p,q) es equivalente a ARIMA(p,0,q)</li>
  <li>Dado un ARIMA(p,d,q), si d>0 se puede modelar como un ARMA ejecutando un ARMA(p,q) después de diferenciar la serie original d veces.</li>
</ul>

# Funcionamiento
<ul type="disk">
  <li>
    <b>Primera fase:</b> consiste en identificar el posible modelo ARIMA que sigue la serie.
    <ul>
      <li>
        Decidir qué transformaciones aplicar para convertir la serie observada en una serie estacionaria
      </li>
      <li>
        Determinar un modelo ARMA para la serie estacionaria, es decir, los órdenes p y q de su estructura autorregresiva y de media móvil.
      </li>
    </ul>
  </li>
  <li>
    <b>Segunda fase:</b> Seleccionado provisionalmente un modelo para la serie estacionaria, se pasa a la segunda etapa de estimación, donde los parámetros AR y MA del modelo se estiman por máxima verosimilitud y se obtienen sus errores estándar y los residuos del modelo.
  </li>
  <li>
    <b>Tercera fase:</b> Es el diagnostico, donde se comprueba que los residuos no tienen estructura de dependencia y siguen un proceso de ruido blanco. Si los residuos muestran estructura se modifica el modelo para incorporarla y se repiten las etapas anteriores hasta obtener un modelo adecuado.
  </li>
  <li>
    <b>Cuarta fase:</b> Es la predicción, una vez que se ha obtenido un modelo adecuado se realizan predicciones con el mismo.
  </li>
</ul>
