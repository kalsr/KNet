

# CGI & VFX Playground — a Streamlit demo of core visual-effects techniques.


import base64
import io

import numpy as np
import plotly.graph_objects as go
import streamlit as st
from PIL import Image, ImageDraw, ImageFilter

st.set_page_config(page_title="CGI & VFX Playground", page_icon="🎬", layout="wide")

W, H = 640, 400  # default frame size


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def to_float(img: Image.Image) -> np.ndarray:
    return np.asarray(img.convert("RGB"), dtype=np.float32) / 255.0


def to_img(arr: np.ndarray) -> Image.Image:
    return Image.fromarray((np.clip(arr, 0, 1) * 255).astype(np.uint8))


def vertical_gradient(top, bottom, w=W, h=H) -> np.ndarray:
    t = np.linspace(0, 1, h)[:, None, None]
    return (1 - t) * np.array(top) / 255 + t * np.array(bottom) / 255 * np.ones((h, w, 3))


def show_gif(frames, duration_ms=50):
    buf = io.BytesIO()
    frames[0].save(buf, format="GIF", save_all=True, append_images=frames[1:],
                   duration=duration_ms, loop=0)
    b64 = base64.b64encode(buf.getvalue()).decode()
    st.markdown(f'<img src="data:image/gif;base64,{b64}" style="width:100%;border-radius:8px">',
                unsafe_allow_html=True)
    return buf.getvalue()


# ----------------------------------------------------------------------------
# Procedural backgrounds (digital set extensions)
# ----------------------------------------------------------------------------
@st.cache_data
def make_background(kind: str, seed: int = 7) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if kind == "Sunset beach":
        img = vertical_gradient((255, 120, 60), (255, 210, 140))
        yy, xx = np.mgrid[0:H, 0:W]
        sun = np.exp(-(((xx - W * 0.7) ** 2 + (yy - H * 0.55) ** 2) / (2 * 45 ** 2)))
        img += sun[..., None] * np.array([1.0, 0.85, 0.5]) * 0.8
        sea = yy > H * 0.62
        img[sea] = img[sea] * 0.25 + np.array([0.05, 0.3, 0.6]) * 0.75
        return np.clip(img, 0, 1)
    if kind == "Outer space":
        img = vertical_gradient((5, 5, 25), (20, 10, 45))
        for _ in range(500):
            x, y = rng.integers(0, W), rng.integers(0, H)
            img[y, x] = rng.uniform(0.5, 1.0)
        yy, xx = np.mgrid[0:H, 0:W]
        d = np.sqrt((xx - W * 0.2) ** 2 + (yy - H * 0.3) ** 2)
        planet = d < 70
        shade = np.clip(1 - (xx - W * 0.2 + 40) / 140, 0.1, 1)
        img[planet] = (np.array([0.8, 0.45, 0.25]) * shade[..., None])[planet]
        return np.clip(img, 0, 1)
    # Alien planet
    img = vertical_gradient((60, 20, 90), (200, 90, 160))
    x = np.arange(W)
    ridge = H * 0.65 + 25 * np.sin(x / 47) + 15 * np.sin(x / 13 + 1) + 8 * np.sin(x / 5)
    yy = np.arange(H)[:, None]
    img[yy > ridge] = np.array([0.15, 0.35, 0.25])
    return np.clip(img, 0, 1)


@st.cache_data
def make_greenscreen_plate(seed: int = 1) -> np.ndarray:
    """A synthetic 'actor' filmed in front of a green screen."""
    rng = np.random.default_rng(seed)
    img = Image.new("RGB", (W, H), (20, 180, 60))
    d = ImageDraw.Draw(img)
    cx = W // 2 - 60
    d.ellipse([cx - 32, 70, cx + 32, 140], fill=(235, 190, 160))              # head
    d.rectangle([cx - 50, 145, cx + 50, 290], fill=(40, 70, 160))             # torso
    d.rectangle([cx - 85, 150, cx - 52, 270], fill=(40, 70, 160))             # arm L
    d.polygon([(cx + 52, 150), (cx + 85, 150), (cx + 140, 90), (cx + 120, 75)],
              fill=(40, 70, 160))                                              # arm R (waving)
    d.rectangle([cx - 45, 290, cx - 8, 400], fill=(30, 30, 35))               # leg L
    d.rectangle([cx + 8, 290, cx + 45, 400], fill=(30, 30, 35))               # leg R
    d.ellipse([cx + 112, 55, cx + 150, 92], fill=(235, 190, 160))             # hand
    img = img.filter(ImageFilter.GaussianBlur(1.2))                          # soft edges
    arr = to_float(img)
    # uneven lighting on the screen + sensor noise, like a real plate
    yy, xx = np.mgrid[0:H, 0:W]
    light = 0.85 + 0.15 * np.exp(-((xx - W / 2) ** 2 + (yy - H / 3) ** 2) / (2 * 220 ** 2))
    arr = arr * light[..., None] + rng.normal(0, 0.015, arr.shape)
    return np.clip(arr, 0, 1)


# ----------------------------------------------------------------------------
# Chroma key
# ----------------------------------------------------------------------------
def chroma_key(fg, bg, low, high, spill):
    r, g, b = fg[..., 0], fg[..., 1], fg[..., 2]
    greenness = g - np.maximum(r, b)
    alpha = 1 - np.clip((greenness - low) / max(high - low, 1e-6), 0, 1)
    out = fg.copy()
    limit = np.maximum(r, b)
    out[..., 1] = g - spill * np.clip(g - limit, 0, None)   # spill suppression
    comp = out * alpha[..., None] + bg * (1 - alpha[..., None])
    return comp, alpha


# ----------------------------------------------------------------------------
# 3D geometry (CGI)
# ----------------------------------------------------------------------------
def make_shape(shape, res, seed):
    u = np.linspace(0, 2 * np.pi, res)
    v = np.linspace(0, 2 * np.pi, res)
    U, V = np.meshgrid(u, v)
    if shape == "Torus (donut)":
        R, r = 2.0, 0.8
        return (R + r * np.cos(V)) * np.cos(U), (R + r * np.cos(V)) * np.sin(U), r * np.sin(V)
    if shape == "Sphere":
        V = V / 2
        return np.cos(U) * np.sin(V), np.sin(U) * np.sin(V), np.cos(V)
    if shape == "Twisted knot":
        X = (2 + np.cos(3 * U)) * np.cos(2 * U)
        Y = (2 + np.cos(3 * U)) * np.sin(2 * U)
        Z = np.sin(3 * U)
        tube = 0.35
        return X + tube * np.cos(V) * np.cos(2 * U), Y + tube * np.cos(V) * np.sin(2 * U), Z + tube * np.sin(V)
    # Procedural terrain: fractal sum of random waves
    rng = np.random.default_rng(seed)
    x = np.linspace(-3, 3, res)
    X, Y = np.meshgrid(x, x)
    Z = np.zeros_like(X)
    amp, freq = 1.0, 0.8
    for _ in range(6):
        for _ in range(3):
            a, ph = rng.uniform(0, 2 * np.pi, 2)
            Z += amp * np.sin(freq * (X * np.cos(a) + Y * np.sin(a)) + ph)
        amp *= 0.5
        freq *= 2.0
    return X, Y, Z * 0.35


def wireframe(X, Y, Z, step=1):
    xs, ys, zs = [], [], []
    for grid in (lambda A: A[::step], lambda A: A.T[::step]):
        for xr, yr, zr in zip(grid(X), grid(Y), grid(Z)):
            xs += list(xr) + [None]
            ys += list(yr) + [None]
            zs += list(zr) + [None]
    return go.Scatter3d(x=xs, y=ys, z=zs, mode="lines",
                        line=dict(color="#7CFC00", width=1.5), hoverinfo="skip", showlegend=False)


# ----------------------------------------------------------------------------
# Particle systems
# ----------------------------------------------------------------------------
def gaussian_kernel(radius):
    ax = np.arange(-radius, radius + 1)
    xx, yy = np.meshgrid(ax, ax)
    return np.exp(-(xx ** 2 + yy ** 2) / (2 * (radius / 2) ** 2))


def splat(canvas, x, y, color, kernel):
    r = kernel.shape[0] // 2
    x, y = int(x), int(y)
    h, w = canvas.shape[:2]
    x0, x1, y0, y1 = max(x - r, 0), min(x + r + 1, w), max(y - r, 0), min(y + r + 1, h)
    if x0 >= x1 or y0 >= y1:
        return
    k = kernel[y0 - (y - r): y1 - (y - r), x0 - (x - r): x1 - (x - r)]
    canvas[y0:y1, x0:x1] += k[..., None] * color


def fire_color(t):
    """t: 0 (new) → 1 (old). White → yellow → orange → red → smoke."""
    stops = np.array([[1, 1, 0.9], [1, 0.85, 0.2], [1, 0.4, 0.05], [0.6, 0.1, 0.02], [0.1, 0.08, 0.08]])
    p = np.clip(t, 0, 0.999) * (len(stops) - 1)
    i = int(p)
    f = p - i
    return stops[i] * (1 - f) + stops[i + 1] * f


@st.cache_data(show_spinner="Simulating particles…")
def simulate(effect, n, frames, wind, gravity, seed, w=480, h=300):
    rng = np.random.default_rng(seed)
    out = []
    if effect == "Snow":
        bg = vertical_gradient((10, 20, 50), (40, 60, 100), w, h)
        pos = np.column_stack([rng.uniform(0, w, n), rng.uniform(0, h, n)])
        size = rng.uniform(0.4, 1.0, n)
        k = gaussian_kernel(3)
        for f in range(frames):
            canvas = bg.copy()
            pos[:, 0] += wind * 2 * size + np.sin(f / 6 + pos[:, 1] / 30) * 0.8
            pos[:, 1] += (1 + gravity) * 2.2 * size
            pos[:, 0] %= w
            pos[:, 1] %= h
            for (x, y), s in zip(pos, size):
                splat(canvas, x, y, np.array([1, 1, 1]) * s * 0.9, k)
            out.append(to_img(canvas))
    elif effect == "Fire":
        bg = vertical_gradient((5, 5, 10), (25, 15, 15), w, h)
        k = gaussian_kernel(10)
        P = np.zeros((0, 5))  # x, y, vx, vy, age
        life = 45
        per_frame = max(n // life, 1)
        for f in range(frames + life):  # warm-up so the fire is already burning
            new = np.column_stack([
                rng.normal(w / 2, 35, per_frame), np.full(per_frame, h - 15.0),
                rng.normal(0, 0.6, per_frame), rng.uniform(-4.5, -2.5, per_frame), np.zeros(per_frame)])
            P = np.vstack([P, new])
            P[:, 2] += wind * 0.15 + (w / 2 - P[:, 0]) * 0.004   # wind + pull to centre
            P[:, 3] -= 0.05 * (1 + gravity)                     # buoyancy
            P[:, 0] += P[:, 2]
            P[:, 1] += P[:, 3]
            P[:, 4] += 1
            P = P[P[:, 4] < life]
            if f >= life:
                canvas = bg.copy()
                for x, y, _, _, age in P:
                    t = age / life
                    splat(canvas, x, y, fire_color(t) * (1 - t) * 0.5, k)
                out.append(to_img(canvas))
    else:  # Explosion
        bg = vertical_gradient((15, 15, 25), (45, 40, 40), w, h)
        k = gaussian_kernel(4)
        ang = rng.uniform(0, 2 * np.pi, n)
        speed = rng.uniform(2, 9, n)
        pos = np.tile([w / 2, h / 2], (n, 1)).astype(float)
        vel = np.column_stack([np.cos(ang), np.sin(ang)]) * speed[:, None]
        for f in range(frames):
            canvas = bg.copy()
            if f < 4:  # initial flash
                yy, xx = np.mgrid[0:h, 0:w]
                flash = np.exp(-((xx - w / 2) ** 2 + (yy - h / 2) ** 2) / (2 * (40 + f * 25) ** 2))
                canvas += flash[..., None] * np.array([1, 0.8, 0.5]) * (1 - f / 4)
            vel *= 0.95                                  # air drag
            vel[:, 1] += 0.12 * (1 + gravity)            # gravity
            vel[:, 0] += wind * 0.05
            pos += vel
            t = f / frames
            for x, y in pos:
                splat(canvas, x, y, fire_color(t * 0.9) * (1 - t) * 0.8, k)
            out.append(to_img(canvas))
    return out


# ----------------------------------------------------------------------------
# Colour grading / finishing
# ----------------------------------------------------------------------------
def grade(img, temperature, tint, contrast, saturation, fog, vignette, grain, seed=0):
    out = img.copy()
    out[..., 0] *= 1 + temperature * 0.3
    out[..., 2] *= 1 - temperature * 0.3
    out[..., 1] *= 1 + tint * 0.2
    out = (out - 0.5) * contrast + 0.5
    lum = out @ np.array([0.299, 0.587, 0.114])
    out = lum[..., None] + (out - lum[..., None]) * saturation
    h, w = out.shape[:2]
    depth = np.linspace(1, 0, h)[:, None, None]  # fake depth: top of frame = far away
    out = out * (1 - fog * depth) + np.array([0.8, 0.85, 0.9]) * fog * depth
    yy, xx = np.mgrid[0:h, 0:w]
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    out *= (1 - vignette * np.clip(r - 0.4, 0, 1) ** 1.5)[..., None]
    out += np.random.default_rng(seed).normal(0, grain, out.shape)
    return np.clip(out, 0, 1)


# ----------------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------------
st.title("🎬 CGI & VFX Playground")
st.caption("Interactive demos of the techniques behind modern visual effects, written in pure Python.")

tabs = st.tabs(["📖 Overview", "🧊 3D CGI", "🟩 Green screen", "🔥 Particles", "🎨 Colour grading"])

# --- Overview ---------------------------------------------------------------
with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("CGI — Computer-Generated Imagery")
        st.write("Images created entirely in software: 3D models, digital characters, "
                 "procedural worlds and simulations.")
        st.markdown("- *Toy Story* (fully CGI film)\n- Gollum, Caesar (motion-capture characters)\n"
                    "- Pandora in *Avatar* (digital world)")
    with c2:
        st.subheader("VFX — Visual Effects")
        st.write("The wider craft of creating or altering imagery that can't be filmed for real. "
                 "CGI is one tool; compositing, keying and cleanup are others.")
        st.markdown("- Green-screen compositing\n- Explosions, fire, weather\n"
                    "- Colour grading, set extensions, wire removal")
    st.divider()
    st.markdown("""
| Tab | Technique | Real-world use |
|---|---|---|
| 🧊 3D CGI | Polygon meshes, shading, lighting, procedural terrain | Characters, props, environments |
| 🟩 Green screen | Chroma keying, mattes, spill suppression, compositing | Superhero films, weather reports |
| 🔥 Particles | Physics simulation of thousands of points | Fire, snow, explosions, magic |
| 🎨 Colour grading | Temperature, contrast, atmosphere, vignette, grain | Every film's final "look" |
""")

# --- 3D CGI -----------------------------------------------------------------
with tabs[1]:
    st.subheader("3D modelling, shading & lighting")
    st.write("Every CGI object starts as a **mesh** of polygons. A renderer then simulates how "
             "light bounces off its surface. Drag the model to orbit the camera.")
    left, right = st.columns([1, 3])
    with left:
        shape = st.selectbox("Model", ["Torus (donut)", "Sphere", "Twisted knot", "Procedural terrain"])
        res = st.slider("Mesh resolution (polygons)", 8, 120, 60,
                        help="Low values show how curved surfaces are approximated with flat faces.")
        view = st.radio("Render mode", ["Shaded", "Wireframe", "Both"], horizontal=True)
        palette = st.selectbox("Material colours", ["Viridis", "Plasma", "Cividis", "Earth", "Ice", "Hot"])
        st.markdown("**Lighting**")
        ambient = st.slider("Ambient", 0.0, 1.0, 0.4)
        diffuse = st.slider("Diffuse", 0.0, 1.0, 0.8)
        specular = st.slider("Specular (shininess)", 0.0, 2.0, 0.6)
        roughness = st.slider("Roughness", 0.0, 1.0, 0.4)
        light_angle = st.slider("Light direction (°)", 0, 360, 45)
        seed = st.number_input("Terrain seed", 0, 9999, 42) if shape == "Procedural terrain" else 0
    with right:
        X, Y, Z = make_shape(shape, res, seed)
        fig = go.Figure()
        if view in ("Shaded", "Both"):
            a = np.radians(light_angle)
            fig.add_trace(go.Surface(
                x=X, y=Y, z=Z, surfacecolor=Z, colorscale=palette, showscale=False,
                lighting=dict(ambient=ambient, diffuse=diffuse, specular=specular,
                              roughness=roughness, fresnel=0.2),
                lightposition=dict(x=1000 * np.cos(a), y=1000 * np.sin(a), z=800)))
        if view in ("Wireframe", "Both"):
            fig.add_trace(wireframe(X, Y, Z, step=max(res // 30, 1)))
        fig.update_layout(height=600, margin=dict(l=0, r=0, t=0, b=0), paper_bgcolor="#0e1117",
                          scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
                                     aspectmode="data", bgcolor="#0e1117"))
        st.plotly_chart(fig, width="stretch")
        st.caption(f"Mesh: {res}×{res} vertices ≈ {2 * (res - 1) ** 2:,} triangles")

# --- Green screen -----------------------------------------------------------
with tabs[2]:
    st.subheader("Chroma keying & compositing")
    st.write("The actor is filmed in front of a green screen. Software turns 'how green is this pixel' "
             "into a transparency **matte**, then layers the actor over a new background.")
    left, right = st.columns([1, 3])
    with left:
        fg_file = st.file_uploader("Your own green-screen image (optional)", type=["png", "jpg", "jpeg"])
        bg_choice = st.selectbox("New background", ["Sunset beach", "Outer space", "Alien planet", "Upload…"])
        bg_file = st.file_uploader("Background image", type=["png", "jpg", "jpeg"]) if bg_choice == "Upload…" else None
        low = st.slider("Key threshold (low)", 0.0, 0.5, 0.08, 0.01)
        high = st.slider("Key threshold (high)", 0.0, 0.8, 0.25, 0.01)
        spill = st.slider("Green spill suppression", 0.0, 1.0, 0.8)
    fg = to_float(Image.open(fg_file).resize((W, H))) if fg_file else make_greenscreen_plate()
    if bg_file:
        bg = to_float(Image.open(bg_file).resize((W, H)))
    else:
        bg = make_background("Sunset beach" if bg_choice == "Upload…" else bg_choice)
    comp, alpha = chroma_key(fg, bg, low, high, spill)
    with right:
        a, b = st.columns(2)
        a.image(to_img(fg), caption="1. Original plate (filmed on set)", width="stretch")
        b.image(to_img(np.repeat(alpha[..., None], 3, axis=2)), caption="2. Matte (white = keep)",
                width="stretch")
        a.image(to_img(bg), caption="3. Digital background", width="stretch")
        b.image(to_img(comp), caption="4. Final composite", width="stretch")
        buf = io.BytesIO()
        to_img(comp).save(buf, format="PNG")
        st.download_button("⬇️ Download composite", buf.getvalue(), "composite.png", "image/png")

# --- Particles --------------------------------------------------------------
with tabs[3]:
    st.subheader("Particle simulation")
    st.write("Fire, smoke, snow and explosions are made from thousands of tiny particles. Each frame, "
             "physics (velocity, gravity, wind, drag) moves them, and they are drawn with additive glow.")
    left, right = st.columns([1, 3])
    with left:
        effect = st.selectbox("Effect", ["Fire", "Snow", "Explosion"])
        n = st.slider("Particles", 50, 1200, 400, 50)
        frames = st.slider("Frames", 10, 60, 30)
        wind = st.slider("Wind", -3.0, 3.0, 0.5)
        gravity = st.slider("Gravity / buoyancy multiplier", -0.5, 2.0, 0.0)
        sim_seed = st.number_input("Random seed", 0, 9999, 3)
    with right:
        gif = show_gif(simulate(effect, n, frames, wind, gravity, sim_seed), duration_ms=50)
        st.download_button("⬇️ Download GIF", gif, f"{effect.lower()}.gif", "image/gif")

# --- Colour grading ---------------------------------------------------------
with tabs[4]:
    st.subheader("Colour grading & atmosphere")
    st.write("The final step: give the whole shot a consistent mood. These 'invisible' effects are "
             "in almost every film. Here they're applied to the green-screen composite.")
    left, right = st.columns([1, 3])
    with left:
        preset = st.selectbox("Preset", ["Custom", "Blockbuster teal & orange", "Cold thriller",
                                         "Vintage film", "Foggy morning"])
        presets = {
            "Blockbuster teal & orange": (0.4, -0.2, 1.25, 1.2, 0.0, 0.6, 0.0),
            "Cold thriller": (-0.6, 0.1, 1.15, 0.6, 0.1, 0.7, 0.02),
            "Vintage film": (0.35, 0.1, 0.85, 0.7, 0.0, 0.8, 0.06),
            "Foggy morning": (-0.1, 0.0, 0.9, 0.8, 0.6, 0.3, 0.01),
        }
        d = presets.get(preset, (0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0))
        temperature = st.slider("Temperature (cool ↔ warm)", -1.0, 1.0, d[0])
        tint = st.slider("Tint (magenta ↔ green)", -1.0, 1.0, d[1])
        contrast = st.slider("Contrast", 0.5, 2.0, d[2])
        saturation = st.slider("Saturation", 0.0, 2.0, d[3])
        fog = st.slider("Atmospheric fog", 0.0, 1.0, d[4])
        vignette = st.slider("Vignette", 0.0, 1.0, d[5])
        grain = st.slider("Film grain", 0.0, 0.1, d[6], 0.005)
    graded = grade(comp, temperature, tint, contrast, saturation, fog, vignette, grain)
    with right:
        a, b = st.columns(2)
        a.image(to_img(comp), caption="Before", width="stretch")
        b.image(to_img(graded), caption="After grading", width="stretch")
