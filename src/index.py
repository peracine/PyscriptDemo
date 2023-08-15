import matplotlib.pyplot as plt
import data
from datetime import datetime
from pyscript import Element, when

#cf: https://docs.pyscript.net/latest/reference/API/attr_to_event.html
@when(event_type='change', selector='#slctYear')
def slctYear_changed(evt) -> None:
    year:int = None
    div_target = 'divPlot'
    if evt.target.value.isnumeric():
        year = int(evt.target.value)
    else:
        return

    #cf: https://docs.pyscript.net/latest/reference/API/element.html
    Element(div_target).clear()

    data1 = data.get_timeseries(1, datetime(year, 1, 1), datetime(year, 12, 31))
    data2 = data.get_timeseries(30, datetime(year, 1, 1), datetime(year, 12, 31))

    fig, ax = plt.subplots()
    plt.title(f'Year: {year}')
    plt.plot(data1.keys(), data1.values(), color='g')
    plt.plot(data2.keys(), data2.values(), color='b')
    ax.legend(['data1', 'data2'])

    #cf: https://docs.pyscript.net/latest/reference/API/display.html
    display(fig, target=div_target)