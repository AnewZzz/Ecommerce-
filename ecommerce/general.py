from . models import Setting, Category

def send_setting_data(request):
    content ={
        'settingData' : Setting.objects.last(),
        'CategoryData' : Category.objects.all()
    }
    
    return content

def make_title(request):
    content= {
        'title' : 'Ecommerce'
    }
    
    return content