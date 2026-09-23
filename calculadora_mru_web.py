import streamlit as st
import matplotlib.pyplot as plt


# -----------------------------
# FUNCIONES MATEMÁTICAS
# -----------------------------

def calcular_rapidez(distancia, tiempo):
    return distancia / tiempo


def calcular_distancia(rapidez, tiempo):
    return rapidez * tiempo


def calcular_tiempo(distancia, rapidez):
    return distancia / rapidez


def generar_datos_movimiento(rapidez, tiempo_final):
    tiempos = []
    distancias = []

    for i in range(11):
        tiempo = tiempo_final * i / 10
        distancia = rapidez * tiempo

        tiempos.append(tiempo)
        distancias.append(distancia)

    return tiempos, distancias


def calcular_pendiente(tiempos, distancias):
    return (
        distancias[-1] - distancias[0]
    ) / (
        tiempos[-1] - tiempos[0]
    )


# -----------------------------
# INTERFAZ WEB
# -----------------------------

st.title("Calculadora MRU")
st.write(
    "Calcula rapidez, distancia o tiempo "
    "y analiza el movimiento mediante una tabla y una gráfica."
)

operacion = st.radio(
    "¿Qué desea calcular?",
    ["Rapidez", "Distancia", "Tiempo"]
)


# -----------------------------
# RAPIDEZ
# -----------------------------

if operacion == "Rapidez":

    distancia = st.number_input(
        "Distancia (m)",
        min_value=0.0
    )

    tiempo = st.number_input(
        "Tiempo (s)",
        min_value=0.0
    )

    if st.button("Calcular"):

        if tiempo <= 0:
            st.error("El tiempo debe ser mayor que cero.")

        else:
            rapidez = calcular_rapidez(
                distancia,
                tiempo
            )

            st.success(
                f"Rapidez = {rapidez:.2f} m/s"
            )

            tiempos, distancias = generar_datos_movimiento(
                rapidez,
                tiempo
            )

            pendiente = calcular_pendiente(
                tiempos,
                distancias
            )

            st.subheader("Tabla tiempo-distancia")

            st.table({
                "Tiempo (s)": [
                    round(t, 2) for t in tiempos
                ],
                "Distancia (m)": [
                    round(d, 2) for d in distancias
                ]
            })

            st.write(
                f"Pendiente de la gráfica: "
                f"{pendiente:.2f} m/s"
            )

            if abs(pendiente - rapidez) < 0.0001:
                st.info(
                    "La pendiente coincide con la rapidez."
                )

            fig, ax = plt.subplots()

            ax.plot(
                tiempos,
                distancias,
                marker="o"
            )

            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Distancia (m)")
            ax.set_title("Gráfica distancia-tiempo")
            ax.grid()

            st.pyplot(fig)


# -----------------------------
# DISTANCIA
# -----------------------------

elif operacion == "Distancia":

    rapidez = st.number_input(
        "Rapidez (m/s)",
        min_value=0.0
    )

    tiempo = st.number_input(
        "Tiempo (s)",
        min_value=0.0
    )

    if st.button("Calcular"):

        distancia = calcular_distancia(
            rapidez,
            tiempo
        )

        st.success(
            f"Distancia = {distancia:.2f} m"
        )

        if tiempo > 0:

            tiempos, distancias = generar_datos_movimiento(
                rapidez,
                tiempo
            )

            pendiente = calcular_pendiente(
                tiempos,
                distancias
            )

            st.subheader("Tabla tiempo-distancia")

            st.table({
                "Tiempo (s)": [
                    round(t, 2) for t in tiempos
                ],
                "Distancia (m)": [
                    round(d, 2) for d in distancias
                ]
            })

            st.write(
                f"Pendiente de la gráfica: "
                f"{pendiente:.2f} m/s"
            )

            fig, ax = plt.subplots()

            ax.plot(
                tiempos,
                distancias,
                marker="o"
            )

            ax.set_xlabel("Tiempo (s)")
            ax.set_ylabel("Distancia (m)")
            ax.set_title("Gráfica distancia-tiempo")
            ax.grid()

            st.pyplot(fig)


# -----------------------------
# TIEMPO
# -----------------------------

elif operacion == "Tiempo":

    distancia = st.number_input(
        "Distancia (m)",
        min_value=0.0
    )

    rapidez = st.number_input(
        "Rapidez (m/s)",
        min_value=0.0
    )

    if st.button("Calcular"):

        if rapidez <= 0:
            st.error(
                "La rapidez debe ser mayor que cero."
            )

        else:
            tiempo = calcular_tiempo(
                distancia,
                rapidez
            )

            st.success(
                f"Tiempo = {tiempo:.2f} s"
            )

            if tiempo > 0:

                tiempos, distancias = generar_datos_movimiento(
                    rapidez,
                    tiempo
                )

                pendiente = calcular_pendiente(
                    tiempos,
                    distancias
                )

                st.subheader("Tabla tiempo-distancia")

                st.table({
                    "Tiempo (s)": [
                        round(t, 2) for t in tiempos
                    ],
                    "Distancia (m)": [
                        round(d, 2) for d in distancias
                    ]
                })

                st.write(
                    f"Pendiente de la gráfica: "
                    f"{pendiente:.2f} m/s"
                )

                fig, ax = plt.subplots()

                ax.plot(
                    tiempos,
                    distancias,
                    marker="o"
                )

                ax.set_xlabel("Tiempo (s)")
                ax.set_ylabel("Distancia (m)")
                ax.set_title("Gráfica distancia-tiempo")
                ax.grid()

                st.pyplot(fig)
