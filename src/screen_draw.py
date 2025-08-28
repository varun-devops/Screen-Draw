import tkinter as tk
from tkinter import Canvas, simpledialog
from pynput import keyboard, mouse
from PIL import ImageGrab
import threading
import ctypes  # For getting accurate screen dimensions
import os

# Global variables
drawing = False
root = None
canvas = None
last_x, last_y = None, None
drawing_color = 'yellow'  # Default drawing color
line_width = 3  # Default line width
drawing_mode = "pen"  # Current drawing mode: pen, text
text_to_add = "Sample Text"  # Default text to add
available_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']  # Color options

def clear_canvas():
    """Clear all drawings from the canvas without exiting"""
    global canvas
    if canvas:
        print("Clearing canvas...")
        canvas.delete("all")  # Delete all drawings
        # Recreate all UI elements
        create_reset_button()  # Recreate the reset button
        create_color_buttons()  # Recreate the color buttons
        create_text_button()   # Recreate the text button
        create_branding()  # Recreate the branding

def set_drawing_color(color):
    """Change the current drawing color"""
    global drawing_color
    old_color = drawing_color
    drawing_color = color
    print(f"Changed drawing color from {old_color} to {color}")
    # Update the color button highlight
    update_color_buttons()

def update_color_buttons():
    """Update the highlight of color buttons based on the current selection"""
    global canvas, drawing_color
    if canvas:
        # First remove all highlights
        for color in available_colors:
            try:
                canvas.itemconfig(f"color_button_{color}", outline='white', width=1)
            except:
                pass  # Skip if the button doesn't exist yet
        # Then highlight the current color
        try:
            canvas.itemconfig(f"color_button_{drawing_color}", outline='white', width=3)
        except:
            pass  # Skip if the button doesn't exist yet

def toggle_text_mode():
    """Toggle between pen drawing mode and text input mode"""
    global drawing_mode, canvas, root
    if drawing_mode == "pen":
        drawing_mode = "text"
        print("Switched to text input mode")
        # Show a simple text input dialog
        if root:
            try:
                show_text_input_dialog()
            except Exception as e:
                print(f"Error showing text input dialog: {e}")
    else:
        drawing_mode = "pen"
        print("Switched to pen drawing mode")

def show_text_input_dialog():
    """Show a dialog for entering text to add to the drawing"""
    global text_to_add, root
    
    # Create a top-level window for text input
    dialog = tk.Toplevel(root)
    dialog.title("Enter Text")
    dialog.attributes('-topmost', True)
    dialog.geometry("300x100")
    
    # Center the dialog on screen
    dialog.update_idletasks()
    x = (root.winfo_screenwidth() - dialog.winfo_width()) // 2
    y = (root.winfo_screenheight() - dialog.winfo_height()) // 2
    dialog.geometry(f"+{x}+{y}")
    
    # Text entry field
    entry_label = tk.Label(dialog, text="Enter text to add:")
    entry_label.pack(pady=5)
    
    entry = tk.Entry(dialog, width=30)
    entry.insert(0, text_to_add)
    entry.pack(pady=5)
    entry.select_range(0, tk.END)
    entry.focus_set()
    
    def on_ok():
        global text_to_add
        text_to_add = entry.get()
        print(f"Text set to: {text_to_add}")
        dialog.destroy()
    
    # OK button
    ok_button = tk.Button(dialog, text="OK", command=on_ok)
    ok_button.pack(pady=5)
    
    # Handle Enter key
    dialog.bind("<Return>", lambda event: on_ok())
    
    # Make dialog modal
    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

def add_text(event):
    """Add text at the clicked position"""
    global canvas, text_to_add, drawing_color
    if drawing_mode == "text" and text_to_add:
        canvas.create_text(
            event.x, event.y, 
            text=text_to_add, 
            fill=drawing_color, 
            font=('Arial', 16),
            tags="drawing"
        )
        print(f"Added text '{text_to_add}' at position ({event.x}, {event.y})")

def create_text_button():
    """Create a button to toggle text input mode"""
    global canvas, root
    if canvas:
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        button_width = 80
        button_height = 30
        
        # Position: right side, below reset button
        button_x = screen_width - 100
        button_y = 50
        
        # Create button rectangle and text
        canvas.create_rectangle(
            button_x, button_y, 
            button_x + button_width, button_y + button_height,
            fill='blue', outline='white', tags="text_button"
        )
        canvas.create_text(
            button_x + 40, button_y + 15, 
            text="TEXT", fill='white',
            font=('Arial', 12, 'bold'), tags="text_button"
        )
        
        # Bind click event to the button area
        canvas.tag_bind("text_button", '<Button-1>', lambda e: toggle_text_mode())

def create_color_buttons():
    """Create color selection buttons at the top of the screen"""
    global canvas, root, available_colors
    if canvas:
        # Get screen width
        screen_width = root.winfo_screenwidth()
        
        # Settings for color buttons
        button_size = 30
        padding = 5
        start_x = 20
        start_y = 10
        
        # Create a button for each available color
        for i, color in enumerate(available_colors):
            button_x = start_x + i * (button_size + padding)
            
            # Create colored button
            canvas.create_rectangle(
                button_x, start_y,
                button_x + button_size, start_y + button_size,
                fill=color, 
                outline='white',
                width=1 if color != drawing_color else 3,
                tags=f"color_button_{color}"
            )
            
            # Bind click event
            canvas.tag_bind(
                f"color_button_{color}",
                '<Button-1>',
                lambda e, c=color: set_drawing_color(c)
            )

def create_branding():
    """Add company branding at the bottom left corner"""
    global canvas, root
    if canvas:
        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        # Create semi-transparent background for branding
        padding = 10
        brand_text = "OnScreenDraw  Webtroops"
        text_width = len(brand_text) * 10  # Approximate width based on text length
        
        # Create background rectangle for branding
        canvas.create_rectangle(
            padding, screen_height - 40 - padding, 
            text_width + (padding * 3), screen_height - padding,
            fill='#333333', outline='#555555', tags="branding"
        )
        
        # Create branding text
        canvas.create_text(
            padding + 10, screen_height - padding - 20,
            text=brand_text, fill='#33ccff', anchor='w',
            font=('Arial', 12, 'bold'), tags="branding"
        )

def create_reset_button():
    """Create a reset button in the top-right corner"""
    global canvas, root
    if canvas:
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        # Create a clear button in the top right corner
        button_x = screen_width - 100
        button_width = 80
        button_height = 30
        
        # Create button rectangle and text
        canvas.create_rectangle(button_x, 10, button_x + button_width, 10 + button_height, 
                               fill='red', outline='white', tags="reset_button")
        canvas.create_text(button_x + 40, 25, text="RESET", fill='white', 
                          font=('Arial', 12, 'bold'), tags="reset_button")
        
        # Bind click event to the button area
        canvas.tag_bind("reset_button", '<Button-1>', lambda e: clear_canvas())

def start_drawing():
    global drawing, root, canvas, last_x, last_y, drawing_mode
    if drawing:
        return
    drawing = True
    drawing_mode = "pen"  # Reset to pen mode when starting
    print("Starting drawing mode...")
    try:
        # Get current mouse position
        m = mouse.Controller()
        x, y = m.position
        
        # Get screen dimensions
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        print(f"Screen dimensions: {screen_width}x{screen_height}")
        
        # Create transparent fullscreen window
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        # Different approach for transparency
        root.wm_attributes('-alpha', 0.3)  # Semi-transparent
        root.config(bg='black')
        
        # Set application icon
        try:
            # Get the base directory
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            icon_path = os.path.join(base_dir, 'assets', 'icon.ico')
            if os.path.exists(icon_path):
                root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Could not set icon: {e}")
        
        # Create canvas with exact screen dimensions
        canvas = Canvas(root, bg='black', highlightthickness=0, 
                       width=screen_width, height=screen_height)
        canvas.pack(fill=tk.BOTH, expand=True)
        
        # Create UI elements
        create_reset_button()
        create_color_buttons()
        create_text_button()
        create_branding()
        
        # Bind mouse events
        canvas.bind('<Button-1>', on_press)
        canvas.bind('<B1-Motion>', on_drag)
        canvas.bind('<ButtonRelease-1>', on_release)
        
        # Bind keyboard event to exit
        root.bind('<Escape>', lambda e: stop_drawing())
        
        # Set initial position to current mouse position
        last_x, last_y = x, y
        
        # Move cursor to the drawing surface
        canvas.focus_set()
        print("Drawing overlay created. Click and drag to draw.")
        print("Press the RESET button to clear, TEXT for text mode, or ESC to exit.")
        
        # Start the mainloop
        root.mainloop()
    except Exception as e:
        print(f"Error in start_drawing: {e}")
        drawing = False

def on_press(event):
    global last_x, last_y, drawing_mode
    # Check if click is on any UI element (button or branding)
    # Get all items at the clicked position
    items = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
    is_ui_element = False
    for item_id in items:
        tags = canvas.gettags(item_id)
        if any(tag in ["reset_button", "text_button", "branding"] or tag.startswith("color_button_") for tag in tags):
            is_ui_element = True
            break
            
    # Only set drawing position if not clicking on a UI element
    if not is_ui_element:
        if drawing_mode == "text":
            # Add text at the clicked position
            add_text(event)
            # Switch back to pen mode after adding text
            drawing_mode = "pen"
            print("Switched back to pen drawing mode after adding text")
        else:
            # Set starting point for line drawing
            last_x, last_y = event.x, event.y
            print(f"Starting line at ({event.x}, {event.y})")

def on_drag(event):
    global last_x, last_y, drawing_color, line_width
    if last_x is not None and last_y is not None:
        # Check if we're dragging on any UI element
        items = canvas.find_overlapping(event.x, event.y, event.x+1, event.y+1)
        for item_id in items:
            tags = canvas.gettags(item_id)
            if any(tag in ["reset_button", "text_button", "branding"] or tag.startswith("color_button_") for tag in tags):
                return  # Don't draw if on UI elements
                
        # Draw the line with current settings
        canvas.create_line(last_x, last_y, event.x, event.y, 
                          fill=drawing_color, width=line_width,
                          capstyle=tk.ROUND, smooth=True, tags="drawing")
    last_x, last_y = event.x, event.y

def on_release(event):
    global last_x, last_y
    # End the current line segment - this prevents "jumping lines" 
    # when clicking in a different location
    last_x, last_y = None, None

def stop_drawing():
    global drawing, root, last_x, last_y
    print("Stopping drawing mode...")
    drawing = False
    # Reset drawing state
    last_x, last_y = None, None
    if root:
        try:
            root.destroy()
            print("Drawing window closed successfully")
        except Exception as e:
            print(f"Error closing window: {e}")  # More detailed error handling

# Hotkey listener
def on_hotkey():
    global drawing
    print(f"Hotkey pressed! Current drawing state: {drawing}")
    if not drawing:
        # Use daemon=True to ensure the thread exits when main thread exits
        drawing_thread = threading.Thread(target=start_drawing, daemon=True)
        drawing_thread.start()
    else:
        stop_drawing()

def test_drawing():
    """Function to test drawing directly without hotkey"""
    print("Testing drawing mode...")
    on_hotkey()

def main():
    print("WebtroopsScreen Draw Tool started")
    print("Press F9 to start/stop drawing")
    print("Instructions:")
    print("- Click and drag to draw on the screen")
    print("- Use color buttons at the top to change drawing color")
    print("- Click TEXT button to add text")
    print("- Press the RESET button in top-right corner to clear drawings")
    print("- Press ESC to exit drawing mode")
    
    # Try both '<f9>' and 'f9' formats for better compatibility
    hotkey_combinations = {
        '<f9>': on_hotkey,
        'f9': on_hotkey,  # Alternative format
        '<alt>+d': on_hotkey  # Backup hotkey
    }
    
    # Set up the hotkey listener
    try:
        hotkey = keyboard.GlobalHotKeys(hotkey_combinations)
        hotkey.start()
        print("Hotkey listener started successfully")
        
        # Start drawing immediately for convenience
        print("Starting drawing mode...")
        threading.Timer(1.0, test_drawing).start()
        
        # Keep the main thread running
        hotkey.join()
    except Exception as e:
        print(f"Error setting up hotkey: {e}")
        print("Trying direct drawing mode instead...")
        # If hotkey setup fails, directly start drawing
        start_drawing()
    except KeyboardInterrupt:
        print("Application terminated by user")
        if drawing:
            stop_drawing()

if __name__ == "__main__":
    main()
