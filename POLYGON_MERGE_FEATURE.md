# Polygon Merge Feature

## Overview

The polygon merge feature allows you to combine multiple adjacent or overlapping polygons into a single unified polygon using geometric union operations.

## Features Implemented

### 1. **Merge Selected Polygons**
- **How to use**: 
  1. Switch to Edit mode (`Ctrl+J`)
  2. Select 2 or more polygons (hold `Ctrl` and click on each polygon)
  3. Press `Ctrl+Shift+M` or go to Edit menu → Merge Polygons
  4. The selected polygons will be merged into one
- **Shortcut**: `Ctrl+Shift+M`
- **Menu location**: Edit → Merge Polygons

### 2. **Automatic Shape Handling**
- **Union operation**: Uses Shapely's `unary_union` for geometric union
- **Self-intersection handling**: Automatically fixes invalid polygons using `buffer(0)`
- **MultiPolygon handling**: If the merge results in disconnected regions, keeps ALL polygons as separate shapes
- **Label preservation**: The merged polygon inherits the label and properties from the first selected shape

## Implementation Details

### Files Modified

| File | Changes |
|------|---------|
| `labelme/shape.py` | Added `Shape.mergeShapes()` static method using Shapely |
| `labelme/widgets/canvas.py` | Added `mergeSelectedShapes()` method |
| `labelme/app.py` | Added UI action, menu item, shortcut, and `mergeSelectedShapes()` handler |
| `labelme/config/default_config.yaml` | Added `merge_polygons: Ctrl+Shift+M` shortcut |

### Algorithm

1. **Filter valid polygons**: Only polygon shapes with 3+ points are considered
2. **Convert to Shapely**: Each Shape is converted to a Shapely Polygon
3. **Validate**: Invalid polygons are fixed using `buffer(0)`
4. **Union**: `unary_union()` combines all polygons
5. **Handle result**:
   - If MultiPolygon: Keep ALL disconnected polygons as separate shapes
   - If Polygon: Use the exterior coordinates
6. **Create merged shape(s)**: Convert back to labelme Shape format (one for each disconnected region)
7. **Update canvas**: Remove original shapes, add merged shape(s)

### Error Handling

- **Validation**: Warns if fewer than 2 polygons are selected
- **Type checking**: Only polygon shapes are merged (rectangles, circles, lines ignored)
- **Geometry validation**: Invalid polygons are auto-fixed or skipped
- **User feedback**: Shows warning dialog if merge fails

## Usage Examples

### Example 1: Merge Adjacent Polygons
```
1. Draw two adjacent polygons
2. Select both (Ctrl+Click on each)
3. Press Ctrl+Shift+M
4. Result: One merged polygon covering both areas
```

### Example 2: Merge Overlapping Regions
```
1. Draw overlapping polygons
2. Select all overlapping shapes
3. Edit → Merge Polygons
4. Result: Single polygon with union of all areas
```

### Example 3: Fill Gaps Between Annotations
```
1. Annotate multiple separate regions
2. Select adjacent polygons
3. Merge to create continuous annotation
4. Useful for segmenting connected objects
```

## Configuration

You can customize the merge shortcut in `~/.labelmerc`:

```yaml
shortcuts:
  merge_polygons: Ctrl+Shift+M  # Change to preferred shortcut
```

## Technical Notes

### Dependencies
- **Shapely**: Required for geometric operations (already installed)
- Shapely version 2.0+ is recommended for better performance

### Limitations
- Only works with polygon shapes (not rectangles, circles, or lines)
- Minimum 2 polygons must be selected
- If merge results in multiple disconnected polygons, only the largest is kept
- Properties (label, color, flags) are inherited from the first selected shape

### Performance
- Fast for typical use cases (< 100 vertices per polygon)
- For complex polygons with thousands of vertices, merge may take 1-2 seconds
- Shapely uses efficient computational geometry algorithms

## UI Elements

### Menu Item
- **Location**: Edit → Merge Polygons
- **Enabled**: Only when 2+ shapes are selected
- **Icon**: None (text only)

### Keyboard Shortcut
- **Default**: `Ctrl+Shift+M`
- **Scope**: Global (works anytime 2+ shapes are selected)

### Context Menu
- Available when right-clicking with 2+ shapes selected

## Related Features

- **Duplicate Polygons** (`Ctrl+D`): Create copies before merging
- **Delete Polygons** (`Delete`): Remove unwanted shapes
- **Edit Label** (`Ctrl+E`): Change label after merging
- **Undo** (`Ctrl+Z`): Undo the merge operation

## Troubleshooting

### "Merge Failed" Error
- **Cause**: Selected shapes are not valid polygons
- **Solution**: Ensure you're selecting polygon shapes (not rectangles, circles, or points)

### Unexpected Result
- **Cause**: Self-intersecting polygons
- **Solution**: The algorithm auto-fixes these, but results may differ from expectations

### Missing Menu Item
- **Cause**: Only 1 or 0 shapes selected
- **Solution**: Select at least 2 polygon shapes using Ctrl+Click

## Future Enhancements

Potential improvements for future versions:
- Support for merging rectangles and circles
- Option to keep all polygons from MultiPolygon result
- Preview before merging
- Customizable label/property inheritance rules
- Batch merge for large datasets

---

## Examples

### Example 1: Merging Adjacent Polygons
**Input**: 2 touching squares (10x10 each)
**Output**: 1 merged polygon (20x10 rectangle)

### Example 2: Merging Disconnected Polygons  
**Input**: 3 separate cars in different locations
**Output**: 3 polygons (one for each car, all with the same label)
**Dialog**: "Merge created 3 disconnected polygons"

### Example 3: Mixed Scenario
**Input**: 2 touching boxes + 1 separate box
**Output**: 2 polygons (1 merged from the touching pair, 1 separate)
**Dialog**: "Merge created 2 disconnected polygons"

---

## Testing

Run the test:
```bash
python3 tmp_rovodev_test_merge.py
```

Tests verify:
- ✓ Adjacent polygons merge into 1 shape
- ✓ Disconnected polygons create multiple shapes
- ✓ Mixed scenarios handled correctly
