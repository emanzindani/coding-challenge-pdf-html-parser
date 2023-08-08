import PyPDF2

def extract_info_from_pdf(pdf_path):

    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)


        meter_number = None
        tax_amount = None


        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()


            meter_number_index = page_text.find('Meter number')
            tax_amount_index = page_text.find('Total Taxes & Fees on Electric Charges')


            if meter_number_index != -1:
                meter_number = page_text[meter_number_index:meter_number_index+20].split(':')[-1].strip()
            if tax_amount_index != -1:
                tax_amount = page_text[tax_amount_index:tax_amount_index+20].split('$')[-1].strip()

        return meter_number, tax_amount


pdf_path = 'sdge_bill.pdf'


electric_meter_number, electric_tax_amount = extract_info_from_pdf(pdf_path)


print("Meter Number:", electric_meter_number)
print("Total Taxes & Fees on Electric Charges:", electric_tax_amount)
