# Grayscale Image Binary Classifier Using Keras for Examining Robotic Grasp Success  
      A binary classifier, based on gray scale images, which determines if a grasping try of the robotic hand 
      is successful or not.
## Model description
**1. Model Architecture**
   - Existing architecures were used to train: AlexNet, Inception V3, InceptionResV2, VGG16. 
   - Variations of existing architecures were used to train. They are discussed in more detail in Section 3 Model Reports.  
       <p>&nbsp;</p>
**2. Data Description**
   - Images used to train this classifier are (1) photos (2) extracted images from videos of an Allegro robotic hand trying to grasp an object.
   - After the robotic hand tries to grasp, if it is successful it has an object in hand. Otherwise, an object is on the desk or floor.
   - All photos and images used to train and test are grayscale.
   - Data samples
     - Photo samples  
       Photos were taken before and after each try.  
       Majority of images were taken from the side (e.g., middle image).    
       Before try  
       <img src="https://github.com/u0953009/images/blob/master/bcgray/object_2_mustard_grasp_0rrd862.png" width="319" height="190"> <img src="https://github.com/u0953009/images/blob/master/bcgray/object_4_lego_grasp_0_side36.png" width="319" height="190">  <img src="https://github.com/u0953009/images/blob/master/bcgray/IMG_20190910_102329671.jpg" width="145" height="190">  
       After try  
       <img src="https://github.com/u0953009/images/blob/master/bcgray/2018-09-05-1109062018ral_img957.jpg" width="319" height="190"> <img src="https://github.com/u0953009/images/blob/master/bcgray/object_0_pringles_grasp_1_lift_side377.png" width="319" height="190">  <img src="https://github.com/u0953009/images/blob/master/bcgray/IMG_20180905_092459phoneral967.jpg" width="145" height="190">  
       
      - Extracted image samples from videos  
       Since images were extracted from video, there are images that capture moments the robotic hand is on the way to grab an object (not just before or after try). And these images are labeled as unsuccessful.    
       <img src="https://github.com/u0953009/images/blob/master/bcgray/frame15049.jpg" width="303" height="170">  <img src="https://github.com/u0953009/images/blob/master/bcgray/frame15855.jpg" width="303" height="170">
	  <p>&nbsp;</p>
**3. Model Reports**  
   - Training configuration  
     - Train - the number of images to train the model   
     - Valid - the number of images to validate the model  
     - Test  - the number of images to test the model
     - Input shape - the input shape of the model  
   - The train data was augmented with factors shown below; factors are applied randomly in each epoch.  
	 <p align="center">  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/augmentation.png" "width="282" height="152">  
																	 </p>  
																	 
																	 
   - 1645 photos (793 successful + 852 unsuccessful) are used to train.
   - 469 photos (225 successful + 244 unsuccessful) are used to validate  
   - 236 photos (115 successful + 121 unsuccessful) are used to test.  
   - In each training, a few models, over 50 epochs, with low loss and high accuracy were selected. Tests were done with these models and only the best results of them are described below.   
   - Test result graph  
	- Left half side is the output values of successful data test set.  
 	- Right half side is the output values of unsuccessful data test set.  
	- If the output value is less than 0.5, the classifier judges as successful and the value is marked as blue in the graph. Otherwise, the classifier judges as unsuccessful and the value is marked as red in the graph.  
	

   - Architecures
      - AlexNet, input shape (227, 227, 3)   
         Pre-trained weight not loaded  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/loss.png" width="352"        height="238">    
	 201 (90/115 successful + 111/121 unsuccessful) out of 236 tests are correct. (accuracy 0.85)  
	  <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/test.png" width="352"        height="238">  
	 
      - AlexNet, input shape (227, 227, 3)  
          Pre-trained weight not loaded  
         Fully connected layers are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/alexdrop/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16/loss.png" width="352"        height="238">    
	 205 (93/115 successful + 112/121 unsuccessful) out of 236 tests are correct. (accuracy 0.86)  
	  <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/alexdrop/test.png" width="352"        height="238">  

      - VGG16, input shape (224, 224, 3)   
         Pre-trained weight not loaded  
	 Fully connected layers are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/loss.png" width="352"        height="238">    
	 216 (113/115 successful + 103/121 unsuccessful) out of 236 tests are correct. (accuracy 0.91)  
	  <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16/test.png" width="352"        height="238">  
	 
      - VGG16, input shape (224, 224, 3)  
          Pre-trained weight loaded  
          Fully connected layers are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16w/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16w/loss.png" width="352"        height="238">    
	 204 (97/115 successful + 107/121 unsuccessful) out of 236 tests are correct. (accuracy 0.86)  
	 <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/vgg16w/test.png" width="352"        height="238">  
	 
	 
	 
	 
      - Inception V3, input shape (350, 350, 3)    
        Pre-trained weight not loaded  
	A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/v3withoutweight/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3withoutweight/loss.png" width="352"        height="238">   
	 185 (83/115 successful + 102/121 unsuccessful) out of 236 tests are correct. (accuracy 0.78)  
	 <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3withoutweight/test.png" width="352"        height="238">  
       
       - Inception V3, input shape (350, 350, 3)  
         Pre-trained weight loaded  
	 A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)   
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3weight/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3weight/loss.png" width="352"        height="238">    
	 212 (96/115 successful + 116/121 unsuccessful) out of 236 tests are correct. (accuracy 0.89)  
	 <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3weight/test.png" width="352"        height="238">  
	 
	 
	 - Inception Res V2, input shape (150, 150, 3)      
           Pre-trained weight loaded  
	   A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.3 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres150/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres150/loss.png" width="352"        height="238">   
	 203 (94/115 successful + 109/121 unsuccessful) out of 236 tests are correct. (accuracy 0.86)  
	 <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres150/test.png" width="352"        height="238">  
	 
	 - Inception Res V2, input shape (350, 350, 3)      
           Pre-trained weight loaded  
	   A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.3 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres350/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres350/loss.png" width="352"        height="238">   
	 214 (106/115 successful + 108/121 unsuccessful) out of 236 tests are correct. (accuracy 0.90)  
	 <p align="center">  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres350/test.png" width="352"        height="238">  
	 

    <p>&nbsp;</p>
**4. Conclusion**
   - Models with pre-trained weights tends to show higher accuracy for relatively complicated architecture.  
   - VGG16 shows the better accuracy when pre-trained weights are not used.
   - Greater dimension of input shape tends to show higher accuracy.
   - Training and prediction time of the AlexNet was the shortest among the architectures used.  
   - Accuracy of VGG16 without weights loaded was the highest.
   

**5. Discussion**
   - Keras doesn't provide pre-trained model for AlexNet, so it was used without loading weights.  
   - Average training and prediction times for grayscale images are less than those for RGB images. 
   - Grayscale images have less dimension of data than RGB images, so for grayscale images, relatively simple architecture seems better for them.  
   - In VGG16 with loaded weight, only fully connected layers were trained and its accuracy was about 86%. When weights were not loaded, all layers were trained and accuracy was about 91%. However, in Inception V3, when weights were loaded, the accuracy was higher. When pre-trained architecture is less complicated, training only fully connected layers doesn't seem to be more efficient.  
   
   
   
   
**6. Related Works**  
   - This grayscale image binary classifier is built based on my previous work on RGB image binary classifier for examining robotic grasp success. Considerations on the amount and balance of data, the size of input shape, etc. are discussed in  
     https://github.com/u0953009/Binary-Classifier.  
   - The video binary classifier for examining robotic grasp sucess is built based on this grayscale image binary classifier. The details are discussed in https://github.com/u0953009/Video-Prediction  
   
   
   

## Files
Weights \
https://drive.google.com/open?id=1EAJlSwU9q2j2gwYkASXkIkbNezWBFDJu - AlexNet  
https://drive.google.com/open?id=1-6n4u1vFHElpIUjHy9YKO6Uo9BcD3pU8 - AlexNet, fully connected layers replaced  

https://drive.google.com/open?id=1-REOAFanW0GSLysMCp2_M9FbcZ7B6cCc  
https://drive.google.com/open?id=1-TSrEV4z-7uu_roUqbPiXJij6tNDW06L - VGG16 with no weights

https://drive.google.com/open?id=1--DLNY0cUt394uFo6RHk5htqacR_xYlQ
https://drive.google.com/open?id=1-086kwufhz4cWaipRN9K0O-ROEfCMXFm - VGG16 with weights

https://drive.google.com/open?id=1cfgnBcqAbDHmOMpNCwD5Pr7h4KMvYvos  
https://drive.google.com/open?id=1VzLZXYxqWxXVgxUB6ucBwR1-9JjfCOMm - Inception V3 with no weights

https://drive.google.com/open?id=1_TNgiIYgf_R_U_wbN6y3FMSQMzjKSFy9  
https://drive.google.com/open?id=1e-0yDuWMTC1GIbMIL3BxOis4GGYf0ZOs - Inception V3 with weights  

https://drive.google.com/open?id=1-zJdlzQq3EmMfq3Ieaey1txfu70mrCQl  
https://drive.google.com/open?id=1-3QBERRAdpoEE9-UhT18V18-pxmbTx8d - Inception ResNet V2, (150,150,3) input_shape  


https://drive.google.com/open?id=18a0ccjb-_6AhurhaVOQ70B0ak6hmVgQy  
https://drive.google.com/open?id=1-1TCy3T5qEGkn4zlSmxfp3SIzjGaHsiw - Inception ResNet v2, (350,350,3) input_shape  




Image data for training and validation \
https://drive.google.com/open?id=14mFpHsZMdnmADks0kzEQIYHEhmSLS2LT - train images   
 

Image data for Test   \
https://drive.google.com/open?id=13_nYOtVE9d61VjCKR_fl1q1hS4imOytL - images for test (successful)     
https://drive.google.com/open?id=1SShxrPhw9gQxvs5Ueoh1MiE8PSzl4BjG - images for test (unsuccessful)      
