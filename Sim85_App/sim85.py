from ui.mainwindow import  MainWindow

MainAppWindow = MainWindow()
memory_mock_data = []
port_mock_data = []
for i in range(0,100):
    memory_mock_data.append([i,255])
    port_mock_data.append([i, 193])
MainAppWindow.HardwarePanel.memory_panel.load_hex_data(data_2d_list=memory_mock_data,has_address_column=True)
MainAppWindow.HardwarePanel.ports_panel.load_hex_data(data_2d_list=memory_mock_data,has_address_column=True)
MainAppWindow.AssemblerOut.print_success(message="i85 Simulator & IDE Initialized.")
MainAppWindow.AssemblerOut.print_success(message="asm85 Assembler Ready.")
MainAppWindow.AssemblerOut.print_success(message="Press run to start assembly")
MainAppWindow.mainloop()

