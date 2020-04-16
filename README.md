# Binary Image classifier using keras
     This classifier is a binary classifier which determines if grasping try is successful or unsuccessful.

## Model description
**1. Model Architecture**
   - The model uses pre-trained model Inception V3
   - Mixed7 layer in Inception V3 is extracted 
   - On top of the pre-trained model, classifier layers are built: 
     
     Fully connected layer and sigmoid layer

**2. Data description**
   - Images used to train this classifier are (1) photos (2) simulation images (3) extracted images of an Allegro robotic hand trying to grasp an object.
   - After the robotic hand tries to grasp, if it is successful it has an object in hand. Otherwise, an object is on the desk or floor.
   - data samples
     - Photo samples  
       Photos were taken before and after each try.\
       Majority of images were taken from side (eg., middle image).  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/2018-09-05-1109062018ral_img957.jpg" width="319" height="190"> <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_pringles_grasp_1_lift_side377.png" width="319" height="190">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/IMG_20180905_092459phoneral967.jpg" width="145" height="190">
       
\
     - Simulation image samples  
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_0td1717303.png" width="303" height="227">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/object_0_3m_high_tack_spray_adhesive_grasp_8_lift_6_880.png" width="303" height="227">    

\
     - Extracted image samples from videos  
       Since images were extracted from video, there are images that capture moments the robotic hand is on the way to grab an object (not just before or after try). And these images are labeled as unseccessful.    
       <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15049.jpg" width="303" height="170">  <img src="https://raw.githubusercontent.com/u0953009/Binary-Classifier/master/images/frame15855.jpg" width="303" height="170">
	
**3. Model reports**  
     Train configuration  
     Train - number of images to train the model   
     Valid - number of images to validate the model  
     input shape - input shape of the model  
  
   - Model 1  
     Train: 700 (photo),  Valid: 500 (photo), input shape: (150,150,3)
   - Model 2  
     Train: 700 (photo),  Valid: 500 (photo), input shape: (350,350,3)
   - Model 3  
     Train: 700 (photo) + 500 (similation),  Valid: 500 (photo), input shape: (350,350,3)  
     To increase the number of training data, simulation images were added.
   - Model 4  
     Train: 700 (photo) + 1007 (extracted),  Valid: 500 (photo), input shape: (350,350,3)  
     To increase the number of training data, images extracted from experiment videos were added.


## Installation
pip install -r requirements.txt

## usage
Model train
>python train.py [train_sample_path] [validation_sample_path] [model_filename] 

The output model will be saved in 'models' folder.

Model predict
>ptyhon predict.py [image_file_folder_path] [model_path]


## samples
Trained model \
https://drive.google.com/file/d/19u42pCy3cQgGv9dTHXnSubFth-g3Igc7/view?usp=sharing 

Image samples for training and validation \
https://drive.google.com/file/d/1HzZBLsKi99RokCF-qLQeA9--L7XnVP5B/view?usp=sharing 
https://drive.google.com/file/d/1U0UE6gjmspQkVea8xOm3CT-wKsbBAwzF/view?usp=sharing 
https://drive.google.com/file/d/15rYkZ-tH4owzg-1yb2Ie1de3lQomhQ5X/view?usp=sharing 

Image samples for Test   \
https://drive.google.com/open?id=19HZBEbFFvHIUM7X5EtDXYP9qyTIDQiDL 
https://drive.google.com/open?id=1dURixYlvkKF6S4_GDUrJhNDqE7OaBGoY  
