import pandas as pd
import folium as F
from geopy.distance import geodesic

longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472
map = F.Map(location=(55.56, 9.69), zoom_start=8)

Location1=(56.11, 10.15)
Location2=(54.82,9.35)

F.Marker((56.11, 10.15), popup='Nye Hus').add_to(map)
F.Marker(location=(54.82,9.35), popup='Gammel Hus').add_to(map)

F.PolyLine(locations=[(56.110000, 10.150000), (54.820000,9.350000)], color='black').add_to(map)
distance = geodesic(Location1, Location2).kilometers

mid_point = [(Location1[0] + Location2[0]) / 2, (Location1[1] + Location2[1]) / 2]
F.Marker(location=mid_point,
         icon=F.DivIcon(html=f'<div style="font-size: 12pt; color: black">{distance:.2f} km</div>')).add_to(map)

map.show_in_browser()
map.save("Map.html")
input("wait for exit")