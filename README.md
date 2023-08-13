
# Motion Detection of multiple vehicles
This code performs motion detection on a video of cars on a highway. 

## Description

The script reads a video file using OpenCV and processes each frame to detect moving cars. It then displays the original frame, the extracted foreground, and the frame with detected cars side by side.

## Key Features

- **Foreground Extraction**: Extracts the moving parts of the video using a background subtractor.
- **Bounding Boxes**: Draws bounding boxes around detected cars.
- **Car Counting**: Counts cars that pass a specific line on the frame.
- **Video Output**: Outputs the processed video with side-by-side frames for easier comparison.

## Code Overview

- The code uses OpenCV's `BackgroundSubtractorMOG2` for background subtraction.
- Contours are then found for the moving objects.
- Bounding boxes are drawn around the large contours to be considered cars.
- A line is drawn across the frame, and cars that pass this line are counted.
- The output is a video that displays the original frame, the extracted foreground, and the frame with detected cars side by side.

## How to Use

1. Make sure you have OpenCV installed.
2. Update the path to the input video in the script.
3. Run the script.
4. Watch the live processing of the video and see the cars being detected in real-time.
5. Check the output video for the side-by-side comparison.

## Feedback and Contributions

- Feel free to fork the repository, open issues, or submit pull requests. Any feedback is welcome!
---

