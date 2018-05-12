import numpy             as np
import datetime          as dt
import pandas            as pd
from   Tkinter           import Tk
from   tkFileDialog      import askopenfilename

# NAME:
#         read_rstn
# PURPOSE:
#         Read 1-second RSTN data (Do not need unzip the file)
# CALLING SECUENCE:
#         df, sta, date_string = read_rstn()
#         Stations: sagamorehill, palehua, sanvito, learmonth
# OUTPUTS:
#         timer (Civil time UT)
#         The maximum solar radio flux observable on each frequency is:
#           245 MHz     500,000 solar flux units (sfu)
#           410 MHz     500,000 sfu
#           610 MHz     500,000 sfu
#          1415 MHz     100,000 sfu
#          2695 MHz      50,000 sfu
#          4995 MHz      50,000 sfu
#          8800 MHz      50,000 sfu
#         15400 MHz      50,000 sfu
#          where one sfu = 10-22 Watts/Meter2/Hertz.
# MODIFICATION HISTORY:
#         Created by Ray Hidalgo 2015-03-30
#         Modificated 2016-10-10
def read_rstn():
    Tk().withdraw()
    filename =    askopenfilename()
    rstn     =    np.genfromtxt(filename, delimiter=2*[4]+5*[2]+8*[7], dtype=('|S10', int, int, int, int, int, int,
                                float, float,float, float,float, float,float, float),
                                names = ['sta','year','mon','day','hour','min','sec','f1','f2','f3','f4','f5','f6',
                                          'f7','f8'])
    date_string = filename[-14:-7]
    station   = {'K7OL':'Sagamore Hill',
                 'PHFF':'Palehua',
                 'LISS': 'San Vito',
                 'APLM': 'Learmonth'}
    timer    =    np.array(map(dt.datetime,rstn['year'],rstn['mon'],rstn['day'],
                                           rstn['hour'],rstn['min'],rstn['sec']))

    data     = np.transpose([rstn['f1'],rstn['f2'],rstn['f3'],rstn['f4'],rstn['f5'],rstn['f6'],rstn['f7'],rstn['f8']])
    df       = pd.DataFrame(data ,index=timer, columns=['245 MHz','410 MHz','610 MHz','1.4 GHz',
                                                          '2.7 GHz','4.9 GHz','8.8 GHz','15.4 GHz'])
    return df, station[rstn['sta'][0]], date_string

# Since some month in 2015 the number of columns change from 7 to 8
def read_rstn_2():
    Tk().withdraw()
    filename =    askopenfilename()
    rstn     =    np.genfromtxt(filename, delimiter=2*[4]+5*[2]+8*[8], dtype=('|S10', int, int, int, int, int, int,
                                float, float,float, float,float, float,float, float),
                                names = ['sta','year','mon','day','hour','min','sec','f1','f2','f3','f4','f5','f6',
                                          'f7','f8'])
    date_string = filename[-14:-7]
    station   = {'K7OL':'Sagamore Hill',
                 'PHFF':'Palehua',
                 'LISS': 'San Vito',
                 'APLM': 'Learmonth'}
    timer    =    np.array(map(dt.datetime,rstn['year'],rstn['mon'],rstn['day'],
                                           rstn['hour'],rstn['min'],rstn['sec']))

    data     = np.transpose([rstn['f1'],rstn['f2'],rstn['f3'],rstn['f4'],rstn['f5'],rstn['f6'],rstn['f7'],rstn['f8']])
    df       = pd.DataFrame(data ,index=timer, columns=['245 MHz','410 MHz','610 MHz','1.4 GHz',
                                                          '2.7 GHz','4.9 GHz','8.8 GHz','15.4 GHz'])
    return df, station[rstn['sta'][0]], date_string
