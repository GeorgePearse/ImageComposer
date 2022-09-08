from PIL import Image, ImageDraw

def crop_polygon(image_path, polygon): 
  original = Image.open(image_path)
  #xy = [(100,100),(1000,100),(1000,800),(100,800)]
  mask = Image.new("L", original.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.polygon(xy, fill=255, outline=None)
  black =  Image.new("L", original.size, 0)
  result = Image.composite(original, black, mask)
  return result
