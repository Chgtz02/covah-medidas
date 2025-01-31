import streamlit as st

# Título de la aplicación
st.title("Covah - Calculadora de Medidas")

# Funciones de cálculo
def calcular_gabinetes_superiores(ancho, alto, tiene_objeto_arriba, tiene_objeto_abajo, num_puertas):
    if tiene_objeto_arriba and tiene_objeto_abajo:
        alto -= .6  # Restar 6 mm si hay objetos arriba y abajo
    elif tiene_objeto_arriba or tiene_objeto_abajo:
        alto -= .3  # Restar 3 mm si hay objeto arriba o abajo

    if num_puertas == 1:
        ancho_puerta = ancho - .4  # Restar 4 mm si es 1 puerta
    elif num_puertas == 2:
        ancho_puerta = (ancho / 2) - .3  # Dividir y restar 3 mm si son 2 puertas
    else:
        raise ValueError("Número de puertas no válido. Debe ser 1 o 2.")

    return ancho_puerta, alto


def calcular_esquinero_superior(lado1, lado2, alto, tiene_objeto_arriba, tiene_objeto_abajo):
    if tiene_objeto_arriba and tiene_objeto_abajo:
        alto -= 0.6  # Restar 6 mm si hay objetos arriba y abajo
    elif tiene_objeto_arriba or tiene_objeto_abajo:
        alto -= 0.3  # Restar 3 mm si hay objeto arriba o abajo

    puerta1 = lado1 - 28.5 - 1.5 - 0.3
    puerta2 = lado2 - 28.5 - 0.3

    return puerta1, puerta2, alto


def calcular_esquinero_inferior(lado1, lado2):
    alto = 67  # La altura del esquinero inferior siempre será 67
    
    puerta1 = lado1 - 58.5 - 1.5 - 0.3
    puerta2 = lado2 - 58.5 - 0.3

    return puerta1, puerta2, alto


def calcular_muebles_inferiores(ancho, num_puertas):
    alto_puerta = 67  # El alto de las puertas siempre es 67 cm

    if num_puertas == 1:
        ancho_puerta = ancho - .4  # Restar 3 mm si es 1 puerta
    elif num_puertas == 2:
        ancho_puerta = (ancho / 2) - 0.3  # Dividir y restar 0.3 mm si son 2 puertas
    else:
        raise ValueError("Número de puertas no válido. Debe ser 1 o 2.")

    return ancho_puerta, alto_puerta


# Gabinetes Superiores
st.header("Gabinetes Superiores")
ancho_sup = st.number_input("Ancho (cm):", key="ancho_sup")
alto_sup = st.number_input("Alto (cm):", key="alto_sup")
num_puertas_sup = st.radio("Número de puertas:", [1, 2], key="num_puertas_sup")
tiene_objeto_arriba_sup = st.checkbox("¿Tiene objeto arriba?", key="objeto_arriba_sup")
tiene_objeto_abajo_sup = st.checkbox("¿Tiene objeto abajo?", key="objeto_abajo_sup")

if st.button("Calcular Gabinetes Superiores"):
    ancho_puerta_sup, alto_puerta_sup = calcular_gabinetes_superiores(
        ancho_sup, alto_sup, tiene_objeto_arriba_sup, tiene_objeto_abajo_sup, num_puertas_sup
    )
    st.success(f"Medidas de la puerta: Ancho = {ancho_puerta_sup} cm, Alto = {alto_puerta_sup} cm")

# Gabinetes Inferiores
st.header("Gabinetes Inferiores")
ancho_inf = st.number_input("Ancho (cm):", key="ancho_inf")
num_puertas_inf = st.radio("Número de puertas:", [1, 2], key="num_puertas_inf")

if st.button("Calcular Gabinetes Inferiores"):
    ancho_puerta_inf, alto_puerta_inf = calcular_muebles_inferiores(ancho_inf, num_puertas_inf)
    st.success(f"Medidas de la puerta: Ancho = {ancho_puerta_inf} cm, Alto = {alto_puerta_inf} cm")

# Esquinero Superior
st.header("Esquinero Superior")
lado1_sup = st.number_input("Lado 1 (cm):", key="lado1_sup")
lado2_sup = st.number_input("Lado 2 (cm):", key="lado2_sup")
alto_esq_sup = st.number_input("Alto (cm):", key="alto_esq_sup")
tiene_objeto_arriba_esq_sup = st.checkbox("¿Tiene objeto arriba?", key="objeto_arriba_esq_sup")
tiene_objeto_abajo_esq_sup = st.checkbox("¿Tiene objeto abajo?", key="objeto_abajo_esq_sup")

if st.button("Calcular Esquinero Superior"):
    puerta1_sup, puerta2_sup, alto_esq_sup = calcular_esquinero_superior(
        lado1_sup, lado2_sup, alto_esq_sup, tiene_objeto_arriba_esq_sup, tiene_objeto_abajo_esq_sup
    )
    st.success(f"Puerta 1: {puerta1_sup} cm, Puerta 2: {puerta2_sup} cm, Alto: {alto_esq_sup} cm")

# Esquinero Inferior
st.header("Esquinero Inferior")
lado1_inf = st.number_input("Lado 1 (cm):", key="lado1_inf")
lado2_inf = st.number_input("Lado 2 (cm):", key="lado2_inf")

if st.button("Calcular Esquinero Inferior"):
    puerta1_inf, puerta2_inf, alto_esq_inf = calcular_esquinero_inferior(
        lado1_inf, lado2_inf
    )
    st.success(f"Puerta 1: {puerta1_inf} cm, Puerta 2: {puerta2_inf} cm, Alto: {alto_esq_inf} cm")
