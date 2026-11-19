import customtkinter as ctk
import tkinter.font as tkfont
from tkinter import ttk


class AppTableView(ctk.CTkFrame):
    """
    A high-performance CustomTkinter-compatible table widget using ttk.Treeview.
    Supports dynamic sizing based on visible row count, custom headers, zero borders,
    zebra striping, column padding, blended scrollbar, and 255+ row batch optimization.
    Populates exclusively through load_hex_data.
    """

    def __init__(
            self,
            master,
            columns=None,
            headers=None,
            font=None,
            row_count=10,
            row_pad=4,
            col_pad=12,
            **kwargs
    ):
        kwargs.setdefault("border_width", 0)
        kwargs.setdefault("corner_radius", 0)
        kwargs.setdefault("fg_color", "#242424")
        super().__init__(master, **kwargs)

        self.font = font
        self.row_pad = row_pad
        self.col_pad = col_pad
        self.row_count = row_count

        if columns is None:
            self.cols = ["Address", "Data"]
        else:
            self.cols = list(columns)

        if headers is not None:
            self.headers = list(headers)
        else:
            self.headers = self.cols

        # Configure TTK Style for dark mode integration
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Determine exact font metrics so row height scales accurately with text
        measured_font = tkfont.Font(font=self.font) if self.font else tkfont.nametofont("TkDefaultFont")
        font_height = measured_font.metrics("linespace")
        self.calculated_rowheight = font_height + (self.row_pad * 2)

        # Remove outer borders and element borders entirely
        self.style.layout("AppTable.Treeview", [("AppTable.Treeview.treearea", {"sticky": "nswe"})])

        style_treeview_kwargs = {
            "background": "#242424",
            "foreground": "white",
            "fieldbackground": "#242424",
            "borderwidth": 0,
            "highlightthickness": 0,
            "relief": "flat",
            "rowheight": self.calculated_rowheight,
        }
        style_heading_kwargs = {
            "background": "#1f1f1f",
            "foreground": "white",
            "borderwidth": 0,
            "relief": "flat",
            "padding": (self.col_pad, self.row_pad),
        }

        if self.font:
            style_treeview_kwargs["font"] = self.font
            style_heading_kwargs["font"] = self.font

        self.style.configure("AppTable.Treeview", **style_treeview_kwargs)
        self.style.configure("AppTable.Treeview.Heading", **style_heading_kwargs)
        self.style.map(
            "AppTable.Treeview.Heading",
            background=[("active", "#333333")]
        )
        self.style.map(
            "AppTable.Treeview",
            background=[("selected", "#404040")],
            foreground=[("selected", "white")]
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Sizing height to row_count displays that exact number of rows before scrolling
        self.tree = ttk.Treeview(
            self,
            columns=self.cols,
            show="headings",
            style="AppTable.Treeview",
            selectmode="browse",
            height=self.row_count
        )

        for idx, col in enumerate(self.cols):
            header_text = self.headers[idx] if idx < len(self.headers) else col
            self.tree.heading(col, text=header_text, anchor="center")
            self.tree.column(col, anchor="center", width=120 + (self.col_pad * 2), minwidth=80)

        self.tree.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        # Blended scrollbar matching background palette with zero margins
        self.scrollbar = ctk.CTkScrollbar(
            self,
            orientation="vertical",
            command=self.tree.yview,
            fg_color="#242424",
            button_color="#363636",
            button_hover_color="#484848",
            width=15,
            corner_radius=5
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns", padx=0, pady=0)

        self.tree.tag_configure("evenrow", background="#242424")
        self.tree.tag_configure("oddrow", background="#2a2a2a")

    def load_hex_data(self, data_2d_list, has_address_column=False, pad_with_zeros=False):
        """Instantly loads and maps hex data into table rows, optimized for 255+ rows."""
        self.tree.delete(*self.tree.get_children())

        target_col_count = len(self.cols) - 1
        pad_val = "0x00" if pad_with_zeros else ""
        insert = self.tree.insert

        # Pre-process rows before passing to tkinter C-bindings
        for i, row_data in enumerate(data_2d_list):
            if has_address_column and len(row_data) > 0:
                raw_addr = row_data[0]
                addr_str = f"0x{raw_addr:04X}" if isinstance(raw_addr, int) else str(raw_addr)
                data_values = row_data[1:]
            else:
                addr_str = f"0x{i * 4:04X}"
                data_values = row_data

            converted_row = []
            for val in data_values:
                if isinstance(val, int):
                    converted_row.append(f"0x{val:02X}")
                elif val is not None and str(val).strip() != "":
                    try:
                        s_val = str(val)
                        int_val = int(s_val, 16) if s_val.startswith("0x") else int(s_val)
                        converted_row.append(f"0x{int_val:02X}")
                    except ValueError:
                        converted_row.append(str(val))
                else:
                    converted_row.append(pad_val)

            diff = target_col_count - len(converted_row)
            if diff > 0:
                converted_row.extend([pad_val] * diff)
            else:
                converted_row = converted_row[:target_col_count]

            tag = "evenrow" if i % 2 == 0 else "oddrow"
            insert("", "end", values=[addr_str] + converted_row, tags=(tag,))

    def clear_table(self):
        """Removes all rows."""
        self.tree.delete(*self.tree.get_children())

    def set_cell_font(self, font):
        """Dynamically updates cell and header fonts and recalculates row height."""
        self.font = font
        measured_font = tkfont.Font(font=self.font) if self.font else tkfont.nametofont("TkDefaultFont")
        font_height = measured_font.metrics("linespace")
        self.calculated_rowheight = font_height + (self.row_pad * 2)

        self.style.configure("AppTable.Treeview", font=self.font or "", rowheight=self.calculated_rowheight)
        self.style.configure("AppTable.Treeview.Heading", font=self.font or "")

    def get_widget(self):
        return self.tree