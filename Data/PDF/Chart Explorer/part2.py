from fpdf import FPDF

# create FPDF object
pdf = FPDF('P','mm','Letter') 

# Set auto page break
pdf.set_auto_page_break(auto=True, margin = 15)

# Add a page
pdf.add_page()

# specify font
pdf.set_font('helvetica', '', 16)

# Add Text
for i in range(1,41):
  pdf.cell(0,10, f'This is line {i}', ln = True)

pdf.output('pdf2.pdf')