import tkinter as tk
from threading import Thread
import time
import math
import random
import pyttsx3
from main import agent_executor, parser

engine = pyttsx3.init()
engine.setProperty('rate', 180)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

class AIAgentUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Agent")
        self.canvas = tk.Canvas(root, width=400, height=300, bg="light grey")
        self.canvas.pack()

        # Create frequency bars instead of a single orb
        self.bars = [self.canvas.create_rectangle(10 + i * 25, 150, 10 + i * 25 + 10, 150, fill="cyan") for i in range(15)]

        self.entry = tk.Entry(root, font=("Arial", 14), width=40)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Ask AI Agent", command=self.on_submit)
        self.button.pack()

        self.output_label = tk.Label(root, text="", wraplength=380, justify="left")
        self.output_label.pack(pady=10)

        self.speaking = False

    def on_submit(self):
        query = self.entry.get()
        self.output_label.config(text="Thinking...")
        Thread(target=self.run_agent, args=(query,)).start()

    def speak(self, text):
        def animate_waveform():
            t = 0
            while self.speaking:
                for i, bar in enumerate(self.bars):
                    height = 50 + 30 * math.sin(t + i * 0.5) + random.randint(-5, 5)
                    self.canvas.coords(bar, 10 + i * 25, 150 - height, 10 + i * 25 + 10, 150 + height)
                self.canvas.update()
                time.sleep(0.05)
                t += 0.2

        def run_speech():
            self.speaking = True
            Thread(target=animate_waveform).start()

            engine.say(text)
            engine.runAndWait()

            self.speaking = False
            # Reset bars to flat line
            for i, bar in enumerate(self.bars):
                self.canvas.coords(bar, 10 + i * 25, 150, 10 + i * 25 + 10, 150)
            self.canvas.update()

        Thread(target=run_speech).start()

    def run_agent(self, query):
        try:
            raw_response = agent_executor.invoke({"query": query})
            parsed = parser.parse(raw_response.get("output", ""))
            output = f"Topic: {parsed.topic}\n\nSummary: {parsed.summary}"
            speech_text = f"Here is the information that I have collected for you about {parsed.topic}. {parsed.summary}"
        except Exception as e:
            output = f"Error: {e}"
            speech_text = "Sorry, I encountered an error."

        self.output_label.config(text=output)
        Thread(target=self.speak, args=(speech_text,)).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = AIAgentUI(root)
    root.mainloop()