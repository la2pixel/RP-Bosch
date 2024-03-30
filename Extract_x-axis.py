totpd = []
for df_name in s1:
    df = globals()[df_name] 
    pd = df['field.eyeTracker.filteredPupilDiameter']
    totpd.extend(pd)

    # 2. Initialize empty lists to store 5s worth time data per intervention phase
    bef_int = []
    dur_int = []
    aft_int = []

    # 3. Iterate through s1 data and change x-axis
for df_name in s1:
    df = globals()[df_name]
    time = df['ser_rostime_0s']
    pd = df['field.eyeTracker.filteredPupilDiameter']
    intervention_flag = df['field.hmiBackgroundState']
    
    # Intervention Condition for S1
    event_indices = intervention_flag[intervention_flag == 4].index
    if len(event_indices) > 0:
        start_time = time[event_indices[0]]
        end_time = start_time + 5  # Trim df
        bef_int.append(pd[(time >= start_time - 5) & (time < start_time)])
        dur_int.append(pd[(time >= start_time) & (time <= end_time)])
        aft_int.append(pd[(time > end_time) & (time <= end_time + 5)])