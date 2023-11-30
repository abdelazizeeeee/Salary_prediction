from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import numpy as np
from django.views import View
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import Features
from .serializers import FeaturesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

# Create your views here.


model = joblib.load(
    "/Users/macmini/Desktop/My work/salary_pred/Salaries_prediction.ipynb"
)
print(model)

class index(View):
    def get(self, request):
        return render(request, "model_deploy/index.html")

    def post(self, request):
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        exp = request.POST.get("experince")
        educ_lvl = request.POST.get("educ_lvl")
        job = request.POST.get("job")
        print(type(age))
        print("jjj", gender)
        prediction = model.predict(
            pd.DataFrame(
                {
                    "Age": [age],
                    "Years of Experience": [exp],
                    "Gender_encoded": [gender],
                    "Education Level_encoded": [educ_lvl],
                    "Job Title_encoded": [job],
                }
            )
        )
        print(prediction)
        prediction = {"prediction": prediction[0]}
        # return HttpResponse("jawek behi")
        return render(request, "model_deploy/result.html", prediction)

#end point to get the salary prediction 
class CreateFeatures(APIView):
    def post(self, request):
        serializer = FeaturesSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            age = serializer.data["age"]
            gender = serializer.data["gender"]
            exp = serializer.data["exp"]
            educ_lvl = serializer.data["educ_lvl"]
            job = serializer.data["job"]
            if gender == "men":
                gender = 1
            else:
                gender = 0
            if educ_lvl == "Bachelor":
                educ_lvl = 0
            elif educ_lvl == "High School":
                educ_lvl = 1
            elif educ_lvl == "Master's":
                educ_lvl = 2
            elif educ_lvl == "Other":
                educ_lvl = 3
            elif educ_lvl == "PhD":
                educ_lvl = 4

            if job == "IT":
                job = 1
            elif job == "Business":
                job = 0
            elif job == "Manager":
                job = 2
            elif job == "Marketing":
                job = 3
            elif job == "Other":
                job = 4
            prediction = model.predict(
                pd.DataFrame(
                    {
                        "Age": [age],
                        "Years of Experience": [exp],
                        "Gender_encoded": [gender],
                        "Education Level_encoded": [educ_lvl],
                        "Job Title_encoded": [job],
                    }
                )
            )
            return Response(prediction, status=status.HTTP_201_CREATED)
