import image

##
## Function: superimpose()
## - 2 Parameters: 
##   >> img, is an image object
##   >> subimg, is an image object
## - superimpose subimg on top of the img object such that the subimg is aligned at the center w.r.t the width of img, and at the bottom w.r.t the height of the img
## - return the modified img  (Hint: Do NOT need to create new image object)
##
## TODO: Implement this function
## end of superimpose


##
## Please do NOT change the following code ##
## You must implement superimpose() method in order to have the following code run without error
##
img = image.Image("babyyoda.jpg")
subimg = image.Image("masteryoda.jpg")

newimg = superimpose(img, subimg)

# Create a window to hold the image
win = image.ImageWin(newimg.getWidth(), newimg.getHeight())
newimg.draw(win)
win.exitonclick()
