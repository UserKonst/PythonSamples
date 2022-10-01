from PIL import Image

mask_img = Image.open("mask.png")
words_img = Image.open("word_matrix.png")

mask_img = mask_img.resize((words_img.width, words_img.height))

# make transparent ~ 50%
mask_img.putalpha(128)

# put maks_img over words_img
words_img.paste(im=mask_img, box=(0, 0), mask=mask_img)


words_img.show()
