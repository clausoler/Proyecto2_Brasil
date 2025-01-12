# 🔎Proyecto: Análisis de la ejecución de ingresos públicos en Brasil

**📃Descripción del proyecto**

Este proyecto realiza un análisis exploratorio y descriptivo sobre la ejecución de ingresos públicos en Brasil. El objetivo principal del proyecto es identificar tendencias, patrones y realizar un análisis descriptivo que nos proporcione una imagen clara sobre cómo el gobierno de Brasil ha gestionado la recaudación de ingresos públicos para financiar servicios y proyectos. Para ello, se han utilizado herramientas pertenecientes a la biblioteca Pandas en Phyton para realizar análisis estadísticos, visualizaciones y modelado de datos. 

**🗼Estructura del proyecto**

        ├── Datos                # Archivos csv
        ├── README.md # Descripción y presentación del proyecto
        ├── src                  # Archivo soporte de limpieza
        ├── .gitignore           # Archivos ignorados
        ├── ingresos_públicos_brasil     # Contenido completo del proyecto

**👩‍💻Instalación y Requisitos**

Este proyecto usa la versión de Phyton 3.12.4 y requiere de las siguientes herramientas:
 
- Biblioteca Pandas
- Biblioteca Numpy
- Gráfica Boxplot
- Gráfica matplotlib.pyplot
- Gráfica Matplotlib.pybar

**🤓Resultados y Conclusiones**
 
Tras analizar los datos, se han encontrado los siguientes hallazgos:
 
- Las categorías económicas con mayor discrepancia entre los ingresos previstos y realizados son Receitas de Capital y Receitas Correntes. En la gráfica de Comparación de ingresos por categoría se ha podido ver que ambas categorías recaudan menos dinero del previsto. Luego, en la gráfica de Comparación de ingresos entre Receitas Correntes y Receitas de Capital se ha obervado que las previsiones y recaudaciones han cambiado a lo largo de los años. En Receitas Correntes en el año 2020 los ingresos previstos son mayores que los realizados, y en el año 2021 los ingresos realizados son mayores que los previstos. En cambio, en Receitas de Capital en el año 2020 los ingresos realizados son mayores que los previstos, y en el año 2021 los ingresos previstos son mayores que los realizados. Por tanto, en las dos categorías económicas hay una tendencia temporal totalmente distinta. 

- En la gráfica de Evolución temporal de los ingresos realizados y previstos se pueden sacar dos conclusiones: En el año 2017 se encuentra la mayor diferencia entre ingresos previstos y realizados, año en el cual hay una subida exponencial de los ingresos previstos y una bajada al mismo tiempo de los ingresos realizados. Luego, en el año 2020 es el único año donde los ingresos realizados superan a los previstos. Ya en el año 2021 la tendencia se revierte.

A continuación se dan algunas posibles explicaciones o causas a los patrones encontrados:
 
1. Discrepancias entre ingresos previstos y realizados en Receitas Correntes y Receitas de Capital
- Causas generales de discrepancias:
- Errores de estimación: Las proyecciones de ingresos suelen basarse en tendencias económicas, marcos legales o esperados cambios macroeconómicos. En años de incertidumbre o cambios rápidos, las estimaciones pueden no coincidir con la realidad.

- Impacto de la pandemia: Entre 2020 y 2021, la pandemia de COVID-19 afectó los flujos de ingresos en muchos sectores. Esto pudo causar las discrepancias observadas.

Tendencias opuestas entre las dos categorías:
- En Receitas Correntes, los ingresos realizados superaron a los previstos en 2021. Esto podría deberse a:
  - Mayor eficiencia en la recaudación de impuestos recurrentes.
  - Políticas económicas que impulsaron la base gravable, como el consumo o el empleo.
  - En Receitas de Capital, los ingresos realizados superaron a los previstos en 2020, pero esta tendencia se invirtió en 2021. Esto podría explicarse por:
    - Año 2020: La venta de activos o concesiones extraordinarias pudo generar más ingresos de lo anticipado.
    - Año 2021: Las estimaciones optimistas para ingresos de capital no se concretaron, posiblemente debido a obstáculos en proyectos de inversión o licitaciones.

2. Mayor diferencia entre ingresos previstos y realizados en 2017

- Incremento exponencial en los ingresos previstos:
  - Políticas ambiciosas: En 2017, pudo haberse establecido un presupuesto con metas extremadamente optimistas, impulsado por:
    - Necesidad de compensar déficits fiscales previos.
    - Proyecciones económicas sobrestimadas.
  - Factores macroeconómicos: Podría haber habido expectativas de crecimiento económico que no se materializaron.
  - Baja en los ingresos realizados:
  - Crisis económica: Si hubo una recesión o bajo rendimiento económico, los ingresos esperados simplemente no se lograron.
  - Fallas en la implementación: Problemas administrativos o cambios legislativos pudieron retrasar la entrada de ingresos.
 
3. Año 2020: Único año donde los ingresos realizados superan los previstos
- Este comportamiento inusual puede atribuirse a:
  - Medidas de emergencia: Durante la pandemia, los gobiernos recurrieron a medidas excepcionales como el cobro de multas, recuperación de deudas o ventas de activos para cubrir déficits.
  - Subestimación en las previsiones: Dada la incertidumbre inicial, las proyecciones para 2020 pudieron ser conservadoras, mientras que las acciones tomadas durante el año generaron ingresos adicionales.
 
4. Reversión en 2021 (ingresos previstos superan a los realizados)
- Este cambio refleja:
  - Optimismo excesivo en las previsiones: Al tratar de recuperarse de 2020, las estimaciones para 2021 pudieron basarse en un retorno acelerado a la normalidad económica, lo que no siempre ocurre.
  - Restricciones operativas: Las unidades gestoras pudieron enfrentar desafíos como falta de recursos, restricciones presupuestarias o atrasos en la implementación de políticas.
   
**👉Próximos pasos**
 
Para mejorar este proyecto, algunas de las cosas que se podrían hacer para mejorar la recaudación de los ingresos públicos en Brasil:

1. Mejorar las herramientas de análisis y proyección
- Uso de modelos predictivos avanzados:
  - Emplear técnicas de inteligencia artificial y machine learning para analizar patrones históricos y prever ingresos con mayor precisión.
  - Considerar factores externos como fluctuaciones económicas, cambios legislativos y eventos globales (ej. pandemias).

2. Crear sistemas de monitoreo continuo
- Indicadores clave de rendimiento (KPI):
  - Establecer KPIs específicos para cada unidad gestora, como el porcentaje de ejecución mensual o trimestral.
  - Automatizar alertas para identificar a tiempo desviaciones entre ingresos previstos y realizados.

3. Innovar en los métodos de recaudación
- Digitalización de procesos:
  - Automatizar el cobro de ingresos y multas para reducir errores y mejorar la eficiencia.
  - Nuevas estrategias de recaudación:
  - Explorar fuentes adicionales de ingresos, como concesiones o alianzas público-privadas, para diversificar los flujos.
   
**✍️Contribuciones**
 
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un push request o una issue.
 
**🗯️Autores y Agradecimientos**
 
**Claudia Soler** - [@clausoler](https://github.com/clausoler/Proyecto2_Brasil)