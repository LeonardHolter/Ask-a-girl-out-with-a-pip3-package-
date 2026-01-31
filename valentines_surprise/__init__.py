"""
A sweet Valentine's Day surprise package 💝
"""

import time
import os
import sys
import math
import random

__version__ = "1.0.0"


def text_to_ascii(text):
    """Convert text to 4-line ASCII block letters"""
    chars = {
        'A': [" ███  ", "█   █ ", "█████ ", "█   █ "],
        'B': ["████  ", "█   █ ", "████  ", "█████ "],
        'C': [" ████ ", "█     ", "█     ", " ████ "],
        'D': ["████  ", "█   █ ", "█   █ ", "████  "],
        'E': ["█████ ", "██    ", "█     ", "█████ "],
        'F': ["█████ ", "██    ", "█     ", "█     "],
        'G': [" ████ ", "█     ", "█  ██ ", " ████ "],
        'H': ["█   █ ", "█████ ", "█   █ ", "█   █ "],
        'I': ["█████ ", "  █   ", "  █   ", "█████ "],
        'J': ["█████ ", "   █  ", "   █  ", "███   "],
        'K': ["█  █  ", "███   ", "█ █   ", "█  █  "],
        'L': ["█     ", "█     ", "█     ", "█████ "],
        'M': ["█   █ ", "██ ██ ", "█ █ █ ", "█   █ "],
        'N': ["█   █ ", "██  █ ", "█ █ █ ", "█  ██ "],
        'O': [" ███  ", "█   █ ", "█   █ ", " ███  "],
        'P': ["████  ", "█   █ ", "████  ", "█     "],
        'Q': [" ███  ", "█   █ ", "█  █  ", " ██ █ "],
        'R': ["████  ", "█   █ ", "████  ", "█  █  "],
        'S': [" ████ ", "██    ", "   ██ ", "████  "],
        'T': ["█████ ", "  █   ", "  █   ", "  █   "],
        'U': ["█   █ ", "█   █ ", "█   █ ", " ███  "],
        'V': ["█   █ ", "█   █ ", " █ █  ", "  █   "],
        'W': ["█   █ ", "█ █ █ ", "█ █ █ ", " █ █  "],
        'X': ["█   █ ", " █ █  ", " █ █  ", "█   █ "],
        'Y': ["█   █ ", " █ █  ", "  █   ", "  █   "],
        'Z': ["█████ ", "  █   ", " █    ", "█████ "],
        ' ': ["   ", "   ", "   ", "   "],
        '0': [" ███  ", "█   █ ", "█   █ ", " ███  "],
        '1': ["  █   ", " ██   ", "  █   ", " ███  "],
        '2': [" ███  ", "   █  ", "  █   ", " ████ "],
        '3': [" ███  ", "  ██  ", "   █  ", " ███  "],
        '4': ["█  █  ", "█  █  ", "█████ ", "   █  "],
        '5': ["█████ ", "███   ", "   ██ ", "███   "],
        '6': [" ███  ", "█     ", "████  ", " ███  "],
        '7': ["█████ ", "   █  ", "  █   ", " █    "],
        '8': [" ███  ", " ███  ", "█   █ ", " ███  "],
        '9': [" ███  ", "█   █ ", " ████ ", "  █   "],
    }
    lines = ["", "", "", ""]
    for char in text.upper():
        if char in chars:
            for i in range(4):
                lines[i] += chars[char][i]
        else:
            for i in range(4):
                lines[i] += "      "
    return lines


def show_message(name=None):
    """Display the Valentine's message"""
    
    # === FULLSCREEN WARNING WITH COUNTDOWN ===
    print("\033[2J\033[H", end="", flush=True)  # Clear screen
    print("\n" * 6)
    
    # Display "MAKE TERMINAL" in big text
    warning1 = text_to_ascii("make terminal")
    for line in warning1:
        line_spaces = 50 - len(line) // 2
        print(" " * max(0, line_spaces) + line)
    
    print()  # Small gap
    
    # Display "FULLSCREEN" in big text
    warning2 = text_to_ascii("fullscreen")
    for line in warning2:
        line_spaces = 50 - len(line) // 2
        print(" " * max(0, line_spaces) + line)
    
    print("\n\n\n\n")  # Space for countdown
    
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        # Move cursor up 4 lines to overwrite countdown
        print("\033[4A", end="", flush=True)
        countdown_lines = text_to_ascii(str(i))
        for line in countdown_lines:
            line_spaces = 50 - len(line) // 2
            # Clear the line and print centered
            print("\033[K" + " " * max(0, line_spaces) + line)
        time.sleep(1)
    
    # === FALLING CHARACTERS RESET ANIMATION ===
    print("\033[2J\033[H", end="", flush=True)  # Clear screen
    print("\x1b[?25l", end='')  # Hide cursor
    
    width = 100
    height = 35
    chars = "█▓▒░♥❤💕✨⭐🌟!@#$%^&*(){}[]|;:<>?/~`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Initialize columns - each has a "head" position that falls
    columns = []
    for x in range(width):
        columns.append({
            'y': random.randint(-height, 0),  # Start position (negative = hasn't appeared yet)
            'speed': random.randint(1, 3),     # Fall speed
            'length': random.randint(5, 15),   # Trail length
            'delay': random.randint(0, 20)     # Start delay
        })
    
    # Screen buffer
    screen = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Run animation for ~2 seconds
    for frame in range(60):
        # Update each column
        for x, col in enumerate(columns):
            if col['delay'] > 0:
                col['delay'] -= 1
                continue
            
            # Move head down
            col['y'] += col['speed']
            
            # Draw the falling trail
            for trail in range(col['length']):
                y = col['y'] - trail
                if 0 <= y < height:
                    if trail == 0:
                        # Head of the trail - bright character
                        screen[y][x] = random.choice(chars)
                    elif trail < 3:
                        # Near head - still visible
                        screen[y][x] = random.choice("█▓▒")
                    else:
                        # Fading trail
                        screen[y][x] = random.choice("░·.")
            
            # Clear behind the trail
            clear_y = col['y'] - col['length']
            if 0 <= clear_y < height:
                screen[clear_y][x] = ' '
            
            # Reset column when it goes off screen
            if col['y'] - col['length'] > height:
                col['y'] = random.randint(-10, -1)
                col['speed'] = random.randint(1, 3)
                col['length'] = random.randint(5, 15)
        
        # Render screen
        print("\x1b[H", end='')
        for row in screen:
            print(''.join(row))
        
        time.sleep(0.033)  # ~30 FPS
    
    # Final clear with fade effect - fill screen then clear
    for fade in range(3):
        print("\x1b[H", end='')
        for y in range(height):
            print(''.join(random.choice("░▒▓█") if random.random() > fade * 0.3 else ' ' for _ in range(width)))
        time.sleep(0.1)
    
    print("\x1b[?25h", end='')  # Show cursor
    print("\033[2J\033[H", end="", flush=True)  # Final clear
    time.sleep(0.3)
    
    # Series of messages with screen clears
    messages = [
        "You are probably",
        "wondering why I made",
        "you install this package",
        "the reason",
        "is because I wanted to ask you",
        "a question",
        "the problem is that",
        "I do not have the balls",
        "to say it in person",
        "so i programmed it"
    ]
    
    for msg in messages:
        print("\033[2J\033[H", end="", flush=True)  # Clear screen
        print("\n" * 8)  # Vertical centering
        lines = text_to_ascii(msg)
        for line in lines:
            line_spaces = 50 - len(line) // 2  # Center at column 50
            print(" " * max(0, line_spaces) + line)
        time.sleep(2.2)  # Pause between messages
    
    # Final clear before animation
    print("\033[2J\033[H", end="", flush=True)
    time.sleep(0.5)
    
    # 3D Spinning and Beating Heart Animation (runs for 10 seconds)
    # Using EXACT code from spinning_heart.py
    print("\x1b[?25l", end='')  # Hide cursor
    zb = [0.0] * 100 * 40
    
    t = 0.0
    frames = 0
    max_frames = 10000  # About 10 seconds (10000 frames * 0.001s each)
    
    # Helper function to generate name display lines
    def get_name_lines(name):
        name_display = name.upper()
        line1 = ""
        line2 = ""
        line3 = ""
        for char in name_display:
            if char == 'E':
                line1 += "███████ "; line2 += "█████   "; line3 += "███████ "
            elif char == 'M':
                line1 += "█     █ "; line2 += "███ ███ "; line3 += "█  █  █ "
            elif char == 'I':
                line1 += "███████ "; line2 += "   █    "; line3 += "███████ "
            elif char == 'L':
                line1 += "█       "; line2 += "█       "; line3 += "███████ "
            elif char == 'Y':
                line1 += "█     █ "; line2 += " █   █  "; line3 += "   █    "
            elif char == 'A':
                line1 += "  ███   "; line2 += " █████  "; line3 += "█     █ "
            elif char == 'O':
                line1 += " █████  "; line2 += "█     █ "; line3 += " █████  "
            elif char == 'N':
                line1 += "█     █ "; line2 += "███   █ "; line3 += "█    ██ "
            elif char == 'S':
                line1 += " █████  "; line2 += " ████   "; line3 += " █████  "
            elif char == 'T':
                line1 += "███████ "; line2 += "   █    "; line3 += "   █    "
            elif char == 'R':
                line1 += "██████  "; line2 += "██████  "; line3 += "█   █   "
            elif char == 'D':
                line1 += "██████  "; line2 += "█     █ "; line3 += "██████  "
            elif char == ' ':
                line1 += "  "; line2 += "  "; line3 += "  "
            else:
                line1 += "█████   "; line2 += "█   █   "; line3 += "█████   "
        return line1, line2, line3
    
    # Helper function to generate one static heart frame
    def generate_heart_frame(t_val, zb_arr):
        maxz, c, s = 0, math.cos(t_val), math.sin(t_val)
        y = -0.5
        while y <= 0.5:
            r = 0.4 + 0.05 * math.pow(0.5 + 0.5 * math.sin(t_val * 6 + y * 2), 8)
            x = -0.5
            while x <= 0.5:
                z = -x * x - math.pow(1.2 * y - abs(x) * 2 / 3, 2) + r * r
                if z >= 0:
                    z = math.sqrt(z) / (2 - y)
                    tz = -z
                    while tz <= z:
                        nx = x * c - tz * s
                        nz = x * s + tz * c
                        p = 1 + nz / 2
                        vx = round((nx * p + 0.5) * 80 + 10)
                        vy = round((-y * p + 0.5) * 39 + 2)
                        idx = vx + vy * 100
                        if zb_arr[idx] <= nz:
                            zb_arr[idx] = nz
                            if maxz < nz:
                                maxz = nz
                        tz += z / 6
                x += 0.01
            y += 0.01
        return maxz
    
    # === STAGGERED INTRO SEQUENCE ===
    if name:
        # Step 1: Show name only
        print("\x1b[H", end='')
        print("\n" * 2)
        line1, line2, line3 = get_name_lines(name)
        for line in [line1, line2, line3]:
            line_spaces = 50 - len(line) // 2
            print(" " * line_spaces + line)
        time.sleep(1)
        
        # Step 2: Show name + heart
        maxz = generate_heart_frame(0, zb)
        print("\x1b[H", end='')
        print("\n" * 2)
        for line in [line1, line2, line3]:
            line_spaces = 50 - len(line) // 2
            print(" " * line_spaces + line)
        print("\n" * 2)
        for i in range(100 * 40):
            print(i % 100 and " .,-~:;=!*#$@@"[round(zb[i] / maxz * 13)] or "\n", end='')
        # Reset zb for animation
        for i in range(100 * 40):
            zb[i] = 0
        time.sleep(1)
        
        # Step 3: Show name + heart + question
        maxz = generate_heart_frame(0, zb)
        print("\x1b[H", end='')
        print("\n" * 2)
        for line in [line1, line2, line3]:
            line_spaces = 50 - len(line) // 2
            print(" " * line_spaces + line)
        print("\n" * 2)
        for i in range(100 * 40):
            print(i % 100 and " .,-~:;=!*#$@@"[round(zb[i] / maxz * 13)] or "\n", end='')
            zb[i] = 0
        print("\n" * 2)
        question = "Will you be my valentine? 👉👈🥺"
        question_spaces = 50 - len(question) // 2
        print(" " * question_spaces + question)
        time.sleep(1)
    
    # === START SPINNING ANIMATION ===
    while frames < max_frames:
        maxz, c, s = 0, math.cos(t), math.sin(t)
        y = -0.5
        while y <= 0.5:
            # Add beating effect
            r = 0.4 + 0.05 * math.pow(0.5 + 0.5 * math.sin(t * 6 + y * 2), 8)
            x = -0.5
            while x <= 0.5:
                # heart formula
                z = -x * x - math.pow(1.2 * y - abs(x) * 2 / 3, 2) + r * r
                if z >= 0:
                    z = math.sqrt(z) / (2 - y)
                    tz = -z
                    while tz <= z:
                        # Rotate
                        nx = x * c - tz * s
                        nz = x * s + tz * c
                        
                        # Add perspective
                        p = 1 + nz / 2
                        vx = round((nx * p + 0.5) * 80 + 10)
                        vy = round((-y * p + 0.5) * 39 + 2)
                        idx = vx + vy * 100
                        if zb[idx] <= nz:
                            zb[idx] = nz
                            if maxz < nz:
                                maxz = nz
                        tz += z / 6
                x += 0.01
            y += 0.01
        
        print("\x1b[H", end='')
        
        # Add spacing from top and display name centered over heart
        # Heart center is at column 50 (based on vx calculation: (0 + 0.5) * 80 + 10 = 50)
        if name:
            print("\n" * 2)
            name_display = name.upper()
            
            # Create bigger ASCII letters (3 lines tall)
            line1 = ""
            line2 = ""
            line3 = ""
            
            for char in name_display:
                if char == 'E':
                    line1 += "███████ "
                    line2 += "█████   "
                    line3 += "███████ "
                elif char == 'M':
                    line1 += "█     █ "
                    line2 += "███ ███ "
                    line3 += "█  █  █ "
                elif char == 'I':
                    line1 += "███████ "
                    line2 += "   █    "
                    line3 += "███████ "
                elif char == 'L':
                    line1 += "█       "
                    line2 += "█       "
                    line3 += "███████ "
                elif char == 'Y':
                    line1 += "█     █ "
                    line2 += " █   █  "
                    line3 += "   █    "
                elif char == 'A':
                    line1 += "  ███   "
                    line2 += " █████  "
                    line3 += "█     █ "
                elif char == 'O':
                    line1 += " █████  "
                    line2 += "█     █ "
                    line3 += " █████  "
                elif char == 'N':
                    line1 += "█     █ "
                    line2 += "███   █ "
                    line3 += "█    ██ "
                elif char == 'S':
                    line1 += " █████  "
                    line2 += " ████   "
                    line3 += " █████  "
                elif char == 'T':
                    line1 += "███████ "
                    line2 += "   █    "
                    line3 += "   █    "
                elif char == 'R':
                    line1 += "██████  "
                    line2 += "██████  "
                    line3 += "█   █   "
                elif char == ' ':
                    line1 += "  "
                    line2 += "  "
                    line3 += "  "
                else:
                    line1 += "█████   "
                    line2 += "█   █   "
                    line3 += "█████   "
            
            # Center each line at column 50
            for line in [line1, line2, line3]:
                line_spaces = 50 - len(line) // 2
                print(" " * line_spaces + line)
            
            print("\n" * 2)  # Reduced spacing before heart
        else:
            print("\n" * 12)
        
        for i in range(100 * 40):
            print(i % 100 and " .,-~:;=!*#$@@"[round(zb[i] / maxz * 13)] or "\n", end='')
            zb[i] = 0
        
        # Add the question at the bottom - also centered at column 50
        if name:
            print("\n" * 2)
            question = "Will you be my valentine? 👉👈🥺"
            question_spaces = 50 - len(question) // 2
            print(" " * question_spaces + question)
        
        t += 0.012  # Much faster spinning (4x original speed)
        frames += 1
        time.sleep(0.001)  # Smoother animation with shorter delay
    
    print("\x1b[?25h", end='')  # Show cursor again
    
    print("\n\n")
    # Center the question
    question = "Will you be my valentine? 👉👈🥺"
    spaces = (80 - len(question)) // 2
    print(" " * spaces + question)
    print("\n\n\n")


def main():
    """Command-line entry point"""
    # Get name from command line arguments
    name = None
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
    
    show_message(name)


# Don't auto-run on import - only run via command line or explicit call
