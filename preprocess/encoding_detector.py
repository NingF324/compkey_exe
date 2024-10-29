from chardet.universaldetector import UniversalDetector

def detect_encoding(filepath):
    detector = UniversalDetector()
    detector.reset()
    with open(filepath, 'rb') as file:
        for each in file:
            detector.feed(each)
            if detector.done:
                break
    detector.close()
    fileencoding = detector.result['encoding']
    if fileencoding in ["GB2312", "GBK"]:
        fileencoding = "GB18030"
    confidence = detector.result['confidence']
    return fileencoding, confidence
