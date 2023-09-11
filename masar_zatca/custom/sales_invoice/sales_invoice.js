frappe.ui.form.on('Sales Invoice', {
    on_submit: function(frm) {
        var d = frm.doc.items[cdt][cdn];
        frappe.call({
            method: "masar_zatca.api.send_to_zatca",
            args: {
                name: frm.doc.name,
                posting_date: frm.doc.posting_date,
                posting_time: frm.doc.posting_time,
                currency: frm.doc.currency,
                item_code: d.item_code,
                item_name: d.item_name,
                net_amount: d.net_amount,
                qty: d.qty,
                idx: d.idx,
            },
            callback: function(response) {
                var result = response.message;
                console.log(result);
            }
        });
    }
});
