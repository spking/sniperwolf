"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Verkefni_SSSkyttuúlfurB_ import app

#database
vorur = [   [0,"AWP GUNGIR", "AWPGUNGNIR.png", 6000]
            [1, "AK-47 ASIIMOV", "akasiimov.png", 40]
            [2, "DESERT EAGLE CORINTH", "deaglecorinth.png", 300]
            [4, "FIVE SEVEN BANANA", "57banana.png", 50]
            [5, "FLIP KNIFE GAMMA DOPPLER", "flipgammadoppler.png", 1600]
            [6, "KARAMBIT FADE", "karambitfade.png", 2000]
            [7, "M9 BAYONET DRAGON LORE", "m9dlore.png", 3000]
            [8, "HUNTSMAN KNIFE MARBLE FADE", "hmmarble.png", 3000]
            [9, "M4A4 EMPEROR", "m4a4emperor.png", 40]
            [10, "M4A1-S HYPER BEAST", "m4a1shyperbeast.png", 25]
            [11, "SG AERIAL", "shae.png", 15]
            [12, "USP-S BLUEPRINT","uspsblu.png", 4]
         ]

@app.route('/')
@app.route('/home')
def index():
    return render_template(
        'index.html',
        title='Verslun',
        year=datetime.now().year,
    )

@app.route('/contact')
def samantekt():
    return render_template(
        'samantekt.html',
        title='Samantekt',
        year=datetime.now().year,
        message='Samantekt'
    )

@app.route('/about/<id>')
def afgreidsla():
    vorur = []
    vorur.append(id)
    session['karfa'] = vorur
    return render_template(
        'form.html',
        title='Afgreiðsla',
        year=datetime.now().year,
        message='Afgreiðsla'
    )
