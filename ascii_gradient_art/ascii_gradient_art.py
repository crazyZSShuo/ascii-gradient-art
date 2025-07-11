
import sys
from ascii_gradient_art.core.generator import generate_ascii_art, render_ascii_art, apply_gradient_color, animate_ascii_art
from ascii_gradient_art.utils.cli_parser import parse_args

def main():
    args = parse_args()

    ascii_art = generate_ascii_art(args.text, args.font)
    processed_art = render_ascii_art(ascii_art, args.render_mode)

    if args.animation_frames > 1:
        animate_ascii_art(
            processed_art,
            theme_name=args.color_theme,
            direction=args.gradient_direction,
            frames=args.animation_frames,
            delay=args.animation_delay
        )
    else:
        final_output = apply_gradient_color(
            processed_art,
            theme_name=args.color_theme,
            direction=args.gradient_direction
        )
        if args.output_file:
            with open(args.output_file, "w") as f:
                f.write(final_output)
        else:
            print(final_output)

if __name__ == "__main__":
    main()



