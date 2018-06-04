from subprocess import call
import os, cv2
import extend, config

def copy_images(path):
    print('##-COPY IMAGES FOR TRAINING')
    sides = os.listdir(path)
    new_path = path + '/t_images'
    if not os.path.isdir(new_path): os.mkdir(new_path)

    if 'model' in sides : sides.remove('model')
    if 't_images' in sides : sides.remove('t_images')
    if 'locationInfo.txt' in sides: sides.remove('locationInfo.txt')
    if 'Origin.jpg' in sides: sides.remove('Origin.jpg')

    for side in sides:
        side_path = path + '/' + side
        classes = os.listdir(side_path)
        print("Copy image classes: ", classes, "in", side)

        for element in classes:
            dir_path = side_path + '/' + element
            eleN_path = new_path + '/' + element
            config.makeDir(eleN_path)
            extend.extend(eleN_path, dir_path)

    '''
    print('# Convert original images to canny images.')
    classes = os.listdir(new_path)
    noise_min = config.NOISE_TRAIN['min']
    noise_max = config.NOISE_TRAIN['max']

    for element in classes :
        path = new_path + '/' + element
        files = os.listdir(path)
        for file in files :
            file_path = path + '/' + file
            origin = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            canny = cv2.Canny(origin, noise_min, noise_max)
            cv2.imwrite(file_path, canny)
    print('# Complete to convert images to canny')
    '''

def execute_Train(device, basePath):
    print('## TRAINING START')
    print('# base path:', basePath)

    _store_path = basePath + '/model/bottleneck'
    _iteration = config.ITERATION
    _model_dir = basePath + '/model/inception'
    _output_graph = basePath + '/model/retrained_graph.pb'
    _output_label = basePath + '/model/retrained_labels.txt'
    _image_dir = basePath + '/t_images'
    _summaries_dir = basePath + '/model/log'
    _tensor_name = device
    cmd = "python ./inception.py --image_dir={image_dir} \
                                    --saved_model_dir={model_dir} \
                                    --bottleneck_dir={store_path} \
                                    --how_many_training_steps={iteration} \
                                    --output_graph={output_graph} \
                                    --output_labels={output_label} \
                                    --summaries_dir={summaries_dir} \
                                    --final_tensor_name={tensor_name}".format(image_dir=_image_dir,
                                                                            model_dir=_model_dir,
                                                                            store_path=_store_path,
                                                                            iteration=_iteration,
                                                                            output_graph=_output_graph,
                                                                            output_label=_output_label,
                                                                            summaries_dir=_summaries_dir,
                                                                            tensor_name=_tensor_name)
    cmd_args = cmd.split()
    call(cmd_args)