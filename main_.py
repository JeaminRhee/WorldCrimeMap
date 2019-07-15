import folium

m = folium.Map(location=[37.537523, 126.876394], tiles="OpenStreetMap", zoom_start=5)

folium.Marker(location=[37.5344742, 126.9908898], popup="Itaewon Murder Case", tooltip="Itaewon Murder Case").add_to(m)
folium.Marker(location=[34.0518732, -118.2952573], popup="1992 LA Riots", tooltip="1992 LA Riots").add_to(m)

m.save("index.html")