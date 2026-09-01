from flask import Flask, render_template, request
app = Flask(__name__)

datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "tiktok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]


def limpiar_usuarios(v):
    v = v.upper().strip()
    if 'B' in v: return float(v.replace('B', '')) * 1000000000
    if 'M' in v: return float(v.replace('M', '')) * 1000000
    return 0.0

@app.route("/")
@app.route("/tabla")
def mostrar_plataformas():
    p_sel = request.args.get("pais", "todos")
    o_por = request.args.get("ordenar", "nombre")
    direc = request.args.get("direccion", "asc")
    p_unicos = sorted(list(set(d["pais"] for d in datos)))
    d_filtrados = datos.copy()
    if p_sel != "todos":
        d_filtrados = [d for d in d_filtrados if d["pais"] == p_sel]
    es_desc = (direc == "dsc")
    if o_por == "usuarios":
        d_filtrados.sort(key = lambda x: limpiar_usuarios(x["usuarios"]), reverse = es_desc)
    elif o_por == "fundado":
        d_filtrados.sort(key = lambda x: int(x["fundado"]), reverse = es_desc)
    else:
        d_filtrados.sort(key = lambda x: x["nombre"].lower(), reverse = es_desc)

    return render_template("tabla.html", plataformas = d_filtrados, paises = p_unicos, pais_sel = p_sel, ordenar_sel = o_por, direccion_sel = direc)


if __name__ == "__main__":
   app.run(debug=True)