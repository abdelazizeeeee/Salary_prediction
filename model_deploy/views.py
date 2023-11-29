from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import numpy as np
from django.views import View

# Create your views here.


model = joblib.load(
    "/Users/macmini/Desktop/My work/deploy_predict/model/model_deploy/Salaries_prediction.ipynb"
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
        prediction={
            "prediction":prediction[0]
        }
        # return HttpResponse("jawek behi")
        return render(request,"model_deploy/result.html",prediction)
    
