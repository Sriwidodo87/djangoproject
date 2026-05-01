from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Kontak',
        'subtitle':'Ini adalah halaman Kontak',
        # 'nav': [
        #     ['/', "Home"],
        #     ['/blog', "Blog"],
        #     ['/kontak', "Kontak"],
        #
        # ],
        'banner': 'images/kontak.png'
    }
    # return render(request,'kontak/index.html',context)
    return render(request,'index.html',context)
