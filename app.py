
import streamlit as st
import pandas as pd

st.set_page_config(page_title="WTK Strategic Planner", layout="wide")

if "plan" not in st.session_state:
    st.session_state.plan = pd.DataFrame({
        "Rok":["Inż I","Inż II","Inż III","Mgr I","Mgr II"],
        "PL":[120,0,0,60,55],
        "Zagraniczni":[10,0,0,3,2]
    })

st.title("🚀 WTK Strategic Planner v3")

tabs = st.tabs(["Dashboard","Planowanie 2027","ROI i wpływy","Algorytm AGH"])

with tabs[1]:
    st.header("Planowanie 2027")
    st.info("Zmiany tutaj wpływają na prognozy w Dashboardzie.")
    st.session_state.plan = st.data_editor(st.session_state.plan, use_container_width=True)

plan = st.session_state.plan
pl = int(plan["PL"].sum())
foreign = int(plan["Zagraniczni"].sum())
weighted_students = pl + 7*foreign

current_students = 120
current_subvention = 5_000_000

growth_factor = weighted_students / max(current_students,1)
forecast_2027 = current_subvention * (1 + 0.25*(growth_factor-1))
forecast_2028 = forecast_2027 * 1.08
forecast_2029 = forecast_2028 * 1.08

with tabs[0]:
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Subwencja 2026", f"{current_subvention:,.0f} zł")
    c2.metric("Prognoza 2027", f"{forecast_2027:,.0f} zł")
    c3.metric("Prognoza 2028", f"{forecast_2028:,.0f} zł")
    c4.metric("Prognoza 2029", f"{forecast_2029:,.0f} zł")

    st.subheader("Studenci")
    st.write(f"PL: {pl}, Zagraniczni: {foreign}, Ważeni: {weighted_students}")

    st.subheader("Największe dźwignie")
    ranking = pd.DataFrame({
        "Działanie":[
            "10 studentów zagranicznych",
            "50 studentów inżynierskich",
            "Kategoria A → A+",
            "1 profesor",
            "1 mln projektów"
        ],
        "Wpływ względny":[100,75,60,35,10]
    })
    st.bar_chart(ranking.set_index("Działanie"))

with tabs[2]:
    st.header("ROI i wpływy krańcowe")

    roi = pd.DataFrame({
        "Działanie":[
            "+1 student",
            "+1 student zagraniczny",
            "+1 profesor",
            "+1 mln projektów",
            "A → A+"
        ],
        "Szacowany wpływ":[
            "+0.03%",
            "+0.20%",
            "+0.08%",
            "+0.01%",
            "+5-15%"
        ]
    })
    st.dataframe(roi, use_container_width=True)

    st.success("Największy potencjał dla WTK: rozwój studiów inżynierskich i studentów zagranicznych.")

with tabs[3]:
    st.header("Jak liczony jest algorytm?")

    st.markdown("""
### §3
50% podziału = rok poprzedni

### §4
Studenci = 33%
Student zagraniczny Wz = 7

### §5
Kadra = 33%
Profesor = 2.5
Profesor zagraniczny = 3.0

### §7
Badania = 29%
Technologie kosmiczne KS = 3.25

### §8
Projekty = 5%

### Stabilizacja
Maksymalny wzrost udziału +4%
Maksymalny spadek udziału -1.5%
""")
