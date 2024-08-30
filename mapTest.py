import pandas as pd
import folium as F
longboi = pd.read_csv("LongBoi.csv")
#53.0765452103364, 8.820692530590472
map = F.Map(location=(53.08, 8.8), zoom_start=12)

F.Marker((53.08, 8.8), popup='Binaur').add_to(map)

F.PolyLine(locations=[(16.350000, 81.050000), (26.383333, 80.166667)], color='blue').add_to(map)
map.show_in_browser()
map.save("Map.html")
input("wait for exit")