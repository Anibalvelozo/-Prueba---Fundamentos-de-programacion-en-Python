def generate_html(birds_info):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aves de Chile</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5 mb-4 text-center">Aves de Chile</h1> 
            <div class="row" id="birds-list">
    """

    for bird in birds_info:
        name_es = bird['name']['spanish']
        name_en = bird['name']['english']
        name_la = bird['name']['latin']
        image_url = bird['images']['main']
        html_content += f"""
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{image_url}" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title"> Nombre en Español: {name_es} / Nombre en Ingles{name_en} / Nombre en Latin{name_la}</h5>
                        </div>
                    </div>
                </div>
        """

    html_content += """
            </div>
        </div>
        <footer class="text-center mt-5">
            <p>© 2024 Aves de Chile. Todos los derechos reservados.</p>
        </footer>
    </body>
    </html>
    """

    with open('aveschile.html', 'w') as f:
        f.write(html_content)

    print("Sitio web generado correctamente como 'aveschile.html'.")

