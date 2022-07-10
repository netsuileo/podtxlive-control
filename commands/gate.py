NOISE_GATE_ENABLE = {
    "description": "0~63=Off ; 64~127=On",
    "command": "22",
    "min": "0",
    "max": "127",
    "name": "Noise Gate Enable",
}
GATE_THRESHOLD = {
    "description": "0<>31=-96dB, 32=-96dB...127=0dB",
    "command": "23",
    "min": "32",
    "max": "127",
    "name": "Gate Threshold",
}
GATE_DECAY_TIME = {
    "description": "0=.1msec; 127=3000msec",
    "command": "24",
    "min": "0",
    "max": "127",
    "name": "Gate Decay Time",
}