from django.shortcuts import render
def index(request):
    context = {
        'title':"My Website",
        "subtitle":" Selamat datang di website gua yang super keren dan beken ",
        # 'nav':[
        #     ['/','Home'],
        #     ['/blog','Blog'],
        #     ['/kontak','Kontak'],
        # ],
        'banner':'images/beranda.png'
    }
    return render(request, 'index.html',context)