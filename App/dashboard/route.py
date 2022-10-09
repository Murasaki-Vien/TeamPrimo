from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
from App import db
from App.models import CebuPlaces

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard/<MyAcc>", methods=['GET', 'POST'])
@login_required
def dashboardPage(MyAcc):
    if request.method == "POST":
        place = request.form.get("place")

        if place == "Moalboal":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))

        elif place == "Bantayan Island":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "Santiago White Beach":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "Blue Water Marigo Beach Resort":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "KAWASAN FALLS - BADIAN, CEBU":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))

    #for Restautrants
        elif place == "":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))



    return render_template("dashboard.html", email=MyAcc)

@dashboard.route("/dashboard/<MyAcc>/<spot>")
@login_required
def TspotsPage(MyAcc, spot):
    picture1 = ""
    picture2 = ""
    picture3 = ""
    content = ""

    if spot == "Moalboal":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = "/static/tspic/Moalboal1.jpg"
        picture2 = "/static/tspic/Moalboal2.jpg"
        picture3 = "/static/tspic/Moalboal3.jpg"
    
    elif spot == "Bantayan Island":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = "/static/tspic/BantayanIsland1.jpg"
        picture2 = "/static/tspic/BantayanIsland2.jpg"
        picture3 = "/static/tspic/BantayanIsland3.jpg"
    
    elif spot == "Santiago White Beach":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = "/static/tspic/SantiagoWhiteBeach1.jpg"
        picture2 = "/static/tspic/SantiagoWhiteBeach2.jpg"
        picture3 = "/static/tspic/SantiagoWhiteBeach3.jpg"

    elif spot == "Blue Water Marigo Beach Resort":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = "/static/tspic/MaribagoBeachResost1.jpg"
        picture2 = "/static/tspic/MaribagoBeachResost2.jpg"
        picture3 = "/static/tspic/MaribagoBeachResost3.jpg"

    elif spot == "KAWASAN FALLS - BADIAN, CEBU":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = "/static/tspic/kawasanfalls1.jpg"
        picture2 = "/static/tspic/kawasanfalls2.jpg"
        picture3 = "/static/tspic/kawasanfalls3.jpg" 

    #For Restaurants

    elif spot == "":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = ""
        picture2 = ""
        picture3 = ""
    
    elif spot == "":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = ""
        picture2 = ""
        picture3 = ""
    
    elif spot == "":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = ""
        picture2 = ""
        picture3 = ""
    
    elif spot == "":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = ""
        picture2 = ""
        picture3 = ""
    
    elif spot == "":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        picture1 = ""
        picture2 = ""
        picture3 = ""
        
    return render_template("mc-info.html", email=MyAcc, places=spot, cont=content, picture1=picture1, picture2=picture2, picture3=picture3)