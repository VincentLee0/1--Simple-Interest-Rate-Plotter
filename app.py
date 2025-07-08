import streamlit as st
import plotly.express as px
import pandas as pd


st.title("Interactive Interest Rate Data Visualization with Plotly and Streamlit")


# Data from user
st.sidebar.header("Input Parameters")
principal = st.sidebar.number_input(
    "Enter the principal amount:", min_value=100, max_value=100000, value=5000, step=100)
rate = st.sidebar.number_input(
    "Enter the interest rate (in %):", min_value=0.1, max_value=20.0, value=5.0, step=0.1)
time = st.sidebar.number_input(
    "Enter the time (in years):", min_value=1, max_value=100, value=5, step=1)


# Total Portfolio Value Calculation via Compounding Interest
data1 = {"Year": [], "Value": []}
for t in range(0, time + 1):
    value = (principal * (1 + rate / 100) ** t) if t > 0 else principal
    data1["Year"].append(t)
    data1["Value"].append(value)
# Pandas DataFrame for compounded interest
df1 = pd.DataFrame(data1)
# Plotly for compounded interest
fig1 = px.line(df1,
               x="Year",
               y="Value",
               title="Compounded Value Over Time",
               labels={"Year": "Year", "Value": "Total Value ($)"},
               markers=True)
# Display the plot in Streamlit
st.plotly_chart(fig1, use_container_width=True)


# Display the Table in Streamlit
st.header("Compounded value over time table")
st.dataframe(df1, use_container_width=True)


# Interest Earned Per Year Calculation
data2 = {"Year": [], "Interest Earned": []}
for t in range(1, time + 1):
    interest_earned = principal * \
        (1 + rate / 100) ** t - principal * (1 + rate / 100) ** (t - 1)
    data2["Year"].append(t)
    data2["Interest Earned"].append(interest_earned)
# Pandas DataFrame for interest earned per year
df2 = pd.DataFrame(data2)
# Plotly for interest earned per year
fig2 = px.bar(df2,
              x="Year",
              y="Interest Earned",
              title="Interest Earned Per Year",
              labels={"Year": "Year",
                      "Interest Earned": "Interest Earned ($)"},
              text="Interest Earned")
# Display the plot in Streamlit
st.plotly_chart(fig2, use_container_width=True)
# Display the Table in Streamlit
st.header("Interest earned per year table")
st.dataframe(df2, use_container_width=True)
# Total Interest Earned Calculation
total_interest_earned = df1["Value"].iloc[-1] - principal
# Display the total interest earned
st.subheader(
    f"Total Interest Earned Over {time} Years: ${total_interest_earned:.2f}")
