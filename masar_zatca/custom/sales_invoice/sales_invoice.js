frappe.ui.form.on('Sales Invoice', {
    on_submit: function(frm) {
		// frappe.msgprint("hi")
        frappe.call({
            method: "master_zatca.api.send_to_zatca",
            args: {
                name:frm.doc.name,
                posting_date:frm.doc.posting_date,
                posting_time:frm.doc.posting_time,
                currency:frm.doc.currency,
                item_code:frm.doc.items[0].item_code,
                item_name:frm.doc.items[0].item_name,
                net_amount:frm.doc.items[0].net_amount,
                qty:frm.doc.items[0].qty,
                qty:frm.doc.items[0].idx,
            },
            callback: function(response) {
                var result = response.message;
                console.log(result);
            }
        });
    }
});