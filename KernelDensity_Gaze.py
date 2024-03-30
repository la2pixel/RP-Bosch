import pandas as pd
# x-axis has taken maximum scenario length from Scenario 3
import seaborn as sns
pastel_palette = sns.color_palette("pastel")
aoi_colors = {
    'ScreenCenter': pastel_palette[0],
    'CenterMirror': pastel_palette[1],
    'InstrumentCluster': pastel_palette[2],
    'RightMirror': pastel_palette[3],
    'LeftMirror': pastel_palette[4],
    'HMIScreen' : pastel_palette[5]
}

gaze_data = []

for df_name in dfs:
    df = globals()[df_name]
    time = df['ser_rostime_0s']
    aois = df['field.aoiZone.zone_name']
    int_flag = df['field.hmiBackgroundState']
    aois = aois[aois != 'HMI Screen']
    
    gaze_data.append((time, aois))

totgaze = pd.concat([pd.DataFrame({'Time': time, 'AOI': aois}) for time, aois in gaze_data])
totgaze = totgaze.interpolate(method='pad')
totgaze = totgaze.dropna(subset=['AOI'])

# Intervention Markings (if needed)
# intervention_start_time = 8.05020655
# intervention_end_time = intervention_start_time + 5

# Kernel Density
plt.figure(figsize=(12, 8))
ax = sns.kdeplot(data=totgaze, x='Time', hue='AOI', multiple='fill', palette=aoi_colors)

# # before and after intervention- adjust x-axis
# plt.xlim(intervention_start_time - 5, intervention_end_time + 5)
# plt.xticks(range(int(intervention_start_time) - 5, int(intervention_end_time) + 6),
#            [str(i - int(intervention_start_time)) for i in range(int(intervention_start_time) - 5, int(intervention_end_time) + 6)])

# # Add a legend for unique AOI values
# legend = ax.get_legend()
# legend.set_title('Glance areas')

plt.xlabel('Time (sec)')
plt.ylabel('Proportion of Glances')
plt.title('General Glance Patterns (All Scenarios combined)')
plt.show()
