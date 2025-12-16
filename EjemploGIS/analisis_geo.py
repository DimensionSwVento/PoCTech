
from arcgis.gis import GIS
import matplotlib.pyplot as plt

# Conexión en modo anónimo
gis = GIS("https://www.arcgis.com", anonymous=True)

print("Conectado como:", "Anónimo")

# Buscar contenido público (ejemplo: mapas relacionados con "population")
resultados = gis.content.search("population", max_items=5)

print("\nResultados públicos encontrados:")
for item in resultados:
    print(f"- {item.title} ({item.type})")

# Buscar capa de incendios
item = gis.content.search("USA Current Wildfires", "Feature Layer", max_items=1)[0]
layer = item.layers[0]

# Consultar primeros 50 incendios
features = layer.query(where="1=1", out_fields="*", result_record_count=50)

x, y = [], []

for f in features.features:
    geom = f.geometry
    if geom is None:
        continue
    # Si es un punto
    if "x" in geom and "y" in geom:
        x.append(geom["x"])
        y.append(geom["y"])
    # Si es polígono, calculamos un centroide aproximado
    elif "rings" in geom:
        coords = geom["rings"][0]  # primer anillo
        xs = [pt[0] for pt in coords]
        ys = [pt[1] for pt in coords]
        x.append(sum(xs)/len(xs))
        y.append(sum(ys)/len(ys))

plt.figure(figsize=(8,6))
plt.scatter(x, y, c="red", marker="^")
plt.title("Wildfires (ejemplo)")
plt.xlabel("Longitud")
plt.ylabel("Latitud")
plt.show()