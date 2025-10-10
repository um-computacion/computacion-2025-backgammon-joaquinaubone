Prompt usado

Necesito generar tests unitarios para la clase Dice (ubicada en Dice/dice.py).  
La clase tiene un método tirar() que usa random.randint para generar dos valores de dado (entre 1 y 6) y los guarda en self.__values__.  

Quiero que me generes tests unitarios para cubrir específicamente el método tirar(), incluyendo:  
- Caso normal con dos valores distintos.  


Modelo usado
	•	ChatGPT (OpenAI, GPT-5, septiembre 2025)

Instrucciones del sistema
	•	No se usaron instrucciones de sistema personalizadas, solo el contexto estándar del asistente.

Respuesta de la IA

La IA generó una clase TestDice con tres métodos de test:
	1.	test_tirar_devuelve_dos_valores
	•	Verifica que con side_effect=[5,2], el método tirar() guarde [5,2] en __values__.


Archivos impactados
	•	Dice/test_dice.py → se agregaron los tests generados por IA.
	