import cv2
import re

def video_edit(path):
    cap = cv2.VideoCapture(path)

    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_index = 0

    path.replace("\\", "/")
    file_name = re.split("/", path)[-1]
    file_format = file_name.split('.')[-1]
    file_name = file_name.split('.'+file_format)[0]

    fourcc = None
    if file_format == 'avi':
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    elif file_format == 'mp4':
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    elif file_format == 'flv':
        fourcc = cv2.VideoWriter_fourcc(*'flv1')

    if fourcc:
        out = cv2.VideoWriter(file_name + '_edited' + '.' + file_format, fourcc, frame_fps, (frame_width,  frame_height))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break

            out.write(frame)
            frame_index += 1
            print("Editing Frame {} / {}".format(frame_index, frame_length))
            
        cap.release()
        out.release()
        print('done')

video_edit('test/test.mp4')