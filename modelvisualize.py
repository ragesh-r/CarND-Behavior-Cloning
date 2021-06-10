
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten, Dense, Lambda, Conv2D, Cropping2D, Dropout
from keras.layers.pooling import MaxPooling2D
from keras.utils.vis_utils import plot_model
model = Sequential()
# Crop the hood of the car and the higher parts of the images 
# which contain irrelevant sky/horizon/trees
model.add( Cropping2D( cropping=( (50,20), (0,0) ), input_shape=(160,320,3)))
#Normalize the data.
model.add( Lambda( lambda x: x/255. - 0.5 ) )
# Nvidia Network
# Convolution Layers
model.add( Conv2D( 24, 5, 5, subsample=(2,2), activation = 'relu' ) )
model.add( Conv2D( 36, 5, 5, subsample=(2,2), activation = 'relu' ) )
model.add( Conv2D( 48, 5, 5, subsample=(2,2), activation = 'relu' ) )
model.add( Conv2D( 64, 3, 3, subsample=(1,1), activation = 'relu' ) )
model.add( Conv2D( 64, 3, 3, subsample=(1,1), activation = 'relu' ) )
# Flatten for transition to fully connected layers.
model.add( Flatten() )
# Fully connected layers
model.add( Dense( 100 ) )
model.add(Dropout(0.2)) # I added this dropout layer myself, because the previous 
                        # fully connected layers has a lot of free parameters 
                        # and seems like the layer most in danger of overfitting. 
model.add( Dense( 50 ) )
model.add( Dense( 10 ) )
model.add( Dense( 1 ) )

plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
