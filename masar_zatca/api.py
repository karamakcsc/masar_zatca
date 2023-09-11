#from future import unicode_literals
import frappe, erpnext
from frappe.utils import flt, cstr, nowdate, comma_and
from frappe import throw, msgprint, _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
import requests , json,datetime
from datetime import datetime
from frappe.utils import get_request_session
from frappe.utils import(
	formatdate,
	getdate,
	DATE_FORMAT
)


@frappe.whitelist()
def send_to_zatca(name,posting_date,posting_time,currency,item_code,item_name,net_amount,qty,idx): 
    url = "http://192.168.0.19/WebApiSite/api/invoice"
    data = {
        "itemDetails": [
            {
                "InvoiceLine_ID": idx,
                "item_code": item_code,
                "InvoiceLine_Item_Name": item_name,
                "InvoiceLine_Price_PriceAmount": net_amount,
                "InvoiceLine_InvoicedQuantity": qty,
            }
        ],
        "Invoice_ID": name,
        "Invoice_IssueDate": posting_date,
        "Invoice_IssueTime": posting_time,
        "Invoice_DocumentCurrencyCode": currency,

    }

    # Serialize the data to JSON format
    json_data = json.dumps(data, ensure_ascii=False)

    # Print the JSON string
    print(json_data)

