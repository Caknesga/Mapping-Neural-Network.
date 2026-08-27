import matplotlib.pyplot as plt
import numpy as np

# Time vector for plotting (adjusted max time to 4 us)
t = np.linspace(0, 4, 2000)

# Simulated output voltage profile 1 (magenta curve settling at 0.84)
v_sim1 = np.zeros_like(t)
for i, time_val in enumerate(t):
    if time_val < 2.0:
        v_sim1[i] = 0.6
    elif 2.0 <= time_val < 4.0:
        v_sim1[i] = 0.82 + 0.81 * np.exp(-(time_val - 2.0)**2 / 0.005)
    else:
        v_sim1[i] = 0.6

# Simulated output voltage profile 2 (green curve settling at 0.6)
v_sim2 = np.zeros_like(t)
for i, time_val in enumerate(t):
    if time_val < 2.0:
        v_sim2[i] = 0.6
    elif 2.0 <= time_val < 4.0:
        v_sim2[i] = 0.6 + 0.1 * np.exp(-(time_val - 2.0)**2 / 0.005)
    else:
        v_sim2[i] = 0.6

fig, ax = plt.subplots(figsize=(10, 6))

# Plot first simulation result in magenta (#C420E9)
ax.plot(t, v_sim1, color='#C420E9', linewidth=1.5, label='Simulation Result 1')

# Plot second simulation result in green (#0F9529) settling at 0.6
ax.plot(t, v_sim2, color='#0F9529', linewidth=1.5, label='Simulation Result 2')



# Add legend
ax.legend(loc='upper right', fontsize=11)

# Axis limits and labels (max time set to 4)
ax.set_xlim(0, 4)
ax.set_ylim(-0.15, 1.5)
ax.set_xticks([2, 4])
ax.set_xticklabels(['2', '4'])
ax.set_yticks([0, 0.5, 0.6, 0.84, 1.0, 1.5])

ax.set_xlabel('Time ($\mu$s)', fontsize=12)
ax.set_ylabel('Output Voltage (V)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()