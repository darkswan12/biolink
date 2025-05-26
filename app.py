from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        'name': 'Darmawan Suhara',
        'bio': 'Informatics Student • Web & Mobile Developer • ML Enthusiast',
        'avatar': '/static/favicon.jpg',
        'links': [
            {'name': 'GitHub', 'url': 'https://github.com/darkswan12', 'icon': 'github', 'prefix': 'fab'},
            {'name': 'LinkedIn', 'url': 'https://www.linkedin.com/in/darmawan-suhara-a9426422b/', 'icon': 'linkedin', 'prefix': 'fab'},
            {'name': 'Instagram', 'url': 'https://instagram.com/darkswan.12', 'icon': 'instagram', 'prefix': 'fab'},
            {'name': 'Discord', 'url': 'https://discord.com/users/275947812439719936', 'icon': 'discord', 'prefix': 'fab'},
            {'name': 'Portfolio', 'url': 'https://darkswan12.pythonanywhere.com/', 'icon': 'address-card', 'prefix': 'fas'},
            {'name': 'Carousel Crop Tools', 'url': 'https://darskwan10.pythonanywhere.com/', 'icon': 'cut', 'prefix': 'fas'},
            {'name': 'Tiktok', 'url': 'https://www.tiktok.com/@darkswan.12', 'icon': 'tiktok', 'prefix': 'fab'},
        ]

    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
