from pynput.mouse import Button, Controller, Listener

mouse = Controller()

#Read Pointer Position
print(f'The current pointer position is {mouse.position}')

# Set Pointer Position
mouse.position = (100,200)
print(f'The mouse has been moved to {mouse.position}')

# Move pointer relative to current position
mouse.move(100,50)

# Press and Release
mouse.press(Button.left)
mouse.release(Button.left)

# Double Click; this is different from pressing and releasing
# Twice on macOS
mouse.click(Button.left,2)

# Scroll two steps down
mouse.scroll(0,2)

