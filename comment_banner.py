#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def make_double_line_banner(text, width=None, padding=1):
    """
    Generate a double-line Unicode banner as Python comments.

    Args:
        text (str): The text to center in the banner.
        width (int, optional): Total banner inner width including padding.
            If None, it is computed from len(text) + 2 * padding.
        padding (int, optional): Number of blank lines above and below the text.
    Returns:
        List[str]: Lines of the banner (each already prefixed with '# ').
    """
    # Determine inner width (space between the vertical bars)
    if width is None:
        inner_width = len(text) + padding * 2
    else:
        inner_width = max(width - 2, len(text) + padding * 2)

    top_border    = "# ╔" + "═" * inner_width + "╗"
    empty_line    = "# ║" + " " * inner_width + "║"
    text_line     = "# ║" + text.center(inner_width) + "║"
    bottom_border = "# ╚" + "═" * inner_width + "╝"

    banner_lines = [top_border]
    # Add padding empty lines
    for _ in range(padding):
        banner_lines.append(empty_line)
    # Add the centered text
    banner_lines.append(text_line)
    # Add padding empty lines
    for _ in range(padding):
        banner_lines.append(empty_line)
    banner_lines.append(bottom_border)

    return banner_lines


if __name__ == "__main__":
    # Example usage:
    title = input("Please enter the comment banner text: ")
    banner = make_double_line_banner(title, width=79, padding=1)
    for line in banner:
        print(line)
