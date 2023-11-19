# Variables

AlbumMusics = int(input("Quantas musicas têm o album?: "))

SegundosTotaisDaMusica = 0

# Validation

# Process

for i in range(1, (AlbumMusics + 1)):
    SegundosDaMusica = int(input(f"Quantos segundos têm a {i}º musica?: "))
    SegundosTotaisDaMusica = SegundosTotaisDaMusica + SegundosDaMusica

# Time conversion
MinutosDoAlbum = int(SegundosTotaisDaMusica / 60)
SegundosDoAlbum = SegundosTotaisDaMusica - (60 * MinutosDoAlbum)

# Output

print(f"O album têm: {MinutosDoAlbum} Minuto(s) e {SegundosDoAlbum} Segundos")