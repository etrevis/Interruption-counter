from tkinter import *
import pandas as pd
from datetime import datetime

data_dict = {'Time': [],
			'Interrupted': [],
			'Self-distracted': []				
			}

master = Tk()

def save_it():
	df = pd.read_csv('workfromhome_interruptions.csv', sep=',', header=0)
	df_int = pd.DataFrame(data_dict)
	print(df.tail())
	new_df = df.append(df_int, ignore_index=True)
	new_df.to_csv('workfromhome_interruptions.csv', sep=',', index=False)
	print('Data saved. Total interruptions: {}'.format(len(new_df['Interrupted'])))
	data_dict['Time'] = []
	data_dict['Interrupted'] = []
	data_dict['Self-distracted'] = []


def interrupted():
	now = datetime.now()
	dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
	data_dict['Time'].append(dt_string)
	data_dict['Interrupted'].append(1)
	data_dict['Self-distracted'].append(0)
	print("Interrupted at: ", dt_string[11:])

def self_interrupted():
	now = datetime.now()
	dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
	data_dict['Time'].append(dt_string)
	data_dict['Interrupted'].append(0)
	data_dict['Self-distracted'].append(1)
	print("Self distrcted at: ", dt_string[11:])

b = Button(master, text="Interrupted", command=interrupted)
c = Button(master, text="Self interrupted", command=self_interrupted)
ex = Button(master, text="Save", command=save_it)
b.pack()
c.pack()
ex.pack()

mainloop()