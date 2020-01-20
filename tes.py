from keras.models import model_from_json
json_file = open("/home/jh/catkin_ws/src/turtlebot3_machine_learning/turtlebot3_dqn/save_model/stage_1_190.json","r")
loaded_json = json_file.read()
json_file.close()
loaded = model_from_json(loaded_json)

loaded.load_weights(loaded_json)
