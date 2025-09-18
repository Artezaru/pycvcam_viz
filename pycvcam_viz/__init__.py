from .__version__ import __version__
print(f"pycvcam_viz version: {__version__}")
import sys
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Python executable: {sys.executable}")

__all__ = [
    "__version__",
]

from .zernike_distortion_visualizer import ZernikeDistortionVisualizerUI
__all__.extend(['ZernikeDistortionVisualizerUI'])