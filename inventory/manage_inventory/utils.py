def format_inventory(product, data):
    pro_details = {
        "product": product,
        "vendor": data.get('vendor'),
        "mrp": data.get('mrp'),
        "batch_number": data.get('batch_no'),
        "batch_date": data.get('batch_date'),
        "quantity": data.get('quantity')
    }
    return pro_details