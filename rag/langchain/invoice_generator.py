import datetime
import os
import random

from fpdf import FPDF


def generate_random_invoice():
    """Generate random invoice data based on the provided specifications."""

    # Create random invoice number in format GTM-XXXXXX
    invoice_number = f"GTM-{random.randint(100000, 999999)}"

    # Random date within the last 3 months
    today = datetime.datetime.now()
    start_date = today - datetime.timedelta(days=90)
    random_days = random.randint(0, 90)
    invoice_date = (start_date + datetime.timedelta(days=random_days)).strftime(
        "%d/%m/%Y"
    )

    # Random due date (7-30 days after invoice date)
    due_date = (
        start_date + datetime.timedelta(days=random_days + random.randint(7, 30))
    ).strftime("%d/%m/%Y")

    # Payment terms
    payment_terms = random.choice(["TT", "LC", "DP", "DA", "CAD"])

    # Shipper lines
    shipper_line = random.choice(
        ["Hapag", "Maersk", "CMA CGM", "MSC", "Evergreen", "COSCO"]
    )

    # Shipment terms
    shipment_terms = random.choice(
        [
            "FOB KARACHI PAKISTAN",
            "CIF SHANGHAI CHINA",
            "FOB ISTANBUL TURKEY",
            "CIF MUMBAI INDIA",
            "FOB LAGOS NIGERIA",
        ]
    )

    # Vendor details
    vendors = [
        {
            "name": "Global Trade Materials Ltd",
            "address": "123 Export Plaza, Karachi, Pakistan",
            "email": "info@gtm.pk",
        },
        {
            "name": "Eastern Supplies Co.",
            "address": "456 Industrial Zone, Shanghai, China",
            "email": "contact@eastsup.cn",
        },
        {
            "name": "Mediterranean Products Inc.",
            "address": "789 Harbor Road, Istanbul, Turkey",
            "email": "sales@medprod.tr",
        },
        {
            "name": "Subcontinental Goods Pvt Ltd",
            "address": "321 Trading Center, Mumbai, India",
            "email": "orders@scgoods.in",
        },
        {
            "name": "African Export Partners",
            "address": "654 Commerce Street, Lagos, Nigeria",
            "email": "business@afexp.ng",
        },
    ]
    vendor = random.choice(vendors)

    # Customer details
    customers = [
        {
            "name": "American Imports LLC",
            "address": "555 Business Ave, New York, USA",
            "email": "purchasing@aimp.com",
        },
        {
            "name": "European Distribution GmbH",
            "address": "777 Market Street, Berlin, Germany",
            "email": "orders@eurodist.de",
        },
        {
            "name": "Pacific Trade Partners",
            "address": "888 Harbor Drive, Sydney, Australia",
            "email": "buy@pacifictrade.au",
        },
        {
            "name": "Nordic Wholesale AB",
            "address": "999 Commerce Road, Stockholm, Sweden",
            "email": "procurement@nordicwh.se",
        },
        {
            "name": "Middle East Retail Group",
            "address": "111 Trade Center, Dubai, UAE",
            "email": "supply@merg.ae",
        },
    ]
    customer = random.choice(customers)

    # Generate line items
    products = [
        {"name": "Cotton Textiles", "unit": "Bales", "price_range": (50, 150)},
        {"name": "Leather Goods", "unit": "Cartons", "price_range": (200, 500)},
        {"name": "Handicrafts", "unit": "Boxes", "price_range": (100, 300)},
        {"name": "Spices", "unit": "Kg", "price_range": (10, 50)},
        {"name": "Sporting Goods", "unit": "Pieces", "price_range": (30, 200)},
        {"name": "Furniture", "unit": "Sets", "price_range": (500, 2000)},
        {"name": "Electronic Components", "unit": "Units", "price_range": (5, 100)},
        {"name": "Medical Supplies", "unit": "Packs", "price_range": (100, 600)},
    ]

    num_items = random.randint(3, 8)
    line_items = []
    subtotal = 0

    for _ in range(num_items):
        product = random.choice(products)
        quantity = random.randint(5, 100)
        unit_price = round(
            random.uniform(product["price_range"][0], product["price_range"][1]), 2
        )
        total = round(quantity * unit_price, 2)
        subtotal += total

        line_items.append(
            {
                "description": product["name"],
                "quantity": quantity,
                "unit": product["unit"],
                "unit_price": unit_price,
                "total": total,
            }
        )

    # Calculate tax and total
    tax_rate = round(random.uniform(0.05, 0.2), 2)
    tax = round(subtotal * tax_rate, 2)
    total_amount = round(subtotal + tax, 2)

    # Container details
    container_type = random.choice(
        ["20ft Standard", "40ft High Cube", "40ft Standard", "45ft High Cube"]
    )
    container_number = f"{random.choice(['MSCU', 'CMAU', 'HLXU', 'TCNU', 'EGHU'])}{random.randint(1000000, 9999999)}"

    # Bill of Lading
    bl_number = f"BL{random.randint(10000000, 99999999)}"

    # Port information
    ports_of_loading = ["KARACHI", "SHANGHAI", "ISTANBUL", "MUMBAI", "LAGOS"]
    ports_of_discharge = ["NEW YORK", "HAMBURG", "SYDNEY", "ROTTERDAM", "JEBEL ALI"]

    port_of_loading = random.choice(ports_of_loading)
    port_of_discharge = random.choice(ports_of_discharge)

    return {
        "invoice_number": invoice_number,
        "invoice_date": invoice_date,
        "due_date": due_date,
        "payment_terms": payment_terms,
        "shipper_line": shipper_line,
        "shipment_terms": shipment_terms,
        "vendor": vendor,
        "customer": customer,
        "line_items": line_items,
        "subtotal": subtotal,
        "tax_rate": tax_rate,
        "tax": tax,
        "total_amount": total_amount,
        "container_type": container_type,
        "container_number": container_number,
        "bl_number": bl_number,
        "port_of_loading": port_of_loading,
        "port_of_discharge": port_of_discharge,
    }


def create_invoice_pdf(invoice_data, output_folder="invoices"):
    """Create a PDF invoice from the given data."""

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add company header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, invoice_data["vendor"]["name"], ln=True, align="C")
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 5, invoice_data["vendor"]["address"], ln=True, align="C")
    pdf.cell(0, 5, f"Email: {invoice_data['vendor']['email']}", ln=True, align="C")
    pdf.ln(10)

    # Add invoice title
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, "COMMERCIAL INVOICE", ln=True, align="C")
    pdf.ln(5)

    # Add invoice details
    pdf.set_font("Arial", "B", 10)
    pdf.cell(95, 7, "Invoice Information:", ln=0)
    pdf.cell(95, 7, "Customer Information:", ln=1)

    pdf.set_font("Arial", size=10)
    pdf.cell(30, 5, "Invoice No:", ln=0)
    pdf.cell(65, 5, invoice_data["invoice_number"], ln=0)
    pdf.cell(30, 5, "Customer:", ln=0)
    pdf.cell(65, 5, invoice_data["customer"]["name"], ln=1)

    pdf.cell(30, 5, "Date:", ln=0)
    pdf.cell(65, 5, invoice_data["invoice_date"], ln=0)
    pdf.cell(30, 5, "Address:", ln=0)
    pdf.cell(65, 5, invoice_data["customer"]["address"], ln=1)

    pdf.cell(30, 5, "Due Date:", ln=0)
    pdf.cell(65, 5, invoice_data["due_date"], ln=0)
    pdf.cell(30, 5, "Email:", ln=0)
    pdf.cell(65, 5, invoice_data["customer"]["email"], ln=1)

    pdf.ln(5)

    # Add shipping details
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 7, "Shipping Information:", ln=1)
    pdf.set_font("Arial", size=10)

    pdf.cell(50, 5, "Shipper Line:", ln=0)
    pdf.cell(50, 5, invoice_data["shipper_line"], ln=0)
    pdf.cell(50, 5, "Container Type:", ln=0)
    pdf.cell(40, 5, invoice_data["container_type"], ln=1)

    pdf.cell(50, 5, "Shipment Terms:", ln=0)
    pdf.cell(50, 5, invoice_data["shipment_terms"], ln=0)
    pdf.cell(50, 5, "Container Number:", ln=0)
    pdf.cell(40, 5, invoice_data["container_number"], ln=1)

    pdf.cell(50, 5, "B/L Number:", ln=0)
    pdf.cell(50, 5, invoice_data["bl_number"], ln=0)
    pdf.cell(50, 5, "Payment Terms:", ln=0)
    pdf.cell(40, 5, invoice_data["payment_terms"], ln=1)

    pdf.cell(50, 5, "Port of Loading:", ln=0)
    pdf.cell(50, 5, invoice_data["port_of_loading"], ln=0)
    pdf.cell(50, 5, "Port of Discharge:", ln=0)
    pdf.cell(40, 5, invoice_data["port_of_discharge"], ln=1)

    pdf.ln(10)

    # Add table header
    pdf.set_font("Arial", "B", 10)
    pdf.cell(80, 7, "Description", 1, 0, "C")
    pdf.cell(25, 7, "Quantity", 1, 0, "C")
    pdf.cell(25, 7, "Unit", 1, 0, "C")
    pdf.cell(30, 7, "Unit Price", 1, 0, "C")
    pdf.cell(30, 7, "Total", 1, 1, "C")

    # Add table rows
    pdf.set_font("Arial", size=10)
    for item in invoice_data["line_items"]:
        pdf.cell(80, 7, item["description"], 1, 0)
        pdf.cell(25, 7, str(item["quantity"]), 1, 0, "C")
        pdf.cell(25, 7, item["unit"], 1, 0, "C")
        pdf.cell(30, 7, f"${item['unit_price']:.2f}", 1, 0, "R")
        pdf.cell(30, 7, f"${item['total']:.2f}", 1, 1, "R")

    # Add totals
    pdf.cell(130, 7, "", 0, 0)
    pdf.cell(30, 7, "Subtotal:", 1, 0)
    pdf.cell(30, 7, f"${invoice_data['subtotal']:.2f}", 1, 1, "R")

    pdf.cell(130, 7, "", 0, 0)
    pdf.cell(30, 7, f"Tax ({invoice_data['tax_rate']*100:.1f}%):", 1, 0)
    pdf.cell(30, 7, f"${invoice_data['tax']:.2f}", 1, 1, "R")

    pdf.set_font("Arial", "B", 10)
    pdf.cell(130, 7, "", 0, 0)
    pdf.cell(30, 7, "TOTAL:", 1, 0)
    pdf.cell(30, 7, f"${invoice_data['total_amount']:.2f}", 1, 1, "R")

    # Add terms and notes
    pdf.ln(10)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 7, "Terms and Conditions:", ln=1)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(
        0,
        5,
        "1. Payment is due by the date specified on this invoice.\n2. All goods remain the property of the seller until paid for in full.\n3. Late payments may be subject to a 2% monthly interest charge.\n4. Please include the invoice number on all payments and correspondence.",
    )

    # Output the PDF to a file
    output_file = os.path.join(
        output_folder, f"Invoice_{invoice_data['invoice_number']}.pdf"
    )
    pdf.output(output_file)

    return output_file


def generate_multiple_invoices(count=5, output_folder="invoices"):
    """Generate multiple random invoices."""

    generated_files = []

    for i in range(count):
        invoice_data = generate_random_invoice()
        output_file = create_invoice_pdf(invoice_data, output_folder)
        generated_files.append(output_file)
        print(f"Generated invoice {i+1}/{count}: {output_file}")

    return generated_files


if __name__ == "__main__":
    # Generate 5 random invoices
    generated_files = generate_multiple_invoices(5)
    print(f"\nSuccessfully generated {len(generated_files)} invoices.")
    print(f"Files are stored in the 'generated_invoices' folder.")