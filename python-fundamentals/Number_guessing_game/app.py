{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting Flask\n",
      "  Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)\n",
      "Collecting Werkzeug>=3.1 (from Flask)\n",
      "  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\hp\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Flask) (3.1.5)\n",
      "Collecting itsdangerous>=2.2 (from Flask)\n",
      "  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting click>=8.1.3 (from Flask)\n",
      "  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)\n",
      "Collecting blinker>=1.9 (from Flask)\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)\n",
      "Requirement already satisfied: colorama in c:\\users\\hp\\appdata\\roaming\\python\\python313\\site-packages (from click>=8.1.3->Flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\hp\\appdata\\local\\programs\\python\\python313\\lib\\site-packages (from Jinja2>=3.1.2->Flask) (3.0.2)\n",
      "Downloading flask-3.1.0-py3-none-any.whl (102 kB)\n",
      "Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Downloading click-8.1.8-py3-none-any.whl (98 kB)\n",
      "Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)\n",
      "Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)\n",
      "Installing collected packages: Werkzeug, itsdangerous, click, blinker, Flask\n",
      "Successfully installed Flask-3.1.0 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 itsdangerous-2.2.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "[notice] A new release of pip is available: 25.0 -> 25.0.1\n",
      "[notice] To update, run: python.exe -m pip install --upgrade pip\n"
     ]
    }
   ],
   "source": [
    "pip install Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with stat\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[31mSystemExit\u001b[39m\u001b[31m:\u001b[39m 1\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request, jsonify\n",
    "import random\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Global variables to store game state\n",
    "random_number = None\n",
    "attempts = 0\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/start_game', methods=['POST'])\n",
    "def start_game():\n",
    "    global random_number, attempts\n",
    "    random_number = random.randint(1, 100)\n",
    "    attempts = 0\n",
    "    return jsonify({\"message\": \"Game started! Guess a number between 1 and 100.\"})\n",
    "\n",
    "@app.route('/guess', methods=['POST'])\n",
    "def guess():\n",
    "    global attempts, random_number\n",
    "    data = request.get_json()\n",
    "    user_guess = int(data.get('guess', 0))\n",
    "    attempts += 1\n",
    "\n",
    "    if user_guess < random_number:\n",
    "        return jsonify({\"message\": \"Too low! Try again.\", \"attempts\": attempts})\n",
    "    elif user_guess > random_number:\n",
    "        return jsonify({\"message\": \"Too high! Try again.\", \"attempts\": attempts})\n",
    "    else:\n",
    "        return jsonify({\n",
    "            \"message\": f\"Congratulations! You guessed it in {attempts} attempts. The number was {random_number}.\",\n",
    "            \"attempts\": attempts\n",
    "        })\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, use_reloader=False)  # use_reloader=False avoids SystemExit in Jupyter\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
