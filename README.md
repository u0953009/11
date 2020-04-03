## Binary Image classifier using keras

Images used to train this classifier are phtos of Allegro robotic hand trying to grasp an object.
After the robotic hand tries to grasp, if it was successful it has an object in hand. Otherwise,
an object is on the desk or floor.

Photos were taken after each try.

This classifier is a binary classifier which determines if grasping try was successful or unsuccessful.

1707 images were used to train.
500 images to validate.

# Installation
pip install -r requirements.txt

# usage
Model train
>python train.py [train_sample_path] [validation_sample_path] [model_filename] 

model will be saved in 'models' folder.

Model predict
>ptyhon predict.py [image_file_folder_path] [model_path]


# samples
Trained model \
https://drive.google.com/file/d/19u42pCy3cQgGv9dTHXnSubFth-g3Igc7/view?usp=sharing 

Train samples  \
https://drive.google.com/file/d/1HzZBLsKi99RokCF-qLQeA9--L7XnVP5B/view?usp=sharing 
https://drive.google.com/file/d/1U0UE6gjmspQkVea8xOm3CT-wKsbBAwzF/view?usp=sharing 
https://drive.google.com/file/d/15rYkZ-tH4owzg-1yb2Ie1de3lQomhQ5X/view?usp=sharing 

Test sample   \
https://drive.google.com/open?id=19HZBEbFFvHIUM7X5EtDXYP9qyTIDQiDL 
https://drive.google.com/open?id=1dURixYlvkKF6S4_GDUrJhNDqE7OaBGoY  

        
