import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import pandas as pd
import matplotlib.pyplot as plt
# 读取 CSV
df = pd.read_csv("weather.csv")
# 转换日期
df["time"] = pd.to_datetime(df["time"])
# 数据预览
print(df.head())
print(df.describe())
# 气温折线图
plt.figure(figsize=(12,5))
plt.plot(df["time"], df["temperature_2m_mean"], color='red')
plt.title("首尔每日气温")
plt.xlabel("日期")
plt.ylabel("气温 (°C)")
plt.grid()
plt.show()
# 湿度折线图
plt.figure(figsize=(12,5))
plt.plot(df["time"], df["relativehumidity_2m_mean"], color='blue')
plt.title("首尔每日湿度")
plt.xlabel("日期")
plt.ylabel("湿度 (%)")
plt.grid()
plt.show()
# 降雨量柱状图
plt.figure(figsize=(12,5))
plt.bar(df["time"], df["precipitation_sum"], color='green')
plt.title("首尔每日降雨量")
plt.xlabel("日期")
plt.ylabel("降水量 (mm)")
plt.grid()
plt.show()
python weather_analysis.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("首尔天气数据仪表板")
# 读取 CSV
df = pd.read_csv("weather.csv")
df["time"] = pd.to_datetime(df["time"])
# 数据预览
st.subheader("数据预览")
st.dataframe(df.head())
# 选择年份
years = df["time"].dt.year.unique()
year = st.selectbox("选择年份", years)
filtered = df[df["time"].dt.year == year]
# 气温图
st.subheader(f"{year} 年气温")
fig1, ax1 = plt.subplots(figsize=(10,4))
ax1.plot(filtered["time"], filtered["temperature_2m_mean"], color='red')
ax1.set_xlabel("日期")
ax1.set_ylabel("气温 (°C)")
st.pyplot(fig1)
# 湿度图
st.subheader(f"{year} 年湿度")
fig2, ax2 = plt.subplots(figsize=(10,4))
ax2.plot(filtered["time"], filtered["relativehumidity_2m_mean"], color='blue')
ax2.set_xlabel("日期")
ax2.set_ylabel("湿度 (%)")
st.pyplot(fig2)
# 降雨量图
st.subheader(f"{year} 年降雨量")
fig3, ax3 = plt.subplots(figsize=(10,4))
ax3.bar(filtered["time"], filtered["precipitation_sum"], color='green')
ax3.set_xlabel("日期")
ax3.set_ylabel("降水量 (mm)")
st.pyplot(fig3)
streamlit run app.py
