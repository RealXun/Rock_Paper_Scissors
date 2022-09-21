# Rock, Paper, Scissors
Rock paper scissors is a hand game originating from China, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand.
<p align="center">
    <img src="https://github.com/RealXun/Rock_Paper_Scissors/blob/main/Resources/Cover.png"alt="drawing" width="500"/>

Let's play the famous game against our computer.

https://es.wikipedia.org/wiki/Piedra,_papel_o_tijera

> Use of functions is recommended.



## Objectives
1. Loop Usage
2. Data capture by console
3. Use if-elif-else
4. Use of try-except
5. Definition of functions. Modular programming.
6. Logical operators.
7. Print by console
8. Import of external modules

## Suggested
- Importa la función choice del módulo random
- https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
- Asigna a una lista las 3 posibles opciones: 'piedra', 'papel' o 'tijeras'. 
- Asigna una variable al número de partidas máxima: 1, 3, 5, etc...
- Asigna una variable al número de partidas que debe ganar un jugador para ganar. 
- Preferiblemente el valor será en función de el número de partidas máximas
- Define una función que devuelva aleatoriamente una de las 3 opciones. 
- Esto corresponderá a la jugada de la máquina. Totalmente aleatoria. 
- Define una función que pregunte tu elección: 'piedra', 'papel' o 'tijeras' sólo debe permitir una de las 3 opciones. Esto es programación defensiva. Si no es piedra, papel o tijeras sigue preguntando hasta que lo sea. 
- Define una función que resuelva un combate. 
- Devuelve 0 si hay empate, 1 si gana la máquina, 2 si gana el jugador humano 
- Define una función que muestre la elección de cada jugador y el estado de la partida
- Esta función debe utilizarse cada vez que se actualicen los puntos acumulados 
- Crea dos variables que acumulen las partidas ganadas de cada participante
- Crea un bucle que itere mientras ningún jugador alcance el mínimo de victorias necesarias para ganar. Dentro del bucle resuelve la jugada de la máquina y pregunta la del jugador. Comparalas y actualiza el valor de las variables que acumulen las partidas ganadas de cada participante.   
- Anuncia por consola el ganador del juego en función de quién tiene más victorias aculumadas
