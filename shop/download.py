import csv
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def download_products_pdf(products):
    template_path = 'shop/shop/products_file.html'
    context = {'products': products}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="products.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def download_products_csv(products):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=products.csv'

    writer = csv.writer(response)
    writer.writerow(['Product Name', 'Category', 'Price', 'Discount Price', 'Stock'])
    
    for product in products:
        writer.writerow([product.name, product.category.name, product.price, product.discount, product.stock])
    return response