#  Drowsiness Alarm system
### This is a drowsiness detection model that was made by fine-tuning the ultralytics yolov5 model on my custom data.
To create a drowsiness detection model, fine-tune the YOLOv5 model on custom labeled data with drowsy and awake states. Prepare and annotate images, configure YOLOv5, train the model, evaluate performance, and deploy for real-time detection in applications like driver safety and workplace monitoring.

![download](https://github.com/VHemanth45/Drowsiness-Alarm/assets/154959821/f8febc28-f750-4897-a6ff-13586ad2fe1f)
### For labeling my data I have used the LabelImg tool 
This is a very useful and easy tool to use. First, we need to create labels such as "awake" and "drowsy" by drawing boxes around the face, giving them a label, and saving the file in Yolo format, as we are using the Yolo model.

![train_batch1](https://github.com/VHemanth45/Drowsiness-Alarm/assets/154959821/e7e92a5e-4d21-454b-b2a8-9d54b17e07f7) ### This is during the training of the model
## labels Correlogram
![labels_correlogram](https://github.com/VHemanth45/Drowsiness-Alarm/assets/154959821/74605833-d947-4030-8274-daee261d8ebd)
## Results of the model
![results](https://github.com/VHemanth45/Drowsiness-Alarm/assets/154959821/ce23c1a1-a277-4170-988a-b5b159af0623)

