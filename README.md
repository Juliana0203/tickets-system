# 🎫 Sistema de Tickets - Prueba Técnica

Aplicación web desarrollada con Django para la gestión de tickets de soporte.
Permite a los usuarios crear tickets y a los administradores gestionarlos desde el panel de administración.

---

## 🚀 Requisitos

* Python 3.10 o superior
* pip
* virtualenv (opcional pero recomendado para correrlo en un ambiente virtaul si no se cuenta con las aplicaciones necesarias para correrlo de forma local)

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd tickets-system
```

---

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

---

## 🌐 Acceso a la aplicación

* Aplicación: http://127.0.0.1:8000/login/

---

## 🔐 Credenciales de prueba

### 👤 Usuario (crear tickets)

* Usuario: `usuario1`
* Contraseña: `Juliana123*`

Este usuario puede:

* Iniciar sesión
* Crear tickets
* Ver sus tickets

---

### 🛠️ Administrador

* Usuario: `admin`
* Contraseña: `admin123`

Este usuario puede:

* Acceder a `/admin/`
* Ver todos los tickets
* Cambiar el estado de los tickets
* Gestionar usuarios

---

## 📌 Funcionalidades implementadas

* Autenticación de usuarios
* Creación de tickets
* Visualización de tickets propios
* Detalle de ticket
* Panel de administración con gestión de estado
* Interfaz básica con Bootstrap

---

## 🧠 Notas

* El sistema utiliza el panel de administración de Django para la gestión de tickets.
* Los usuarios solo pueden ver sus propios tickets.
* Los administradores pueden actualizar el estado de los tickets.

---

## 📄 Autor

Prueba técnica desarrollada por Juliana Moreno Narvaez
