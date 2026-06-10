import plotly.express as px

def create_bar_chart(data, x, y, title):
    return px.bar(
        data,
        x=x,
        y=y,
        title=title
    )

def create_pie_chart(data, names, values, title):
    return px.pie(
        data,
        names=names,
        values=values,
        title=title
    )