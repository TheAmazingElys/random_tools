from tbd_tools import true_every

def test_true_every():
    
    it_s_true_time = true_every(10)
        
    for i in range(25):
        """
        Should be true only at 9 and 19
        """
        if i== 9 or i==19:
            assert next(it_s_true_time)
        else:
            assert not next(it_s_true_time)
        
