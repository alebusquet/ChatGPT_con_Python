from config import API_KEY                                          # leo la api-key del archivo config.py

import openai                                                       # importo la librería

openai.api_key = API_KEY                                            # asigno la api-key

while True:
    
    prompt = input("\n Ingresa una pregunta o ‘exit’ para salir: ")
    
    if prompt == "exit":
        break	

    completion = openai.Completion.create(engine="text-davinci-003",    # se almacena la respuesta de la API
											prompt = prompt,
											n=1,	                # nro de respuestas, 1 es por default y se podría eliminar
											max_tokens=2048)        # longitud de la respuesta (max=4096)

    print(completion.choices[0].text)		                        # se accede a la primera opción (índice 0) de esa respuesta
