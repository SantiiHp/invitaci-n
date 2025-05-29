from flask import Flask, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Invitación Especial 🎬💖</title>
    <style>
        body {
            background: #fce4ec;
            font-family: 'Segoe UI', sans-serif;
            text-align: center;
            padding: 50px;
            color: #880e4f;
        }

        .card {
            background: white;
            padding: 40px;
            border-radius: 20px;
            max-width: 600px;
            margin: auto;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        h1 {
            font-size: 2.5em;
        }

        p {
            font-size: 1.2em;
        }

        .emoji {
            font-size: 2em;
        }

        .button {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 24px;
            background: #d81b60;
            color: white;
            border-radius: 10px;
            text-decoration: none;
            font-weight: bold;
            cursor: pointer;
        }

        .button:hover {
            background: #ad1457;
        }

        #mensaje {
            margin-top: 30px;
            font-size: 1.3em;
            color: #ad1457;
            display: none;
        }
    </style>
    <script>
        function mostrarMensaje() {
            document.getElementById('mensaje').style.display = 'block';
        }
    </script>
</head>
<body>
    <div class="card">
        <div class="emoji">🍿🎥💕</div>
        <h1>¿Te gustaría ver películas conmigo?</h1>
        <p>
            Tengo una selección especial de pelis, mantas suaves<br>
            y palomitas listas para compartir.<br><br>
            ¿Te animas a una noche de cine en casa?
        </p>
        <div class="button" onclick="mostrarMensaje()">¡Claro que sí! 💞</div>
        <div id="mensaje">Te espero en mi casa para arruncharnos a ver pelis juntos 💕🍿.</div>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

