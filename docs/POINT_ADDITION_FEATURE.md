# Point Addition Feature

## Overview

Added functionality to add single and multiple points to polygon edges, complementing the existing point removal feature.

## Features

### 1. **Single Point Addition** (Enhanced Existing)
- **How to use**: `Alt + Click` on any edge of a polygon or linestrip
- **Behavior**: Adds a single point at the exact mouse position on the edge
- **Status message**: "ALT + Click to create point on shape"

### 2. **Multiple Point Addition** (New)
- **How to use**: 
  1. Hover over an edge (edge will be highlighted)
  2. Press `Ctrl+M` (configurable in `default_config.yaml`)
  3. Enter the number of points in the dialog (default: 1)
  4. Points will be evenly distributed along the edge
- **Shortcut**: `Ctrl+M`
- **Dialog**: Input dialog with min=1, max=100
- **Default value**: Configurable via `default_num_points_to_add` in config

### 3. **Point Removal** (Existing)
- **How to use**: `Alt+Shift+Click` on vertex, or `Meta+H` / `Backspace`
- **Behavior**: Removes the selected vertex from polygon

## Implementation Details

### Files Modified

1. **`labelme/shape.py`**
   - Added `addPointToEdge(i, point, label)`: Add single point to edge
   - Added `addMultiplePointsToEdge(i, num_points)`: Add multiple evenly-spaced points

2. **`labelme/widgets/canvas.py`**
   - Added `addMultiplePointsToEdge(num_points)`: Canvas method for multi-point addition
   - Added `edgeSelected` signal emission for enabling/disabling UI actions
   - Enhanced status messages for edge hovering

3. **`labelme/app.py`**
   - Added `addMultiplePoints` action with shortcut
   - Added `addMultiplePointsToEdge()` method with input dialog
   - Connected edge selection signal to enable/disable action
   - Added action to edit menu and context menu

4. **`labelme/config/default_config.yaml`**
   - Added `default_num_points_to_add: 1` configuration option
   - Added `add_multiple_points: Ctrl+Shift+A` shortcut

## Algorithm: Even Distribution

Points are distributed evenly along an edge using linear interpolation:

```python
for j in range(1, num_points + 1):
    t = j / (num_points + 1)  # Fraction along edge (0 < t < 1)
    new_point = p1 + t * (p2 - p1)
```

**Example** (edge from (0,0) to (10,10), 3 points):
- Point 1 at t=0.25: (2.5, 2.5)
- Point 2 at t=0.50: (5.0, 5.0)
- Point 3 at t=0.75: (7.5, 7.5)

## Configuration

### Default Number of Points
Edit `~/.labelmerc` or `labelme/config/default_config.yaml`:

```yaml
default_num_points_to_add: 1  # Change to preferred default (1-100)
```

### Keyboard Shortcut
Edit `~/.labelmerc` or `labelme/config/default_config.yaml`:

```yaml
shortcuts:
  add_multiple_points: Ctrl+M  # Change to preferred shortcut
```

## User Workflow

### Adding Points to Refine a Polygon

**Scenario**: You have a coarse polygon and want to add detail to one edge.

1. **Switch to Edit mode** (`Ctrl+J`)
2. **Hover over the edge** you want to refine
3. **Method A - Single point at cursor**:
   - Hold `Alt` and click at desired position
4. **Method B - Multiple evenly-spaced points**:
   - Press `Ctrl+M` while hovering
   - Enter number of points (e.g., 5)
   - Points are automatically distributed

### Example Use Cases

1. **Smooth curves**: Add 10-20 points along a straight edge, then manually adjust them to create a smooth curve
2. **Detailed boundaries**: Add 3-5 points to an edge that needs more detail
3. **Regular spacing**: Create evenly-spaced control points for consistent annotation

## Menu Locations

- **Edit Menu**: Edit → Add Multiple Points
- **Context Menu** (right-click on canvas): Add Multiple Points
- **Status Bar**: Shows availability when hovering over edges

## Code Structure

```
Shape.addMultiplePointsToEdge(i, num_points)
    ↓
Canvas.addMultiplePointsToEdge(num_points)
    ↓ (via signal)
MainWindow.addMultiplePointsToEdge()
    ↓ (shows dialog)
User enters count → Canvas updates → Shape modified → setDirty()
```

## Testing

Tested with:
- ✓ Single point addition (default behavior)
- ✓ 3 points evenly distributed
- ✓ 10 points evenly distributed
- ✓ Edge cases (1 point = midpoint)
- ✓ Mathematical correctness of interpolation

## Future Enhancements

Potential improvements:
- [ ] Add points with adaptive density based on edge curvature
- [ ] Undo/redo support for point addition
- [ ] Visual preview before confirming
- [ ] Remember last-used point count per session
- [ ] Add points to all edges simultaneously
