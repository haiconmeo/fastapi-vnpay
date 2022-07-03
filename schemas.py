from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class requestData(BaseModel):
    vnp_Version:str
    vnp_Command:str
    vnp_TmnCode:str
    vnp_Amount:str
    vnp_CurrCode:str
    vnp_TxnRef:str
    vnp_OrderInfo:str
    vnp_OrderType:str
    vnp_Locale:str
    vnp_BankCode:Optional[str]=None
    vnp_CreateDate:str = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_IpAddr:str
    vnp_ReturnUrl:Optional[str]=None