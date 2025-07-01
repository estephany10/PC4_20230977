# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Inicio', 'Experiencia', 'Gráficos']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Inicio':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>La persona detrás de las palabras 💗</h1>", unsafe_allow_html=True)

    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto_perfil.jpeg", caption='Esta soy yo :)', width=300)

    col1.image("buen_pastor.png", caption='"Yo soy el buen pastor; el buen pastor su vida da por las ovejas" - Juan 10:11', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """
    ¡Hola! Soy Estephany Ramirez y nací en Lima, Perú. Actualmente, me encuentro estudiando la carrera de Publicidad en la Pontificia Universidad Católica del Perú. Lo que más me llamó la atención para elegir esta profesión, fue la combinación de herramientas creativas con la base investigativa para poder realizar campañas y spots que muestran mensajes concisos y positivos en la vida del público. Me resulta muy interesante que estas dos áreas se combinen en una sola carrera, además que puedo ahondar y comprender el comportamiento del consumidor más allá de la compra sino entendiendo realmente sus percepciones de vida, sus necesidades y emociones que los llevan a tomar decisiones.
    """
    
    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # Creamos más códigos de texto para que se separen en párrafos continuos
    texto2 = """
    En el futuro, me gustaría desarrollar una propia empresa que combine tres de los ámbitos que más me importan: mi relación con Dios, mi familia y mis estudios. Soy cristiana y el impacto que Dios ha tenido en mi vida ha sido increíble, ya que, aún yo no estando abierta a recibirlo, Él siempre me sostuvo y me brindó un amor inigualable en mis momentos más difíciles. Por eso, me gustaría que todo lo que realice y haga sea admirable a sus ojos, no por obligación sino por gratitud. Específicamente, aún no tengo decidido si lo que me gustaría formar sería una cafetería o una tienda de ropa que pueda incentivar a partir de mi formación académica, pero siento que se complementan muy bien para poder brindar un espacio dónde más personas puedan conocer a Dios de maneras diferentes a las usuales y espero que sea un punto de encuentro para familias que quieran crecer en su fe.
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto2}</div>", unsafe_allow_html=True)

    texto3 = """
    Pero, por el momento, aún sigo estudiando para poder lograr este objetivo. Para ello, uno de mis cursos de formación académica este ciclo ha sido Pensamiento Computacional y, en esta oportunidad, les comparto mi blog que cuenta con algunas piezas audiovisuales y gráficos que he desarrollado durante el ciclo. ¡Espero que les guste! 🤍
    """
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto3}</div>", unsafe_allow_html=True)


    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Experiencia':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    # En esta sección debes describir y comentar tu experiencia aprendiendo a programar
    # ¿Cómo te sentiste al principio?, 
    # ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
    # ¿Qué te gustaría hacer con la programación en el futuro? 

    # Agregar un  texto para la respuesta
    texto_2x1 = """
    Ingresar por primera vez a plataformas de programación fue todo un desafío, ya que implicaba adentrarse a un nuevo mundo, con un lenguaje distinto al que ya dominaba y dónde la atención al detalle se vuelve esencial para poder resolver problemas de códigos que, a simple vista, son confusos o complejos de resolver. 
    """

    # Mostramos el texto
    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2x1}</div>", unsafe_allow_html=True)

    # Creamos nuevos códigos de texto para el orden de los párrafos
    texto_2x2 = """
    La programación me ha enseñado, más allá de conocer y probar distintas formulaciones de símbolos, ha tener paciencia debido a qué hubo muchos momentos que no entendía por qué salía error o no quería correr el código que había colocado, incluso ya habiéndolos corregido aún seguían en la misma condición. Ante ello, he aprendido a probar nuevos puntos de vista y seguir perseverando a pesar de las dificultades. 
    """

    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2x2}</div>", unsafe_allow_html=True)

    texto_2x3 = """
    Lo que más me gusta de programar es que puedes experimentar con los códigos y hacer de estos símbolos un significado más grande del que se plantean. Puedes crear desde un gráfico de barras hasta un blog. Definitivamente, hay mucho que puedes hacer mientras sigas aprendiendo y descubriendo este mundo innovador. Sería interesante que más adelante pudiera realizar sitios web interactivos con nuevas bases de investigación que aún no están muy desarrolladas. 
    """

    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2x3}</div>", unsafe_allow_html=True)

    texto_2x4 = """
    En esta sección te comparto un par de videos que he grabado durante el semestre que hablan acerca de términos esenciales para empezar a programar. El lenguaje que utilizo es sencillo para que puedas comprender los conceptos y utilizarlo en ejemplos parecidos :)  
    """

    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2x4}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

    # Agregamos un subtítulo para el video
    st.markdown("<h2 style='text-align: center;'>Aprende conmigo sobre los operadores booleanos</h2>", unsafe_allow_html=True)
    
    # Agregamos una imagen
    st.image("operador.png", width=700)

    # <h2 style='text-align: center;'>Aquí escribe un nombre creativo para presentar tu video</h2>: Esta es una cadena de código HTML.
    # La etiqueta <h2> se utiliza para un encabezado de segundo nivel en una página web.
    # El texto está centrado (text-align: center;).
    # El texto dentro de las etiquetas <h2> ("Aquí escribe un nombre creativo para presentar tu video") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.
    # Por ejemplo, puedes agregar un emoji de video 🎥 

    # Agregamos un video realizado en las practicas anteriores
    # st.video("https://drive.google.com/file/d/1UwFb4H3hXoWLtVR-5DJnXngaOPhOKBIK/view?usp=sharing")

    # st.video("https://www.youtube.com/watch?v=X_Z7d04x9-E"): Esta línea está mostrando un video en la aplicación web.
    # La función video toma como primer argumento la URL del video que se desea mostrar.
    # En este caso, la URL es "https://www.youtube.com/watch?v=X_Z7d04x9-E".
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.

    # O creamos un botón para ir al enlace del video con button
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1UwFb4H3hXoWLtVR-5DJnXngaOPhOKBIK/view?usp=sharing' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # Agregar otro video
    st.markdown("<h2 style='text-align: center;'>Aprende a diferenciar el bucle for y while</h2>", unsafe_allow_html=True)

    st.image("bucle.png", width=700)

    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1FKiZsj63xXwZYRf-SFaSWREZ_pNfI8P3/view?usp=sharing' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

    # <div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>:
    # Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el contenido está centrado (text-align: center;).
    # La etiqueta <a> se utiliza para crear un enlace.
    # El atributo href especifica la URL a la que se dirige el enlace.
    # En este caso, la URL es 'https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link'.
    # El atributo target='_blank' indica que el enlace se abrirá en una nueva pestaña del navegador.
    # La etiqueta <button> se utiliza para crear un botón.
    # El texto dentro de las etiquetas <button> ("Ver video") es el contenido del botón.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
    # Puedes cambiar la URL por la de tu video en YouTube o en otra plataforma de video.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Gráficos realizados durante el ciclo 2025-1</h1>", unsafe_allow_html=True)

    # Creamos una lista de gráficos
    graficos = ['Gráfico pastel del tipo de contenido en Netflix', 'Gráfico de barras verticales de redes sociales de los ministerios del Perú', 'Mapa de mis películas favoritas']

    # Creamos un cuadro de selección en la página de gráficos
    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    # El cuadro de selección se crea con la función selectbox.
    # El primer argumento es el texto que se muestra en el cuadro de selección.
    # El segundo argumento es una lista de opciones que se pueden seleccionar.
    # En este caso, las opciones son los elementos de la lista graficos.
    # La opción seleccionada se asigna a la variable grafico_seleccionado.
    # La variable grafico_seleccionado se utiliza para mostrar el gráfico correspondiente en la aplicación web.
    

    # Mostramos el gráfico seleccionado
    if grafico_seleccionado == 'Gráfico pastel del tipo de contenido en Netflix':
        st.markdown("<div style='text-align: justify; font-size: 18px;'>A partir del contenido distribuido en Netflix, se identifica el porcentaje de series y películas que se encuentran dentro de su catálogo. Se puede apreciar que la mayoría de producciones son películas, ya que cumplen la función de entretener en periodos más cortos de tiempo y ser menos demandantes que algunas series. Asimismo, este porcentaje también se puede ver influenciado en lo económico debido a que ciertas películas implican un menor costo de adquisición en comparación a algunas series que requieren licencias más extensas o que se desarrollan a lo largo de varias temporadas.</div>", unsafe_allow_html=True)
        st.image("pastel_netflix.png", caption='Gráfico de tipo de contenido en Netflix', width=700)
        pass
    elif grafico_seleccionado == 'Gráfico de barras verticales de redes sociales de los ministerios del Perú':
        st.markdown("<div style='text-align: justify; font-size: 18px;'>Para analizar el alcance que tienen los ministerios del Perú en el público a través de las redes sociales, se consultó una base de datos institucional que indicaba cuántos de ellos contaban con perfiles en las principales plataformas digitales. En la gráfica se presenta una lista de seis redes sociales, junto con el número de ministerios que poseen cuentas activas en cada una, como parte de su estrategia para llegar a la ciudadanía. Los datos evidencian una clara preferencia por redes como Instagram, Twitter, Facebook y YouTube, dado que son las más utilizadas por la población. Estas plataformas permiten una mayor cercanía con el entorno digital del público y facilitan una comunicación directa, ya sea para contrarrestar la difusión de noticias falsas o para anunciar información institucional relevante. Por otro lado, redes como LinkedIn y TikTok —que no son utilizadas por todos los ministerios— parecen tener una menor relevancia para los fines comunicacionales del Estado, ya que el tipo de contenido y el público al que se dirigen difieren del que se busca alcanzar prioritariamente.</div>", unsafe_allow_html=True)
        st.image("ministerios_redes_seaborn.png", caption='Gráfico de redes sociales', width=700)
        pass
    elif grafico_seleccionado == 'Mapa de mis películas favoritas':
        st.markdown("<div style='text-align: justify; font-size: 18px;'>En el mapa se pueden observar las locaciones de rodaje de mi top 5 de películas favoritas. Cada marcador incluye información sobre el director y el año de estreno de cada obra audiovisual. Se evidencia que la mayoría de estas locaciones se encuentran en Estados Unidos, con la excepción de una que está ubicada en Inglaterra. Esto refleja una inclinación hacia el consumo de cine norteamericano por encima del producido en otros países, lo que sugiere una mayor admiración o preferencia por las producciones originadas en ese contexto.</div>", unsafe_allow_html=True)
        # Si "mapa_cusco.html" es un archivo HTML (no una imagen), debes mostrarlo con st.components.v1.html
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
        pass

    # if grafico_seleccionado == 'Gráfico de barras verticales de lenguas aisladas':
    # st.markdown("<div style='text-align: justify; font-size: 20px;'>Aquí debe ir una breve interpretación de tu gráfico</div>", unsafe_allow_html=True)
    # st.image("aisladas_base_datos.png", caption='Gráfico de lenguas aisladas', width=500): Esta línea está mostrando una imagen en la aplicación web.
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar.
    # En este caso, la imagen es "aisladas_base_datos.png".
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen,
    # en este caso "Gráfico de lenguas aisladas".
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 500 píxeles.

    # elif grafico_seleccionado == 'mapa_cusco':
    # import streamlit.components.v1 as components
    # with open("mapa_cusco.html", "r", encoding="utf-8") as f:
    #     html_content = f.read()
    # components.html(html_content, height=500): Esta línea está mostrando un archivo HTML en la aplicación web.
    # La función components.html toma como primer argumento el contenido HTML que se desea mostrar.
    # En este caso, el contenido HTML se lee desde el archivo "mapa_cusco.html".
    # El argumento height se utiliza para especificar la altura del contenido HTML, en este caso 500 píxeles.
    
    # Si no tenemos el archivo HTML, podemos agregar el código para crear el mapa de Cusco directamente en Streamlit.
    # Primero debes crear el diccionario de coordenadas del mapa de Cusco.
    # Luego debes crear el mapa utilizando la librería folium y streamlit-folium.
    # pip install folium
    # pip install streamlit-folium
        #import folium
        #from streamlit_folium import st_folium

        # Mostrar el mapa en Streamlit
        #st_folium(mapa_cusco, width=700, height=500)
    
