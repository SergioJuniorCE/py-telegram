# Py-telegram: Herramienta de automatizacion de likes de videos de youtube

El proposito de este script es tomar ventaja del fraude que está circulando en WhatsApp sobre una campaña de likes a videos de YouTube.

Esta "campaña" te invita a dar likes a videos de youtube por $10 MXN por video, pero te ofrecen depositar $500 MXN o más para poder entrar a una membresia VIP donde te "pagan" mas por video. El problema es que a los dias de que se crea el grupo y suficiente gente ha pagado la membresia, los "recepcionistas" (las personas a las que les mandas evidecia de que diste like al video) borran la cuenta y ya no puedes ganar más dinero, actuando como una "flor de la abundancia".

Con este script podemos automatizar el proceso de abrir telegram, buscar el video, dar like y mandar evidencia al recepcionista para ganar nuestra comision.

# Requisitos

Tener instalado:

- Python 3.11
- Telegram
- Navegador web

# Instalacion

Una vez el repositorio descargado hay que instalar los modulos

`pip install -r requirements.txt`

Luego, ya que llegué un mensaje con alguna tarea, correr el script `fraude.py`

Esto hara que busque el link y numero de la mision en el mensaje, luego abrira el link en el navegador predeterminado, dara like al video, tomara el screenshot, removera el link y mandara el mensaje a tu recepcionista con la evidencia

Ya que se manda la evidencia el programa espera la cantidad mencionada en el mensaje para volver a repetir el proceso, haciendo que sea esto 100% automatico
