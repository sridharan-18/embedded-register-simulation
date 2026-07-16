# Embedded Register Simulator ⭐⭐⭐⭐⭐

A comprehensive GPIO register simulator built with Python and Tkinter, designed for embedded systems education and development.

## Features

- **STM32-like Register Map**: Realistic register names and memory addresses
- **32-bit Registers**: All registers use 32-bit width matching STM32 ARM Cortex-M architecture
- **GPIO Register Simulation**: GPIOA and GPIOB port registers (MODER, ODR, IDR)
- **Peripheral Registers**: UART, SPI, ADC, and Timer control registers
- **Bit Operations**: Set, Clear, Toggle, and Read individual bits with visual feedback
- **Visual LEDs**: Real-time LED indicators showing the state of each register bit
- **Binary Register View**: Live binary representation of register values
- **Multiple Display Formats**: Binary, Decimal, and Hexadecimal display
- **Interrupt Simulation**: Enable/disable interrupts with callback logging
- **Multiple Registers**: Switch between different peripheral registers
- **Direct Value Input**: Set entire register values at once
- **Reset Function**: Reset register to zero with one click
- **Quick Access Buttons**: Toggle bits instantly with dedicated buttons
- **Live Memory Map**: Display all registers with addresses and current values
- **Memory-Mapped I/O**: Learn how peripherals are mapped to memory addresses

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

The simulator includes STM32-like registers with realistic memory addresses:

**GPIO Port A Registers:**
- **GPIOA_MODER (0x48000000)**: GPIOA Mode Register - Configures pin modes (input/output/alternate/analog)
- **GPIOA_ODR (0x48000014)**: GPIOA Output Data Register - Controls output pin states
- **GPIOA_IDR (0x48000010)**: GPIOA Input Data Register - Reads input pin states

**GPIO Port B Registers:**
- **GPIOB_ODR (0x48000414)**: GPIOB Output Data Register - Controls output pin states
- **GPIOB_IDR (0x48000410)**: GPIOB Input Data Register - Reads input pin states

**UART Registers:**
- **UART_CR1 (0x40011000)**: UART Control Register 1 - Configures UART settings
- **UART_SR (0x40011000)**: UART Status Register - Shows UART status flags

**SPI Registers:**
- **SPI_CR1 (0x40013000)**: SPI Control Register 1 - Configures SPI settings

**ADC Registers:**
- **ADC_CR (0x50000000)**: ADC Control Register - Controls ADC operations

**Timer Registers:**
- **TIM_CR1 (0x40000000)**: Timer Control Register 1 - Configures timer settings

All registers are 32-bit, matching the STM32 ARM Cortex-M architecture.

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

### Register Selection

- Select different peripheral registers from the dropdown
- All registers are 32-bit (STM32 ARM Cortex-M architecture)
- Memory addresses are displayed in hexadecimal format
- LED indicators and binary view show all 32 bits
- Bit position range is 0-31 for all registers

### Register Memory Map

The simulator includes a live memory map display that shows:
- All registers organized by peripheral type (GPIOA, GPIOB, UART, SPI, ADC, TIM)
- Memory addresses in hexadecimal format (e.g., 0x40020000)
- Current values of all registers
- Currently selected register highlighted with ">>>" marker

**Example Memory Map Display:**
```
ADC:
    0x50000000 ADC_CR = 0x00000000

GPIOA:
    0x48000000 GPIOA_MODER = 0x00000000
    0x48000010 GPIOA_IDR = 0x00000000
>>> 0x48000014 GPIOA_ODR = 0x00000000

GPIOB:
    0x48000410 GPIOB_IDR = 0x00000000
    0x48000414 GPIOB_ODR = 0x00000000

SPI:
    0x40013000 SPI_CR1 = 0x00000000

TIM:
    0x40000000 TIM_CR1 = 0x00000000

UART:
    0x40011000 UART_CR1 = 0x00000000
    0x40011000 UART_SR = 0x00000000
```

This helps students understand **memory-mapped I/O** concepts used in embedded systems.

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
- **Address Display**: Shows realistic STM32 memory addresses

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
