import frappe

@frappe.whitelist()
def check_if_absend(doc, method):
    if not doc.check_in or not doc.check_out:
        doc.status = "Absent"
