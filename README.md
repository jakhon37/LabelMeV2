# labelme - Enhanced Edition

<div align="center">
  <img src="labelme/icons/icon-256.png" width="200" height="200">
  
  ### Image Annotation Tool with Advanced Polygon Editing
  
  [![PyPI](https://img.shields.io/pypi/v/labelme.svg)](https://pypi.python.org/pypi/labelme)
  [![CI](https://github.com/wkentaro/labelme/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/wkentaro/labelme/actions)
  [![Python Version](https://img.shields.io/pypi/pyversions/labelme.svg)](https://pypi.org/project/labelme/)
  [![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
  [![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](LICENSE)
  [![Tests](https://img.shields.io/badge/tests-38%20passed-brightgreen.svg)]()
  
  **Enhanced fork of [wkentaro/labelme](https://github.com/wkentaro/labelme) with productivity features**
</div>

---

## 🎯 What's New in This Fork

This enhanced version adds powerful polygon editing features and improved defaults to speed up your annotation workflow:

### ✨ New Features

#### 1. **Multiple Point Addition** (`Ctrl+M`)
Quickly refine polygon boundaries by adding multiple evenly-spaced points along edges.

- Hover over any polygon edge in edit mode
- Press `Ctrl+M` and enter number of points (1-100)
- Points are automatically distributed evenly
- Perfect for curved edges or complex boundaries

**Example:** Add 10 points to a curved car windshield edge in one action instead of clicking 10 times.

#### 2. **Polygon Merge** (`Ctrl+Shift+M`)
Merge multiple polygons into one or batch-apply labels to disconnected objects.

- Select 2+ polygons (hold `Ctrl` while clicking)
- Press `Ctrl+Shift+M` to merge
- Smart handling:
  - **Connected/overlapping** → Single merged polygon
  - **Disconnected objects** → Multiple polygons with same label
  - **Mixed** → Intelligent separation based on connectivity

**Example:** Annotate 20 cars by drawing rough boxes, select all, merge once - all labeled "car" instantly.

#### 3. **Dark Mode** (View → Dark Mode)
Eye-friendly dark theme inspired by VS Code.

- Toggle instantly via View menu
- Persistent setting saved in config
- Reduces eye strain during long sessions
- Professional color scheme

#### 4. **Improved Default Settings**
Better defaults for faster annotation workflow:

| Setting | Old Default | New Default | Why? |
|---------|-------------|-------------|------|
| `auto_save` | `false` | `true` | Never lose work |
| `store_data` | `true` | `false` | Smaller JSON files |
| `keep_prev_brightness_contrast` | `false` | `true` | Consistent visuals |
| `dark_mode` | N/A | `true` | Eye comfort |
| `canvas.fill_drawing` | `true` | `false` | See through shapes |
| `canvas.num_backups` | 10 | 20 | More undo history |

#### 5. **Better Keyboard Shortcuts**
More intuitive shortcuts that don't conflict:

| Action | Old Shortcut | New Shortcut |
|--------|--------------|--------------|
| Create Polygon | `Ctrl+N` | `Ctrl+Shift+C` |
| Create Rectangle | `Ctrl+R` | `Ctrl+Shift+X` |
| Edit Polygon | `Ctrl+J` | `Ctrl+Shift+V` |

---

## 📦 Installation

```bash
# Clone this enhanced version
git clone https://github.com/YOUR_USERNAME/labelme.git
cd labelme

# Install with pip
pip install -e .

# Or use uv (faster)
uv pip install -e .
```

---

## 🚀 Quick Start

```bash
# Launch labelme
labelme

# Enable dark mode (if not already on)
View → Dark Mode

# Try the new features:
# 1. Draw a polygon
# 2. Press Ctrl+Shift+V to enter edit mode
# 3. Hover over an edge and press Ctrl+M
# 4. Enter "5" to add 5 points
# 5. Adjust the points as needed
```

### New Feature Quick Reference

| Feature | Shortcut | Usage |
|---------|----------|-------|
| **Add Multiple Points** | `Ctrl+M` | Edit mode → Hover edge → Ctrl+M → Enter count |
| **Merge Polygons** | `Ctrl+Shift+M` | Select multiple → Ctrl+Shift+M |
| **Dark Mode** | View menu | View → Dark Mode (toggles instantly) |
| **Edit Mode** | `Ctrl+Shift+V` | Enter polygon editing mode |

---

## 📚 Documentation

- **New Features Guide**: [docs/NEW_FEATURES.md](docs/NEW_FEATURES.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Original Documentation**: See [wkentaro/labelme](https://github.com/wkentaro/labelme) for:
  - Basic usage and examples
  - Export formats (VOC, COCO)
  - AI-assisted annotation
  - Command-line tools
  - Video annotation
  - Classification/segmentation workflows

---

## 🎬 Examples

### Polygon Refinement Workflow
```
1. Draw rough polygon around object
2. Ctrl+Shift+V (edit mode)
3. Hover over curved edge
4. Ctrl+M → Enter "8" → OK
5. Adjust 8 new points to match boundary perfectly
```

### Batch Labeling Workflow
```
1. Draw boxes around 15 cars (quick rough boxes)
2. Ctrl+Click each box to select all
3. Ctrl+Shift+M (merge)
4. Result: 15 separate polygons all labeled "car"
```

---

## 🔧 Configuration

Enhanced defaults in `~/.labelmerc`:

```yaml
# New/modified defaults
auto_save: true
dark_mode: true
store_data: false
keep_prev_brightness_contrast: true

# New features config
default_num_points_to_add: 1

shortcuts:
  add_multiple_points: Ctrl+M
  merge_polygons: Ctrl+Shift+M
  create_polygon: Ctrl+Shift+C
  create_rectangle: Ctrl+Shift+X
  edit_polygon: Ctrl+Shift+V
```

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Development setup
- Code style guidelines
- Testing procedures
- Feature implementation details

---

## 📄 License

GPL-3.0-only - Same as original [wkentaro/labelme](https://github.com/wkentaro/labelme)

---

## 🙏 Acknowledgments

This is an enhanced fork of [wkentaro/labelme](https://github.com/wkentaro/labelme) by Kentaro Wada.

**Original repo**: <https://github.com/wkentaro/labelme>  
**Original author**: [Kentaro Wada](https://github.com/wkentaro)

New features in this fork:
- Multiple point addition
- Polygon merge
- Dark mode
- Improved defaults
- Better keyboard shortcuts

---

## ⭐ Star History

If you find these enhancements useful, please star this repo!

For the original labelme and its extensive documentation, visit the [official repository](https://github.com/wkentaro/labelme).
