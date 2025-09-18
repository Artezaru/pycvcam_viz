import argparse
import sys

from .visualizers import ZernikeDistortionVisualizerUI
from PyQt5.QtWidgets import QApplication

def __main__() -> None:
    r"""
    Main entry point of the package.

    This method contains the script to run if the user enter the name of the package on the command line. 

    .. code-block:: console

        pycvcam_viz
        
    """
    parser = argparse.ArgumentParser(
        description="pycvcam_viz command-line interface"
    )
    parser.add_argument(
        "-zernike",
        action="store_true",
        help="Launch the zernike Distortion GUI"
    )
    args = parser.parse_args()

    if args.zernike:
        app = QApplication(sys.argv)
        window = ZernikeDistortionVisualizerUI()
        window.resize(1800, 800)
        window.show()
        sys.exit(app.exec_())
    else:
        parser.print_help()
        sys.exit(0)
