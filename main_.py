import folium
from  folium import LayerControl, FeatureGroup, plugins
from folium.plugins import MousePosition, Draw
from folium.features import CustomIcon

# Customizing Marker
url = 'http://leafletjs.com/examples/custom-icons/{}'.format
icon_image = url('leaf-red.png')
shadow_image = url('leaf-shadow.png')

icon = CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76)
)



# Setting The Beginning Point
min_lon, max_lon = -45, -35
min_lat, max_lat = -45, -15
f = folium.Figure(width=1000, height=500)
m = folium.Map(max_bounds=True, location=[37.537523, 126.876394], tiles="CartoDB dark_matter", zoom_start=2,  max_zoom=10, min_lat=min_lat).add_to(f)


# Adding Tile Layers
folium.TileLayer('openstreetmap').add_to(m)
folium.TileLayer('cartodbpositron').add_to(m)
folium.TileLayer('stamentoner').add_to(m)

WCH = FeatureGroup(name='World Crime History')
W50DC = FeatureGroup(name='The World 50 Dangerous Cities')
GunGroup = FeatureGroup(name='Gun-Possessing Allowed Countries')
USCrimeGroup = FeatureGroup(name='US-The Most Dangerous Cities')

# World Crime History
folium.Marker(location=[37.5344742, 126.9908898], popup="Stamen Terrain",icon=folium.Icon(icon='cloud'), tooltip="Itaewon Murder Case").add_to(WCH)
folium.Marker(location=[34.0518732, -118.2952573], popup="1992 LA Riots", icon=folium.Icon(icon='cloud'), tooltip="1992 LA Riots").add_to(WCH)

# The World 50 Dangerous Cities
folium.Marker(location=[23.2707228, -110.3272912], popup="Total murders (2017): 365 \nMurders per 100,000 people: 111.33", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'), tooltip="Los Cabos").add_to(W50DC)
folium.Marker(location=[10.4683612, -67.0304547], popup="In 2018, Caracas had a population of 2,980,\n492 people and 2,980 homicides.", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'), tooltip="Caracas").add_to(W50DC)
folium.Marker(location=[16.8359278, -100.142516], popup="Homicide Rate(Per 100,000): 106.63", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Acapulco").add_to(W50DC)
folium.Marker(location=[-5.8268438, -35.2419186], popup="Homicide Rate(Per 100,000): 102.56", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Natal, Brazil").add_to(W50DC)
folium.Marker(location=[32.4969713, -117.087895], popup="Homicide Rate(Per 100,000): 100.77", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Tijuana").add_to(W50DC)
folium.Marker(location=[24.1165776, -110.3727681], popup="Homicide Rate(Per 100,000): 84.79", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="La Paz, Mexico").add_to(W50DC)
folium.Marker(location=[-3.7897468, -38.6590366], popup="Homicide Rate(Per 100,000): 83.48", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Fortaleza - State of Ceará, Brazil").add_to(W50DC)
folium.Marker(location=[23.7411381, -99.2133792], popup="Homicide Rate(Per 100,000): 83.32", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Ciudad Victoria, Mexico").add_to(W50DC)
folium.Marker(location=[8.291212, -62.849257], popup="Homicide Rate(Per 100,000): 80.28", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Ciudad Guayana, Venezuela").add_to(W50DC)
folium.Marker(location=[8.291212, -62.849257], popup="Homicide Rate(Per 100,000): 71.38", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Belém, Pará").add_to(W50DC)
folium.Marker(location=[-14.8641344, -40.9130183], popup="Homicide Rate(Per 100,000): 70.26",icon=folium.Icon(color='lightgray', icon='home', prefix='fa'), tooltip="Vitoria da Conquista").add_to(W50DC)
folium.Marker(location=[24.8050567, -107.4933552], popup="Homicide Rate(Per 100,000): 70.10", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Culiacan").add_to(W50DC)
folium.Marker(location=[38.6532851, -90.3835492], popup="Homicide Rate(Per 100,000): 65.83", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="St. Louis").add_to(W50DC)
folium.Marker(location=[-33.9131286, 18.0955756], popup="Homicide Rate(Per 100,000): 62.25", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Cape Town").add_to(W50DC)
folium.Marker(location=[18.018087, -76.8706976], popup="Homicide Rate(Per 100,000): 59.71", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Kingston").add_to(W50DC)
folium.Marker(location=[13.6916351, -89.2852931], popup="Homicide Rate(Per 100,000): 59.06", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="San Salvador").add_to(W50DC)
folium.Marker(location=[-11.0056387, -37.2432457], popup="Homicide Rate(Per 100,000): 58.88", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Aracaju").add_to(W50DC)
folium.Marker(location=[-12.2449081, -38.9483658], popup="Homicide Rate(Per 100,000): 58.81", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Feira de Santana").add_to(W50DC)
folium.Marker(location=[31.4685722, -106.8722774], popup="Homicide Rate(Per 100,000): 56.16", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Ciudad Juárez").add_to(W50DC)
folium.Marker(location=[39.2848882, -76.7605731], popup="Homicide Rate(Per 100,000): 55.48",icon=folium.Icon(color='lightgray', icon='home', prefix='fa'), tooltip="Baltimore").add_to(W50DC)
folium.Marker(location=[-8.0418006,-35.0787252], popup="Homicide Rate(Per 100,000): 54.96", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Recife").add_to(W50DC)
folium.Marker(location=[9.7498167,-63.3309065], popup="Homicide Rate(Per 100,000): 54.43", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Maturin").add_to(W50DC)
folium.Marker(location=[14.6263757,-90.5626018], popup="Homicide Rate(Per 100,000): 53.49",icon=folium.Icon(color='lightgray', icon='home', prefix='fa'), tooltip="Guatemala City").add_to(W50DC)
folium.Marker(location=[-12.9012521,-38.5598969], popup="Homicide Rate(Per 100,000): 51.58", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Salvador").add_to(W50DC)
folium.Marker(location=[15.5198897,-88.0555308], popup="Homicide Rate(Per 100,000): 51.18", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="San Pedro Sula").add_to(W50DC)
folium.Marker(location=[10.1727434,-68.0642653], popup="Homicide Rate(Per 100,000): 49.74", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Valencia").add_to(W50DC)
folium.Marker(location=[3.395397,-76.6657539], popup="Homicide Rate(Per 100,000): 49.59", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Cali, Valle del Cauca, Colombia").add_to(W50DC)
folium.Marker(location=[28.6711604,-106.2047067], popup="Homicide Rate(Per 100,000): 49.48", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Chihuahua").add_to(W50DC)
folium.Marker(location=[-7.1464332,-34.9516388], popup="Homicide Rate(Per 100,000): 49.17", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Joao Pessoa").add_to(W50DC)
folium.Marker(location=[21.1322351,-101.6916145], popup="Homicide Rate(Per 100,000): 48.96", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Obregon").add_to(W50DC)
folium.Marker(location=[20.403538,-100.0435132], popup="Homicide Rate(Per 100,000): 48.96", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="San Juan").add_to(W50DC)
folium.Marker(location=[-3.0443101,-60.1071938], popup="Homicide Rate(Per 100,000): 48.07", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Manaus").add_to(W50DC)
folium.Marker(location=[14.1056636,-87.2036231], popup="Homicide Rate(Per 100,000): 48.00", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Distrito Central").add_to(W50DC)
folium.Marker(location=[21.5011309,-104.9469458], popup="Homicide Rate(Per 100,000): 47.09", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Tepic").add_to(W50DC)
folium.Marker(location=[3.5320986,-76.3304453], popup="Homicide Rate(Per 100,000): 46.65", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Palmira").add_to(W50DC)
folium.Marker(location=[26.0314841,-98.436292], popup="Homicide Rate(Per 100,000): 41.95", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Reynosa").add_to(W50DC)
folium.Marker(location=[-30.1084987,-51.3172295], popup="Homicide Rate(Per 100,000): 40.96", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Porto Alegre").add_to(W50DC)
folium.Marker(location=[0.0310596,-51.0651359], popup="Homicide Rate(Per 100,000): 40.24", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Macapa").add_to(W50DC)
folium.Marker(location=[30.0332941,-90.1627658], popup="Homicide Rate(Per 100,000): 40.10", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="New Orleans").add_to(W50DC)
folium.Marker(location=[42.3528795,-83.2392917], popup="Homicide Rate(Per 100,000): 39.69", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Detroit").add_to(W50DC)
folium.Marker(location=[23.2468861,-106.4923183], popup="Homicide Rate(Per 100,000): 39.32", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Mazatlan").add_to(W50DC)
folium.Marker(location=[-29.848212,30.9224217], popup="Homicide Rate(Per 100,000): 38.12", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Durban").add_to(W50DC)
folium.Marker(location=[-21.7769086,-41.454651], popup="Homicide Rate(Per 100,000): 37.53", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Campos dos Goytacazes").add_to(W50DC)
folium.Marker(location=[-33.8003035,24.9711044], popup="Homicide Rate(Per 100,000): 37.53", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Nelson Mandela Bay").add_to(W50DC)
folium.Marker(location=[-7.242662,-35.9716057], popup="Homicide Rate(Per 100,000): 37.29", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Campina Grande").add_to(W50DC)
folium.Marker(location=[-5.0933825,-42.881168], popup="Homicide Rate(Per 100,000): 37.05", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Teresina, State of Piauí, Brazil").add_to(W50DC)
folium.Marker(location=[-20.2820166,-40.3557448], popup="Homicide Rate(Per 100,000): 36.07", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Vitoria").add_to(W50DC)
folium.Marker(location=[7.9089243,-72.5744619], popup="Homicide Rate(Per 100,000): 34.78", icon=folium.Icon(color='lightgray', icon='home', prefix='fa'),tooltip="Cucuta").add_to(W50DC)

# Gun-Possessing Allowed Countries
folium.Marker(location=[41.8333925,-88.0121484], popup="No Permit Required To Get Firearms", icon=folium.Icon(color='red',icon='info-sign'), tooltip="USA").add_to(GunGroup)
folium.Marker(location=[15.262779,9.6834804], popup="No Permit Required To Get Firearms", icon=folium.Icon(color='red',icon='info-sign'), tooltip="Chad").add_to(GunGroup)
folium.Marker(location=[47.3444607,4.3648709], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Austria").add_to(GunGroup)
folium.Marker(location=[-0.6856399,5.8225698], popup="Possessing Guss Is Legal",  icon=folium.Icon(color='red',icon='info-sign'),tooltip="Republic of Congo").add_to(GunGroup)
folium.Marker(location=[15.179543,-90.7094955], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Honduras").add_to(GunGroup)
folium.Marker(location=[4.9477384,131.7352345], popup="No Permit Required To Get Firearms",  icon=folium.Icon(color='red',icon='info-sign'),tooltip="Micronesia").add_to(GunGroup)
folium.Marker(location=[4.9477384,131.7352345], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Namibia").add_to(GunGroup)
folium.Marker(location=[-22.7109105,9.3260071], popup="No Permit Required To Get Firearms",  icon=folium.Icon(color='red',icon='info-sign'),tooltip="Micronesia").add_to(GunGroup)
folium.Marker(location=[8.9230342,-0.3807499], popup="No Permit Required To Get Firearms",  icon=folium.Icon(color='red',icon='info-sign'), tooltip="Nigeria").add_to(GunGroup)
folium.Marker(location=[29.0909861,51.131844], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Pakistan").add_to(GunGroup)
folium.Marker(location=[11.1119969,104.1729581], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Philippines").add_to(GunGroup)
folium.Marker(location=[14.4361563,-19.0172273], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Senegal").add_to(GunGroup)
folium.Marker(location=[-6.2939602,25.929914], popup="No Permit Required To Get Firearms",  icon=folium.Icon(color='red',icon='info-sign'),tooltip="Tanzania").add_to(GunGroup)
folium.Marker(location=[15.2157512,39.1427183], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Yemen").add_to(GunGroup)
folium.Marker(location=[-12.9821971,18.7998868], popup="No Permit Required To Get Firearms",   icon=folium.Icon(color='red',icon='info-sign'),tooltip="Zambia").add_to(GunGroup)

# USCrimeGroup
folium.Marker(location=[38.6530169,-90.3835487], popup="2017 Violent crime rate: 2,082 per 100,000 • 2017 Homicides: 205 • Poverty rate: 26.7% • Unemployment rate: 4.4%", icon=folium.Icon(color='green'), tooltip="St. Louis, Missouri").add_to(USCrimeGroup)
folium.Marker(location=[42.3523699,-83.3793979], popup="2017 Violent crime rate: 2,057 per 100,000 • 2017 Homicides: 267 • Poverty rate: 39.4% • Unemployment rate: 9.3%", icon=folium.Icon(color='green'),tooltip="Detroit, Michigan").add_to(USCrimeGroup)
folium.Marker(location=[39.2846225,-76.7605726], popup="2017 Violent crime rate: 2,027 per 100,000 • 2017 Homicides: 342 • Poverty rate: 23.1% • Unemployment rate: 6.1%", icon=folium.Icon(color='green'),tooltip="Baltimore, Maryland").add_to(USCrimeGroup)
folium.Marker(location=[35.1278958,-90.5312753], popup="2017 Violent crime rate: 2,003 per 100,000 • 2017 Homicides: 181 • Poverty rate: 27.6% • Unemployment rate: 4.8%", icon=folium.Icon(color='green'),tooltip="Memphis, Tennessee").add_to(USCrimeGroup)
folium.Marker(location=[39.0915837,-94.8559147], popup="2017 Violent crime rate: 1,724 per 100,000 • 2017 Homicides: 150 • Poverty rate: 18.3% • Unemployment rate: 4.3%", icon=folium.Icon(color='green'),tooltip=" Kansas City, Missouri").add_to(USCrimeGroup)
folium.Marker(location=[34.7236841,-92.6181255], popup="2017 Violent crime rate: 1,634 per 100,000 • 2017 Homicides: 55 • Poverty rate: 18.5% • Unemployment rate: 3.3%", icon=folium.Icon(color='green'),tooltip="Little Rock, Arkansas").add_to(USCrimeGroup)
folium.Marker(location=[43.057806,-88.107516], popup="2017 Violent crime rate: 1,597 per 100,000 • 2017 Homicides: 118 • Poverty rate: 28.4% • Unemployment rate: 4.6%", icon=folium.Icon(color='green'),tooltip=" Milwaukee, Wisconsin").add_to(USCrimeGroup)
folium.Marker(location=[42.2526365,-89.3482524], popup="2017 Violent crime rate: 1,588 per 100,000 • 2017 Homicides: 18 • Poverty rate: 22.7% • Unemployment rate: 7.5%", icon=folium.Icon(color='green'),tooltip="Rockford, Illinois").add_to(USCrimeGroup)
folium.Marker(location=[41.497192,-81.9860534], popup="2017 Violent crime rate: 1,557 per 100,000 • 2017 Homicides: 107 • Poverty rate: 36.0% • Unemployment rate: 7.4%", icon=folium.Icon(color='green'),tooltip=" Cleveland, Ohio").add_to(USCrimeGroup)
folium.Marker(location=[37.9726911,-121.5820735], popup="2017 Violent crime rate: 1,415 per 100,000 • 2017 Homicides: 55 • Poverty rate: 23.7% • Unemployment rate: 8.0%", icon=folium.Icon(color='green'),tooltip="Stockton, California").add_to(USCrimeGroup)
folium.Marker(location=[35.0820877,-106.9566772], popup="2017 Violent crime rate: 1,369 per 100,000 • 2017 Homicides: 70 • Poverty rate: 18.9% • Unemployment rate: 5.5%", icon=folium.Icon(color='green'),tooltip="Albuquerque, New Mexico").add_to(USCrimeGroup)
folium.Marker(location=[37.1787746,-93.576521], popup="2017 Violent crime rate: 1,339 per 100,000 • 2017 Homicides: 14 • Poverty rate: 25.9% • Unemployment rate: 3.2%", icon=folium.Icon(color='green'),tooltip="Springfield, Missouri").add_to(USCrimeGroup)
folium.Marker(location=[39.7794476,-86.4129447], popup="2017 Violent crime rate: 1,334 per 100,000 • 2017 Homicides: 156 • Poverty rate: 20.9% • Unemployment rate: 3.6%", icon=folium.Icon(color='green'),tooltip="Indianapolis, Indiana").add_to(USCrimeGroup)
folium.Marker(location=[37.7583859,-122.515504], popup="2017 Violent crime rate: 1,299 per 100,000 • 2017 Homicides: 69 • Poverty rate: 20.0% • Unemployment rate: 4.2%", icon=folium.Icon(color='green'),tooltip="Oakland, California").add_to(USCrimeGroup)
folium.Marker(location=[34.1485581,-117.574843], popup="2017 Violent crime rate: 1,291 per 100,000 • 2017 Homicides: 34 • Poverty rate: 32.3% • Unemployment rate: 6.3%", icon=folium.Icon(color='green'),tooltip="San Bernardino, California").add_to(USCrimeGroup)
folium.Marker(location=[61.0902967,-151.6825336], popup="2017 Violent crime rate: 1,203 per 100,000 • 2017 Homicides: 27 • Poverty rate: 8.1% • Unemployment rate: 6.0%", icon=folium.Icon(color='green'),tooltip="Anchorage, Alaska").add_to(USCrimeGroup)
folium.Marker(location=[36.1157336,-87.3367153], popup="2017 Violent crime rate: 1,138 per 100,000 • 2017 Homicides: 110 • Poverty rate: 18.0% • Unemployment rate: N/A", icon=folium.Icon(color='green'),tooltip="Nashville Metropolitan Area, Tennessee").add_to(USCrimeGroup)
folium.Marker(location=[42.7083401,-84.8396201], popup="2017 Violent crime rate: 1,136 per 100,000 • 2017 Homicides: 14 • Poverty rate: 29.5% • Unemployment rate: 6.3%", icon=folium.Icon(color='green'),tooltip="Lansing, Michigan").add_to(USCrimeGroup)
folium.Marker(location=[30.0318085,-90.4430649], popup="2017 Violent crime rate: 1,121 per 100,000 • 2017 Homicides: 157 • Poverty rate: 26.2% • Unemployment rate: 5.1%", icon=folium.Icon(color='green'),tooltip="New Orleans, Louisiana").add_to(USCrimeGroup)
folium.Marker(location=[44.9706114,-93.4015641], popup="2017 Violent crime rate: 1,101 per 100,000 • 2017 Homicides: 42 • Poverty rate: 21.3% • Unemployment rate: 3.1%", icon=folium.Icon(color='green'),tooltip="Minneapolis, Minnesota ").add_to(USCrimeGroup)
folium.Marker(location=[41.9531494,-87.8094564], popup="2017 Violent crime rate: 1,099 per 100,000 • 2017 Homicides: 653 • Poverty rate: 21.7% • Unemployment rate: 5.5%", icon=folium.Icon(color='green'),tooltip="Chicago, Illinois").add_to(USCrimeGroup)
folium.Marker(location=[29.8159952,-95.9617934], popup="2017 Violent crime rate: 1,095 per 100,000 • 2017 Homicides: 269 • Poverty rate: 21.9% • Unemployment rate: 4.8%", icon=folium.Icon(color='green'),tooltip="Houston, Texas").add_to(USCrimeGroup)
folium.Marker(location=[41.7656662,-72.7501274], popup="2017 Violent crime rate: 1,093 per 100,000 • 2017 Homicides: 29 • Poverty rate: 31.9% • Unemployment rate: 8.1%", icon=folium.Icon(color='green'),tooltip="Hartford, Connecticut").add_to(USCrimeGroup)
folium.Marker(location=[35.0979732,-85.51888], popup="2017 Violent crime rate: 1,066 per 100,000 • 2017 Homicides: 31• Poverty rate: 21.1% • Unemployment rate: 3.9%", icon=folium.Icon(color='green'),tooltip="Chattanooga, Tennessee").add_to(USCrimeGroup)
folium.Marker(location=[30.0810662,-94.267996], popup="2017 Violent crime rate: 1,063 per 100,000 • 2017 Homicides: 16 • Poverty rate: 20.8% • Unemployment rate: 6.4%", icon=folium.Icon(color='green'),tooltip="Beaumont, Texas").add_to(USCrimeGroup)


WCH.add_to(m)
W50DC.add_to(m)
GunGroup.add_to(m)
USCrimeGroup.add_to(m)
LayerControl().add_to(m)

# plugins.MarkerCluster().add_to(m)
plugins.ScrollZoomToggler().add_to(m)

# Boat Marker
plugins.BoatMarker( location=(34, -43), heading=45, wind_heading=150, wind_speed=45, color='#8f8' ).add_to(m)
plugins.BoatMarker( location=(46, -30), heading=-20, wind_heading=46, wind_speed=25, color='#88f' ).add_to(m)

# Full Screen
plugins.Fullscreen( position='topright', title='Expand me', title_cancel='Exit me', force_separate_button=True ).add_to(m)

# Mini Map
minimap = plugins.MiniMap()
m.add_child(minimap)

# Mouse Position
MousePosition().add_to(m)

# Locate Control
plugins.LocateControl().add_to(m)

# Draw
draw = Draw()
draw.add_to(m)

# folium.LayerControl(collapsed=False).add_to(m)

m.save("index.html")