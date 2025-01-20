# Django Minicore: Gestión y Filtro de Gastos

![Django](https://img.shields.io/badge/Framework-Django-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-blue)
![Deployed](https://img.shields.io/badge/Deployed-on_Render-orange)

Este es un proyecto desarrollado con **Django**, enfocado en la gestión y filtro de gastos de empleados por departamento. Incluye una interfaz moderna y funcional que permite visualizar los gastos y calcular los totales por departamento dentro de un rango de fechas específico.

## 🌐 Enlace de la Aplicación
- **Deploy en Render**: [Django Minicore](https://django-gastos-filtro-mvc.onrender.com/)

## 📂 Repositorio
- **GitHub**: [Django Minicore Repository](https://github.com/CrisJurado10/DJANGO_MINICORE.git)

## 🚀 Funcionalidades
- **Filtrado de gastos**: Permite seleccionar un rango de fechas para mostrar los gastos realizados por empleados.
- **Totales por departamento**: Calcula automáticamente el total de gastos para departamentos como IT, Desarrollo, Diseño y Marketing.
- **Interfaz elegante**: Uso de **Bootstrap** para una experiencia de usuario intuitiva y moderna.
- **Datos dinámicos**: Genera información actualizada en tiempo real desde la base de datos.

## ⚙️ Tecnologías Utilizadas
- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **Base de Datos**: MySQL (Railway)
- **Despliegue**: Render
- **Servidor de producción**: Gunicorn

## 📋 Requisitos Previos
Para ejecutar este proyecto localmente, asegúrate de tener instalado:
- Python 3.8 o superior
- MySQL Server
- Virtualenv (opcional, pero recomendado)

## 📦 Instalación y Ejecución Local
1. Clona el repositorio:
   ```bash
   git clone https://github.com/CrisJurado10/DJANGO_MINICORE.git
   cd DJANGO_MINICORE
Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias:
pip install -r requirements.txt

Configura tu base de datos en el archivo settings.py:

Modifica los valores de DATABASES con tus credenciales de MySQL.
python manage.py makemigrations
python manage.py migrate
Inicia el servidor:
python manage.py runserver
Accede a la aplicación localmente en: http://127.0.0.1:8000/
📜 Funcionalidad Clave
Filtrar Gastos
El usuario puede ingresar un rango de fechas para filtrar los gastos realizados por los empleados. Los resultados se presentan en:
Una lista con detalles del empleado, descripción y monto del gasto.
Totales agrupados por departamento.
Cálculo Dinámico
Utilizando consultas a la base de datos, los totales por departamento se actualizan automáticamente.
Interfaz
El diseño de la interfaz utiliza Bootstrap para garantizar que sea responsiva y visualmente atractiva.
🛠 Despliegue
El proyecto está desplegado en Render, utilizando Gunicorn como servidor de producción. Puedes probar la aplicación en vivo en el siguiente enlace:

Django Minicore en Render
🧑‍💻 Autor
Cristian Jurado
GitHub: CrisJurado10
📄 Licencia
Este proyecto está bajo la Licencia MIT. ¡Eres libre de usarlo y modificarlo! 😊
