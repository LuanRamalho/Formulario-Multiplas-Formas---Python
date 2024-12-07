import tkinter as tk
from tkinter import messagebox

class MultiStepFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulário Multi-Etapas")
        self.root.geometry("400x500")
        self.root.config(bg="#3d91f5")

        self.current_step = 0
        self.steps_data = [
            [("Nome", "text"), ("Sobrenome", "text")],
            [("Email", "email"), ("Telefone", "number")],
            [("Senha", "password"), ("Data de Nascimento", "date")],
            [("Endereço", "text"), ("Código PIN", "number")],
        ]
        self.step_labels = []
        self.entries = []

        self.create_header()
        self.create_form()
        self.create_buttons()
        self.update_form()

    def create_header(self):
        self.header_frame = tk.Frame(self.root, bg="#3d91f5")
        self.header_frame.pack(pady=20)

        for i in range(len(self.steps_data)):
            lbl = tk.Label(
                self.header_frame,
                text=str(i + 1),
                font=("Arial", 12, "bold"),
                bg="#c7c9f1",
                fg="white",
                width=3,
                height=2,
                relief="solid",
            )
            lbl.grid(row=0, column=i, padx=5)
            self.step_labels.append(lbl)

    def create_form(self):
        self.form_frame = tk.Frame(self.root, bg="#ffffff", padx=10, pady=10)
        self.form_frame.pack(fill="both", expand=True, pady=10)

    def create_buttons(self):
        self.btn_frame = tk.Frame(self.root, bg="#3d91f5")
        self.btn_frame.pack(pady=10)

        self.previous_btn = tk.Button(
            self.btn_frame, text="Anterior", command=self.previous_step, state="disabled"
        )
        self.previous_btn.grid(row=0, column=0, padx=10)

        self.next_btn = tk.Button(
            self.btn_frame, text="Próximo", command=self.next_step
        )
        self.next_btn.grid(row=0, column=1, padx=10)

        self.submit_btn = tk.Button(
            self.btn_frame, text="Enviar", command=self.submit_form, state="disabled"
        )
        self.submit_btn.grid(row=0, column=2, padx=10)

    def update_form(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        self.entries = []
        for label, input_type in self.steps_data[self.current_step]:
            lbl = tk.Label(self.form_frame, text=label, bg="#ffffff", font=("Arial", 10))
            lbl.pack(anchor="w", pady=5)
            if input_type == "password":
                entry = tk.Entry(self.form_frame, show="*")
            else:
                entry = tk.Entry(self.form_frame)
            entry.pack(fill="x", pady=5)
            self.entries.append((entry, input_type))

        self.update_header()
        self.update_buttons()

    def update_header(self):
        for i, lbl in enumerate(self.step_labels):
            lbl.config(bg="#c7c9f1", fg="white")
        self.step_labels[self.current_step].config(bg="#3d91f5", fg="white")

    def update_buttons(self):
        self.previous_btn.config(state="normal" if self.current_step > 0 else "disabled")
        self.next_btn.config(
            state="normal" if self.current_step < len(self.steps_data) - 1 else "disabled"
        )
        self.submit_btn.config(
            state="normal" if self.current_step == len(self.steps_data) - 1 else "disabled"
        )

    def validate_inputs(self):
        for entry, input_type in self.entries:
            value = entry.get().strip()
            if input_type == "email" and "@" not in value:
                messagebox.showerror("Erro", "Por favor, insira um email válido.")
                return False
            if input_type == "number" and not value.isdigit():
                messagebox.showerror("Erro", "Por favor, insira um número válido.")
                return False
            if input_type == "password" and len(value) < 8:
                messagebox.showerror("Erro", "Senha deve ter pelo menos 8 caracteres.")
                return False
            if not value:
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                return False
        return True

    def next_step(self):
        if self.validate_inputs():
            self.current_step += 1
            self.update_form()

    def previous_step(self):
        self.current_step -= 1
        self.update_form()

    def submit_form(self):
        if self.validate_inputs():
            messagebox.showinfo("Sucesso", "Formulário enviado com sucesso!")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiStepFormApp(root)
    root.mainloop()
