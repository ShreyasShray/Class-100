class Cars(object):
    def __init__(self, modalName, modalColor, company, speedLimit):
        self.modalName = modalName
        self.modalColor = modalColor
        self.company = company
        self.speedLimit = speedLimit
    
    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")

    def accelerate(self):
        print("Accelerating")

    def changeGear(self):
        print("Changing gear")

