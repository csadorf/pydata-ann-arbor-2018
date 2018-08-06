import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation, patches


def get_t_max(v, theta, g=9.81):
    return 2 * v * np.sin(theta) / g


def compute_xy(t, v, theta, g=9.81):
    return v * np.cos(theta) * t, v * np.sin(theta) * t - (g/2) * t**2


def plot(velocity, theta):
    t = np.linspace(0, get_t_max(velocity, theta), 100)
    xy = np.asarray(compute_xy(t, velocity, theta)) / 1000

    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_aspect('equal')
    ax.set_title("v={} m/s, \u03b8={:.1f}\u00b0".format(velocity, theta * 180 / np.pi))
    ax.set_xlabel('x [km]')
    ax.set_ylabel('y [km]')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 500)
    ax.plot(* xy, ls=':')
    return fig, ax


def animate(velocity, theta, duration=5, frame_rate=24, x=300):
    "Animate the trajectory for the given velocity and launch angle 'theta'."
    import numpy as np
    # Compute the trajectory
    t_max = get_t_max(velocity, theta)
    t = np.linspace(0, t_max, int(t_max * frame_rate / x))
    xy = np.asarray(compute_xy(t, velocity, theta)).T / 1000  # km

    # Animate the trajectory
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.set_aspect('equal')
    ax.set_title("v={} m/s \u03b8={:.1f}\u00b0".format(velocity, theta * 180 / np.pi))
    ax.set_xlabel('x [km]')
    ax.set_ylabel('y [km]')
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 500)
    line, = ax.plot(*xy[0], ls=':')
    patch = ax.add_patch(patches.Circle(xy=xy[0], radius=10))
    timer = ax.text(0.7, 0.8, "t=0 min", transform=ax.transAxes)

    def draw_frame(i):
        line.set_data(* xy[:min(i, len(xy)-1)].T)
        patch.center = xy[min(i, len(xy)-1)]
        timer.set_text("t={:.0f} sec".format(x * i / frame_rate))
        return line, patch

    anim = animation.FuncAnimation(
            fig, draw_frame, frames=duration*frame_rate, interval=1000 // frame_rate, blit=True)
    plt.close()
    return anim
