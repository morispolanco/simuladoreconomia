import streamlit as st

def main():
    st.title("10 Conceptos Económicos Complejos Explicados")
    st.write("Selecciona un concepto para aprender más sobre él")

    # Diccionario con conceptos económicos y sus explicaciones
    conceptos = {
        "1. Producto Interno Bruto (PIB)": """
        El PIB mide el valor total de bienes y servicios finales producidos en un país durante un período específico. 
        Es como tomar el pulso económico de una nación. Existen tres enfoques para calcularlo: producción, ingreso y gasto.
        """,
        
        "2. Inflación": """
        Es el aumento sostenido y generalizado en los precios de bienes y servicios. Imagina que tu dinero pierde poder 
        adquisitivo con el tiempo, como si se "derritiera" lentamente.
        """,
        
        "3. Política Monetaria": """
        Son las acciones de un banco central para controlar la cantidad de dinero y crédito en la economía. Es como 
        ajustar las válvulas de una gran máquina económica.
        """,
        
        "4. Curva de Phillips": """
        Muestra la relación inversa entre inflación y desempleo a corto plazo. Piensa en ello como una balanza: cuando 
        el desempleo baja, la inflación tiende a subir, y viceversa.
        """,
        
        "5. Ventaja Comparativa": """
        Es la capacidad de un país para producir un bien a un costo de oportunidad menor que otro. Es como especializarse 
        en lo que eres relativamente mejor, incluso si no eres el mejor absoluto.
        """,
        
        "6. Elasticidad de la Demanda": """
        Mide cómo responde la cantidad demandada de un bien ante cambios en su precio. Imagina un resorte: algunos bienes 
        tienen demanda elástica (muy sensible), otros inelástica (poco sensible).
        """,
        
        "7. Externalidades": """
        Son costos o beneficios que afectan a terceros no involucrados en una transacción. Como cuando la contaminación 
        de una fábrica afecta a los vecinos, sin que ellos compren sus productos.
        """,
        
        "8. Teoría de Juegos": """
        Estudia cómo toman decisiones los agentes cuando sus resultados dependen de las elecciones de otros. Es como 
        jugar ajedrez económico, anticipando movimientos rivales.
        """,
        
        "9. Paridad del Poder Adquisitivo": """
        Sugiere que a largo plazo, los tipos de cambio deberían ajustarse para igualar el poder de compra entre países. 
        Piensa en ello como una balanza internacional de precios.
        """,
        
        "10. Ciclos Económicos": """
        Son las fluctuaciones recurrentes en la actividad económica: expansión, pico, recesión y recuperación. Como las 
        olas en el océano de la economía.
        """
    }

    # Menú de selección
    concepto_seleccionado = st.selectbox("Elige un concepto:", list(conceptos.keys()))
    
    # Mostrar explicación
    st.subheader("Explicación:")
    st.write(conceptos[concepto_seleccionado])
    
    # Ejemplo práctico
    st.subheader("Ejemplo práctico:")
    if concepto_seleccionado == "1. Producto Interno Bruto (PIB)":
        st.write("Si un país produce $100 en autos y $50 en alimentos en un año, su PIB sería $150.")
    elif concepto_seleccionado == "2. Inflación":
        st.write("Si un café costaba $1 el año pasado y ahora $1.10, la inflación fue del 10%.")
    # Podrías agregar más ejemplos para cada concepto
    
    # Gráfico simple de ejemplo
    if st.button("Mostrar gráfico de ejemplo"):
        import matplotlib.pyplot as plt
        import numpy as np
        
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("Gráfico ilustrativo")
        st.pyplot(plt)

if __name__ == "__main__":
    main()
