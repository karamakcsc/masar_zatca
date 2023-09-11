import json
import frappe
import requests

@frappe.whitelist()
def send_to_zatca(name, posting_date, posting_time, currency, item_code, item_name, net_amount, qty, idx):
    url = "http://192.168.0.19/WebApiSite/api/invoice"
    
    # Create a dictionary for the JSON data
    data = {
        "itemDetails": [
            {
                "InvoiceLine_ID": idx,
                "item_code": item_code,
                "InvoiceLine_Item_Name": item_name,
                "InvoiceLine_Price_PriceAmount": net_amount,
                "InvoiceLine_InvoicedQuantity": qty
            }
        ],
        "Invoice_ID": name,
        "Invoice_IssueDate": posting_date,
        "Invoice_IssueTime": posting_time,
        "Invoice_DocumentCurrencyCode": currency
    }

    # Serialize the data to JSON format
    json_data = json.dumps(data, ensure_ascii=False)

    # Print the JSON string (optional)
    frappe.msgprint(json_data)

    # Send the JSON data as a POST request
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json_data.encode('utf-8'), headers=headers)

    # Check the response from the server
    if response.status_code == 200:
        # Request was successful
        frappe.msgprint("Request was successful")
        # You can also print the response content if needed:
        # frappe.msgprint(response.text)
    else:
        # Request failed
        frappe.msgprint(f"Request failed with status code {response.status_code}")
        frappe.msgprint(response.text)
