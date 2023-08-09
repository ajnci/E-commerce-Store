from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def download_order_info(order):
    template_path = 'shop/orders/checkout/order_info_file.html'
    context = {'order': order}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="order_detail.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response