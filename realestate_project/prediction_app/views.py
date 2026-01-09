from django.shortcuts import render
import pickle
import pandas as pd
from .models import Property

model = pickle.load(open("prediction_app/house_price_model.pkl", "rb"))

def predict_price(request):
    if request.method == "POST":

        # Numeric fields
        area = float(request.POST["area"])
        bedrooms = int(request.POST["bedrooms"])
        bathrooms = int(request.POST["bathrooms"])
        stories = int(request.POST["stories"])
        parking = int(request.POST["parking"])

        # Categorical fields
        mainroad = request.POST["mainroad"]
        guestroom = request.POST["guestroom"]
        basement = request.POST["basement"]
        hotwaterheating = request.POST["hotwaterheating"]
        airconditioning = request.POST["airconditioning"]
        prefarea = request.POST["prefarea"]
        furnishingstatus = request.POST["furnishingstatus"]

        # Create dictionary exactly like the original training columns
        input_dict = {
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "stories": [stories],
            "parking": [parking],
            "mainroad": [mainroad],
            "guestroom": [guestroom],
            "basement": [basement],
            "hotwaterheating": [hotwaterheating],
            "airconditioning": [airconditioning],
            "prefarea": [prefarea],
            "furnishingstatus": [furnishingstatus]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame(input_dict)

        # Predict
        pred = model.predict(input_df)[0]

        # Save to DB
        Property.objects.create(
            area=area,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            stories=stories,
            parking=parking,
            mainroad=mainroad,
            guestroom=guestroom,
            basement=basement,
            hotwaterheating=hotwaterheating,
            airconditioning=airconditioning,
            prefarea=prefarea,
            furnishingstatus=furnishingstatus,
            prediction=pred
        )

        return render(request, "result.html", {"pred": round(pred, 2)})

    return render(request, "input_form.html")
