 # hello_ai.py
# Author: Daniel Wante
# Date: 10/21/2026

import datetime

# Simple reflex agent program


	def get_time_of_day():
		hour = datetime.datetime.now().hour
		if hour < 12:
			return "morning"
		elif hour < 18:
			return "afternoon"
		else:
			return "evening"


	def main():
		print("Hello! I am your simple AI agent.")
		name = input("What is your name? ").strip()
		if name:
			print(f"Nice to meet you, {name}!")
		else:
			print("Nice to meet you!")
		print(f"It is currently the {get_time_of_day()}.")

		# Ask user how they feel
		mood = input("How are you feeling today? ").lower()

		# Mood keyword checks (required + extra)
		if "happy" in mood:
			print("I'm glad you're feeling happy!")
		elif "sad" in mood:
			print("I'm sorry you're feeling sad.")
		elif "tired" in mood:
			print("Make sure to get some rest.")
		elif "angry" in mood:  # EXTRA mood check
			print("I hope things get better soon.")
		else:
			print("Thank you for sharing how you feel.")

		print("\nHere are some AI facts:")

		# AI facts (required + 2 extra)
		print("- AI stands for Artificial Intelligence.")
		print("- Machine learning is a subset of AI.")
		print("- Neural networks are inspired by the human brain.")
		print("- AI can recognize patterns in large amounts of data.")  # EXTRA
		print("- Modern AI models can generate text, images, and code.")  # EXTRA

		print("\nThanks for running the program!")


	if __name__ == "__main__":
		main()
