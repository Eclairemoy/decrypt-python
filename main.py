# `data` is the data you encrypted and passed into `evervault.run` from your server. The Function 
# automatically decrypts and returns the data.
def handler(data, context):
    return {'data': data}
