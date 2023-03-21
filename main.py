import tkinter as tk
import json
import yaml

class StructEdit:
    def __init__(self, json_data=None, yaml_data=None):
        self.root = tk.Tk()
        self.root.title("JSON/YAML Editor")

        self.json_text = tk.Text(self.root)
        self.json_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.yaml_text = tk.Text(self.root)
        self.yaml_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.json_data = json_data or {}
        self.yaml_data = yaml_data or {}

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

if __name__ == '__main__':
    example_json = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip": "12345"
        }
    }

    example_yaml = """
    name: Jane Doe
    age: 25
    address:
      street: 456 Elm St
      city: Anycity
      state: NY
      zip: 54321
    """

    StructEdit(json_data=example_json, yaml_data=example_yaml)
