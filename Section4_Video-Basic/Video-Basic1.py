import cv2

camera = cv2.VideoCapture(0)
width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)

# WINDOWS -- *'DIVX'
# MAC, LUNUX -- *'XVID'
# Output Video File
#writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))


while True:
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.rectangle(frame, (300, 300), (700, 700), color=(0, 0, 255), thickness=10)

    # OPERATION DRAWING
    # writer.wrtie(frame)


    # Color Video Image
    cv2.imshow('frame', frame)
    #cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# writer.release()
camera.release()
cv2.destroyAllWindows()
