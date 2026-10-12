# FSM Designs in Verilog and SystemVerilog

This repository contains five finite state machine designs, each written in both Verilog and SystemVerilog and verified in Xilinx Vivado. Every design also has a browser-based simulation that shows the state diagram, the inputs and outputs, and a timing waveform as the clock advances.

## Designs

| Design | Description | Simulation |
|---|---|---|
| Lock_Door | 3-bit serial password lock, one-hot encoded | [lock_door_fsm.html](https://lucabrasis.github.io/FSM/Simulations/lock_door_fsm.html) |
| Array2_Detector | Detects the sequences 1101 and 1011 in a serial bit stream, including overlapping matches | [array2_detector.html](https://lucabrasis.github.io/FSM/Simulations/array2_detector.html) |
| Elevator Controller | 4-floor elevator, 9-state Moore machine with door sensor and emergency stop | [elevator-fsm-explorer.html](https://lucabrasis.github.io/FSM/Simulations/elevator-fsm-explorer.html) |
| FIFO | Synchronous FIFO, 8 entries of 8 bits, with full and empty flags | [sync_fifo_explorer.html](https://lucabrasis.github.io/FSM/Simulations/sync_fifo_explorer.html) |
| Toggle_LED | Counter-based clock divider driving a blinking LED | [toggle_led_explorer.html](https://lucabrasis.github.io/FSM/Simulations/toggle_led_explorer.html) |

## Verification

Each module has its own testbench. In addition, `SystemVerilog/ALL_TB.sv` runs all five modules in a single simulation and covers both passing and failing cases: a correct and a wrong password, sequence hits and misses, FIFO overflow and underflow, an obstacle at the elevator door and an emergency stop.

Behavioral simulation of `ALL_TB` in Vivado:

![Vivado waveform](vivado_sim/RESULT.png)

Console output of the same run:

![Vivado console output](vivado_sim/Results_Sum.png)

## Browser simulations

The files in `Simulations/` run in any modern browser without installation. You can drive the inputs, step the clock one edge at a time or let it run, and follow the active state on the diagram. The explanations panel replays successful and failing scenarios for each design. The interface is available in Turkish and English.

## Repository layout

```
Verilog/          Verilog-2001 modules and testbenches
SystemVerilog/    SystemVerilog modules, testbenches and ALL_TB.sv
Simulations/      Browser-based simulations
vivado_sim/       Vivado simulation screenshots
```

## Tools

Xilinx Vivado 2025.2 (xsim) for simulation. The browser simulations are plain HTML and JavaScript.
