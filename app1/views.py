from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generatehtml(request):
    if request.method=='POST':
        scrapsrc = request.POST['scrapsrc'] 
        
        import requests
        from bs4 import BeautifulSoup

        # Making a GET request
        page = requests.get(scrapsrc)
 
        soup = BeautifulSoup(page.text, 'html.parser')
        
        #nicely formatted Unicode string
        result = soup.prettify()
        
        # fname1='html1.html'
        # fname2='text.txt'
        # with open(fname1, "w", encoding="utf-8") as f:
        #     f.write(page.text)
        # with open(fname2, "w", encoding="utf-8") as f:
        #     f.write(result)
        ################################################################################################
        # Creating an HTML file
        Func = open("static/html.html","w", encoding="utf-8")
        
        # Adding input data to the HTML file
        Func.write(result)
              
        # Saving the data into the HTML file
        Func.close()
         ################################################################################################
        # Creating an text file
        Func = open("static/text.txt","w", encoding="utf-8")
        
        # Adding input data to the HTML file
        Func.write(result)
              
        # Saving the data into the HTML file
        Func.close()
        
        # check status code for response received
        # success code - 200
        # print(page)
 
        # print content of request
        # print(page.content)
        # print(page.text)
        
        
        return render(request, 'result.html',{'page':page.content})  

