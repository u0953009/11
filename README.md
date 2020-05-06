# Binary Image classifier using keras for Examining Robotic Grasp Success
     This classifier is a binary classifier which determines if a grasping try of the robotic hand is successful or not.

## Model description
**1. Model Architecture**
   - The model uses the architecture of Inception V3 model.
   - Inception v3 is a widely-used image recognition model that has been shown to attain greater than 78.1% accuracy on the ImageNet dataset. (https://cloud.google.com/tpu/docs/inception-v3-advanced)   
   - A few top layers of Inception V3 are removed: from the top to right above mixed7 layer. (https://github.com/u0953009/Binary-Classifier/blob/master/images/inception%20v3/inception.txt)    
   - On top of the pre-trained model, classification layers are built: Fully connected layer (1024 units, ReLU), drop out rate 0.3, and output layer (1, Sigmoid).  
   - The weights of Inception V3 was not loaded. 
     - Typically, both the architecture and the weights of a pre-trained model are used, but the weights of Inception V3 were not loaded here. The weights of Inception V3 could not be loaded when grayscale images were used as input.  
       <p>&nbsp;</p>
**2. Data description**
   - Images used to train this classifier are (1) photos (2) simulation images (3) extracted images from videos of an Allegro robotic hand trying to grasp an object.
   - After the robotic hand tries to grasp, if it is successful it has an object in hand. Otherwise, an object is on the desk or floor.
   - All photos and images used to train and test are grayscale.
   - data samples
     - Photo samples  
       Photos were taken before and after each try.  
       Majority of images were taken from the side (eg., middle image).    
       Before try  
       <img src="https://github.com/u0953009/Binary-Classifier/blob/master/images/object_2_mustard_grasp_0rrd862.png" width="319" height="190"> <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_4_lego_grasp_0_side36.png" width="319" height="190">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/IMG_20190910_102329671.jpg" width="145" height="190">  
       After try  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/2018-09-05-1109062018ral_img957.jpg" width="319" height="190"> <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_pringles_grasp_1_lift_side377.png" width="319" height="190">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/IMG_20180905_092459phoneral967.jpg" width="145" height="190"><p>&nbsp;</p>
     - Simulation image samples  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_0td1717303.png" width="303" height="227">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_8_lift_6_880.png" width="303" height="227"> 
         <p>&nbsp;</p>      
     - Extracted image samples from videos  
       Since images were extracted from video, there are images that capture moments the robotic hand is on the way to grab an object (not just before or after try). And these images are labeled as unsuccessful.    
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15049.jpg" width="303" height="170">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15855.jpg" width="303" height="170">
	  <p>&nbsp;</p>
**3. Model reports**  
   - Training configuration  
     - Train - the number of images to train the model   
     - Valid - the number of images to validate the model  
     - test  - the number of images to test the model
     - input shape - the input shape of the model  
   - The train data was augmented with factors shown below; factors are applied randomly in each epoch.  
	 <p align="center">  
	 <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/augmentation.png" "width="282" height="152">  
																	 </p>  
																	 
																	 
   - 700 photos (300 successful + 400 unusccessful) and 1007 extracted images (562 successful + 445 unsuccessful) are used to train.
   - 1000 simulation images (500 successful + 500 unsuccessful) are used to train.  
   - There were 4 differnet types of training depending on the number and the type of data, and input shape of the model architecture.
      - Training 1 - Train : 700 (photo), valid : 500 (photo), test : 143 (photo), input shaep : (150,150,1)  
      - Training 2 - Train : 700 (photo), valid : 500 (photo), test : 143 (photo), input shape : (350,350,1)  
      - Training 3 - Train : 700 (photo) + 1000 (simulation), valid : 500 (photo), test : 143 (photo) input shape: (350,350,3)  
      - Training 4 - Train : 700 (photo) + 1007 (extracted),  Valid: 500 (photo), test : 143 (photo) input shape: (350,350,3)  
   - 143 photos (71 successful + 72 unsuccessful) are used to test.  
   - When testing, a few models with low loss and high accuracy were selected and only the best result in each training are described below.  

   - Models
      - Training 1   
	 <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/150/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/150/loss.png" width="352"        height="238">    
	 97 (31 successful + 66 unsuccessful) out of 143 tests are correct. (accuracy 0.68)  
	 
      - Model 2  
	  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350/loss.png" width="352"        height="238">    
	 106 (43 successful + 63 unsuccessful) out of 143 tests are correct. (accuracy 0.74)
	 
	 
      - Model 3  
        To increase the number of training data, simulation images were added.
	 <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350sim/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350sim/loss.png" width="352"        height="238">   
	 103 (46 successful + 57 unsuccessful) out of 143 tests are correct. (accuracy 0.72)
	 
	 
      - Model 4  
        To increase the number of training data, images extracted from experiment videos were added.
	  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350ext/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350ext/loss.png" width="352"        height="238">  
	 Accuracy range is from 0.96 to 0.97 over 30 epochs.  
	 111 (44 successful + 67 unsuccessful) out of 143 tests are correct. (accuracy 0.77)

         <p>&nbsp;</p>
**4. Conclusion**
   - During the training, there was noticeable improvement in identifying unsuccessful tries when input dimension was increased from 150x150 to 350x350.  
   - Adding simulation images didn't improve the test accuracy at all even though more than 50% of the number of original images were added. It seems that simulation images barely help to improve the accuracy of classification.  
   - When adding extraced images from videos, there was a slight improvement.
   - Model 4 shows 77% accuracy on the test. It is a moderate number. The model classified unsuccessful photos much better than successful photos.  

**5. Discussion**
   - First of all, insufficient number of training data was the most chllanging problem to solve in training the model.  
   - Secondly, the dataset is not balanced. 
      - Photos taken from the side comprise the majority of the dataset, while photos taken from different angles, such as from the top, are relatively few.  
      - In case of the extracted images, though the images are taken from various angles, they are not balanced either.  
      - Validation accuracy and loss fluctuated a lot. This also could be caused by bias in dataset.
   - It is needed to obtain more experiment photos and videos in order to improve the accuracy. Finding techniques to balance the data is also worth a try.  
   
   
   
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
