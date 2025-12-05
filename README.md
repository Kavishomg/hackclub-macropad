# The Orbital Control Station 🛰️
### A Custom 5-Key Macropad with OLED & Rotary Control

Welcome to my submission for **Hack Club Blueprint**! This isn't just a keypad; it's a fully custom-engineered "Mission Control" designed to handle media, macros, and workflow shortcuts with style.

I designed this from scratch using **KiCad** for the electronics and **Onshape** for the mechanical enclosure, ensuring a perfect fit between the digital and physical worlds.

---

## 📸 1. The Full Assembly
*The complete vision: Custom PCB meets Parametric Case.*

![Full Assembly](images/assembly.png)
*(Note to Reviewer: This STEP file is available in the CAD folder as Macropad_Assembly.step)*

---

## 🚀 Why I Built This
I wanted a device that did more than just click. I needed a controller that could give me visual feedback and precise analog control. 

This project combines my interests in **electronics, 3D design, and embedded firmware**. It features:
* **Visual Feedback:** A 0.91" OLED screen to display layers and modes.
* **Analog Input:** A Rotary Encoder for precise volume or scrolling control.
* **Aesthetics:** Underglow RGB lighting tucked between the switches.
* **Ergonomics:** A high-profile, 3D-printed case designed with 5mm clearances for Cherry MX switches.

---

## ⚡ 2. The Electronics (Schematic)
I designed the circuit around the **Seeed XIAO RP2040** because of its powerful dual-core processor and CircuitPython support. The schematic ensures no pin conflicts while maximizing the limited I/O.

![Schematic](images/schematic.png)

* **MCU:** Seeed XIAO RP2040
* **Display Protocol:** I2C (Pins D4/D5)
* **Lighting:** PWM/Data driver for SK6812 LEDs

---

## 📟 3. The PCB Design
This was routed in KiCad 8.0. I utilized a **Ground Pour** on both top and bottom layers to ensure signal stability and reduce noise.

![PCB Layout](images/pcb.png)

* **Mounting:** 4x M3 Holes aligned to the case standoffs.
* **Placement:** Symmetric layout with the Rotary Encoder as the centerpiece.
* **Lighting:** LEDs are strategically placed in the gaps between switches to create a diffuse glow.

---

## 📦 4. The Mechanical Case
Designed in **Onshape**. This is a 3D-printable case featuring a **1.6mm integrated top plate** to perfectly snap-fit Cherry MX switches.

![Case Design](images/case.png)

* **Material:** PLA / PETG
* **Wall Thickness:** 3mm for structural rigidity.
* **Clearance:** 5mm standoff height to protect the PCB underside.
* **Access:** Precision cutout for USB-C cable.

---

## 🧾 5. Bill of Materials (BOM)
I have adhered strictly to the Hack Club "Allowed Parts List" for the core components.

| Component | Quantity | Description |
| :--- | :--- | :--- |
| **Microcontroller** | 1 | Seeed XIAO RP2040 |
| **Switches** | 5 | Cherry MX Style Mechanical Switches |
| **Input** | 1 | EC11 Rotary Encoder |
| **Display** | 1 | 0.91" OLED Display (I2C) |
| **Lighting** | 2 | SK6812 MINI-E RGB LEDs |
| **Case** | 1 | Custom 3D Printed Enclosure (STL/STEP provided) |
| **Hardware** | 4 | M3 Screws |

---

## 🐍 Firmware Plan
The board will run on **KMK Firmware** (CircuitPython). This allows for dynamic key remapping and OLED layer display without recompiling code.

**Planned Keymap:**
* **Encoder:** Volume Up/Down (Press to Mute)
* **OLED:** Displays current "Layer" (e.g., Media, Editing, Gaming)
* **Keys:** Play/Pause, Next, Prev, Copy, Paste

*(Placeholder code is available in the Firmware folder)*

---

### Acknowledgments
Huge thanks to the **Hack Club Blueprint** team for making hardware engineering accessible!
