import matplotlib.pyplot as plt
import numpy as np

# Frequency vector from 10^1 to 10^11 Hz (logarithmic scale)
freq = np.logspace(1, 11, 2000)

# Recreating the noise spectral density curve (#E14714)
noise_density = 4.2 * (freq / 10)**(-0.85) + 0.01

# Simulating Curve 2: Total Integrated Noise (Cumulative RMS Voltage starting low and rising to a plateau of 114 uV)
integrated_noise = 114 * (1 - np.exp(-(np.log10(freq) - 1) / 2.5))
integrated_noise = np.clip(integrated_noise, 0, 114)

# Set up dark theme to match Cadence Virtuoso style
fig, ax1 = plt.subplots(figsize=(8, 5))

# Plot the spectral noise density curve in #E14714 on primary axis
line1 = ax1.plot(freq, noise_density, color='#E14714', linewidth=1.2, label='Noise Spectral Density')
ax1.set_xscale('log')
ax1.set_xlim(10**1, 10**11)
ax1.set_ylim(-0.4, 4.4)
ax1.set_xlabel('Frequency (Hz)', fontsize=10)
ax1.set_ylabel('V**2/Hz (nV**2/Hz)', fontsize=10, color='#E14714')
ax1.tick_params(axis='y', labelcolor='#E14714')

# Create secondary y-axis for the Total Integrated Noise (Curve 2)
ax2 = ax1.twinx()
line2 = ax2.plot(freq, integrated_noise, color='#243DA3', linewidth=1.5, linestyle='-', label='Total Integrated Noise ($V_{RMS}$)')

# Add 114 uV explicitly to the right y-axis ticks/labels and remove the arrow annotation
current_yticks = list(ax2.get_yticks())
if 114 not in current_yticks:
    current_yticks.append(114)
ax2.set_yticks(sorted([t for t in current_yticks if 0 <= t <= 140]))

ytick_labels = [f'{int(t)}' if t != 114 else '114 µV' for t in ax2.get_yticks()]
ax2.set_yticklabels(ytick_labels)

ax2.set_ylim(0, 140)
ax2.set_ylabel('Integrated Noise ($\mu$V)', fontsize=10, color='#243DA3')
ax2.tick_params(axis='y', labelcolor='#243DA3')

# Title and grid
plt.title('Noise Analysis & Total Integrated Noise Result', fontsize=12)
ax1.grid(True, which='both', linestyle='-', linewidth=0.3, alpha=0.3)

# Combine legends and place them at the top left corner
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=9)

plt.tight_layout()
plt.show()