from typing import Union
from vnpay import Vnpay
from fastapi import FastAPI, Request
from schemas import requestData
from datetime import datetime
from fastapi.responses import RedirectResponse
app = FastAPI()
VNPAY_RETURN_URL = 'http://localhost:3000/payment_return'  # get from config
VNPAY_PAYMENT_URL = 'https://sandbox.vnpayment.vn/paymentv2/vpcpay.html'  # get from config
VNPAY_API_URL = 'https://sandbox.vnpayment.vn/merchant_webapi/merchant.html'
VNPAY_TMN_CODE = ''  # Website ID in VNPAY System, get from config
VNPAY_HASH_SECRET_KEY = ''
vnpay = Vnpay(
    tmn_code=VNPAY_TMN_CODE,
    secret_key=VNPAY_HASH_SECRET_KEY,
    return_url=VNPAY_RETURN_URL,
    vnpay_payment_url=VNPAY_PAYMENT_URL,
    api_url=VNPAY_API_URL
)
@app.get("/payment")
def read_root():
    req= {        
        "vnp_Version": "2.1.0",
        "vnp_Command": "pay",
        "vnp_TmnCode": "string",
        "vnp_Amount": "10000000",
        "vnp_CurrCode": "VND",
        "vnp_TxnRef": "string123",
        "vnp_OrderInfo": "123123",
        "vnp_OrderType": "ao_tunaasd",
        "vnp_Locale": "vn",
        "vnp_BankCode":"NCB",
        "vnp_CreateDate": datetime.now().strftime('%Y%m%d%H%M%S'),
        "vnp_IpAddr": "192.168.1.11"
    }
    req['vnp_TmnCode']='D9B4Q4OV'
    req['vnp_ReturnUrl']='http://localhost:8000/payment_return'
    return RedirectResponse(vnpay.get_payment_url(req))

    


@app.get("/payment_return")
def read_item(request:Request):
    data = request.query_params.items()
    response={}
    for i in data:
        response[i[0]] = i[1]
    if vnpay.validate_response(response):
        return "Thành công"
    else:
        return "Thất bại"