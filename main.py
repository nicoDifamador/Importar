import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Gestor de Importaciones", layout="wide")

st.title("🚀 Herramienta Multi-Tareas Importación")
st.markdown("---")

# Barra lateral para configuración básica
with st.sidebar:
    st.header("Configuración")
    tc = st.number_input("Tipo de Cambio (S/)", value=3.75, step=0.01)
    unidades = st.number_input("Cantidad de Unidades", value=180)

# Cuerpo principal
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Costos de Importación")
    costo_usd = st.number_input("Costo por Unidad (USD)", value=699.0)
    transporte_pen = st.number_input("Transporte Total (Soles)", value=20.0)
    mkt_pen = st.number_input("Marketing por Unidad (Soles)", value=15.0)

with col2:
    st.subheader("💰 Precio de Venta")
    venta_usd = st.number_input("Precio Venta sugerido (USD)", value=799.0)
    igv_val = st.checkbox("Incluir cálculo de IGV (18%)", value=True)

# Lógica de cálculos
costo_total_soles = (costo_usd * tc) + transporte_pen + mkt_pen
venta_total_soles = (venta_usd * tc)

if igv_val:
    igv_unidad = venta_total_soles - (venta_total_soles / 1.18)
else:
    igv_unidad = 0

ganancia_neta_unidad = venta_total_soles - costo_total_soles - igv_unidad
ganancia_total_lote = ganancia_neta_unidad * unidades

st.markdown("---")
st.header("📊 Resultados Finales")

res1, res2, res3 = st.columns(3)
res1.metric("Ganancia por Unidad", f"S/ {ganancia_neta_unidad:.2f}")
res2.metric("Ganancia Total Lote", f"S/ {ganancia_total_lote:,.2f}")
res3.metric("Impuesto (IGV)", f"S/ {igv_unidad:.2f}")

if ganancia_neta_unidad > 0:
    st.success(f"✅ ¡Es rentable! Estás ganando S/ {ganancia_total_lote:,.2f} en total.")
else:
    st.error("⚠️ Cuidado: Estás operando a pérdida o margen cero.")
