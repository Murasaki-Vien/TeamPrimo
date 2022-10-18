from flask import Blueprint, render_template, url_for, redirect, request
from flask_login import login_required, current_user
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
        
        elif place == "Kawasan Falls, Badian":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "LexMin Resort, Argao":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))

    #for Restautrants
        elif place == "Anzani New Mediterranean":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "Amihan Restaurant Malapascua":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "Smooth Cafe, Moalboal":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "The Pig & Palm":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
        
        elif place == "Thai-Phoon, Bantayan Island":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))
       
        elif place == "Entoy's Bakasihan, Cordova":
            cebu_places=CebuPlaces.query.filter_by(name=place).first()
            return redirect(url_for("dashboard.TspotsPage", MyAcc=MyAcc, spot=cebu_places.name))



    return render_template("dashboard.html", email=MyAcc)

@dashboard.route("/dashboard/<MyAcc>/<spot>")
@login_required
def TspotsPage(MyAcc, spot):
    picture1 = ""
    picture2 = ""
    picture3 = ""
    picture4 = ""
    picture5 = ""
    picture6 = ""
    content = ""
    TspotsName = ""

    if spot == "Moalboal":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/tspic/Moalboal1.jpg"
        picture2 = "/static/tspic/Moalboal2.jpg"
        picture3 = "/static/tspic/Moalboal3.jpg"
        picture4 = "/static/tspic/Moalboal4.jpg"
        picture5 = "/static/tspic/Moalboal5.jpg"
        picture6 = "/static/tspic/Moalboal6.jpg"
    
    elif spot == "Bantayan Island":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/tspic/BantayanIsland1.jpg"
        picture2 = "/static/tspic/BantayanIsland2.jpg"
        picture3 = "/static/tspic/BantayanIsland3.jpg"
        picture4 = "/static/tspic/BantayanIsland4.jpg"
        picture5 = "/static/tspic/BantayanIsland5.jpg"
        picture6 = "/static/tspic/BantayanIsland6.jpg"
    
    elif spot == "Santiago White Beach":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        TspotsName = cebu_places.name
        picture1 = "/static/tspic/SantiagoWhiteBeach1.jpg"
        picture2 = "/static/tspic/SantiagoWhiteBeach2.jpg"
        picture3 = "/static/tspic/SantiagoWhiteBeach3.jpg"
        picture4 = "/static/tspic/SantiagoWhiteBeach4.jpg"
        picture5 = "/static/tspic/SantiagoWhiteBeach5.jpg"
        picture6 = "/static/tspic/SantiagoWhiteBeach6.jpg"

    elif spot == "Blue Water Marigo Beach Resort":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        TspotsName = cebu_places.name
        picture1 = "/static/tspic/MaribagoBeachResost1.jpg"
        picture2 = "/static/tspic/MaribagoBeachResost2.jpg"
        picture3 = "/static/tspic/MaribagoBeachResost3.jpg"
        picture4 = "/static/tspic/MaribagoBeachResost4.jpg"
        picture5 = "/static/tspic/MaribagoBeachResost5.jpg"
        picture6 = "/static/tspic/MaribagoBeachResost6.jpg"

    elif spot == "Kawasan Falls, Badian":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        TspotsName = cebu_places.name
        picture1 = "/static/tspic/kawasanfalls1.jpg"
        picture2 = "/static/tspic/kawasanfalls2.jpg"
        picture3 = "/static/tspic/kawasanfalls3.jpg"
        picture4 = "/static/tspic/kawasanfalls4.jpg"
        picture5 = "/static/tspic/kawasanfalls5.jpg"
        picture6 = "/static/tspic/kawasanfalls6.jpg"

    elif spot == "LexMin Resort, Argao":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        content = cebu_places.information
        TspotsName = cebu_places.name
        picture1 = "/static/tspic/Lexmin1.jpg"
        picture2 = "/static/tspic/Lexmin2.jpg"
        picture3 = "/static/tspic/Lexmin3.jpg"
        picture4 = "/static/tspic/lexmin4.jpg"  
        picture5 = "/static/tspic/lexmin5.jpg"  
        picture6 = "/static/tspic/lexmin6.jpg"  

    #For Restaurants

    elif spot == "Anzani New Mediterranean":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/Anzani1.jpg"
        picture2 = "/static/rstaurnts/Anzani2.jpg"
        picture3 = "/static/rstaurnts/Anzani3.jpg"
        picture4 = "/static/rstaurnts/AnzaniMenu1.jpg"
        picture5 = "/static/rstaurnts/AnzaniMenu2.jpg"
        picture6 = "/static/rstaurnts/AnzaniMenu3.jpg"
    
    elif spot == "Amihan Restaurant Malapascua":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/Amihan1.jpg"
        picture2 = "/static/rstaurnts/Amihan2.jpg"
        picture3 = "/static/rstaurnts/Amihan3.jpg"
        picture4 = "/static/rstaurnts/AmihanMenu1.jpg"
        picture5 = "/static/rstaurnts/AmihanMenu2.jpg"
        picture6 = "/static/rstaurnts/AmihanMenu3.jpg"
    
    elif spot == "Smooth Cafe, Moalboal":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/SmoothCafe1.jpg"
        picture2 = "/static/rstaurnts/SmoothCafe2.jpg"
        picture3 = "/static/rstaurnts/SmoothCafe3.jpg"
        picture4 = "/static/rstaurnts/SmoothCafeMenu1.jpg"
        picture5 = "/static/rstaurnts/SmoothCafeMenu2.jpg"
        picture6 = "/static/rstaurnts/SmoothCafeMenu3.jpg"
    
    elif spot == "The Pig & Palm":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/PigandPalm1.jpg"
        picture2 = "/static/rstaurnts/PigandPalm2.jpg"
        picture3 = "/static/rstaurnts/PigandPalm3.jpg"
        picture4 = "/static/rstaurnts/PigandPalmMenu1.jpg"
        picture5 = "/static/rstaurnts/PigandPalmMenu2.jpg"
        picture6 = "/static/rstaurnts/PigandPalmMenu3.jpg"
    
    elif spot == "Thai-Phoon, Bantayan Island":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/Thai1.jpg"
        picture2 = "/static/rstaurnts/Thai2.jpg"
        picture3 = "/static/rstaurnts/Thai3.jpg"
        picture4 = "/static/rstaurnts/ThaiMenu1.jpg"
        picture5 = "/static/rstaurnts/ThaiMenu2.jpg"
        picture6 = "/static/rstaurnts/ThaiMenu3.jpg"

    elif spot == "Entoy's Bakasihan, Cordova":
        cebu_places=CebuPlaces.query.filter_by(name=spot).first()
        TspotsName = cebu_places.name
        content = cebu_places.information
        picture1 = "/static/rstaurnts/entoys-bakasihan-cordova1.jpg"
        picture2 = "/static/rstaurnts/entoys-bakasihan-cordova2.jpg"
        picture3 = "/static/rstaurnts/entoy-s-bakasihan-cordova3.jpg"
        picture4 = "/static/rstaurnts/entoys-bakasihan-cordova4.jpg"
        picture5 = "/static/rstaurnts/entoys-bakasihan-cordova5.jpg"
        picture6 = "/static/rstaurnts/entoys-bakasihan-cordova6.jpg"
        
    return render_template("mc-info.html", email=MyAcc, places=spot, cont=content, picture1=picture1, picture2=picture2, picture3=picture3, picture4=picture4, picture5=picture5, picture6=picture6, TsName=TspotsName)

@dashboard.route("dashboard/<MyAcc>/car-rentals")
@login_required
def carRentalPage(MyAcc):
    
    return render_template("rentalpage.html", email=MyAcc)
