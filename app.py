import streamlit as st

st.title("Clasificación Jerárquica de AML según el Consenso Internacional")
st.write("Este aplicativo implementa la clasificación de la Leucemia Mieloide Aguda (AML) basada en el Consenso Internacional de Clasificación (ICC).")

# Variables para almacenar el diagnóstico principal y los cualificadores
primary_diagnosis_category = ""
diagnostic_qualifiers = []

# Entrada para el porcentaje de blastos
st.subheader("Paso 1: Porcentaje de blastos mieloides")
blast_percentage = st.number_input(
    "¿Cuál es el porcentaje de blastos mieloides en la médula ósea? (Debe ser ≥ 10%)",
    min_value=0, max_value=100, step=1, value=10
)

# Validación del porcentaje de blastos
if blast_percentage < 10:
    st.error("El porcentaje de blastos debe ser al menos 10% para diagnosticar AML/MDS según esta clasificación.")
    st.stop()

# 1. Anomalías Genéticas Recurrentes (AGR)
st.subheader("Paso 2: Anomalías Genéticas Recurrentes (AGR)")
AGR_input = st.radio(
    "¿El paciente presenta anomalías genéticas recurrentes (AGR)?",
    ("Sí", "No")
).lower()

if AGR_input == "sí":
    if blast_percentage >= 20:
        primary_diagnosis_category = "AML con anomalías genéticas recurrentes"
    else:  # 10-19% blastos
        primary_diagnosis_category = "MDS/AML con anomalías genéticas recurrentes"
    st.write(f"El paciente presenta **{primary_diagnosis_category}**.")
    st.write("Requiere tratamiento inmediato.")
else:
    st.write("No se detectaron anomalías genéticas recurrentes, continuamos la indagación.")

# 2. Mutación en TP53
if not primary_diagnosis_category:
    st.subheader("Paso 3: Mutación en TP53")
    TP53_mutation_input = st.radio(
        "¿El paciente presenta mutación en TP53 (patogénica con VAF ≥10%)?",
        ("Sí", "No")
    ).lower()
    if TP53_mutation_input == "sí":
        if blast_percentage >= 20:
            primary_diagnosis_category = "AML con TP53 mutado"
        else:  # 10-19% blastos
            primary_diagnosis_category = "MDS/AML con TP53 mutado"
        st.write(f"El paciente presenta **{primary_diagnosis_category}**.")
    else:
        st.write("No se detectó mutación en TP53, continuamos la indagación.")

# 3. Mutaciones en genes relacionados con mielodisplasia
if not primary_diagnosis_category:
    st.subheader("Paso 4: Mutaciones en genes relacionados con mielodisplasia")
    MDS_gene_mutation_input = st.radio(
        "¿El paciente presenta mutaciones en genes relacionados con mielodisplasia (ASXL1, BCOR, EZH2, RUNX1, SF3B1, SRSF2, STAG2, U2AF1, y/o ZRSR2)?",
        ("Sí", "No")
    ).lower()
    if MDS_gene_mutation_input == "sí":
        if blast_percentage >= 20:
            primary_diagnosis_category = "AML con mutaciones en genes relacionados con mielodisplasia"
        else:  # 10-19% blastos
            primary_diagnosis_category = "MDS/AML con mutaciones en genes relacionados con mielodisplasia"
        st.write(f"El paciente presenta **{primary_diagnosis_category}**.")
    else:
        st.write("No se detectaron mutaciones en genes relacionados con mielodisplasia, continuamos la indagación.")

# 4. Anormalidades citogenéticas relacionadas con mielodisplasia
if not primary_diagnosis_category:
    st.subheader("Paso 5: Anormalidades citogenéticas relacionadas con mielodisplasia")
    MDS_cytogenetic_abnormality_input = st.radio(
        "¿El paciente presenta anormalidades citogenéticas relacionadas con mielodisplasia (cariotipo complejo, del(5q)/t(5q)/add(5q), –7/del(7q), +8, del(12p)/t(12p)/add(12p), i(17q), –17/add(17p)/del(17p), del(20q), o idic(X)(q13))?",
        ("Sí", "No")
    ).lower()
    if MDS_cytogenetic_abnormality_input == "sí":
        if blast_percentage >= 20:
            primary_diagnosis_category = "AML con anormalidades citogenéticas relacionadas con mielodisplasia"
        else:  # 10-19% blastos
            primary_diagnosis_category = "MDS/AML con anormalidades citogenéticas relacionadas con mielodisplasia"
        st.write(f"El paciente presenta **{primary_diagnosis_category}**.")
    else:
        st.write("No se detectaron anormalidades citogenéticas relacionadas con mielodisplasia, continuamos la indagación.")

# 5. AML no especificado de otra manera (NOS)
if not primary_diagnosis_category:
    st.subheader("Paso 6: AML no especificado de otra manera")
    if blast_percentage >= 20:
        primary_diagnosis_category = "AML no especificado de otra manera"
    else:  # 10-19% blastos
        primary_diagnosis_category = "MDS/AML no especificado de otra manera"
    st.write(f"El paciente presenta **{primary_diagnosis_category}**.")

# 6. Cualificadores Diagnósticos
st.subheader("Paso 7: Cualificadores Diagnósticos")
therapy_related = st.radio(
    "¿El paciente tiene antecedentes de 'Terapia-relacionada'?",
    ("Sí", "No")
).lower()
if therapy_related == "sí":
    diagnostic_qualifiers.append("Terapia-relacionada")

prior_mds_mpn = st.radio(
    "¿El paciente tiene antecedentes de 'Mielodisplasia (MDS)' o 'MDS/Neoplasia Mieloproliferativa (MPN)'?",
    ("Sí", "No")
).lower()
if prior_mds_mpn == "sí":
    diagnostic_qualifiers.append("Antecedentes de MDS o MDS/MPN")

germline_predisposition = st.radio(
    "¿El paciente tiene una 'Predisposición Germinal' a AML?",
    ("Sí", "No")
).lower()
if germline_predisposition == "sí":
    diagnostic_qualifiers.append("Predisposición Germinal")

# Resumen del Diagnóstico
st.subheader("Resumen del Diagnóstico")
if primary_diagnosis_category:
    st.write(f"El diagnóstico principal del paciente es: **{primary_diagnosis_category}**.")
else:
    st.write("No se pudo establecer un diagnóstico principal de AML/MDS con los datos proporcionados.")

if diagnostic_qualifiers:
    st.write("Cualificadores diagnósticos adicionales:")
    for qualifier in diagnostic_qualifiers:
        st.write(f"- {qualifier}")
else:
    st.write("No se identificaron cualificadores diagnósticos adicionales.")

st.write("--- Fin de la Clasificación ---")
