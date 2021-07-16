import folium
# Primeiro criamos o objeto m para o mapa
mapa1 = folium.Map(location=[-15.793889, -47.882778], zoom_start=11)
# Depois adicionamos o marcador.
folium.Marker(location=[-15.7589665, -47.879422],
              popup='Esplanada dos Ministerios',
              icon=folium.Icon(color='red', icon='info-sign')
).add_to(mapa1)
mapa1

# Salva html do mapa #
mapa1.save(r'.\mapa1.html')



