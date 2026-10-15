
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Literacy Explorer",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------------------------
# AI LITERACY & RESPONSIBLE USE EXPLORER
# Synthetic demonstration data only
# -------------------------------------------------

st.title("AI Literacy & Responsible Use Explorer")
st.write(
    "Explore student generative AI usage, verification "
    "habits, and responsible AI awareness."
)

st.info(
    "Research demo: all records below are synthetic. "
    "They are not real student responses or research findings."
)

# Sample data for demonstration
data = [
    ["S001", "Undergraduate", "Daily", "Assignments", "Always", "High", "Yes"],
    ["S002", "Postgraduate", "Weekly", "Research", "Often", "High", "Yes"],
    ["S003", "Undergraduate", "Daily", "Writing", "Sometimes", "Medium", "No"],
    ["S004", "Postgraduate", "Monthly", "Research", "Always", "High", "Yes"],
    ["S005", "Undergraduate", "Weekly", "Learning", "Often", "Medium", "Yes"],
    ["S006", "Postgraduate", "Daily", "Assignments", "Sometimes", "Medium", "No"],
    ["S007", "Undergraduate", "Rarely", "Learning", "Always", "Low", "Yes"],
    ["S008", "Postgraduate", "Weekly", "Writing", "Often", "High", "Yes"],
    ["S009", "Undergraduate", "Daily", "Assignments", "Rarely", "Low", "No"],
    ["S010", "Postgraduate", "Daily", "Research", "Always", "High", "Yes"],
    ["S011", "Undergraduate", "Weekly", "Writing", "Sometimes", "Medium", "Yes"],
    ["S012", "Postgraduate", "Monthly", "Learning", "Often", "Medium", "Yes"],
    ["S013", "Undergraduate", "Daily", "Assignments", "Often", "High", "No"],
    ["S014", "Postgraduate", "Weekly", "Research", "Always", "High", "Yes"],
    ["S015", "Undergraduate", "Rarely", "Writing", "Sometimes", "Low", "No"],
    ["S016", "Postgraduate", "Daily", "Research", "Often", "Medium", "Yes"],
    ["S017", "Undergraduate", "Weekly", "Learning", "Always", "Medium", "Yes"],
    ["S018", "Postgraduate", "Daily", "Assignments", "Rarely", "Low", "No"],
    ["S019", "Undergraduate", "Monthly", "Writing", "Often", "Medium", "Yes"],
    ["S020", "Postgraduate", "Weekly", "Research", "Always", "High", "Yes"],
]

columns = [
    "Response_ID",
    "Study_Level",
    "AI_Usage",
    "Primary_Purpose",
    "Verification_Habit",
    "AI_Literacy_Self_Rating",
    "Privacy_Awareness"
]

df = pd.DataFrame(data, columns=columns)

# Sidebar filters
st.sidebar.header("Explore the responses")

study_levels = st.sidebar.multiselect(
    "Study level",
    options=df["Study_Level"].unique().tolist(),
    default=df["Study_Level"].unique().tolist()
)

usage_levels = st.sidebar.multiselect(
    "AI usage frequency",
    options=["Daily", "Weekly", "Monthly", "Rarely"],
    default=["Daily", "Weekly", "Monthly", "Rarely"]
)

filtered = df[
    df["Study_Level"].isin(study_levels)
    & df["AI_Usage"].isin(usage_levels)
]

# Summary metrics
st.subheader("Survey Overview")

total = len(filtered)

daily_users = (
    filtered["AI_Usage"] == "Daily"
).sum()

regular_verification = filtered[
    "Verification_Habit"].isin(["Always", "Often"]
).sum()

privacy_aware = (
    filtered["Privacy_Awareness"] == "Yes"
).sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Responses", total)
c2.metric(
    "Daily AI Users",
    int(daily_users),
    f"{daily_users / total:.0%} of filtered responses"
    if total else "No responses"
)
c3.metric(
    "Often/Always Verify",
    int(regular_verification),
    f"{regular_verification / total:.0%} of filtered responses"
    if total else "No responses"
)
c4.metric(
    "Privacy Awareness",
    int(privacy_aware),
    f"{privacy_aware / total:.0%} of filtered responses"
    if total else "No responses"
)

st.caption(
    "Percentages describe only the selected synthetic records. "
    "Self-ratings and reported habits are not objective tests."
)

# Charts
st.subheader("AI Usage Patterns")

left, right = st.columns(2)

with left:
    st.write("**AI usage frequency**")
    if not filtered.empty:
        st.bar_chart(
            filtered["AI_Usage"].value_counts().reindex(
                ["Daily", "Weekly", "Monthly", "Rarely"],
                fill_value=0
            )
        )
    else:
        st.write("No responses match these filters.")

with right:
    st.write("**Primary purpose of AI use**")
    if not filtered.empty:
        st.bar_chart(filtered["Primary_Purpose"].value_counts())
    else:
        st.write("No responses match these filters.")

st.subheader("Responsible AI Practices")

left, right = st.columns(2)

with left:
    st.write("**Information verification habits**")
    if not filtered.empty:
        st.bar_chart(
            filtered["Verification_Habit"].value_counts().reindex(
                ["Always", "Often", "Sometimes", "Rarely"],
                fill_value=0
            )
        )

with right:
    st.write("**Self-rated AI literacy**")
    if not filtered.empty:
        st.bar_chart(
            filtered["AI_Literacy_Self_Rating"].value_counts().reindex(
                ["High", "Medium", "Low"],
                fill_value=0
            )
        )

# Detailed data
st.subheader("Explore Survey Records")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

# CSV download
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered responses (CSV)",
    data=csv,
    file_name="ai_literacy_demo_responses.csv",
    mime="text/csv"
)

# Research reflection
st.subheader("Questions for Further Research")

st.markdown("""
- Does AI usage frequency vary by study level?
- How frequently do students verify AI-generated information?
- Does self-rated AI literacy correspond with reported verification habits?
- How aware are students of privacy considerations when using AI?
- What educational interventions could support responsible AI use?
""")

st.warning(
    "These charts are descriptive, not evidence of causation. "
    "The sample is synthetic and must not be used to claim "
    "findings about real university students."
)

st.caption(
    "Built with Python, Streamlit and Pandas | "
    "Educational research prototype"
)
