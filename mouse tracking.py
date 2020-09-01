import win32gui
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig_1 = plt.figure(1)
ax1 = fig_1.add_subplot(1,1,1)
xs = []
ys = []

#function that takes the position of the mouse cursor and appends it to the list
def animate_mouse_movement(i, xs, ys):
    x, y = win32gui.GetCursorPos()
    y = -y + 1079
    
    #removing earlier points to prevent cluttering
    if len(xs) >= 500:
        xs.remove(xs[0])
        ys.remove(ys[0])
        xs.append(x)
        ys.append(y)
    else:
        xs.append(x)
        ys.append(y)
        
    ax1.clear()
    ax1.plot(xs, ys)
    plt.title('Real Time Mouse Movement')
    plt.xlabel('Movement on x-axis')
    plt.ylabel('Movement on y-axis')
    
#using the list, create a graph of mouse movement
animate_mouse = animation.FuncAnimation(fig_1, animate_mouse_movement,
                              fargs=(xs, ys), interval=10)

plt.show()
    
