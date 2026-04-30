#  Documento de Diseño - Sistema de Tickets

---

## Presentación

Soy Juliana Moreno, estudiante de Ingeniería de Sistemas en sexto semestre.
Cuento con conocimientos en desarrollo de software, especialmente en backend con Python (framework Django) y Java (framework Node.js). También tengo conocimientos de frontend usando el framework Angular y manejando frameworks como tailwind y bootstrap. Por la parte de bases de datos tengo conocimientos usando PostgresSQL, MySQL, MongoDB y C3. Me interesa el desarrollo de aplicaciones web y la construcción de soluciones prácticas orientadas a resolver problemas reales.

---

## Decisiones de diseño

Para el desarrollo del sistema se tomaron las siguientes decisiones:

* **Uso de Django:** Se eligió Django por ser un framework robusto que permite desarrollar aplicaciones web de forma rápida, segura y estructurada.
* **Separación de roles:** Se definieron dos tipos de usuarios:

  * Usuario normal: crea y consulta sus tickets.
  * Administrador: gestiona todos los tickets desde el panel de administración.
* **Uso del admin de Django:** En lugar de crear un panel desde cero, se utilizó el panel administrativo de Django para gestionar los tickets, optimizando el tiempo de desarrollo.
* **Restricción de acceso:** Los usuarios solo pueden ver sus propios tickets, garantizando privacidad.
* **Interfaz simple:** Se utilizó Bootstrap para lograr una interfaz básica pero funcional.

---

## Modelo de datos

Se diseñaron los siguientes modelos principales:

### 1. Ticket

Representa una solicitud o incidencia creada por un usuario.

Campos principales:

* `titulo`: nombre del ticket
* `descripcion`: detalle del problema
* `estado`: estado actual del ticket (pendiente, en proceso, resuelto)
* `usuario`: relación con el usuario que crea el ticket
* `fecha_creacion`: fecha de creación automática

### 2. Categoria

Permite clasificar los tickets según su tipo.

Campos:

* `nombre`: nombre de la categoría

Relación:

* Un ticket pertenece a una categoría

---

## Supuestos realizados

Durante el desarrollo se asumió que:

* No se requiere registro público de usuarios por lo que los usuarios son creados manualmente desde la interfaz de admin en Django.
* El sistema no necesita manejo de roles complejos (solo usuario y administrador).
* La gestión de tickets por parte del administrador se realiza exclusivamente desde el panel de Django.
* No se implementa notificación en tiempo real ni envío de correos.
* El sistema está pensado para uso básico sin interfaz compleja.

---

## Uso de Inteligencia Artificial

Sí, se utilizó inteligencia artificial como apoyo durante el desarrollo. Más que todo para revisar errores que se podían generar durante la realización del código. El resto del código es de autoría própia. El readme fue estructurado por una IA generativa para mejorar su aspecto visual.El uso de IA fue como herramienta de apoyo, manteniendo comprensión y control sobre el código desarrollado.

* **Herramienta utilizada:** ChatGPT

* **Propósito:**

  * Resolución de errores técnicos
  * Mejora de estructura del código
  * Apoyo en la creación de documentación

---

##  Definición de categorías de tickets

Se propusieron las siguientes categorías:

* **Soporte técnico:** problemas con funcionamiento del sistema
* **Acceso:** inconvenientes con login o permisos
* **Facturación:** temas relacionados con pagos o cobros

### Criterio utilizado

Las categorías fueron definidas con base en:

* Tipos de problemas más comunes en sistemas reales
* Claridad para el usuario al momento de clasificar su solicitud
* Facilidad de gestión para el administrador

Se buscó un equilibrio entre simplicidad y utilidad, evitando una categorización excesiva.

---

##  Conclusión

El sistema implementado cumple con los requerimientos básicos de gestión de tickets, permitiendo la interacción entre usuarios y administradores de forma clara y estructurada. Se priorizó la simplicidad, funcionalidad y el uso eficiente de herramientas disponibles como el admin de Django.
