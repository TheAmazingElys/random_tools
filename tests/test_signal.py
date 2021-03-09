from tbd_tools import Signal, signal

signals = [Signal, signal]

def test_signal():
    
    class Logger():
        """
        A  class to log objects passed to self.log(x) into the list self.data
        """
        def __init__(self):
            self.data = []
            
        def log(self, x):
            self.data.append(x)
            
            
    for i in range(len(signals)):
        """ Test for both the Signal class and the proxy signal"""
        
        i_signal = signals[i]() # create the signal
        logger = Logger() # create the logger
        i_signal.connect(logger.log) # connect the signal to the logger
        
        i_signal.emit("stuff")
        i_signal.emit("thing")
        
        assert logger.data == ["stuff", "thing"] # check if everything was logged
        


