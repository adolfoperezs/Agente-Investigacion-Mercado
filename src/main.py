import os
from dotenv import load_dotenv

# Usamos las mismas importaciones del bloque anterior
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()

def main():
    # Verificación de claves de API
    if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
        print("Error: Asegúrate de que OPENAI_API_KEY y TAVILY_API_KEY estén en tu archivo .env")
        return
    
    print("✅ ¡Claves de API encontradas!")

    # 1. Definir el LLM de OpenAI
    # Puedes usar "gpt-4-turbo" para resultados de mayor calidad si tienes acceso.
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 2. Herramientas (seguimos con Tavily)
    # Aumentamos a 3 resultados para darle más contexto al agente.
    tools = [TavilySearchResults(max_results=3, description="Herramienta de búsqueda web para obtener información actualizada.")]

    # 3. Crear el Prompt Avanzado (el corazón de este bloque)
    # Este prompt le da al agente un rol, instrucciones y un formato de salida estricto.
    prompt_template = """
    Eres un Analista de Investigación de Mercado Senior. Tu objetivo es generar un informe claro y conciso
    en formato MARKDOWN sobre el tema que te proporcionen.

    Tienes acceso a las siguientes herramientas:

    {tools}

    Debes investigar usando las herramientas disponibles para recopilar la información necesaria y luego
    estructurar la respuesta final siguiendo EXACTAMENTE el siguiente formato Markdown:

    # Informe de Investigación de Mercado: {input}

    ## 1. Resumen Ejecutivo
    *Un párrafo conciso que resuma los puntos más importantes del informe.*

    ## 2. Análisis de la Competencia
    *Identifica 2-3 competidores clave.*
    * **Competidor A:** Breve descripción, fortalezas y debilidades.
    * **Competidor B:** Breve descripción, fortalezas y debilidades.

    ## 3. Tendencias Actuales del Mercado
    *Describe 2-3 tendencias importantes que estén afectando a este mercado.*
    * **Tendencia 1:** [Descripción]
    * **Tendencia 2:** [Descripción]

    ## 4. Análisis FODA (SWOT) Simplificado
    * **Fortalezas:** [Enumera 1-2 fortalezas internas del sector/producto]
    * **Oportunidades:** [Enumera 1-2 oportunidades externas del mercado]
    * **Debilidades:** [Enumera 1-2 debilidades internas del sector/producto]
    * **Amenazas:** [Enumera 1-2 amenazas externas del mercado]

    ## 5. Conclusión y Recomendaciones
    *Un párrafo final con tu conclusión sobre el estado del mercado y una recomendación estratégica.*

    ---

    Para generar el informe, sigue el proceso de pensamiento y acción. Usa la herramienta de búsqueda
    tantas veces como sea necesario para obtener toda la información para CADA sección del informe antes de
    escribir tu respuesta final.

    Usa el siguiente formato:

    Pregunta: la pregunta que debes responder
    Pensamiento: siempre debes pensar en lo que vas a hacer
    Acción: la acción a tomar, debe ser una de [{tool_names}]
    Entrada de la Acción: la entrada para la acción
    Observación: el resultado de la acción
    ... (este Pensamiento/Acción/Entrada de la Acción/Observación puede repetirse N veces)
    Pensamiento: Ahora sé la respuesta final
    Respuesta Final: la respuesta final a la pregunta original

    Comienza el proceso.

    Pregunta: Genera un informe de mercado para "{input}"
    Pensamiento:{agent_scratchpad}
    """
    
    prompt = PromptTemplate.from_template(prompt_template)

    # 4. Crear el Agente (Reactivo)
    agent = create_react_agent(llm, tools, prompt)

    # 5. Crear el Ejecutor del Agente
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    
    # 6. Invocar el agente con un tema de investigación
    tema_investigacion = "el mercado de las cafeterías de especialidad en Santiago de Chile"
    print(f"\n🤖 Iniciando investigación para: '{tema_investigacion}'...")
    
    resultado = agent_executor.invoke({"input": tema_investigacion})

    print("\n\n✅✅✅ INFORME FINAL GENERADO ✅✅✅")
    print("--------------------------------------------------")
    print(resultado["output"])
    
if __name__ == '__main__':
    main()