from django.shortcuts import render
import pandas as pd
import numpy as np
import pickle

# Main page
def main_page(request):
    return render(request, "index.html")


# Prediction page
def prediction_page(request):
    if request.method == "POST":
        # Getting features input from HTML form
        company_name = request.POST["companyName"]
        company_age = int(request.POST["companyAge"])
        country = request.POST["country"]
        category = request.POST["category"]
        total_funding = float(request.POST["totalFunding"])
        funding_rounds = float(request.POST["fundingRounds"])
        milestones = int(request.POST["milestones"])
        relationships = int(request.POST["relationships"])
        investment_rounds = int(request.POST["investmentRounds"])
        ROI = float(request.POST["ROI"])
        features = [category, country, investment_rounds, funding_rounds, total_funding, milestones, relationships, ROI,
                    company_age]

        # Creating dataframe of form input
        data_headers = ["category_code", "country_code", "investment_rounds", "funding_rounds", "funding_total_usd",
                        "milestones", "relationships", "ROI", "active_days"]
        data = pd.DataFrame([np.asarray(features)], columns=data_headers)

        # Loading ML model
        with open("RandomForestClassifier-Model.pkl", "rb") as in_file:
            model = pickle.load(in_file)

        # Predicting status of company
        status = model.predict(data)
        output = "Status of your company " + "\"" + company_name + "\"" + " is "
        if status == 1:
            output += "\"operating\"."
        else:
            output += "\"not operating\"."
        return render(request, "prediction.html", {"output": output})



    return render(request, "prediction.html", {"output": "Something went wrong!"})