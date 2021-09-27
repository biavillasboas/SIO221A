import numpy as np

def overlapping_segments1D(x, segment_length, overlap=0.0):
    """Divides array into overlapping segments
    Parameters
    ----------
    x : 
        input 1D array
    segment_length :
        length of each segment
    overlap : float, optional
        fraction of overlapping between segments. The default overlap is zero.
    Returns
    -------
    segments :
        ndarray with number of segments as the first dimension and segment length in the
        second dimension.
    Notes
    -----
    For this function to work segment_length times overlap has to be an integer. 
    The length of the input array len(x) divided by segment_length also has to be an integer.
    """
    
    assert isinstance(x, np.ndarray), "x must be a Numpy array"
    assert x.ndim == 1, "x must be a 1D Numpy array"
    
    N = len(x) 
    assert (N/segment_length).is_integer(), "The number of segments must be an integer"
    assert (overlap*segment_length).is_integer(), "The number of points to overlap must be an integer"
    
    n_seg = N//segment_length    
    left = range(0, N-segment_length+1, round((1-overlap)*segment_length))
    segments = []
    for l in left:
        r = l + segment_length
        segments.append(x[l:r])
    segments = np.array(segments)
    return segments
