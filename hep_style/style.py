import matplotlib.pyplot as plt
import matplotlib as mpl
import mplhep as hep

def setup_style():
    # Load style sheet
    plt.style.use(hep.style.ROOT)  # or ATLAS/LHCb2
    # Set font size and family
    mpl.rcParams['font.size']   = 14
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['figure.figsize']   = (8, 6)  # Set figure size