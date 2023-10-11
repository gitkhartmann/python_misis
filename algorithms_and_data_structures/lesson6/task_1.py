import numpy as np
import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import make_interp_spline

try:
    conn = psycopg2.connect(database='lesson5_db', user='sergo', password='197612', host='localhost', port='5432')

    cursor = conn.cursor()

    cursor.execute(
        "SELECT timestamp, can_data FROM messages WHERE terminal_id = '433100526928004' LIMIT 500;")

    data = cursor.fetchall()

    cursor.execute(
        "SELECT calibrating_data FROM calibrating WHERE deviceid_port = '433100526928004_4';")

    [calibrating_data] = cursor.fetchall()
    calibrating_data, = calibrating_data

    calibrating_data_input = []
    calibrating_data_output = []

    for inputs in calibrating_data:
        calibrating_data_input.append(inputs['input_value'])
        calibrating_data_output.append(inputs['output_value'])

    f = interpolate.interp1d(calibrating_data_input, calibrating_data_output)
    t = []
    cd = []
    t_stamp = []

    for time, can_data in data:
        if time not in t_stamp:
            t_stamp.append(time)
            tm = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
            t.append(tm)
            cd.append(f(can_data['LLS_0']))

    for k in range(len(t) - 1):
        for j in range(len(t) - 1):
            if t[j] > t[j + 1]:
                t[j + 1], t[j] = t[j], t[j + 1]
                cd[j + 1], cd[j] = cd[j], cd[j + 1]
            if t_stamp[j] > t_stamp[j + 1]:
                t_stamp[j + 1], t_stamp[j] = t_stamp[j], t_stamp[j + 1]

    x = np.array(t_stamp)
    y = np.array(cd)

    xnew = np.linspace(x.min(), x.max(), 200)

    spl = make_interp_spline(x, y)
    y_smooth = spl(xnew)

    plt.plot(xnew, y_smooth)
    plt.show()
except:
    print('Can`t connection to database')
