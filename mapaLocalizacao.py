import folium

# Cria o mapa #
mapa = folium.Map(
    location=[-23.550093493433984, -46.6341472592547],
    #Location=[-29.66554784653492, -51.100264580796846],
    tiles='Stamen Terrain', # Estilo do mapa
    zoom_start=16
)

# Adiciona o marcador no mapa #
folium.Marker(
    location=[-23.550093493433984, -46.6341472592547],
    #[-29.66554784653492, -51.100264580796846],
    popup='<i>Novo Hamburgo</i>', 
    tooltip='Click aqui!'
).add_to(mapa)

# Salva html do mapa #
mapa.save(r'.\mapa.html')