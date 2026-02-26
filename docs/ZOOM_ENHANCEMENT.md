# Enhanced Zoom Capabilities for Tiny Defect Annotation

## Problem
Users needed to annotate tiny defects but the zoom was limited to 1000% (10x magnification), making it difficult to see and accurately annotate microscopic details.

## Solution
Enhanced zoom capabilities with the following improvements:

### 1. Increased Maximum Zoom
- **Before**: 1000% (10x magnification)
- **After**: 5000% (50x magnification) - configurable
- **Benefit**: 5x more zoom capability for annotating tiny defects

### 2. Configurable Zoom Settings
Added two new configuration options in `default_config.yaml`:

```yaml
# Zoom settings for better control
zoom_increment: 1.1  # Multiplier for zoom in/out (1.1 = 10% steps)
max_zoom: 5000       # Maximum zoom percentage (5000% = 50x)
```

#### `zoom_increment`
- Controls how much the zoom changes with each mouse wheel scroll or keyboard shortcut
- Default: 1.1 (10% steps)
- Smaller values (e.g., 1.05) = finer control, more steps needed
- Larger values (e.g., 1.2) = coarser control, fewer steps needed

#### `max_zoom`
- Maximum zoom level in percentage
- Default: 5000 (50x magnification)
- Can be increased even further if needed for extreme microscopy
- Can be decreased to save memory on lower-end systems

### 3. Smoother Zoom Control
- Mouse wheel zoom now uses configurable increment
- More predictable zoom behavior
- Better control when zooming in/out at high magnification levels

## Usage

### Mouse Wheel Zoom
1. **Hover** over the area you want to examine
2. **Scroll** the mouse wheel up to zoom in
3. The view will zoom centered on your cursor position
4. Continue scrolling to reach up to 5000% zoom

### Keyboard Shortcuts
- **Zoom In**: `Ctrl+` or `Ctrl+=`
- **Zoom Out**: `Ctrl+-`
- **Reset to 100%**: `Ctrl+0`
- **Fit to Window**: `Ctrl+F`
- **Fit Width**: `Ctrl+Shift+F`

### Manual Zoom Entry
1. Click on the zoom percentage box (bottom of window)
2. Type any value from 1% to 5000%
3. Press Enter

### Custom Configuration
To customize zoom behavior, edit `~/.labelmerc`:

```yaml
# For even higher zoom (e.g., electron microscopy)
max_zoom: 10000  # 100x magnification

# For finer zoom control
zoom_increment: 1.05  # 5% steps instead of 10%

# For faster zoom
zoom_increment: 1.25  # 25% steps
```

## Use Cases

### Tiny Defect Inspection
- **PCB defects**: Solder bridges, hairline cracks
- **Surface inspection**: Scratches, pits, discoloration
- **Microscopy**: Cellular structures, tissue samples
- **Material science**: Crystal structures, grain boundaries

### Best Practices

1. **Start Wide, Then Zoom**
   - First annotate at normal zoom (100-200%)
   - Then zoom in to refine boundaries
   - Use high zoom for final precision

2. **Use Cursor-Centered Zoom**
   - Position cursor on detail you want to examine
   - Scroll to zoom - it will center on cursor
   - Much faster than zoom + pan

3. **Adjust Zoom Increment for Task**
   - Fine work: Use 1.05 (many small steps)
   - General work: Use 1.1 (default)
   - Quick navigation: Use 1.25 (fewer large steps)

4. **Memory Considerations**
   - Very high zoom on large images uses more memory
   - If experiencing slowness, reduce `max_zoom`
   - Close other applications when working at extreme zoom

## Technical Details

### Files Modified
- `labelme/widgets/zoom_widget.py`: Made max zoom configurable
- `labelme/app.py`: Use config for zoom increment and max zoom
- `labelme/config/default_config.yaml`: Added zoom configuration

### Implementation
```python
# ZoomWidget now accepts max_zoom parameter
class ZoomWidget(QtWidgets.QSpinBox):
    def __init__(self, value=100, max_zoom=5000):
        self.setRange(1, max_zoom)
        # ...

# App uses configurable zoom
max_zoom = self._config.get("max_zoom", 5000)
self.zoomWidget = ZoomWidget(max_zoom=max_zoom)

# Zoom increment from config
increment = self._config.get("zoom_increment", 1.1)
self._add_zoom(increment=increment if delta > 0 else 1.0 / increment)
```

### Performance
- No performance impact at normal zoom levels
- At extreme zoom (>3000%), image rendering may be slower on large images
- GPU acceleration helps (if available)
- Consider downsampling very large images before annotation

## Examples

### PCB Defect Annotation
```yaml
# Recommended config for PCB inspection
max_zoom: 3000       # 30x is usually sufficient
zoom_increment: 1.08 # Finer control for precision
```

### Medical Imaging
```yaml
# Recommended config for histology slides
max_zoom: 5000       # Full 50x magnification
zoom_increment: 1.1  # Standard control
```

### Microscopy
```yaml
# Recommended config for electron microscopy
max_zoom: 10000      # 100x for extreme detail
zoom_increment: 1.05 # Very fine control
```

## Troubleshooting

### Zoom is too fast/slow
Adjust `zoom_increment` in your config:
- Too fast: Use smaller value (e.g., 1.05)
- Too slow: Use larger value (e.g., 1.2)

### Can't zoom in enough
Increase `max_zoom` in your config:
```yaml
max_zoom: 10000  # or even higher
```

### App is slow at high zoom
- Reduce `max_zoom` to limit memory usage
- Close other applications
- Use smaller images if possible
- Consider using ROI (region of interest) cropping

### Zoom jumps around
- Ensure cursor is over the area you want to zoom into
- The zoom centers on cursor position (by design)
- Use keyboard shortcuts for non-centered zoom

## Related Features

- **Multiple Point Addition** (`Ctrl+M`): Add points along edges for precision at high zoom
- **Edit Mode** (`Ctrl+Shift+V`): Adjust polygon vertices with pixel precision
- **Dark Mode**: Reduces eye strain during long annotation sessions at high zoom

---

**Now you can annotate even the tiniest defects with confidence! 🔬**
