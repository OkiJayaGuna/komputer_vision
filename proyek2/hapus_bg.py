from rembg import remove
from PIL import Image
import io

input = 'foto_01.jpg'
output = 'foto_01'

with open(input, 'rb') as input_file:
    input_image = input_file.read()

output_image = remove(input_image)

with open(output, 'wb') as output_file:
    output_file.write(output_image)

image = Image.open(io.BytesIO(output_image))
image.show()