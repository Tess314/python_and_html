from django.shortcuts import render

def button(request):

    return render(request,'tess.html')

def output(request):
    
    output_data = "Hello, Tess!"
    
    return render(request,"tess.html",{"output_data":output_data})
    
