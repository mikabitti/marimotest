import marimo

__generated_with = "0.17.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from datetime import datetime, timedelta
    import time
    import re
    return datetime, re


@app.cell
def _(re):
    kelloteksti= "Kello on tällä hetkellä 18:49. Hauskaa päivänjatkoa!"
    times = re.findall(r'\b\d{1,2}:\d{2}\b', kelloteksti)
    print(times)  # Output: ['18:30', '09:15']
    return (times,)


@app.cell
def _(datetime, times):
    timestring = times[0]
    now = datetime.now()
    return now, timestring


@app.cell
def _(datetime, now, timestring):
    time_parts = datetime.strptime(timestring, "%H:%M")
    time_object = now.replace(
        hour=time_parts.hour,
        minute=time_parts.minute,
        second=0,
        microsecond=0
    )

    difference = now - time_object
    return (difference,)


@app.cell
def _(difference):
    m = difference.seconds//60
    s = difference.seconds - m*60

    print(m, s)

    return


if __name__ == "__main__":
    app.run()
