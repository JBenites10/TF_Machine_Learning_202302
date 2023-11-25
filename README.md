


![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.001.jpeg)

**UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS**


Machine Learning - CC57

Trabajo Final




**INTEGRANTES**

Benites Diaz, Juan Alejandro			u202010449

Tumbalobos Cubas, Kevin William		u201922518

Guevara Dominguez, Sebastian Aaron 		u20181h207


**SECCIÓN**

CC72



**DOCENTE**

:Canaval Sanchez, Luis Martin




**CICLO 2023-02**


**Glosario**


[**1. Introducción	3**](#_789tbnw08n3)**

[**2. Objetivos	3**](#_u9qns02ef3fm)

[**3. Desarrollo	4**](#_6j649fyx9chd)

[a. Milestone 4:	4](#_iervidipkp3x)

[b. Milestone 5:	7](#_ky0za4v0t9cg)

[c. Final Milestone:	11](#_mh4kpvujq7zy)

[**4. Conclusiones:	12**](#_2ugp4er9ir2w)

[**5. Referencias:	13**](#_9qx1ge5te23z)










































1. # <a name="_789tbnw08n3"></a>**Introducción**

El machine learning es un campo de la inteligencia artificial que se centra en el desarrollo de algoritmos y modelos que permiten a las computadoras aprender y tomar decisiones a partir de datos, sin ser programadas explícitamente para cada tarea. Utiliza técnicas que permiten a las máquinas reconocer patrones, hacer predicciones o tomar decisiones basadas en ejemplos previos.

Por otro lado, la impresión 3D es una tecnología que permite crear objetos tridimensionales mediante la superposición de capas sucesivas de material. Funciona a través de la interpretación de modelos digitales en un software para luego ser materializados en objetos físicos, ofreciendo flexibilidad y personalización en la fabricación de diversos productos.

La intersección de machine learning y la impresión 3D es fascinante. El machine learning puede emplearse para mejorar y optimizar los procesos de impresión 3D. Por ejemplo, se pueden utilizar algoritmos para analizar diseños, detectar errores potenciales o incluso predecir el comportamiento de un objeto impreso en función de parámetros específicos.

A su vez, la impresión 3D puede ser utilizada para crear componentes personalizados para experimentos de machine learning, como carcasas para sensores, piezas para robots o prototipos de dispositivos específicos.

La combinación de estas dos tecnologías está generando avances significativos en sectores como la medicina, la manufactura y la ingeniería, permitiendo la creación de objetos y dispositivos más eficientes y adaptados a necesidades particulares.

1. # <a name="_u9qns02ef3fm"></a>**Objetivos**
   Investigar la Aplicabilidad del Machine Learning en la Impresión 3D:

Explorar y analizar cómo la implementación estratégica de técnicas de machine learning puede ser efectiva en mejorar aspectos clave de la impresión 3D, tales como la calidad de las impresiones, la eficiencia del proceso y la optimización de recursos.

Identificar Parámetros Críticos y Variables Relevantes:

Determinar los factores esenciales dentro del proceso de impresión 3D que pueden ser influenciados por la integración de modelos de machine learning, incluyendo la velocidad y temperatura de impresión, el diseño de los objetos a imprimir, así como la selección del material.

Validar la Eficacia del Modelo Propuesto:

Realizar pruebas rigurosas para verificar la precisión y confiabilidad del modelo de machine learning desarrollado, mediante el uso de conjuntos de datos representativos y la evaluación exhaustiva de su capacidad para anticipar y corregir posibles errores de impresión.
1. # <a name="_6j649fyx9chd"></a>**Desarrollo**
   1. ## <a name="_iervidipkp3x"></a>Milestone 4:











![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.002.jpeg)

El código implementa un conjunto de funciones para la conversión entre archivos OFF y STL, la voxelización de modelos 3D, y la visualización de modelos en diferentes etapas del proceso. Inicia leyendo modelos en formato OFF, los convierte a STL y realiza la voxelización para generar tensores 3D. Posteriormente, se realiza la conversión a un formato de imagen y se procesan directorios completos de modelos 3D. Finalmente, se carga un conjunto de datos preprocesado desde archivos Numpy (.npy) o, en caso de no existir, se realiza el procesamiento y se guardan estos archivos para su uso futuro. Se proporciona una función adicional para visualizar un archivo OFF en un formato STL y se muestra un ejemplo de uso al final del script, donde se visualiza un modelo 3D a partir de un archivo OFF específico.

**Ejemplos:**

3D en OFF

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.003.png)

PNG

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.004.png)

Voxel
![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.005.png)




**Printing plan:** 

PrusaSlicer es un software de código abierto diseñado especialmente para preparar modelos 3D para impresoras 3D FDM (Fused Deposition Modeling) y SLA (Stereolithography). Está desarrollado por Prusa Research y se centra en ser compatible con sus propias impresoras 3D, como la línea Original Prusa i3.

Este software permite a los usuarios realizar varias tareas importantes antes de imprimir un modelo en 3D. Algunas de sus características clave incluyen:

Slicing: La función principal del software es dividir el modelo 3D en capas delgadas, lo que se conoce como "slicing". Esto es esencial para la impresión 3D, ya que la impresora construye el objeto capa por capa.

Configuración avanzada: Ofrece una amplia gama de configuraciones para ajustar los parámetros de impresión, como la velocidad de impresión, la densidad del relleno, la temperatura de la boquilla, entre otros. Esto permite adaptar la impresión según las necesidades específicas del modelo y del material utilizado.

Previsualización: Proporciona una vista previa de cómo se imprimirá el modelo, mostrando las capas individuales y permitiendo al usuario detectar posibles problemas antes de la impresión real.

Soporte de múltiples formatos: Es compatible con varios tipos de archivos de modelos 3D, como STL, OBJ, AMF y otros, lo que brinda versatilidad para trabajar con diferentes diseños.

Compatibilidad con múltiples impresoras: Aunque está optimizado para las impresoras Prusa, también es compatible con muchas otras marcas y modelos, lo que lo hace más accesible para una amplia gama de usuarios.
1. ## <a name="_ky0za4v0t9cg"></a>Milestone 5:
   La función *make\_generator* construye un modelo donde los GANs (Generative Adversarial Networks),  son diseñados para generar datos imitativos como imágenes 3D. Este inicia con 2 entradas: etiquetas y una imagen en escala grises. Las etiquetas se transforman en vectores densos (embedding) y se combinan con características extraídas de la imagen a través de capas convolucionales. Posteriormente, esta combinación se remodela y procesa a través de varias capas convolucionales transpuestas para construir una imagen 3D, utilizando una activación 'tanh' para normalizar los valores de salida. El generador tiene un total de 269,707,329 parámetros, de los cuales 269,703,777 son entrenables. 

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.006.jpeg)








Por otro lado, *make\_discriminator* forma un modelo discriminativo, que en los GANs sirve para evaluar si los datos son reales o generados por el generador. Empieza con entradas de etiquetas y vóxeles (datos 3D), donde las etiquetas se convierten en vectores densos y los vóxeles se procesan a través de capas convolucionales. Luego, se combinan las características de ambos, procesadas por capas densas adicionales, para determinar la autenticidad de los datos. Este modelo es crucial en la dinámica de entrenamiento de los GANs, donde generador y discriminador se entrenan en competencia para mejorar la calidad de los datos generados. La suma total de los parámetros entrenables en esta red es de 41,161,248, con todos los parámetros marcados como entrenables. 
## ![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.007.jpeg)




<a name="_ke0p92cxznfs"></a>**Trainig Setup:**

La función train\_gan en el código proporcionado implementa el entrenamiento de una red generativa adversarial (GAN) compuesta por un generador y un discriminador. Durante cada época, la GAN se entrena alternativamente: primero, el discriminador se ajusta para distinguir entre datos voxelizados reales y generados, y luego, el generador se ajusta para engañar al discriminador al generar datos voxelizados que parecen reales. Se imprimen las pérdidas del discriminador y el generador en cada lote, y al final de cada época, proporcionando información sobre el rendimiento del modelo durante el entrenamiento. Después de la definición de la función, se carga un conjunto de datos de imágenes y voxelizados, se normalizan y redimensionan, y se utiliza la función train\_gan para entrenar la GAN con estos datos.

Es importante destacar que, para nuestro trabajo específico, el proceso de entrenamiento de la GAN se llevó a cabo de manera local utilizando el entorno de desarrollo VSCode. La máquina utilizada para este propósito está equipada con un procesador AMD Ryzen 5 5600X, una GPU AMD 5700, y 16 GB de RAM a 3600 MHz. Este proceso de entrenamiento, que abarcó aproximadamente entre 23 y 24 horas, subraya la intensidad computacional asociada con la formación de modelos GAN, incluso en configuraciones de hardware robustas como la mencionada..

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.008.jpeg)

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.009.jpeg)![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.010.png)




















La impresora Prusa MK4 es una impresora 3D de alta calidad fabricada por Prusa Research. Se trata de un kit que requiere montaje, pero ofrece una excelente experiencia de impresión una vez ensamblado. Destaca por su fiabilidad, precisión y facilidad de uso, con características como una estructura robusta, sistema de autonivelación, y soporte para una amplia variedad de materiales de impresión. Es reconocida en la comunidad de impresión 3D por su calidad y rendimiento consistentes.

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.011.jpeg)


1. ## <a name="_mh4kpvujq7zy"></a>Final Milestone:
![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.012.png)

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.013.png)

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.014.png)

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.015.png)

![image](https://github.com/JBenites10/TF_Machine_Learning_202302/blob/main/TF_ML/Aspose.Words.289df711-1037-462f-af3f-1c945806a6a8.016.png)


1. # <a name="_2ugp4er9ir2w"></a>**Conclusiones:**
- Se ha demostrado que la aplicación estratégica de algoritmos de aprendizaje automático puede influir positivamente en múltiples aspectos del proceso de impresión 3D. Desde la identificación temprana de posibles defectos hasta la optimización dinámica de parámetros, el machine learning ha mostrado su capacidad para mejorar la calidad final de las impresiones.
- Se vislumbra un amplio potencial para la evolución continua de la impresión 3D mediante la integración cada vez más sofisticada de técnicas de machine learning. Se recomienda una mayor exploración en la adaptación dinámica de parámetros, la incorporación de modelos más complejos y la aplicación en tiempo real en entornos de fabricación.
- Las pruebas y validaciones realizadas han confirmado la eficacia y precisión del modelo de machine learning propuesto. Su capacidad para prever y corregir errores durante el proceso de impresión ha sido demostrada mediante la utilización de conjuntos de datos representativos y escenarios de prueba realistas.

1. # <a name="_9qx1ge5te23z"></a>**Referencias:**
- *What is FDM (Fused Deposition Modeling) 3D printing? | Hubs*. (s. f.). Hubs. https://www.hubs.com/knowledge-base/what-is-fdm-3d-printing/
- *Stereolithography Technology | Stratasys*. (s. f.). <https://www.stratasys.com/en/guide-to-3d-printing/technologies-and-materials/stereolithography-technology/#:~:text=Stereolithography%20is%20an%20additive%20manufacturing,from%20the%20vat%20of%20resin>.
- Budek, K. (2023, 14 noviembre). Machine Learning in 3D modeling – Tooploox at NeURIPS 2020. *Tooploox*. https://tooploox.com/machine-learning-in-3d-modeling-tooploox-at-neurips-2020



