
import pyfiglet
import time
from ascii_gradient_art.core.color_utils import lerp_color, rgb_to_ansi, reset_ansi
from ascii_gradient_art.themes.default_themes import COLOR_THEMES

def generate_ascii_art(text, font='standard'):
    """
    生成基本的 ASCII 艺术字。
    """
    try:
        fig = pyfiglet.Figlet(font=font)
        return fig.renderText(text)
    except pyfiglet.FigletError:
        return f"Error: Font '{font}' not found or invalid. Using default font.\n" + pyfiglet.Figlet(font='standard').renderText(text)

def render_ascii_art(ascii_art_text, render_mode='outline'):
    """
    根据渲染模式处理 ASCII 艺术字。
    - 'outline': 保持 pyfiglet 原始输出。
    - 'fill': 将 ASCII 艺术字内部的空白区域填充为实心块字符。
    """
    if render_mode == 'outline':
        return ascii_art_text
    elif render_mode == 'fill':
        lines = ascii_art_text.splitlines()
        filled_lines = []
        for line in lines:
            first_char_idx = -1
            last_char_idx = -1
            for i, char in enumerate(line):
                if char != ' ':
                    if first_char_idx == -1:
                        first_char_idx = i
                    last_char_idx = i
            
            if first_char_idx == -1: 
                filled_lines.append(line)
                continue

            filled_line = list(line)
            for i in range(first_char_idx, last_char_idx + 1):
                if filled_line[i] == ' ':
                    filled_line[i] = '█'
            filled_lines.append(''.join(filled_line))
        return '\n'.join(filled_lines)
    else:
        raise ValueError("Invalid render_mode. Must be 'outline' or 'fill'.")

def apply_gradient_color(ascii_art_text, theme_name='rainbow', direction='horizontal'):
    """
    将渐变色彩应用到 ASCII 艺术字上。
    """
    theme = COLOR_THEMES.get(theme_name)
    if not theme:
        raise ValueError(f"Color theme '{theme_name}' not found.")

    lines = ascii_art_text.splitlines()
    colored_lines = []
    max_width = max(len(line) for line in lines)
    max_height = len(lines)

    for y, line in enumerate(lines):
        colored_line = []
        for x, char in enumerate(line):
            if char == ' ':
                colored_line.append(char)
                continue

            t = 0.0
            if direction == 'horizontal':
                t = x / (max_width - 1) if max_width > 1 else 0.0
            elif direction == 'vertical':
                t = y / (max_height - 1) if max_height > 1 else 0.0
            elif direction == 'diagonal_up':
                t = ((x + (max_height - 1 - y)) / (max_width + max_height - 2)) if (max_width + max_height - 2) > 0 else 0.0
            elif direction == 'diagonal_down':
                t = ((x + y) / (max_width + max_height - 2)) if (max_width + max_height - 2) > 0 else 0.0
            else:
                raise ValueError("Invalid gradient direction.")

            start_color_node = theme[0]
            end_color_node = theme[-1]
            for i in range(len(theme) - 1):
                if theme[i]['pos'] <= t <= theme[i+1]['pos']:
                    start_color_node = theme[i]
                    end_color_node = theme[i+1]
                    break
            
            segment_t = 0.0
            if end_color_node['pos'] != start_color_node['pos']:
                segment_t = (t - start_color_node['pos']) / (end_color_node['pos'] - start_color_node['pos'])
            
            r, g, b = lerp_color(start_color_node['color'], end_color_node['color'], segment_t)
            colored_line.append(f"{rgb_to_ansi(r, g, b)}{char}{reset_ansi()}")
        colored_lines.append(''.join(colored_line))
    return '\n'.join(colored_lines)

def animate_ascii_art(ascii_art_text, theme_name='rainbow', direction='horizontal', frames=1, delay=0.1):
    """
    生成并播放 ASCII 艺术字动画。
    """
    if frames <= 1:
        print(apply_gradient_color(ascii_art_text, theme_name, direction))
        return

    num_lines = len(ascii_art_text.splitlines())

    for i in range(frames):
        animation_progress = i / (frames - 1) if frames > 1 else 0.0

        current_theme = COLOR_THEMES.get(theme_name)
        if not current_theme:
            raise ValueError(f"Color theme '{theme_name}' not found.")

        animated_theme = []
        for node in current_theme:
            new_pos = (node['pos'] + animation_progress) % 1.0
            animated_theme.append({'pos': new_pos, 'color': node['color']})
        
        animated_theme.sort(key=lambda x: x['pos'])

        original_theme = COLOR_THEMES[theme_name]
        COLOR_THEMES[theme_name] = animated_theme
        
        colored_frame = apply_gradient_color(ascii_art_text, theme_name, direction)
        
        COLOR_THEMES[theme_name] = original_theme

        print("\033[H\033[J", end="")
        print(colored_frame)
        time.sleep(delay)



