import cv2
import numpy as np

def compute_centroid(x, y, w, h):
    return (int(x + w/2), int(y + h/2))

video = cv2.VideoCapture(r'Motion Detection of multiple cars\baseline_highway-2.gif')

_, frame = video.read()
height, width, _ = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter(r'Motion Detection of multiple cars\Output_video.mp4', fourcc, 20.0, (width*3, height))

kernel = None
backgroundObject = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

line_y = int(3 * height / 4)
car_count = 0

previous_centroids = []

while True:
    ret, frame = video.read()

    if not ret:
        break

    current_centroids = []

    foreground_mask = backgroundObject.apply(frame)
    _, foreground_mask = cv2.threshold(foreground_mask, 250, 255, cv2.THRESH_BINARY)
    foreground_mask = cv2.erode(foreground_mask, kernel, iterations=1)
    foreground_mask = cv2.dilate(foreground_mask, kernel, iterations=2)

    contours, _ = cv2.findContours(foreground_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    frameCopy = frame.copy()

    for cnt in contours:
        if cv2.contourArea(cnt) > 400:
            x, y, w, h = cv2.boundingRect(cnt)    
            centroid = compute_centroid(x, y, w, h)

            if centroid[1] > line_y:
                current_centroids.append(centroid)
            
            cv2.rectangle(frameCopy, (x , y), (x + w, y + h),(0, 0, 255), 2)
            cv2.putText(frameCopy, 'Car Detected', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0), 1, cv2.LINE_AA)

    foregroundPart = cv2.bitwise_and(frame, frame, mask=foreground_mask)
    stacked_frame = np.hstack((frame, foregroundPart, frameCopy))

    out.write(stacked_frame)

    cv2.imshow('Original Frame, Extracted Foreground and Detected Cars', cv2.resize(stacked_frame, None, fx=0.5, fy=0.5))
    k = cv2.waitKey(1) & 0xff
    if k == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()