# Ask a person to be your valentine with a pip3 package installation 📦

> *"A utility package for system maintenance tasks"* — or so it seems...

Are you a developer? Do you have a crush that is also a developer? Do you want to ask that person to be your valentine, but you don't have the balls to do it in person? I got you. Ask them to be your valentine by making them install this disguised pip3 package.

## What you have to trick them into doing on their pc: 

```
$ pip3 install boring-package
$ boring-package <Name of the crush>
```

<img width="685" height="797" alt="image" src="https://github.com/user-attachments/assets/3312fd37-cf72-43ed-a6e6-608fd0ee1a00" />




## Installation

### From PyPI
```bash
pip3 install boring-package
```

### From Source
```bash
git clone https://github.com/yourusername/boring-package.git
cd boring-package
pip3 install .
```

### Development
```bash
git clone https://github.com/yourusername/boring-package.git
cd boring-package
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Usage

```bash
# Basic usage with personalized name
boring-package <name>

# Examples
boring-package Emily
boring-package "My Love"
```

**Pro tip**: Make sure the terminal is fullscreen for the best experience!

## How It Works

### Architecture

```
boring-package/
├── setup.py                 # Package configuration & entry points
├── valentines_surprise/
│   └── __init__.py          # Core animation engine
└── dist/                    # Built distribution files
```

### Animation Pipeline

1. **Fullscreen Warning** → Block-letter ASCII text with countdown timer
2. **Matrix Rain** → Procedurally generated falling character animation
3. **Story Sequence** → Screen-clearing message reveal with timing
4. **Staggered Reveal** → Name → Heart → Question appear sequentially
5. **3D Heart Loop** → Continuous rotation with beating effect

### 3D Heart Rendering

The heart animation uses parametric equations and rotation matrices:

```python
# Heart surface equation
z = -x² - (1.2y - |x|^(2/3))² + r²

# 3D rotation transformation
nx = x * cos(t) - z * sin(t)
nz = x * sin(t) + z * cos(t)

# Perspective projection
p = 1 + nz / 2
screen_x = (nx * p + 0.5) * width
screen_y = (-y * p + 0.5) * height
```

The depth buffer maps z-coordinates to ASCII characters for shading:
```
" .,-~:;=!*#$@@"  →  (dark to bright)
```

## Configuration

The animation parameters can be modified in `__init__.py`:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `max_frames` | 10000 | Heart animation duration (~10 seconds) |
| `t += 0.012` | 0.012 | Rotation speed |
| `time.sleep(0.001)` | 0.001 | Frame delay (smoothness) |
| `time.sleep(2.2)` | 2.2 | Message display duration |

## Requirements

- Python 3.7+
- Terminal with ANSI escape code support
- Recommended: 100+ column terminal width

## Building & Distribution

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Upload to PyPI
twine upload dist/*
```

## Contributing

Contributions are welcome! Feel free to:

- Add new animation effects
- Support additional character sets
- Improve cross-platform compatibility
- Add localization for messages

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Inspired by classic ASCII art demos and the demoscene
- 3D heart algorithm adapted from mathematical parametric surfaces
- Built with love (and Python) 💝

---

<p align="center">
  <i>Because sometimes the best code comes from the heart.</i>
</p>
# Ask-a-girl-out-with-a-pip3-package-
