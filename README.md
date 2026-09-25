//////
Notas

- Antes de los locks, los procesos se mandaban mensajes entre si para saber el estado de las cosas, muchas veces leian mientras otro escribia, escribian mientras otro leia, o escribian uno encima del otro.
Esto lo solucionan los locks, que dan una llave de acceso para que escriban o lean por turnos, y los demas no tengan acceso durante ese tiempo. Esto igual lleva problemas por lo que se usa memmoria compartida
para que todos lean y escriban de un mismo lugar, agilizando todo.

- La **memoria compartida en el multiprocesamiento** se divide en dos clases, **values** en el que se reserva un espacio en la memoria para solo un valor (ejemplo numero de trabajadores, edad, etc. solo un valor)
y **arrays** en el que se reserva un bloque de una lista (como un array de imagen convertida a digital, frame de video, etc.).
Un ejemplo es una camara de seguridad, va pidiendo constantemente la llave de acceso para guardar un nuevo frame de video en el array, y otro proceso va pidiendo la llave constantemente para leer los datos de ese array.

 - En python la memoria se puede asignar dinamicamente, pero para memoria compartida se debe reservar exactamente el tamaño del hueco que se necesita utilizar, para esto usamos ctype, en c, que permite asignar memoria exacta.
 - La clase lock tiene tres tipos:
   1. lock = Lock
   2. lock = false: se deja abierto para los espacios de memoria compartida que estemos seguros que nunca van a chocar procesos
   3. lock = cerradura: candado comunu para dos procesos que esten ligados, que sean dependientes. Ejemplo, en una aplicacion de banco, el poder editar los movimientos y ver el saldo. ambos tienen el mismo candado para que
mientras un proceso modifica el historial otro no modifique el monto de la cuenta.

- Se usa numpy para poder hacer operaciones mas complejas y de matrices, ya que el otro es muy basico. Hay que tener cuidado en definir el tipo de dato correctamente en ambos para no tener problemas.
- Un problema practico real en que esto se utiliza es en el filtrado de imagenes. aplicar el filtro pixel por piel es muy lento, es mejor aplicar el filtro por bloques en paralelo para filtrarla. cada pixel
o bloque de filas se puede calcular independientemente, y para no copiarla para cada proceso, se utiliza la memoria compartida utilizando multiprocessing + array. 


///


Granularidad FIna: Creamos una tarea indeendiente para calcular cada celda individual de la matriz resultante. Si la matriz es grande generarìa demasiadas tareas independientes pequeñas, dando un costo altisimo. Demoraria mas asignando tareas y memoria que calculando.

Granularidad Media (fila por fila): Cada tarea calcula una fila completa de la matriz resultante. el numero de tareas es igual al de filas, muchas menos que con granularidad fina. 
