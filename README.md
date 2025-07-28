# Agente de Investigación de Mercado

## Descripción

Este proyecto implementa un agente de investigación de mercado automatizado utilizando tecnologías de Inteligencia Artificial. El agente es capaz de generar informes de mercado estructurados y detallados sobre cualquier tema o sector, utilizando información actualizada de internet.

## Características Principales

- **Investigación Automatizada**: Realiza búsquedas web en tiempo real para obtener información actualizada.
- **Informes Estructurados**: Genera informes en formato Markdown con secciones predefinidas.
- **Análisis Completo**: Incluye resumen ejecutivo, análisis de competencia, tendencias de mercado y análisis FODA.
- **Personalizable**: Fácilmente adaptable para diferentes temas de investigación.
- **Compatibilidad con Modelos Avanzados**: Soporte para modelos de OpenAI, incluyendo gpt-4o-mini.

## Requisitos Técnicos

- Python 3.x
- Claves de API:
  - OpenAI API Key
  - Tavily API Key (para búsquedas web)

## Instalación

1. Clona este repositorio:
   ```
   git clone [URL del repositorio]
   cd agente-investigador
   ```

2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

3. Configura las variables de entorno:
   - Crea un archivo `.env` en la raíz del proyecto
   - Añade tus claves de API:
     ```
     OPENAI_API_KEY=tu_clave_de_openai
     TAVILY_API_KEY=tu_clave_de_tavily
     ```

## Uso

1. Ejecuta el script principal:
   ```
   python src/main.py
   ```

2. Por defecto, el agente generará un informe sobre "el mercado de las cafeterías de especialidad en Santiago de Chile". Para cambiar el tema de investigación, modifica la variable `tema_investigacion` en el archivo `src/main.py`.

## Estructura del Proyecto

```
agente-investigador/
├── .env                  # Archivo de variables de entorno (no incluido en el repositorio)
├── requirements.txt      # Dependencias del proyecto
├── src/
│   ├── main.py          # Script principal que ejecuta el agente
│   └── custom_chat_model.py  # Clase personalizada para compatibilidad con o4-mini
└── README.md            # Este archivo
```

## Componentes Principales

### 1. Modelo de Lenguaje (LLM)

El proyecto utiliza el modelo `gpt-4o-mini` de OpenAI a través de la biblioteca LangChain. Se ha implementado una clase personalizada `CustomChatOpenAI` para manejar la compatibilidad con este modelo, específicamente para gestionar el parámetro 'stop' que no es compatible con o4-mini.

### 2. Herramientas de Búsqueda

Se utiliza la API de Tavily para realizar búsquedas web en tiempo real y obtener información actualizada sobre el tema de investigación.

### 3. Agente Reactivo

El proyecto implementa un agente reactivo utilizando el framework de LangChain, que sigue un proceso de pensamiento y acción para generar el informe final.

### 4. Prompt Estructurado

El agente utiliza un prompt detallado que define:
- El rol del agente como Analista de Investigación de Mercado Senior
- Las herramientas disponibles
- El formato exacto del informe final
- El proceso de pensamiento y acción a seguir

## Formato del Informe

Los informes generados siguen esta estructura:

1. **Resumen Ejecutivo**: Síntesis de los puntos clave del informe.
2. **Análisis de la Competencia**: Identificación de 2-3 competidores clave con sus fortalezas y debilidades.
3. **Tendencias Actuales del Mercado**: Descripción de 2-3 tendencias relevantes.
4. **Análisis FODA (SWOT)**: Fortalezas, Oportunidades, Debilidades y Amenazas del mercado.
5. **Conclusión y Recomendaciones**: Conclusiones finales y recomendaciones estratégicas.

## Personalización

Para personalizar el agente:

1. **Cambiar el Modelo**: Modifica la variable `model` en la instancia de `ChatOpenAI` en `main.py`.
2. **Ajustar el Prompt**: Modifica la plantilla de prompt en `main.py` para cambiar el formato o las instrucciones.
3. **Cambiar el Tema**: Actualiza la variable `tema_investigacion` para investigar diferentes mercados.

## Licencia

[Especificar la licencia del proyecto]

---

Desarrollado con ❤️ utilizando LangChain y OpenAI