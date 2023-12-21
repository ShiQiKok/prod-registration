# example/views.py

from django.shortcuts import render
import pandas as pd


def index(request):

    excel_file_path = "./Registration Data.xlsx"
    df = pd.read_excel(excel_file_path)
    names = df.iloc[:, 4].to_list()
    
    context = {
        'participants': names,
    }

    if request.method == "POST":
        selected_name = request.POST.get('participants_dropdown')
        
        reg_code = names.index(selected_name) + 1
    
        context.update({"code": reg_code})
        context.update({"selected_name": selected_name})
    

    return render(request, "index.html", context)