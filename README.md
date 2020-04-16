# Binary Image classifier using keras
     This classifier is a binary classifier which determines if grasping try is successful or unsuccessful.

## Model description
**1. Model Architecture**
   - The model uses pre-trained model Inception V3.  
   - Mixed7 layer in Inception V3 is extracted.   
   - On top of the pre-trained model, classifier layers are built: Fully connected layer and sigmoid layer.
       <p>&nbsp;</p>
**2. Data description**
   - Images used to train this classifier are (1) photos (2) simulation images (3) extracted images of an Allegro robotic hand trying to grasp an object.
   - After the robotic hand tries to grasp, if it is successful it has an object in hand. Otherwise, an object is on the desk or floor.
   - data samples
     - Photo samples  
       Photos were taken before and after each try.  
       Majority of images were taken from side (eg., middle image).  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/2018-09-05-1109062018ral_img957.jpg" width="319" height="190"> <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_pringles_grasp_1_lift_side377.png" width="319" height="190">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/IMG_20180905_092459phoneral967.jpg" width="145" height="190"> <p>&nbsp;</p>
     - Simulation image samples  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_0td1717303.png" width="303" height="227">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_8_lift_6_880.png" width="303" height="227"> 
         <p>&nbsp;</p>      
     - Extracted image samples from videos  
       Since images were extracted from video, there are images that capture moments the robotic hand is on the way to grab an object (not just before or after try). And these images are labeled as unseccessful.    
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15049.jpg" width="303" height="170">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15855.jpg" width="303" height="170">
	  <p>&nbsp;</p>
**3. Model reports**  
   - Training configuration  
     - Train - the number of images to train the model   
     - Valid - the number of images to validate the model  
     - test  - the number of images to test the model
     - input shape - the input shape of the model  
   - Models
      - Model 1  
        Train: 700 (photo),  Valid: 500 (photo),  test: 143 (photo),  input shape: (150,150,3)  
	 <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/150/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/150/loss.png" width="352"        height="238">  
	 Accuracy range is from 0.75 to 0.79 over 30 epochs.  
	 108 out of 143 tests are correct.  
	 
      - Model 2  
        Train: 700 (photo),  Valid: 500 (photo),  test: 143 (photo),  input shape: (350,350,3)
	  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350/loss.png" width="352"        height="238">  
	 Accuracy range is from 0.82 to 0.86 over 30 epochs.  
	 112 out of 143 tests are correct.
	 
	 
      - Model 3  
        Train: 700 (photo) + 500 (similation),  Valid: 500 (photo), input shape: (350,350,3)  
        To increase the number of training data, simulation images were added.
	   Train: 700 (photo),  Valid: 500 (photo),  test: 143 (photo),  input shape: (350,350,3)
	  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350sim/accuracy.png" width="352"        height="238">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/350sim/loss.png" width="352"        height="238">  
	 Accuracy range is from 0.79 to 0.82 over 30 epochs.  
	 113 out of 143 tests are correct.
	 
	 
      - Model 4  
        Train: 700 (photo) + 1007 (extracted),  Valid: 500 (photo), input shape: (350,350,3)  
        To increase the number of training data, images extracted from experiment videos were added.

         <p>&nbsp;</p>
## Installation
>pip install -r requirements.txt

## Usage
Model training
>python train.py [train_sample_path] [validation_sample_path] [model_filename]

The output model will be saved in 'models' folder.
<br></br>
Model prediction  
>ptyhon predict.py [image_file_folder_path] [model_path]

## Samples
Trained model \
https://drive.google.com/file/d/19u42pCy3cQgGv9dTHXnSubFth-g3Igc7/view?usp=sharing 

Image samples for training and validation \
https://drive.google.com/file/d/1HzZBLsKi99RokCF-qLQeA9--L7XnVP5B/view?usp=sharing 
https://drive.google.com/file/d/1U0UE6gjmspQkVea8xOm3CT-wKsbBAwzF/view?usp=sharing 
https://drive.google.com/file/d/15rYkZ-tH4owzg-1yb2Ie1de3lQomhQ5X/view?usp=sharing 

Image samples for Test   \
https://drive.google.com/open?id=19HZBEbFFvHIUM7X5EtDXYP9qyTIDQiDL 
https://drive.google.com/open?id=1dURixYlvkKF6S4_GDUrJhNDqE7OaBGoY  
