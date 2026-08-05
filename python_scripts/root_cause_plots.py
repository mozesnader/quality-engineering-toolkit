import pandas as pd
import matplotlib.pyplot as plt

def generate_pareto_chart(defect_counts):
    """
    Creates an automated 80/20 Pareto Chart for Root Cause Analysis.
    """
    df = pd.DataFrame(list(defect_counts.items()), columns=['Defect_Type', 'Count'])
    df = df.sort_values(by='Count', ascending=False).reset_index(drop=True)
    
    # Calculate cumulative metrics
    df['Cumulative_Sum'] = df['Count'].cumsum()
    df['Cumulative_Percent'] = (df['Cumulative_Sum'] / df['Count'].sum()) * 100
    
    # Build chart
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Primary bar chart for raw counts
    ax1.bar(df['Defect_Type'], df['Count'], color='steelblue', edgecolor='black')
    ax1.set_ylabel('Defect Frequency (Count)', color='steelblue')
    ax1.tick_params(axis='y', labelcolor='steelblue')
    plt.xticks(rotation=45, ha='right')
    
    # Secondary line graph for percentage distribution
    ax2 = ax1.twinx()
    ax2.plot(df['Defect_Type'], df['Cumulative_Percent'], color='crimson', marker='o', linewidth=2)
    ax2.set_ylabel('Cumulative Percentage (%)', color='crimson')
    ax2.tick_params(axis='y', labelcolor='crimson')
    ax2.axhline(80, color='gray', linestyle='--', alpha=0.7, label='80% Threshold')
    
    plt.title("Production Line Scrap Breakdown (Pareto Analysis)")
    fig.tight_layout()
    # plt.show() # Uncomment to view the chart locally

# --- Practical Test (Sample Scrap Categories) ---
if __name__ == "__main__":
    scrap_log = {
        "Dimensional Deviation": 45,
        "Surface Scratch": 28,
        "Improper Assembly": 12,
        "Material Contamination": 6,
        "Labeling Error": 3
    }
    generate_pareto_chart(scrap_log)
