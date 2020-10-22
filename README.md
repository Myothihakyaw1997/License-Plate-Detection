# License-Plate-Detection

## Require Python3.8 or above

## Pre requisites tesseract-ocr , torch and torchvison

### Installation

**First create virtualenv with require python version.Then install dependencies by following command.**

```
pip install -r requiremnets.txt
```

### File explanation

- `easy_ocr_test.py` is the testing file for assessing effectiveness of easy_ocr library.
- `google_cloud_vision.py` is the local testing file for google vision.
- `license_plate_detection_cv2.py` and `license_detection.py` are files for assessing effectiveness of pytesseract libray combination with opencv library.
- `pytesseract_test.py` is testing file for pytesseract libray.

### Running programs

```
python3 program_name.py
```

### Program Effectiveness

| No | Program Library | Accuracy |
| 1 | easy_ocr | **80%** |
| 2 | google-vision | **90%** |
| 3 | Pytessearct | **70%** |

> Pytessearct need opencv to pre process image
> Depend on pre processing of image pytessearct accuracy may differ.
