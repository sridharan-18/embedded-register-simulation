#!/usr/bin/env python3
"""
Embedded Register Simulator
A comprehensive GPIO register simulator with visual feedback and interrupt simulation
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Callable


class Register:
    """Represents a hardware register with bit operations"""
    
    def __init__(self, name: str, size: int = 8, address: int = 0x00):
        self.name = name
        self.size = size
        self.address = address
        self.value = 0
        self.interrupt_enabled = False
        self.interrupt_callback: Callable = None
    
    def set_bit(self, bit_position: int) -> None:
        """Set a specific bit (1)"""
        if 0 <= bit_position < self.size:
            self.value |= (1 << bit_position)
            self._check_interrupt()
    
    def clear_bit(self, bit_position: int) -> None:
        """Clear a specific bit (0)"""
        if 0 <= bit_position < self.size:
            self.value &= ~(1 << bit_position)
            self._check_interrupt()
    
    def toggle_bit(self, bit_position: int) -> None:
        """Toggle a specific bit"""
        if 0 <= bit_position < self.size:
            self.value ^= (1 << bit_position)
            self._check_interrupt()
    
    def get_bit(self, bit_position: int) -> int:
        """Get the value of a specific bit"""
        if 0 <= bit_position < self.size:
            return (self.value >> bit_position) & 1
        return 0
    
    def set_value(self, value: int) -> None:
        """Set the entire register value"""
        self.value = value & ((1 << self.size) - 1)
        self._check_interrupt()
    
    def get_binary_string(self) -> str:
        """Get binary representation of the register"""
        return format(self.value, f'0{self.size}b')
    
    def get_hex_string(self) -> str:
        """Get hexadecimal representation of the register"""
        hex_digits = max(1, self.size // 4)
        return format(self.value, f'0{hex_digits}X')
    
    def reset(self) -> None:
        """Reset register to 0"""
        self.value = 0
        self._check_interrupt()
    
    def enable_interrupt(self, callback: Callable) -> None:
        """Enable interrupt with callback function"""
        self.interrupt_enabled = True
        self.interrupt_callback = callback
    
    def disable_interrupt(self) -> None:
        """Disable interrupt"""
        self.interrupt_enabled = False
        self.interrupt_callback = None
    
    def _check_interrupt(self) -> None:
        """Check if interrupt should be triggered"""
        if self.interrupt_enabled and self.interrupt_callback:
            self.interrupt_callback(self.name, self.value)


class LEDIndicator:
    """Visual LED indicator for register bits"""
    
    def __init__(self, parent, size: int = 8):
        self.frame = ttk.Frame(parent)
        self.leds: List[tk.Canvas] = []
        self.size = size
        
        for i in range(size):
            led = tk.Canvas(self.frame, width=30, height=30, bg='#2d2d2d', 
                          highlightthickness=1, highlightbackground='#444')
            led.grid(row=0, column=size - 1 - i, padx=2, pady=2)
            self.leds.append(led)
            
            # Add bit label
            label = ttk.Label(self.frame, text=f'B{i}', font=('Arial', 8))
            label.grid(row=1, column=size - 1 - i)
    
    def update(self, value: int) -> None:
        """Update LED states based on register value"""
        for i, led in enumerate(self.leds):
            bit_value = (value >> i) & 1
            if bit_value:
                led.config(bg='#00ff00', highlightbackground='#00ff00')  # Green for ON
            else:
                led.config(bg='#2d2d2d', highlightbackground='#444')  # Dark for OFF
    
    def pack(self, **kwargs) -> None:
        """Pack the LED frame"""
        self.frame.pack(**kwargs)


class BinaryView:
    """Binary representation display for register"""
    
    def __init__(self, parent, size: int = 8):
        self.frame = ttk.Frame(parent)
        self.size = size
        self.labels: List[ttk.Label] = []
        
        for i in range(size):
            label = ttk.Label(self.frame, text='0', font=('Courier New', 14, 'bold'),
                             foreground='#00ff00', background='#1e1e1e', width=2)
            label.grid(row=0, column=size - 1 - i, padx=1)
            self.labels.append(label)
            
            # Add bit position label
            pos_label = ttk.Label(self.frame, text=str(i), font=('Arial', 8))
            pos_label.grid(row=1, column=size - 1 - i)
    
    def update(self, value: int) -> None:
        """Update binary display"""
        binary_str = format(value, f'0{self.size}b')
        for i, char in enumerate(binary_str):
            bit_pos = self.size - 1 - i
            self.labels[bit_pos].config(text=char)
    
    def pack(self, **kwargs) -> None:
        """Pack the binary view frame"""
        self.frame.pack(**kwargs)


class InterruptLogger:
    """Log interrupt events"""
    
    def __init__(self, parent):
        self.frame = ttk.LabelFrame(parent, text="Interrupt Log")
        self.text = tk.Text(self.frame, height=8, width=50, 
                           bg='#1e1e1e', fg='#00ff00', font=('Courier New', 9))
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)
    
    def log(self, message: str) -> None:
        """Log an interrupt event"""
        self.text.insert(tk.END, f"> {message}\n")
        self.text.see(tk.END)
    
    def clear(self) -> None:
        """Clear the log"""
        self.text.delete(1.0, tk.END)
    
    def pack(self, **kwargs) -> None:
        """Pack the logger frame"""
        self.frame.pack(**kwargs)


class RegisterSimulatorGUI:
    """Main GUI for the Register Simulator"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Embedded Register Simulator")
        self.root.geometry("900x700")
        self.root.configure(bg='#2d2d2d')
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#2d2d2d')
        self.style.configure('TLabel', background='#2d2d2d', foreground='white')
        self.style.configure('TLabelFrame', background='#2d2d2d', foreground='white')
        self.style.configure('TLabelFrame.Label', background='#2d2d2d', foreground='white')
        self.style.configure('TButton', background='#444', foreground='white')
        self.style.configure('TEntry', fieldbackground='#444', foreground='white')
        
        # Initialize registers with different sizes
        self.registers: Dict[str, Register] = {
            'REG8_0':  Register('REG8_0', 8, 0x00),   # 8-bit register
            'REG8_1':  Register('REG8_1', 8, 0x01),   # 8-bit register
            'REG16_0': Register('REG16_0', 16, 0x10),  # 16-bit register
            'REG16_1': Register('REG16_1', 16, 0x12),  # 16-bit register
            'REG32_0': Register('REG32_0', 32, 0x20),  # 32-bit register
            'REG32_1': Register('REG32_1', 32, 0x24),  # 32-bit register
        }
        
        self.current_register = self.registers['REG8_0']
        self.current_size = 8
        
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Register selection
        reg_frame = ttk.LabelFrame(main_frame, text="Register Selection")
        reg_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(reg_frame, text="Select Register:").pack(side=tk.LEFT, padx=5)
        self.reg_var = tk.StringVar(value='REG8_0')
        reg_combo = ttk.Combobox(reg_frame, textvariable=self.reg_var, 
                                values=list(self.registers.keys()), state='readonly')
        reg_combo.pack(side=tk.LEFT, padx=5)
        reg_combo.bind('<<ComboboxSelected>>', self.on_register_change)
        
        # Address display
        self.addr_label = ttk.Label(reg_frame, text=f"Address: 0x{self.current_register.address:02X}")
        self.addr_label.pack(side=tk.LEFT, padx=20)
        
        # Size display
        self.size_label = ttk.Label(reg_frame, text=f"Size: {self.current_register.size}-bit")
        self.size_label.pack(side=tk.LEFT, padx=20)
        
        # Visual LED display
        self.led_frame = ttk.LabelFrame(main_frame, text="LED Indicators")
        self.led_frame.pack(fill=tk.X, pady=5)
        
        self.led_display = LEDIndicator(self.led_frame, self.current_size)
        self.led_display.pack(pady=10)
        
        # Binary view
        self.binary_frame = ttk.LabelFrame(main_frame, text="Binary View")
        self.binary_frame.pack(fill=tk.X, pady=5)
        
        self.binary_view = BinaryView(self.binary_frame, self.current_size)
        self.binary_view.pack(pady=10)
        
        # Value display
        value_frame = ttk.LabelFrame(main_frame, text="Register Value")
        value_frame.pack(fill=tk.X, pady=5)
        
        self.hex_label = ttk.Label(value_frame, text="HEX: 0x00", font=('Courier New', 12, 'bold'))
        self.hex_label.pack(side=tk.LEFT, padx=20)
        
        self.dec_label = ttk.Label(value_frame, text="DEC: 0", font=('Courier New', 12, 'bold'))
        self.dec_label.pack(side=tk.LEFT, padx=20)
        
        # Bit operations
        bit_frame = ttk.LabelFrame(main_frame, text="Bit Operations")
        bit_frame.pack(fill=tk.X, pady=5)
        
        # Bit selection
        self.bit_pos_label = ttk.Label(bit_frame, text=f"Bit Position (0-{self.current_size-1}):")
        self.bit_pos_label.grid(row=0, column=0, padx=5, pady=5)
        self.bit_entry = ttk.Entry(bit_frame, width=5)
        self.bit_entry.grid(row=0, column=1, padx=5, pady=5)
        self.bit_entry.insert(0, '0')
        
        # Operation buttons
        ttk.Button(bit_frame, text="Set Bit", command=self.set_bit).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(bit_frame, text="Clear Bit", command=self.clear_bit).grid(row=0, column=3, padx=5, pady=5)
        ttk.Button(bit_frame, text="Toggle Bit", command=self.toggle_bit).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(bit_frame, text="Read Bit", command=self.read_bit).grid(row=0, column=5, padx=5, pady=5)
        
        # Direct value input
        max_val = (1 << self.current_size) - 1
        self.value_label = ttk.Label(bit_frame, text=f"Direct Value (0-{max_val}):")
        self.value_label.grid(row=1, column=0, padx=5, pady=5)
        self.value_entry = ttk.Entry(bit_frame, width=8)
        self.value_entry.grid(row=1, column=1, padx=5, pady=5)
        self.value_entry.insert(0, '0')
        ttk.Button(bit_frame, text="Set Value", command=self.set_value).grid(row=1, column=2, padx=5, pady=5)
        ttk.Button(bit_frame, text="Reset", command=self.reset_register).grid(row=1, column=3, padx=5, pady=5)
        
        # Quick bit buttons
        self.quick_frame = ttk.LabelFrame(main_frame, text="Quick Bit Access")
        self.quick_frame.pack(fill=tk.X, pady=5)
        self.quick_buttons = []
        
        self.create_quick_buttons()
        
        # Interrupt controls
        int_frame = ttk.LabelFrame(main_frame, text="Interrupt Control")
        int_frame.pack(fill=tk.X, pady=5)
        
        self.interrupt_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(int_frame, text="Enable Interrupts", variable=self.interrupt_var,
                       command=self.toggle_interrupt).pack(side=tk.LEFT, padx=10)
        
        ttk.Button(int_frame, text="Manual Interrupt", command=self.manual_interrupt).pack(side=tk.LEFT, padx=10)
        
        # Interrupt logger
        self.interrupt_logger = InterruptLogger(main_frame)
        self.interrupt_logger.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Clear log button
        ttk.Button(main_frame, text="Clear Log", command=self.interrupt_logger.clear).pack(pady=5)
        
        # Enable interrupts for current register
        self.current_register.enable_interrupt(self.interrupt_callback)
    
    def create_quick_buttons(self):
        """Create quick access buttons for bits based on current register size"""
        # Clear existing buttons
        for btn in self.quick_buttons:
            btn.destroy()
        self.quick_buttons.clear()
        
        # Create new buttons
        for i in range(self.current_size):
            btn = ttk.Button(self.quick_frame, text=f'B{i}', width=4,
                           command=lambda bit=i: self.toggle_bit_direct(bit))
            btn.grid(row=0, column=i, padx=2, pady=5)
            self.quick_buttons.append(btn)
    
    def on_register_change(self, event):
        """Handle register selection change"""
        reg_name = self.reg_var.get()
        self.current_register = self.registers[reg_name]
        self.current_size = self.current_register.size
        
        # Update address and size labels
        self.addr_label.config(text=f"Address: 0x{self.current_register.address:02X}")
        self.size_label.config(text=f"Size: {self.current_register.size}-bit")
        
        # Recreate LED and BinaryView with new size
        self.led_display.frame.destroy()
        self.led_display = LEDIndicator(self.led_frame, self.current_size)
        self.led_display.pack(pady=10)
        
        self.binary_view.frame.destroy()
        self.binary_view = BinaryView(self.binary_frame, self.current_size)
        self.binary_view.pack(pady=10)
        
        # Update bit position label
        self.bit_pos_label.config(text=f"Bit Position (0-{self.current_size-1}):")
        
        # Update value label
        max_val = (1 << self.current_size) - 1
        self.value_label.config(text=f"Direct Value (0-{max_val}):")
        
        # Recreate quick buttons
        self.create_quick_buttons()
        
        # Re-enable interrupt if it was enabled
        if self.interrupt_var.get():
            self.current_register.enable_interrupt(self.interrupt_callback)
        
        self.update_display()
    
    def set_bit(self):
        """Set a specific bit"""
        try:
            bit = int(self.bit_entry.get())
            if 0 <= bit < self.current_size:
                self.current_register.set_bit(bit)
                self.update_display()
            else:
                messagebox.showerror("Error", f"Bit position must be between 0 and {self.current_size-1}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bit position")
    
    def clear_bit(self):
        """Clear a specific bit"""
        try:
            bit = int(self.bit_entry.get())
            if 0 <= bit < self.current_size:
                self.current_register.clear_bit(bit)
                self.update_display()
            else:
                messagebox.showerror("Error", f"Bit position must be between 0 and {self.current_size-1}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bit position")
    
    def toggle_bit(self):
        """Toggle a specific bit"""
        try:
            bit = int(self.bit_entry.get())
            if 0 <= bit < self.current_size:
                self.current_register.toggle_bit(bit)
                self.update_display()
            else:
                messagebox.showerror("Error", f"Bit position must be between 0 and {self.current_size-1}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bit position")
    
    def read_bit(self):
        """Read a specific bit"""
        try:
            bit = int(self.bit_entry.get())
            if 0 <= bit < self.current_size:
                bit_value = self.current_register.get_bit(bit)
                messagebox.showinfo("Bit Read", f"Bit {bit} value: {bit_value}")
            else:
                messagebox.showerror("Error", f"Bit position must be between 0 and {self.current_size-1}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid bit position")
    
    def toggle_bit_direct(self, bit):
        """Toggle a bit directly from quick access buttons"""
        self.current_register.toggle_bit(bit)
        self.bit_entry.delete(0, tk.END)
        self.bit_entry.insert(0, str(bit))
        self.update_display()
    
    def set_value(self):
        """Set the entire register value"""
        try:
            value = int(self.value_entry.get())
            max_val = (1 << self.current_size) - 1
            if 0 <= value <= max_val:
                self.current_register.set_value(value)
                self.update_display()
            else:
                messagebox.showerror("Error", f"Value must be between 0 and {max_val}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid value")
    
    def reset_register(self):
        """Reset register to 0"""
        self.current_register.reset()
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, '0')
        self.update_display()
    
    def toggle_interrupt(self):
        """Toggle interrupt enable/disable"""
        if self.interrupt_var.get():
            self.current_register.enable_interrupt(self.interrupt_callback)
            self.interrupt_logger.log(f"Interrupt enabled for {self.current_register.name}")
        else:
            self.current_register.disable_interrupt()
            self.interrupt_logger.log(f"Interrupt disabled for {self.current_register.name}")
    
    def manual_interrupt(self):
        """Trigger a manual interrupt"""
        self.interrupt_logger.log(f"Manual interrupt triggered on {self.current_register.name}")
        messagebox.showinfo("Interrupt", f"Interrupt triggered on {self.current_register.name}")
    
    def interrupt_callback(self, reg_name: str, value: int):
        """Callback function for interrupts"""
        hex_digits = max(1, self.current_size // 4)
        self.interrupt_logger.log(f"Interrupt: {reg_name} changed to 0x{value:0{hex_digits}X}")
    
    def update_display(self):
        """Update all display elements"""
        value = self.current_register.value
        
        # Update LEDs
        self.led_display.update(value)
        
        # Update binary view
        self.binary_view.update(value)
        
        # Update value labels
        self.hex_label.config(text=f"HEX: {self.current_register.get_hex_string()}")
        self.dec_label.config(text=f"DEC: {value}")
        
        # Update value entry
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, str(value))


def main():
    """Main entry point"""
    root = tk.Tk()
    app = RegisterSimulatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
