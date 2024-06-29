from fastapi import BackgroundTasks

class Logging:
    """
    Clase para gestionar el envío de logs en segundo plano.

    Esta clase se encarga de agregar una tarea de envío de logs al sistema de
    tareas en segundo plano de FastAPI.

    Atributos:
    - background_task: Instancia de BackgroundTasks para gestionar tareas en segundo plano.

    Métodos:
    - __init__(background_task): Inicializa la clase Logging y agrega una tarea de envío de logs.
    - _send_log(): Método privado para enviar logs (definido como asíncrono).
    """

    def __init__(self, background_task: BackgroundTasks):
        """
        Inicializa una nueva instancia de la clase Logging.

        Este método agrega una tarea asíncrona de envío de logs al gestor de tareas
        en segundo plano proporcionado por FastAPI.

        Parámetros:
        - background_task: Instancia de BackgroundTasks.
        """
        background_task.add_task(self._send_log)

    async def _send_log(self):
        """
        Método privado para enviar logs.

        Este método debería contener la lógica para enviar los logs a un servicio
        externo o almacenarlos en una base de datos. Actualmente está vacío y debe
        ser implementado según las necesidades específicas.
        """
        pass
