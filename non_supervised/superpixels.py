from skimage.segmentation import mark_boundaries
from skimage.segmentation import slic
import matplotlib.pyplot as plt
import imageio.v3 as im
from PIL import Image, ImageDraw


def superpixels(path_img, num_segments : int, compactness : int = 10):
  img = im.imread(path_img)
  superpixel_labels = slic(img, n_segments=num_segments, compactness=compactness)
  super_img = mark_boundaries(img, superpixel_labels, \
                        color=(1, 1, 1), outline_color=(0, 0, 0), \
                        mode='thick')
  super_img = (super_img * 255).astype('uint8')
  #background_pil = Image.fromarray(im.imread('0_1.jpeg')).convert("RGBA")
  #mask_pil = Image.fromarray((super_img * 255).astype(np.uint8)).convert("RGBA")
  #combined = Image.alpha_composite(background_pil, mask_pil)
  plt.imshow(img)
  plt.show()
  plt.imshow(super_img)
  plt.show()
  return super_img
