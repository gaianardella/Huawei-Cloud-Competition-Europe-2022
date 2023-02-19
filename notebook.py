import matplotlib.image as plt
import numpy as np
import io
import matplotlib.pyplot as plt

resp1=obs_client.getObject(bucketName="clothes", objectKey='T-Shirt/1676800851.937637')
# data = resp['body'].read()
response_wrapper1 = resp1.body['response']
content1 = response_wrapper1.read()

# Create a file-like object from the raw bytes
img_file1 = io.BytesIO(content1)

# Read the image data using imread
img1 = mpimg.imread(img_file1, format='jpg')

# Display the image using imshow
# plt.imshow(img1)
# plt.show()

# Rotate the image by 90 degrees counterclockwise
# img_rotated1 = np.rot90(img1, k=3)



resp2=obs_client.getObject(bucketName="clothes", objectKey="Shorts/1676799974.093065")
# data = resp['body'].read()
response_wrapper2 = resp2.body['response']
content2 = response_wrapper2.read()

# Create a file-like object from the raw bytes
img_file2 = io.BytesIO(content2)

# Read the image data using imread
img2 = mpimg.imread(img_file2, format='jpg')

# Display the image using imshow
# plt.imshow(img2)
# plt.show()

# Check the shape of the image arrays
if img1.shape[0] < img1.shape[1]:
    img1 = np.rot90(img1, k=3)
    
if img2.shape[0] < img2.shape[1]:
    img2 = np.rot90(img2, k=3)
    
# Stack the two images horizontally
img_horizontal = np.concatenate([img1, img2], axis=1)

# Display the stacked image using imshow
plt.imshow(img_horizontal)
plt.show()
# plt.imshow(img1)
# plt.show()

# plt.imshow(img2)
# plt.show()
