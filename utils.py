import cv2


def stream_iphone(address=r"http://192.168.8.100:4747/video"):
    video = cv2.VideoCapture(address)
    return video


