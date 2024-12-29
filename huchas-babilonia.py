import streamlit as st
import pandas as pd

def calculate_budget(income, percentages):
    return {category: income * percentage / 100 for category, percentage in percentages.items()}

# Configuración inicial
st.title("💰 Las huchas de Babilonia 💰")
st.markdown("""
El camino hacia la libertad financiera según "El hombre más rico de Babilonia". 

Puedes ajustar los porcentajes si lo deseas. Si estás en el móvil, toca la flecha superior izquierda ">" para ajustarlos.
""")

# Entrada de ingresos
ingresos = st.number_input("Introduce tus ingresos del mes:", min_value=0.0, step=10.0)

# Porcentajes preestablecidos
percentages = {
    "Libertad financiera": 10,
    "Ahorro a largo plazo": 10,
    "Básicos": 55,
    "Disfrute": 10,
    "Educación": 10,
    "Dar": 5
}

# Mostrar sliders en el sidebar
st.sidebar.header("Ajusta los porcentajes")
for category in percentages.keys():
    percentages[category] = st.sidebar.slider(
        f"{category} (%)", min_value=0, max_value=100, value=percentages[category]
    )

# Verificación de que los porcentajes sumen 100
if sum(percentages.values()) != 100:
    st.error(f"Los porcentajes deben sumar 100%. Actualmente suman {sum(percentages.values())}%.")
else:
    # Cálculo del presupuesto
    presupuesto = calculate_budget(ingresos, percentages)

    # Mostrar resultados
    st.header("Distribución del presupuesto")
    for category, amount in presupuesto.items():
        st.write(f"{category} ({percentages[category]}%): {amount:.2f} €")