
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate colorful ASCII art with gradients and animations."
    )
    parser.add_argument(
        "--text", 
        type=str, 
        required=True, 
        help="Text to convert to ASCII art."
    )
    parser.add_argument(
        "--font", 
        type=str, 
        default="standard", 
        help="Font style for ASCII art (e.g., standard, slant, big)."
    )
    parser.add_argument(
        "--color-theme",
        type=str,
        default="rainbow",
        help="Gradient color theme (e.g., rainbow, ocean, fire)."
    )
    parser.add_argument(
        "--gradient-direction",
        type=str,
        default="horizontal",
        choices=["horizontal", "vertical", "diagonal_up", "diagonal_down"],
        help="Direction of the color gradient."
    )
    parser.add_argument(
        "--render-mode",
        type=str,
        default="outline",
        choices=["outline", "fill"],
        help="Rendering mode: outline or fill."
    )
    parser.add_argument(
        "--animation-frames",
        type=int,
        default=1,
        help="Number of animation frames. Set > 1 for animation."
    )
    parser.add_argument(
        "--animation-delay",
        type=float,
        default=0.1,
        help="Delay between animation frames in seconds."
    )
    parser.add_argument(
        "--output-file",
        type=str,
        help="Output ASCII art to a file instead of stdout."
    )
    return parser.parse_args()



