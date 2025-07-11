
def lerp_color(color1, color2, t):
    """
    在两个 RGB 颜色之间进行线性插值。
    color1, color2: (R, G, B) 元组。
    t: 0.0 到 1.0 之间的浮点数。
    """
    r = int(color1[0] + (color2[0] - color1[0]) * t)
    g = int(color1[1] + (color2[1] - color1[1]) * t)
    b = int(color1[2] + (color2[2] - color1[2]) * t)
    return (r, g, b)

def rgb_to_ansi(r, g, b, background=False):
    """
    将 RGB 颜色转换为 ANSI 24 位真彩色转义码。
    """
    if background:
        return f"\033[48;2;{r};{g};{b}m"
    else:
        return f"\033[38;2;{r};{g};{b}m"

def reset_ansi():
    """
    返回重置终端颜色的 ANSI 转义码。
    """
    return "\033[0m"



