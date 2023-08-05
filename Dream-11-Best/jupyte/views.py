import subprocess
from django.shortcuts import render

def base(request):
    return render(request, 'jupyte/base.html')

def home(request):
    return render(request, 'jupyte/home.html')
def index(request):
    return render(request, 'jupyte/index.html')
def contact(request):
    return render(request, 'jupyte/contact.html')
import os
from django.shortcuts import render, redirect
global ml
ml=[]
def process_players(request):
    
    global ml
    if request.method == 'POST':
        for i in range(1, 23):
            player_name = request.POST.get(f'player{i}', '')  # Get the checkbox value
            if player_name:
                ml.append(player_name)
            
            # print("name formpost method",player_name)
            # ml.append(player_name)
        print(ml)
        if ml:
            file_path = './player_names.txt'
            with open(file_path, 'w') as f:
                f.write("")
            for i in ml:
                with open(file_path, 'a') as f:
                    f.write(i)
                    f.write("\n")
            
        try:
            subprocess.run([ 'python','./your_file.py'], check=True)
        except subprocess.CalledProcessError as e:
            print("Error executing Jupyter file:")
            print(e.stderr)
    #         # print("Data written to player_names.txt:", player_names)
    #         return redirect('jupyte:result')
    #     else:
    #         return render(request, 'jupyte/index.html')
    # else:
        player_names=[]
        file_path='./player_names.txt'
        with open(file_path, 'r') as f:
                player_names = f.read().splitlines()
        print(player_names)
        context = {
            'player_names': player_names,
        }
        return render(request, 'jupyte/result.html',context)
