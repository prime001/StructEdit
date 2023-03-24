import tkinter as tk
import json
import yaml
import parser
from tkinter import filedialog


class StructEdit:
    def __init__(self, json_data=None, yaml_data=None):
        self.root = tk.Tk()
        self.root.title("JSON/YAML Editor")

        self.json_text = tk.Text(self.root)
        self.json_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.yaml_text = tk.Text(self.root)
        self.yaml_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.file_menu = tk.Menu(menu)
        self.menu.add_cascade(label="File", menu=file_menu)
        self.file_menu.add_command(label="Open", command=open_file)

        self.parser = parser.SchemaParser(open_file)

        self.load_data()

        self.save_button = tk.Button(self.root, text="Save", command=self.save_data)
        self.save_button.pack(side=tk.BOTTOM)

        self.root.mainloop()

    def load_data(self):
        self.json_text.delete('1.0', tk.END)
        self.yaml_text.delete('1.0', tk.END)

        self.json_text.insert(tk.END, json.dumps(self.json_data, indent=2))
        self.yaml_text.insert(tk.END, yaml.dump(self.yaml_data))

    def save_data(self):
        self.json_data = json.loads(self.json_text.get('1.0', tk.END))
        self.yaml_data = yaml.load(self.yaml_text.get('1.0', tk.END), Loader=yaml.FullLoader)

        self.load_data()
        
    def open_file():
        filename = filedialog.askopenfilename()
        print(f"Selected file: {filename}")

if __name__ == '__main__':
    """TK Inter Main Menu"""
    

    StructEdit(json_data=example_json, yaml_data=example_yaml)
