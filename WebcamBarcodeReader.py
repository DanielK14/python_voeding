import cv2
import keyboard
import pyzbar.pyzbar as pb

font_duplex = cv2.FONT_HERSHEY_DUPLEX
font_simple = cv2.FONT_HERSHEY_PLAIN

def setText(_img, _string, _pos, _font, _scale, _color, _thickness):
  # putText(img, string, pos, font, scale, color, thickness)
  txt_shadow = cv2.putText(_img, _string, _pos, _font, _scale, (0, 0, 0), _thickness + 1)
  txt = cv2.putText(_img, _string, _pos, _font, _scale, _color, _thickness)

# Main loop
cam = cv2.VideoCapture(0)
while cam.isOpened():
  read, frame = cam.read()
  if not read:
    break

  cam_window = cv2.imshow('Barcode Webcam Scanner', frame)

  decoded = pb.decode(frame)
  if decoded != []:
    objects = []
    for decode in decoded:
      name = str(decode.data).replace("b'", "")
      name = name.replace("'", "")
      type = decode.type
      rect = decode.rect
      objects.append({'name': name, 'type': type, 'rect': rect})

    for o in objects:
      setText(frame, f"{o['name']}", (o['rect'].left - 50, o['rect'].top - 50), font_duplex, 1, (255, 255, 255), 2)
      setText(frame, f"{o['type']}", (o['rect'].left - 50, o['rect'].top - 20), font_simple, 2, (255, 255, 255), 2)

    cam_window = cv2.imshow('Barcode Webcam Scanner', frame)

  # Stop program when x/escape key is pressed
  if (keyboard.is_pressed('x')  or keyboard.is_pressed('Esc')) & cv2.waitKey(1):
    break

cam.release()