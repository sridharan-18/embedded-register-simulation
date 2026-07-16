# Embedded Register Simulator ⭐⭐⭐⭐⭐

A comprehensive GPIO register simulator built with Python and Tkinter, designed for embedded systems education and development.

## Features

- **Multiple Register Sizes**: Support for 8-bit, 16-bit, and 32-bit registers
- **GPIO Register Simulation**: Simulate multiple registers with different bit widths
- **Bit Operations**: Set, Clear, Toggle, and Read individual bits with visual feedback
- **Visual LEDs**: Real-time LED indicators showing the state of each register bit
- **Binary Register View**: Live binary representation of register values
- **Multiple Display Formats**: Binary, Decimal, and Hexadecimal display
- **Interrupt Simulation**: Enable/disable interrupts with callback logging
- **Multiple Registers**: Switch between different registers (8-bit, 16-bit, 32-bit)
- **Direct Value Input**: Set entire register values at once
- **Reset Function**: Reset register to zero with one click
- **Quick Access Buttons**: Toggle bits instantly with dedicated buttons

## Tech Stack

- **Language**: Python 3
- **GUI Framework**: Tkinter (built-in)
- **Architecture**: Object-oriented design with separate classes for Register, LED, BinaryView, and GUI

## Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sridharan-18/embedded-register-simulator.git
cd embedded-register-simulator
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Running the Simulator

```bash
python register_simulator.py
```

### Register Types

The simulator includes registers of different sizes:

**8-bit Registers:**
- **REG8_0 (0x00)**: 8-bit general-purpose register
- **REG8_1 (0x01)**: 8-bit general-purpose register

**16-bit Registers:**
- **REG16_0 (0x10)**: 16-bit general-purpose register
- **REG16_1 (0x12)**: 16-bit general-purpose register

**32-bit Registers:**
- **REG32_0 (0x20)**: 32-bit general-purpose register
- **REG32_1 (0x24)**: 32-bit general-purpose register

### Bit Operations

1. **Set Bit**: Sets a specific bit to 1
   - Enter bit position (0 to size-1)
   - Click "Set Bit"

2. **Clear Bit**: Sets a specific bit to 0
   - Enter bit position (0 to size-1)
   - Click "Clear Bit"

3. **Toggle Bit**: Flips a specific bit
   - Enter bit position (0 to size-1)
   - Click "Toggle Bit"
   - Or use quick access buttons (B0-Bn)

4. **Read Bit**: Reads the value of a specific bit
   - Enter bit position (0 to size-1)
   - Click "Read Bit"
   - Displays the bit value in a popup

### Direct Value Input

- Enter a value (0 to max based on register size) in the "Direct Value" field
- Click "Set Value" to update the entire register
- Click "Reset" to reset all bits to 0

### Register Size Selection

- Select different registers from the dropdown
- The GUI automatically adapts to the register size (8, 16, or 32 bits)
- LED indicators and binary view update accordingly
- Bit position limits adjust based on register size

### Interrupt Simulation

1. Check "Enable Interrupts" to activate interrupt callbacks
2. Any register change will trigger an interrupt event
3. View interrupt events in the Interrupt Log
4. Click "Manual Interrupt" to test interrupt handling
5. Click "Clear Log" to clear the interrupt history

### Visual Feedback

- **LED Indicators**: Green LEDs indicate bit=1, dark LEDs indicate bit=0
- **Binary View**: Shows real-time binary representation
- **Value Display**: Shows hexadecimal, decimal, and binary values
- **Interrupt Log**: Timestamped log of all interrupt events
- **Size Indicator**: Shows current register bit width (8/16/32-bit)

## Architecture

### Class Structure

- **Register**: Core register class with bit manipulation methods
- **LEDIndicator**: Visual LED display component
- **BinaryView**: Binary representation display
- **InterruptLogger**: Event logging for interrupts
- **RegisterSimulatorGUI**: Main application GUI

### Key Methods

```python
# Register operations
register.set_bit(bit_position)    # Set bit to 1
register.clear_bit(bit_position)  # Set bit to 0
register.toggle_bit(bit_position) # Flip bit
register.get_bit(bit_position)    # Read bit value
register.set_value(value)         # Set entire register
register.reset()                  # Reset register to 0
register.get_binary_string()      # Get binary representation
register.get_hex_string()         # Get hexadecimal representation
```

## Example Use Cases

### Education

- Learn about register-based programming
- Understand bit manipulation operations
- Visualize GPIO pin states

### Development

- Test register logic before hardware implementation
- Simulate interrupt handling
- Debug bit-level operations

### Prototyping

- Plan register layouts
- Design interrupt schemes
- Validate bit field configurations

## Screenshots

The simulator provides:
- Real-time visual feedback
- Multiple register support
- Comprehensive interrupt logging
- Intuitive bit manipulation interface

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open source and available for educational purposes.

## Author

Created by [sridharan-18](https://github.com/sridharan-18)

## Acknowledgments

- Built with Python's Tkinter for cross-platform compatibility
- Inspired by embedded systems development tools
- Designed for embedded systems education
