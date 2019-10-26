import folium


def getIcon(per, max=1):
    if per / max > 0.30:
        return folium.Icon(color="blue")
    elif per / max > 0.20:
        return folium.Icon(color="green")
    elif per / max > 0.10:
        return folium.Icon(color="lightgreen")
    else:
        return folium.Icon(color="red")


def getForeingPercentage(headers, values):
    return float(values[headers.index("Poblacion nacida en otra entidad")]) / float(
        values[headers.index("Poblacion Total")]
    )


dataFile = open("demografiasZMG2010.csv", "r", errors="ignore")
m = folium.Map(location=[20.6564561, -103.3468714], zoom_start=12)
line = dataFile.readline()
headers = line.split(",")
line = dataFile.readline()

while line:
    values = line.split(",")
    porcentageDeForaneos = getForeingPercentage(headers, values)
    coordinates = [
        float(values[headers.index("LAT")]),
        float(values[headers.index("LONG")]),
    ]
    text = (
        values[headers.index("Colonia")]
        + " "
        + str(round(porcentageDeForaneos * 100, 2))
        + "%"
    )
    folium.Marker(coordinates, popup=text, icon=getIcon(porcentageDeForaneos)).add_to(m)
    line = dataFile.readline()

path = "demoMap.html"
m.save(path)
print("Saved Succeded")
