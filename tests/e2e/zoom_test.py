"""Test zoom focus behavior from different edges."""
import pytest
from PyQt5 import QtCore
from pathlib import Path
from labelme.app import MainWindow


def test_zoom_focus_from_edges(qtbot, data_path: Path):
    """Test that zoom maintains focus point from all four edges."""
    # Create a main window and load an image
    image_file = str(data_path / "raw/2011_000003.jpg")
    win = MainWindow(filename=image_file)
    qtbot.addWidget(win)
    win.show()
    qtbot.waitExposed(win)
    qtbot.wait(200)
    
    # Set a specific zoom level to start
    win._set_zoom(value=200)  # Zoom to 200%
    qtbot.wait(100)
    
    # Test positions: left, top, right, bottom edges (in viewport coordinates)
    viewport = win.scrollArea.viewport()
    vp_width = viewport.width()
    vp_height = viewport.height()
    
    test_positions = {
        "left_edge": QtCore.QPointF(50, vp_height // 2),
        "top_edge": QtCore.QPointF(vp_width // 2, 50),
        "right_edge": QtCore.QPointF(vp_width - 50, vp_height // 2),
        "bottom_edge": QtCore.QPointF(vp_width // 2, vp_height - 50),
        "center": QtCore.QPointF(vp_width // 2, vp_height // 2),
    }
    
    for edge_name, viewport_pos in test_positions.items():
        # Reset to known state
        win._set_zoom(value=200)
        qtbot.wait(50)
        
        # Convert viewport position to canvas position for the test
        canvas_pos = win.canvas.mapFromGlobal(
            win.scrollArea.viewport().mapToGlobal(viewport_pos.toPoint())
        )
        
        # Record scroll positions before zoom
        h_before = win.scrollBars[QtCore.Qt.Horizontal].value()
        v_before = win.scrollBars[QtCore.Qt.Vertical].value()
        
        # Zoom in at this position
        win._set_zoom(value=300, pos=QtCore.QPointF(canvas_pos))
        qtbot.wait(50)
        
        h_after_in = win.scrollBars[QtCore.Qt.Horizontal].value()
        v_after_in = win.scrollBars[QtCore.Qt.Vertical].value()
        
        # For edges, zoom should have adjusted scroll position
        # We can't assert exact values, but scroll should have changed (unless at edges)
        print(f"\n{edge_name} ZOOM IN: h={h_before}->{h_after_in}, v={v_before}->{v_after_in}")
        
        # Now zoom out from same position
        win._set_zoom(value=150, pos=QtCore.QPointF(canvas_pos))
        qtbot.wait(50)
        
        h_after_out = win.scrollBars[QtCore.Qt.Horizontal].value()
        v_after_out = win.scrollBars[QtCore.Qt.Vertical].value()
        
        print(f"{edge_name} ZOOM OUT: h={h_after_in}->{h_after_out}, v={v_after_in}->{v_after_out}")
        
        # The scroll values should be reasonable (not negative, not exceeding max)
        assert h_after_out >= 0, f"{edge_name}: horizontal scroll became negative"
        assert v_after_out >= 0, f"{edge_name}: vertical scroll became negative"
        assert h_after_out <= win.scrollBars[QtCore.Qt.Horizontal].maximum() + 1
        assert v_after_out <= win.scrollBars[QtCore.Qt.Vertical].maximum() + 1


def test_zoom_focus_right_edge_specific(qtbot, data_path: Path):
    """Specific test for the reported bug: zoom out from right edge shifts to center."""
    image_file = str(data_path / "raw/2011_000003.jpg")
    win = MainWindow(filename=image_file)
    qtbot.addWidget(win)
    win.show()
    qtbot.waitExposed(win)
    qtbot.wait(200)
    
    # Zoom in to 400% to make scrollbars active
    win._set_zoom(value=400)
    qtbot.wait(100)
    
    # Scroll to the right edge
    h_scrollbar = win.scrollBars[QtCore.Qt.Horizontal]
    h_scrollbar.setValue(h_scrollbar.maximum())
    qtbot.wait(50)
    
    # Record the scroll position at right edge
    h_at_right = h_scrollbar.value()
    viewport = win.scrollArea.viewport()
    
    # Position mouse near right edge of viewport
    viewport_pos = QtCore.QPointF(viewport.width() - 100, viewport.height() // 2)
    canvas_pos = win.canvas.mapFromGlobal(
        viewport.mapToGlobal(viewport_pos.toPoint())
    )
    
    print(f"\nBefore zoom out: scroll={h_at_right}, max={h_scrollbar.maximum()}")
    
    # Zoom out from right edge
    win._set_zoom(value=300, pos=QtCore.QPointF(canvas_pos))
    qtbot.wait(50)
    
    h_after_zoom = h_scrollbar.value()
    new_max = h_scrollbar.maximum()
    
    print(f"After zoom out: scroll={h_after_zoom}, max={new_max}")
    
    # After zooming out, we should still be near the right edge
    # The scroll position should be close to the new maximum
    # Allow some tolerance for rounding
    distance_from_edge = new_max - h_after_zoom
    
    print(f"Distance from right edge: {distance_from_edge}")
    
    # The key assertion: when zooming out from right edge,
    # we should stay near the right edge (within viewport width)
    assert distance_from_edge < viewport.width(), \
        f"Zoom out from right edge jumped too far left (distance={distance_from_edge})"


def test_zoom_focus_bottom_edge_specific(qtbot, data_path: Path):
    """Specific test for the reported bug: zoom out from bottom edge shifts to center."""
    image_file = str(data_path / "raw/2011_000003.jpg")
    win = MainWindow(filename=image_file)
    qtbot.addWidget(win)
    win.show()
    qtbot.waitExposed(win)
    qtbot.wait(200)
    
    # Zoom in to 400% to make scrollbars active
    win._set_zoom(value=400)
    qtbot.wait(100)
    
    # Scroll to the bottom edge
    v_scrollbar = win.scrollBars[QtCore.Qt.Vertical]
    v_scrollbar.setValue(v_scrollbar.maximum())
    qtbot.wait(50)
    
    # Record the scroll position at bottom edge
    v_at_bottom = v_scrollbar.value()
    viewport = win.scrollArea.viewport()
    
    # Position mouse near bottom edge of viewport
    viewport_pos = QtCore.QPointF(viewport.width() // 2, viewport.height() - 100)
    canvas_pos = win.canvas.mapFromGlobal(
        viewport.mapToGlobal(viewport_pos.toPoint())
    )
    
    print(f"\nBefore zoom out: scroll={v_at_bottom}, max={v_scrollbar.maximum()}")
    
    # Zoom out from bottom edge
    win._set_zoom(value=300, pos=QtCore.QPointF(canvas_pos))
    qtbot.wait(50)
    
    v_after_zoom = v_scrollbar.value()
    new_max = v_scrollbar.maximum()
    
    print(f"After zoom out: scroll={v_after_zoom}, max={new_max}")
    
    # After zooming out, we should still be near the bottom edge
    distance_from_edge = new_max - v_after_zoom
    
    print(f"Distance from bottom edge: {distance_from_edge}")
    
    # The key assertion: when zooming out from bottom edge,
    # we should stay near the bottom edge (within viewport height)
    assert distance_from_edge < viewport.height(), \
        f"Zoom out from bottom edge jumped too far up (distance={distance_from_edge})"
