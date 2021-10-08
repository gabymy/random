import barcode
from barcode.writer import ImageWriter

text = 'Genial'
text1 = str(text)
code = barcode.get_barcode_class('code 128')
image = code(text, writer=ImageWriter())
save_img = image.save('final')
