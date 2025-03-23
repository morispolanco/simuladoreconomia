import streamlit as st
import requests

# Configuración de la API Key desde Streamlit Secrets (sin valor por defecto en el código)
API_KEY = st.secrets["API_KEY"]

# Diccionario con conceptos económicos y sus explicaciones
economic_concepts = {
    "1. Elasticidad de la demanda": {
        "description": "Mide cómo responde la cantidad demandada de un bien ante cambios en su precio.",
        "simulation": "Si el precio de un café sube de $2 a $3 y la demanda cae de 100 a 80 tazas, la elasticidad es -0.67."
    },
    "2. Costo de oportunidad": {
        "description": "El valor de la mejor alternativa a la que se renuncia al tomar una decisión.",
        "simulation": "Si estudias 2 horas en vez de trabajar ($10/hora), tu costo de oportunidad es $20."
    },
    "3. Ventaja comparativa": {
        "description": "Capacidad de producir un bien a un menor costo de oportunidad que otros.",
        "simulation": "País A produce 10 carros o 5 casas, País B produce 6 carros o 4 casas."
    },
    "4. Externalidades": {
        "description": "Costos o beneficios que afectan a terceros no involucrados en la transacción.",
        "simulation": "Una fábrica contamina un río, afectando a pescadores cercanos."
    },
    "5. Producto Marginal": {
        "description": "Aumento en la producción al añadir una unidad más de un factor.",
        "simulation": "Con 2 trabajadores produces 10 sillas, con 3 produces 18: MP = 8."
    },
    "6. Inflación": {
        "description": "Aumento sostenido en el nivel general de precios.",
        "simulation": "Si un pan costaba $1 y ahora $1.10, la inflación es del 10%."
    },
    "7. Curva de Phillips": {
        "description": "Relación inversa entre inflación y desempleo a corto plazo.",
        "simulation": "Inflación sube al 5%, desempleo baja al 3%."
    },
    "8. Multiplicador keynesiano": {
        "description": "Efecto amplificado del gasto público en la economía.",
        "simulation": "$100 de gasto público generan $250 en actividad económica (multiplicador = 2.5)."
    },
    "9. Asimetría de información": {
        "description": "Cuando una parte tiene más información que la otra en una transacción.",
        "simulation": "Un vendedor de autos usados sabe de fallos que el comprador ignora."
    },
    "10. Equilibrio de Nash": {
        "description": "Situación donde nadie mejora cambiando su estrategia unilateralmente.",
        "simulation": "Dos empresas eligen precios: si ambas bajan, ninguna gana más."
    }
}

# Función para consultar la API
def get_api_response(concept):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "qwen/qwq-32b:free",
        "messages": [{"role": "user", "content": f"Explain {concept} in simple terms"}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"No se pudo conectar a la API: {str(e)}"

# Configuración de la aplicación Streamlit
st.title("Simulador de Conceptos Económicos")
st.write("Explora 10 conceptos económicos complejos con explicaciones y simulaciones simples.")

# Menú desplegable para seleccionar concepto
concept = st.selectbox("Selecciona un concepto económico:", list(economic_concepts.keys()))

# Mostrar descripción y simulación
st.subheader("Explicación")
st.write(economic_concepts[concept]["description"])

st.subheader("Simulación")
st.write(economic_concepts[concept]["simulation"])

# Opción para consultar la API
if st.button("Obtener explicación adicional desde API"):
    api_response = get_api_response(concept)
    st.write("Respuesta de la API:", api_response)

# Gráfico simple como ejemplo (para elasticidad)
if concept == "1. Elasticidad de la demanda":
    st.line_chart({"Precio": [2, 3], "Demanda": [100, 80]})
