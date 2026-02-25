# New Features Guide

This document describes the advanced polygon editing features added to labelme.

## 📌 Table of Contents

- [Multiple Point Addition](#multiple-point-addition)
- [Polygon Merge](#polygon-merge)
- [Quick Reference](#quick-reference)
- [Configuration](#configuration)

---

## Multiple Point Addition

### Overview

Efficiently add multiple evenly-spaced points to polygon edges for detailed boundary refinement.

### Basic Usage

1. **Enter Edit Mode**: Press `Ctrl+J`
2. **Hover Over Edge**: Move cursor over a polygon edge (it will highlight)
3. **Trigger Action**: Press `Ctrl+M`
4. **Enter Count**: Type number of points (1-100) in the dialog
5. **Result**: Points are automatically distributed evenly along the edge

### Use Cases

| Scenario | Recommended Points | Workflow |
|----------|-------------------|----------|
| **Smooth Curves** | 5-10 points | Add points → Manually adjust to follow curve |
| **Detail Refinement** | 2-3 points | Add points where boundary needs precision |
| **Straighten Edge** | 1-2 points | Add points → Drag to straighten line |

### Examples

#### Example 1: Refining a Curved Boundary
```
1. Draw rough polygon around object with curved edge
2. Hover over the curved section
3. Press Ctrl+M, enter "8"
4. Manually adjust the 8 new points to follow the curve
5. Result: Smooth, accurate boundary
```

#### Example 2: Adding Detail
```
Initial: Rectangle with 4 points
Goal: Add detail to top edge
1. Hover over top edge
2. Press Ctrl+M, enter "3"
3. Result: Top edge now has 5 points (original 2 + 3 new)
```

### Technical Details

- **Algorithm**: Linear interpolation `p = p1 + t * (p2 - p1)` where `t = j/(n+1)`
- **Distribution**: Points are evenly spaced between edge vertices
- **Supported Shapes**: Polygons and linestrips only
- **Limitations**: Not available for rectangles, circles, or lines

---

## Polygon Merge

### Overview

Merge multiple polygons using geometric union operations with intelligent handling of connected and disconnected regions.

### Basic Usage

1. **Enter Edit Mode**: Press `Ctrl+J`
2. **Select Polygons**: Hold `Ctrl` and click each polygon to merge (minimum 2)
3. **Trigger Merge**: Press `Ctrl+Shift+M`
4. **Review Result**: Check info dialog for merge outcome

### Smart Behavior

The merge feature intelligently handles different scenarios:

#### ✅ Scenario 1: Adjacent/Overlapping Polygons
```
Input:  [Box A][Box B]  (touching)
Output: [   A+B     ]   (1 merged polygon)
Message: "Merged 2 polygons into 1 polygon"
```

#### ⚠️ Scenario 2: Disconnected Polygons
```
Input:  [Car A]    [Car B]    [Car C]  (all separate)
Output: [Car A]    [Car B]    [Car C]  (3 polygons, same label)
Message: "The selected 3 polygons are not touching each other..."
```

#### 🔀 Scenario 3: Mixed (Partial Connectivity)
```
Input:  [A][B]    [C]  (A&B touching, C separate)
Output: [A+B]     [C]  (2 polygons, same label)
Message: "Merged 3 polygons into 2 polygons. Some polygons were not touching..."
```

### Use Cases

| Use Case | Description | Example |
|----------|-------------|---------|
| **Fix Over-segmentation** | Combine regions that should be one object | Merge 3 overlapping "car" annotations into 1 |
| **Batch Labeling** | Label multiple objects with same label quickly | Draw rough boxes around 10 cars → merge → all labeled "car" |
| **Clean Boundaries** | Remove gaps between adjacent annotations | Merge 2 adjacent "building" polygons |
| **Simplify Annotations** | Reduce number of separate shapes | Combine partial annotations into complete ones |

### Technical Details

- **Algorithm**: Shapely's `unary_union()` geometric operation
- **Validation**: Auto-fixes self-intersecting polygons using `buffer(0)`
- **MultiPolygon Handling**: All disconnected regions are preserved as separate shapes
- **Label Inheritance**: All resulting polygons inherit label from first selected shape
- **Supported Shapes**: Polygons only (not rectangles, circles, lines, or points)

### Advanced Examples

#### Example 1: Merging Complex Shapes
```python
# Before merge:
Shape 1: L-shaped polygon (label: "building")
Shape 2: Rectangle touching Shape 1 (label: "building")
Shape 3: Circle separate from others (label: "building")

# After Ctrl+Shift+M:
Result 1: Merged L-shape + Rectangle (label: "building")
Result 2: Circle unchanged (label: "building")
Info: "Merged 3 polygons into 2 disconnected polygons"
```

#### Example 2: Batch Labeling Workflow
```
Task: Label 5 cars in an image
1. Draw rough polygons around each car (don't worry about labels)
2. Select all 5 polygons (Ctrl+Click each)
3. Press Ctrl+Shift+M
4. Enter label "car" once
5. Result: 5 separate car polygons, all labeled "car"
```

---

## Quick Reference

### Keyboard Shortcuts

| Action | Shortcut | Context |
|--------|----------|---------|
| **Add 1 Point** | `Alt+Click` on edge | Point added at cursor position |
| **Add N Points** | `Ctrl+M` on edge | Opens dialog for point count |
| **Remove Point** | `Backspace` OR `Alt+Shift+Click` | Removes selected vertex |
| **Merge Polygons** | `Ctrl+Shift+M` | Merges 2+ selected polygons |
| **Edit Mode** | `Ctrl+J` | Required for all editing operations |
| **Select Multiple** | `Ctrl+Click` | Select multiple shapes |

### Menu Locations

- **Edit → Add Multiple Points**: Add points to highlighted edge
- **Edit → Merge Polygons**: Merge selected polygons
- **Right-click menu**: Both options available in context menu

### Status Bar Messages

| Message | Meaning |
|---------|---------|
| `"ALT + Click to create point on shape"` | Hovering over edge, single-point mode ready |
| `"Ctrl+M to add multiple points"` | Hovering over edge, multi-point available |
| `"ALT + SHIFT + Click to delete point"` | Hovering over vertex, can delete |

---

## Configuration

### Custom Shortcuts

Edit `~/.labelmerc` or `labelme/config/default_config.yaml`:

```yaml
shortcuts:
  add_multiple_points: Ctrl+M        # Change shortcut
  merge_polygons: Ctrl+Shift+M       # Change shortcut
  remove_selected_point: [Meta+H, Backspace]  # Multiple shortcuts
```

### Default Point Count

```yaml
default_num_points_to_add: 1  # Default value in dialog (1-100)
```

### Example Custom Configuration

```yaml
# Prefer adding 3 points by default
default_num_points_to_add: 3

# Use simpler shortcuts
shortcuts:
  add_multiple_points: Ctrl+P
  merge_polygons: Ctrl+M
  
# Enable auto-save after merge
auto_save: true
```

---

## Troubleshooting

### Multiple Point Addition

**Problem**: "Add Multiple Points" is grayed out  
**Solutions**:
- ✅ Make sure you're in Edit mode (`Ctrl+J`)
- ✅ Hover over an **edge** (line), not a vertex (point)
- ✅ Only works on polygons/linestrips, not rectangles/circles
- ✅ Edge should be highlighted when hovering

**Problem**: Points not evenly distributed  
**Cause**: This is expected behavior - points are evenly spaced along the straight line between vertices  
**Solution**: For curved edges, add points first, then manually adjust each point to follow the curve

### Polygon Merge

**Problem**: "Merge Failed" error  
**Solutions**:
- ✅ Select at least 2 shapes
- ✅ Only polygon shapes can be merged (convert other shapes first)
- ✅ Check that shapes are valid (no self-intersections)

**Problem**: Disconnected polygons didn't merge into one  
**Explanation**: This is correct behavior! Polygons must be touching or overlapping to merge into a single polygon. Disconnected regions cannot geometrically form a single polygon.  
**Workaround**: If you want to label them all the same, merging still works - all resulting polygons will have the same label.

**Problem**: Changes disappeared after reopening  
**Solution**: Press `Ctrl+S` to save, or enable `auto_save: true` in config

**Problem**: Wrong label after merge  
**Cause**: Label is inherited from the first selected polygon  
**Solution**: Either select the desired polygon first, or edit label after merge (`Ctrl+E`)

---

## Tips & Best Practices

### Point Addition
- 💡 Start with fewer points, add more if needed
- 💡 For smooth curves, add 5-10 points then manually adjust
- 💡 Use `Ctrl+Z` to undo if you add too many
- 💡 Remember: more points = more precise but slower to edit

### Polygon Merge
- 💡 Select desired label source first (it's always first selected shape)
- 💡 Use merge for batch labeling: draw quick boxes → merge → all get same label
- 💡 Check the info dialog to understand merge results
- 💡 Enable auto-save to avoid losing changes
- 💡 For disconnected objects, merge still applies same label to all

---

## API Reference

### Shape Class Methods

```python
# Add multiple points to edge i
shape.addMultiplePointsToEdge(i: int, num_points: int = 1)

# Merge multiple shapes (static method)
merged_shapes = Shape.mergeShapes(shapes: list[Shape]) -> list[Shape] | None
```

### Canvas Class Methods

```python
# Add multiple points to currently highlighted edge
canvas.addMultiplePointsToEdge(num_points: int = 1)

# Merge currently selected shapes
canvas.mergeSelectedShapes()
```

---

**For more information, see:**
- [QUICK_START.md](../QUICK_START.md) - Quick reference guide
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Development guide
- [examples/](../examples/) - Example workflows
