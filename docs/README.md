# Labelme Documentation

Welcome to the enhanced labelme documentation!

## Quick Links

### Getting Started
- [README](../README.md) - Overview and installation
- [Usage Guide](USAGE_GUIDE.md) - Complete usage instructions
- [New Features](NEW_FEATURES.md) - Enhanced features in this fork

### Feature Documentation
- [Point Addition Feature](POINT_ADDITION_FEATURE.md) - Multiple point addition details
- [Documentation Index](DOCUMENTATION_INDEX.md) - All available documentation

### Development
- [Contributing Guide](../CONTRIBUTING.md) - How to contribute
- [Changelog](../CHANGELOG.md) - Version history
- [Security Policy](../SECURITY.md) - Security information

## Examples

Check the [examples directory](../examples/) for:
- Instance segmentation
- Semantic segmentation
- Bounding box detection
- Classification
- Video annotation
- Tutorial

## Support

- **Issues**: Report bugs on GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Discord**: Join our community (link in README)

## Architecture

```
labelme/
├── app.py              # Main application window
├── shape.py            # Shape operations and geometry
├── widgets/
│   ├── canvas.py      # Drawing canvas
│   └── label_dialog.py # Label input dialogs
├── utils/             # Utility functions
├── config/            # Configuration management
└── cli/               # Command-line tools
```

## Key Concepts

### Shapes
- **Polygon**: Multi-point closed shape for segmentation
- **Rectangle**: Quick bounding boxes
- **Circle**: Circular regions
- **Point**: Single point annotations
- **Line/Linestrip**: Linear annotations

### Modes
- **Create Mode**: Drawing new shapes
- **Edit Mode** (`Ctrl+Shift+V`): Modifying existing shapes
- **Select Mode**: Selecting and managing shapes

### Workflow
1. Open image or directory
2. Create shapes (polygon, rectangle, etc.)
3. Label each shape
4. Save annotations (auto-saved by default)
5. Export to desired format (VOC, COCO, etc.)

## Enhanced Features

This fork adds:
1. **Multiple Point Addition** - Add N points along edges
2. **Polygon Merge** - Merge multiple polygons intelligently
3. **Dark Mode** - Eye-friendly interface
4. **Better Defaults** - Production-ready settings
5. **Improved Shortcuts** - Non-conflicting keybindings

See [NEW_FEATURES.md](NEW_FEATURES.md) for details.
