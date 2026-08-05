import numpy as np
import matplotlib.pyplot as plt

def calculate_process_capability(data, lsl, usl):
    """
    Calculates Mean, Sigma, Cp, and Cpk for a manufacturing process dataset.
    """
    mean = np.mean(data)
    sigma = np.std(data, ddof=1) # Sample standard deviation
    
    # Calculate capability indices
    cp = (usl - lsl) / (6 * sigma)
    cpu = (usl - mean) / (3 * sigma)
    cpl = (mean - lsl) / (3 * sigma)
    cpk = min(cpu, cpl)
    
    return mean, sigma, cp, cpk

# --- Practical Test (e.g., Battery Cell Thickness in mm) ---
if __name__ == "__main__":
    # Target: 5.0mm, Tolerances: 4.8mm to 5.2mm
    LSL, USL = 4.8, 5.2
    
    # Simulating 100 sample measurements from the production line
    np.random.seed(42)
    sample_data = np.random.normal(loc=5.01, scale=0.04, size=100)
    
    # Run analysis
    m, s, cp, cpk = calculate_process_capability(sample_data, LSL, USL)
    
    print(f"--- Quality Metrics Summary ---")
    print(f"Process Mean: {m:.4f}")
    print(f"Process Sigma (StDev): {s:.4f}")
    print(f"Cp Index: {cp:.2f}")
    print(f"Cpk Index: {cpk:.2f} (Process is {'Capable' if cpk >= 1.33 else 'Not Capable'})")

    # Generate Engineering Visual Alignment Plot
    plt.figure(figsize=(8, 5))
    plt.hist(sample_data, bins=15, edgecolor='black', alpha=0.6, label='Product Samples')
    plt.axvline(LSL, color='red', linestyle='--', linewidth=2, label=f'LSL ({LSL})')
    plt.axvline(USL, color='red', linestyle='--', linewidth=2, label=f'USL ({USL})')
    plt.axvline(m, color='green', linestyle='-', linewidth=2, label=f'Mean ({m:.2f})')
    plt.title("Process Capability Analysis Histogram")
    plt.xlabel("Measurement Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True, alpha=0.3)
    # plt.show() # Uncomment to run locally and view the plot image
