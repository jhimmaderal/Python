from fpdf import FPDF

# create FPDF object
# Layout('P', 'L') Portrait or Landscape
# Unit('mm', 'cc', 'in')
# format('A3', 'A4', 'A5', 'Letter', 'Legal',(100,150))
pdf = FPDF('P','mm','Letter') 

# Add a page
pdf.add_page()

# specify font
# fonts('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B', 'I', '', 'combination', 'BU'
pdf.set_font('helvetica', '', 16)
pdf.set_text_color(220,50,50)

# Add Text
# w = width
# h = height
pdf.cell(120, 10, 'Hello World!', ln=True, border= True)
pdf.cell(80,10, 'Good Bye World!')

pdf.output('pdf1.pdf')