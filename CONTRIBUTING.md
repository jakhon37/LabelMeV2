# Contributing to Labelme

Thank you for your interest in contributing to labelme! This document provides guidelines and information for contributors.

## 🎯 New Features in This Version

This fork includes two major polygon editing enhancements:

### 1. Multiple Point Addition (`Ctrl+M`)

**Purpose**: Efficiently add multiple evenly-spaced points to polygon edges for detailed boundary refinement.

**Implementation**:
- **Files**: `labelme/shape.py`, `labelme/widgets/canvas.py`, `labelme/app.py`
- **Algorithm**: Linear interpolation between edge vertices
- **Config**: `default_num_points_to_add` in `default_config.yaml`

**Usage**:
```
1. Enter edit mode (Ctrl+J)
2. Hover over polygon edge (will highlight)
3. Press Ctrl+M
4. Enter number of points (1-100)
5. Points are distributed evenly along edge
```

**Use Cases**:
- Refining curved boundaries (add 5-10 points then adjust)
- Creating smooth transitions
- Adding detail to coarse annotations

### 2. Polygon Merge (`Ctrl+Shift+M`)

**Purpose**: Merge multiple polygons using geometric union operations with intelligent handling of connected/disconnected regions.

**Implementation**:
- **Files**: `labelme/shape.py`, `labelme/widgets/canvas.py`, `labelme/app.py`
- **Algorithm**: Shapely's `unary_union()` with automatic MultiPolygon handling
- **Behavior**: 
  - Adjacent/overlapping polygons → Single merged polygon
  - Disconnected polygons → Multiple separate polygons (ALL preserved with same label)
  - Mixed scenarios → Multiple polygons based on connectivity

**Usage**:
```
1. Enter edit mode (Ctrl+J)
2. Select 2+ polygons (Ctrl+Click each)
3. Press Ctrl+Shift+M
4. Polygons merge with label from first selected
```

**Use Cases**:
- Combining over-segmented regions
- Batch labeling multiple objects with same label
- Fixing annotation boundaries
- Merging adjacent annotations

**Smart Handling Example**:
```
Input: [Box A][Box B]  [Box C]  (A&B touching, C separate)
Output: [  A+B  ]      [  C  ]  (2 polygons, both labeled same)
Info: "Merged 3 polygons into 2 disconnected polygons"
```

## 🏗️ Architecture

### Key Components

```
labelme/
├── app.py                 # Main application window & UI actions
├── shape.py              # Shape class with geometry operations
├── widgets/
│   ├── canvas.py         # Drawing canvas & interaction
│   └── label_dialog.py   # Label input dialogs
├── utils/
│   ├── shape.py          # Shape utility functions
│   └── image.py          # Image processing utilities
└── config/
    └── default_config.yaml  # Default configuration
```

### Adding New Features

#### 1. Shape Operations

Add methods to `Shape` class in `labelme/shape.py`:

```python
class Shape:
    def yourNewMethod(self, params):
        """
        Your implementation
        """
        # Modify self.points
        # Return result if needed
```

#### 2. Canvas Interactions

Add methods to `Canvas` class in `labelme/widgets/canvas.py`:

```python
class Canvas:
    def yourCanvasMethod(self):
        if self.hShape:  # Currently highlighted shape
            # Process shape
            self.update()
```

#### 3. UI Actions

Add actions in `MainWindow` class in `labelme/app.py`:

```python
# In __init__:
action = functools.partial(newAction, ...)
self.actions.yourAction = action(
    self, "Action Name", self.yourHandler,
    "Ctrl+K", "icon.svg", "Tooltip"
)
self.menus.edit.addAction(self.actions.yourAction)

def yourHandler(self):
    # Implementation
    self.canvas.yourCanvasMethod()
    self.setDirty()
```

#### 4. Configuration

Add settings to `labelme/config/default_config.yaml`:

```yaml
your_setting: default_value

shortcuts:
  your_action: Ctrl+K
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/shape_test.py

# Run with coverage
pytest --cov=labelme

# Run GUI tests
pytest -m gui
```

### Writing Tests

Create test files in `tests/unit/` or `tests/e2e/`:

```python
import pytest
from labelme.shape import Shape

def test_your_feature():
    shape = Shape("polygon")
    shape.addPoint(QtCore.QPointF(0, 0))
    shape.addPoint(QtCore.QPointF(10, 0))
    shape.addPoint(QtCore.QPointF(10, 10))
    
    # Test your feature
    result = shape.yourMethod()
    assert result == expected_value
```

### Manual Testing

```bash
# Install in development mode
pip install -e .

# Run labelme
labelme

# Test with sample data
cd examples/instance_segmentation
labelme data_annotated/
```

## 📝 Code Style

This project uses:
- **Linter**: `ruff` for code quality
- **Formatter**: `ruff format` for consistent style
- **Type hints**: Python type annotations where applicable

```bash
# Format code
ruff format .

# Check linting
ruff check .

# Auto-fix issues
ruff check --fix .
```

### Style Guidelines

- Use descriptive variable names
- Add docstrings to public methods
- Keep methods focused (single responsibility)
- Use type hints for function parameters
- Follow Qt naming conventions for UI elements

## 🔍 Debugging

### Enable Debug Logging

Edit `~/.labelmerc`:

```yaml
logger_level: debug
```

### Console Output

```bash
# Run with verbose output
labelme --logger-level debug

# Check Python errors
python -c "import labelme; labelme.main()"
```

### Qt Debugging

```python
# In your code:
from loguru import logger

logger.debug(f"Value: {your_variable}")
logger.info("Important event")
logger.warning("Something unexpected")
logger.error("Error occurred")
```

## 📚 Documentation

### Code Documentation

- Add docstrings to all public methods
- Use Google-style docstrings:

```python
def mergeShapes(shapes: list["Shape"]) -> list["Shape"] | None:
    """Merge multiple shapes using geometric union.
    
    Args:
        shapes: List of Shape objects to merge
        
    Returns:
        List of merged Shape objects, or None if merge fails
        
    Example:
        >>> merged = Shape.mergeShapes([shape1, shape2])
    """
```

### User Documentation

- Update README.md for major features
- Add examples to `examples/` directory
- Create detailed guides in separate .md files
- Update QUICK_START.md for new shortcuts

## 🐛 Bug Reports

When reporting bugs, include:

1. **Environment**: OS, Python version, labelme version
2. **Steps to reproduce**: Exact steps to trigger the bug
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Screenshots**: If applicable
6. **Error messages**: Full error traceback

## 💡 Feature Requests

When requesting features:

1. **Use case**: Describe the problem you're solving
2. **Proposed solution**: How should it work?
3. **Alternatives**: Other ways you've considered
4. **Examples**: Screenshots or mockups if applicable

## 📋 Pull Request Process

1. **Fork & Branch**
   ```bash
   git clone https://github.com/YOUR_USERNAME/labelme.git
   git checkout -b feature/your-feature-name
   ```

2. **Develop & Test**
   ```bash
   pip install -e .
   # Make changes
   pytest
   ruff check .
   ```

3. **Commit**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```
   
   Use conventional commits:
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation
   - `refactor:` Code refactoring
   - `test:` Adding tests
   - `chore:` Maintenance

4. **Push & PR**
   ```bash
   git push origin feature/your-feature-name
   # Create PR on GitHub
   ```

5. **PR Checklist**
   - [ ] Tests pass (`pytest`)
   - [ ] Code formatted (`ruff format`)
   - [ ] No linting errors (`ruff check`)
   - [ ] Documentation updated
   - [ ] CHANGELOG.md updated (if applicable)
   - [ ] Clear commit messages

## 🌍 Internationalization

### Adding Translations

1. Edit translation files in `labelme/translate/`:
   ```
   labelme/translate/
   ├── ja_JP.ts   # Japanese
   ├── zh_CN.ts   # Simplified Chinese
   └── ...
   ```

2. Compile translations:
   ```bash
   python tools/update_translate.py
   ```

3. Test:
   ```bash
   LANG=ja_JP.UTF-8 labelme
   ```

## 🔗 Useful Resources

- **Qt Documentation**: https://doc.qt.io/qt-5/
- **Shapely Docs**: https://shapely.readthedocs.io/
- **labelme.io**: https://www.labelme.io/

## 📞 Getting Help

- **Discord**: https://discord.com/invite/uAjxGcJm83
- **Issues**: https://github.com/wkentaro/labelme/issues
- **Discussions**: https://github.com/wkentaro/labelme/discussions

## 🎓 Learning Path

1. **Start Simple**: Fix typos, update docs
2. **Small Features**: Add shortcuts, UI improvements
3. **Medium Features**: New shape types, export formats
4. **Complex Features**: AI integration, geometric operations

## ⚖️ License

By contributing, you agree that your contributions will be licensed under the GPLv3 License.

---

**Thank you for contributing to labelme!** 🎉
