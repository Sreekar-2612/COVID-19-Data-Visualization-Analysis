import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('Set2')
sns.set_context("talk")
plt.rcParams['figure.figsize'] = (10, 5)


df = pd.read_csv("owid-covid-data.csv")  # Replace with your dataset path
print("Dataset shape:", df.shape)
print("Columns available:", df.columns[:10].tolist())
print(df.head(5))  # Works in command line


columns_needed = ['location', 'date', 'total_cases', 'new_cases', 
                  'total_deaths', 'new_deaths', 'total_vaccinations', 'population']

available_columns = [col for col in columns_needed if col in df.columns]
df = df[available_columns]
print(f"Columns retained: {list(df.columns)}")

# Handle missing 'total_vaccinations'
if 'total_vaccinations' not in df.columns:
    df['total_vaccinations'] = np.nan
    print("Note: 'total_vaccinations' column not found, added as empty.")


# Data Cleaning

df['date'] = pd.to_datetime(df['date'], errors='coerce', format='mixed')
df.dropna(subset=['date'], inplace=True)

# Fill missing numeric values with 0 for cumulative metrics
for col in ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'total_vaccinations']:
    if col in df.columns:
        df[col] = df[col].fillna(0)

print("\n✅ Data Summary:")
print(df.describe())
print("\nNumber of countries/locations:", df['location'].nunique())


# Top 10 countries by total cases

latest_data = df.sort_values('date').groupby('location').tail(1)  # most recent entry per country
top_cases = latest_data.sort_values('total_cases', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_cases['total_cases'], y=top_cases['location'], palette='Reds_r')
plt.title('🌍 Top 10 Countries by Total COVID-19 Cases', fontsize=15, weight='bold')
plt.xlabel('Total Cases')
plt.ylabel('')
for index, value in enumerate(top_cases['total_cases']):
    plt.text(value + 1000, index, f"{int(value):,}", va='center', fontweight='bold')
plt.show()


# Top 10 countries by total deaths

top_deaths = latest_data.sort_values('total_deaths', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_deaths['total_deaths'], y=top_deaths['location'], palette='Greys_r')
plt.title('⚰️ Top 10 Countries by Total COVID-19 Deaths', fontsize=15, weight='bold')
plt.xlabel('Total Deaths')
plt.ylabel('')
for index, value in enumerate(top_deaths['total_deaths']):
    plt.text(value + 1000, index, f"{int(value):,}", va='center', fontweight='bold')
plt.show()

#  Global Trend: Cases, Deaths, Vaccinations Over Time

global_data = df.groupby('date')[['new_cases','new_deaths','total_vaccinations']].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(x='date', y='new_cases', data=global_data, label='New Cases', color='tomato')
sns.lineplot(x='date', y='new_deaths', data=global_data, label='New Deaths', color='grey')
if df['total_vaccinations'].sum() > 0:
    sns.lineplot(x='date', y='total_vaccinations', data=global_data, label='Total Vaccinations', color='green')
plt.title('📈 Global COVID-19 Trend Over Time', fontsize=15, weight='bold')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.show()

# Interactive Plot: Cases vs Deaths per Country

# Ensure 'population' column exists
if 'population' not in latest_data.columns:
    latest_data['population'] = 1  # fallback to avoid NaN

# Replace NaN or 0 with a small number to avoid Plotly errors
latest_data['population'] = latest_data['population'].fillna(1)
latest_data['population'] = latest_data['population'].replace(0, 1)

# Interactive scatter plot
fig = px.scatter(latest_data, x='total_cases', y='total_deaths',
                 size='population', color='location', hover_name='location',
                 title='🦠 COVID-19: Total Cases vs Total Deaths (Bubble size = Population)',
                 log_x=True, log_y=True, size_max=60,
                 template='plotly_dark', color_discrete_sequence=px.colors.qualitative.Safe)
fig.show()


# Vaccination Progress (Optional)

if df['total_vaccinations'].sum() > 0:
    top_vax = latest_data.sort_values('total_vaccinations', ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=top_vax['total_vaccinations'], y=top_vax['location'], palette='Greens_r')
    plt.title('💉 Top 10 Countries by Total Vaccinations', fontsize=15, weight='bold')
    plt.xlabel('Total Vaccinations')
    plt.ylabel('')
    for index, value in enumerate(top_vax['total_vaccinations']):
        plt.text(value + 1000, index, f"{int(value):,}", va='center', fontweight='bold')
    plt.show()


print("\n📊 Key Insights:")
print(f"- Total countries tracked: {df['location'].nunique()}")
print(f"- Country with highest total cases: {latest_data.loc[latest_data['total_cases'].idxmax(),'location']}")
print(f"- Country with highest total deaths: {latest_data.loc[latest_data['total_deaths'].idxmax(),'location']}")
if df['total_vaccinations'].sum() > 0:
    print(f"- Country with highest total vaccinations: {latest_data.loc[latest_data['total_vaccinations'].idxmax(),'location']}")
print("\n✨ Visualization by Sreekar | Data Source: Kaggle COVID-19 Dataset")
