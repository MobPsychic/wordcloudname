from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

shape_mask = np.array(Image.open('khanimage.jpg'))

with open('listofname.txt', 'r', encoding='utf-8') as input_file:
    content = input_file.read()


cloud = WordCloud(
    mask=shape_mask,
    contour_color='black',
    contour_width=5,
    background_color='black',
    max_words=300,
    colormap='plasma'
).generate(content)


plt.figure(figsize=(10, 6))  
plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')  
plt.tight_layout()  
plt.show()
