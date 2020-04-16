# Binary Image classifier using keras



1. Model Architecture
   - The model uses pre-trained model Inception V3
   - Mixed7 layer in Inception V3 is extracted 
   - On top of the pre-trained model, classifier layers are built. 
     
     Fully connected layer and sigmoid layer

2. Data dsecription
   - Images used to train this classifier are photos of an Allegro robotic hand trying to grasp an object.
   - After the robotic hand tries to grasp, if it is successful it has an object in hand. Otherwise, an object is on the desk or floor.
   - Photos were taken before and after each try.
   - This classifier is a binary classifier which determines if grasping try was successful or unsuccessful.
   - Sample images
   
      Majority of images were taken from side(eg., middle image)
	  
     <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/2018-09-05-1109062018ral_img957.jpg" width="290" height="161"><img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_pringles_grasp_1_lift_side377.png" width="290" height="163"><img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/IMG_20180905_092459phoneral967.jpg" width="145" height="193">

   - Simulation images
  
      <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_0td1717303.png" width="303" height="227">
      <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_8_lift_6_880.png" width="303" height="227">  

   - Extracted imgaes
  
     Extract frames from video. Since images were extracted from video, there are images that capture moments the robotic hand is on the way to grab an object (not just before or after try). And these images are labeld as unseccessful.
     <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15049.jpg" width="303" height="170">
     <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15855.jpg" width="303" height="170">
	
3. Model reports
   Train configuration 
   Train - number of images to train the model
   Valid - number of images to validate the model
   image dimension - input shape of the model
  
   - Train: 700(photo)  Valid: 500(photo), input dimension: (150,150,3)
   - Train: 700(phpot)  Valid: 500(photo), input dimension: (350,350,3)
   - Train: 700(photo)+500(similation)  Valid: 500(photo), input dimension: (350,350,3)
     To increases number of training data, use simulation images.
   - Train: 1707(photo)  Valid: 500(photo), input dimension: (350,350,3)
     To increases number of training data, extract images from experiment video.


## Installation
pip install -r requirements.txt

## usage
Model train
>python train.py [train_sample_path] [validation_sample_path] [model_filename] 

model will be saved in 'models' folder.

Model predict
>ptyhon predict.py [image_file_folder_path] [model_path]


## samples
Trained model \
https://drive.google.com/file/d/19u42pCy3cQgGv9dTHXnSubFth-g3Igc7/view?usp=sharing 

Train samples  \
https://drive.google.com/file/d/1HzZBLsKi99RokCF-qLQeA9--L7XnVP5B/view?usp=sharing 
https://drive.google.com/file/d/1U0UE6gjmspQkVea8xOm3CT-wKsbBAwzF/view?usp=sharing 
https://drive.google.com/file/d/15rYkZ-tH4owzg-1yb2Ie1de3lQomhQ5X/view?usp=sharing 

Test sample   \
https://drive.google.com/open?id=19HZBEbFFvHIUM7X5EtDXYP9qyTIDQiDL 
https://drive.google.com/open?id=1dURixYlvkKF6S4_GDUrJhNDqE7OaBGoY  
