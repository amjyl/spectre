from PIL import Image
import numpy as np

for i in range(1, 202):
    img_leaves = Image.open(fr"C:\Users\domas\Downloads\листья\15-49-34_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.tif")
    img_leaves_array = np.asarray(img_leaves)

    img_paper = Image.open(fr"C:\Users\domas\Downloads\бумага\16-02-18_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.tif")
    img_paper_array = np.asarray(img_paper)

    im = np.where(img_paper_array==0, 0, img_leaves_array / img_paper_array)*255
    np.save(fr"C:\Users\domas\OneDrive\Desktop\results3\figure_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.npy", im)

# for i in range(1, 202):
#     img_leaves = Image.open(fr"C:\Users\domas\Downloads\листья\15-49-34_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.tif")
#     img_leaves_array = np.asarray(img_leaves)
#
#     img_paper = Image.open(fr"C:\Users\domas\Downloads\бумага\16-02-18_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.tif")
#     img_paper_array = np.asarray(img_paper)
#
#     im = np.divide(img_leaves, img_paper)*255
#     plt.imshow(im)
#     im = Image.fromarray(np.uint8(im))
#     im.save(fr"C:\Users\domas\OneDrive\Desktop\results2\figure_wl{450+2*(i-1)},00_{i//100}{i//10%10}{i%10}.png")