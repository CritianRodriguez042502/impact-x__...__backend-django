
# IMPACT X | Backend |

Este es el repositorio del backend de Impact X, la plataforma de blogs desarrollada en conjunto con React y Vite. El backend de Impact X gestiona la lógica de negocio y la comunicación con la base de datos para hacer funcionar todas las características del sistema.


## Características Destacadas

* **Gestión de Usuarios** : El backend administra la creación de cuentas de usuario, la activación de cuentas a través de correos electrónicos, el inicio de sesión, el cambio de contraseñas y nombres de usuario, así como la gestión de imágenes de perfil de usuario.
* **Gestión de Blogs** : Gestiona la creación, actualización y eliminación de blogs, incluyendo campos como título, descripción, imagen de portada, configuración de privacidad, categoría y contenido de blog.
* **Comentarios y Likes** : Administra la funcionalidad de comentarios y likes en los blogs, asegurando que los comentarios siempre aparezcan en la parte superior y sean editables o eliminables.

## Requisitos

Asegúrate de tener instalado Python y Django en tu entorno de desarrollo.

## Instalación

1. Clona el repositorio :

    **git clone https://github.com/tuusuario/tuprojecto-backend.git**


2. Navega al directorio del proyecto :

    **cd tuproyecto-backend**


3. Crea un entorno virtual e instala las dependencias :

    **python -m venv venv
      source venv/bin/activate  # En sistemas Unix
      venv\Scripts\activate
      pip install -r requirements.txt**


4. Configura las variables de entorno en un archivo `.env` siguiendo el formato proporcionado en `.env.example`.
5. Realiza las migraciones y crea la base de datos :

   **python manage.py makemigrations
   python manage.py migrate**
7. Inicia el proyecto :

   **python manage.py runserver**


## Contribución

Si deseas contribuir a este proyecto, sigue estas pautas:

* Realiza un fork del repositorio.
* Crea una rama para tu contribución.
* Realiza los cambios y crea una solicitud de extracción (PR) describiendo tus contribuciones.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](https://chat.openai.com/c/LICENSE) para obtener más detalles.


## Contacto

Para preguntas o comentarios, puedes contactarme a través de [cuentagit1111@gmail.com](mailto:cuentagit1111@gmail.com).


## Agradecimientos

Agradecemos a todos los colaboradores que han hecho posible el desarrollo del backend de Impact X.
