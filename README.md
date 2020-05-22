# Grayscale Image Binary classifier using keras for Examining Robotic Grasp Success  
      A binary classifier, based on gray scale images, which determines if a grasping try of the robotic hand 
      is successful or not.
## Model description
**1. Model Architecture**
   - Existing architecures were used to train: AlexNet, Inception V3, InceptionResV2, VGG16. 
   - Variations of existing architecures were used to train. They are discussed in more detail in Section 3 Model Reports.  
       <p>&nbsp;</p>
**2. Data description**
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
**3. Model reports**  
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

   - Architecures
      - AlexNet, input shape (227, 227, 3)   
         Pre-trained weight not loaded  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/alex/loss.png" width="352"        height="238">    
	 201 (90/115 successful + 111/121 unsuccessful) out of 236 tests are correct. (accuracy 0.85)  
	 
      - AlexNet, input shape (227, 227, 3)  
          Pre-trained weight not loaded  
         Fully connected layers are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/alexdrop/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/alexdrop/loss.png" width="352"        height="238">    
	 205 (93/115 successful + 112/121 unsuccessful) out of 236 tests are correct. (accuracy 0.86)
	 
	 
      - Inception V3, input shape (350, 350, 3)    
        Pre-trained weight not loaded  
	A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/v3withoutweight/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3withoutweight/loss.png" width="352"        height="238">   
	 185 (83/115 successful + 102/121 unsuccessful) out of 236 tests are correct. (accuracy 0.78)  
       
       - Inception V3, input shape (350, 350, 3)  
         Pre-trained weight loaded  
	 A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.2 drop out rate + 1 unit output layer (sigmoid)   
	  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3weight/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/v3weight/loss.png" width="352"        height="238">    
	 212 (96/115 successful + 116/121 unsuccessful) out of 236 tests are correct. (accuracy 0.89)  
	 
	 
	 - Inception Res V2, input shape (150, 150, 3)      
           Pre-trained weight loaded  
	   A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.3 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres150/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres150/loss.png" width="352"        height="238">   
	 203 (94/115 successful + 109/121 unsuccessful) out of 236 tests are correct. (accuracy 0.86)  
	 
	 - Inception Res V2, input shape (350, 350, 3)      
           Pre-trained weight loaded  
	   A few top layers + fully connected layers in the original architecture are replaced with 1024 hidden units layer with 0.3 drop out rate + 1 unit output layer (sigmoid)  
	 <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres350/acc.png" width="352"        height="238">  <img src="https://github.com/u0953009/images/blob/master/bcgray/inceptionres350/loss.png" width="352"        height="238">   
	 214 (106/115 successful + 108/121 unsuccessful) out of 236 tests are correct. (accuracy 0.90)  
	 

         <p>&nbsp;</p>
**4. Conclusion**
   - Models with pre-trained weights tends to show higher accuracy.
   - Greater dimension of input shape tends to show higher accuracy.
   - Training and prediction time of the AlexNet was the shortest among other architectures.
   - Accuracy of Inception Res V2 with input shape (350, 350, 3) was the highest.
   

**5. Discussion**
   - Keras doesn't provide pre-trained model for AlexNet, so it was used without loading weights. If pre-trained weights can be found, its accuracy could improve.  
   - Average training and prediction times for grayscale images are less than those for RGB images.
   - Inception Res V2 shows the best accuracy, but the accuracy of Inception V3 is very close.
   - The accuracy of AlexNet is about 85% and the accuracy of Inception Res V2 is about 90%. Thus, considering the prediction time, AlexNet could perform better.  
   
   
   
   
## Installation
>pip install -r requirements.txt

## Usage
Model training
>python train.py [train_sample_path] [validation_sample_path] [model_filename]

The output model will be saved in 'models' folder.
<br></br>
Model prediction  
>ptyhon predict.py [image_file_folder_path] [model_path]

## Files
Trained model \
https://drive.google.com/open?id=1FWcQ0TrORz8ImdYoDcJxHfZ94K-GCKm2 - model 1  
https://drive.google.com/open?id=1-6AGEURKuotEC49KJMP9sld1tt68hDGR - model 2  
https://drive.google.com/open?id=1-FBzk1nadSrNQuBvSc-fFNDC1pKw9KwX - model 3  
https://drive.google.com/open?id=1I-qJqWQztP6DxLSHUhBNZyeHfyXsFH2I - model 4  


Image samples for training and validation \
https://drive.google.com/open?id=1YnY1sbOd6FMZc66HS0Ng7PyFw777hMXa - photo images   
https://drive.google.com/open?id=16TyVfg-CWPLr8wIA8VfzgAwWspvF2RIk - simulation images (successful)  
https://drive.google.com/open?id=1MRG2JlDXaRgsXnGGr5wYfcKDJJnxzFR5 - simulation images (unsuccessful)  
https://drive.google.com/open?id=1U0UE6gjmspQkVea8xOm3CT-wKsbBAwzF - Extracted images (successful)     
https://drive.google.com/open?id=15rYkZ-tH4owzg-1yb2Ie1de3lQomhQ5X - Extracted images (unsuccessful)    

Image samples for Test   \
https://drive.google.com/open?id=1_Y3puvQj4Ef6TCx3nj5FcPNnhj9y2sYr - images for test (successful)     
https://drive.google.com/open?id=1yhIuF0tRbcNnaHivrFa5fga4zsbTfWLt - images for test (unsuccessful)      
