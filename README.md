## Automation framework 

La idea con este proyecto es conocer el funcionamiento de selenium internamente teniendo como base la información
suministrada en la w3c (https://www.w3.org/TR/webdriver/) que es un consorcio internacional que genera recomendaciones 
y estándares de la internet, por lo cual se intentara crear un framework de automatización de pruebas,
con su propia libreria webDriver para el final realizar un ejemplo de automatización.

El funcionamiento como tal de selenium es coger el Chrome
Driver que funciona como una especie de servidor que le envía peticiones, como
por ejemplo levántame el browser, encuéntreme este elemento, cierre el browser etc. En el cual estas peticiones se le pueden enviar
en un formato .json

- Subprocess: Permite abrir el chromedriver, de esta manera tengo un control de cuando abrir y cerrar el chromedriver https://recursospython.com/guias-y-manuales/subprocess-creacion-y-comunicacion-con-procesos/
- Disared capability: Se almacenan las propiedades del navegador que se van a utilizar para la prueba https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities 
- Session: Para levantar chrome o hacer test se necesita generar una sesion dentro del servidor
- SessionId: Es el que se va usar en todo el ciclo de prueba, ya que todas las url que necesite hacer peticiones tiene que ser con el sessionId

### Diseño propuesto para realizar el proyecto

Se anexa el diagrama de componentes y de clases del proyecto


![](Desing/Components%20Diagram.png)

![](Desing/Class%20Diagram.png)