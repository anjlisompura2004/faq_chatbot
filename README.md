# faq_chatbot
<h1 align="center">🤖 FAQ Chatbot using NLP</h1>

<p align="center">
A simple and intelligent FAQ Chatbot built using Python and NLP techniques.<br>
It answers user questions by finding the most relevant response from a predefined dataset.
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
This project is a <b>FAQ-based Chatbot</b> that responds to user queries by matching them 
with the most similar question stored in a dataset. It uses <b>Natural Language Processing (NLP)</b> 
to understand and process user input.
</p>

<p>
The chatbot is useful for:
</p>
<ul>
  <li>Customer Support Automation</li>
  <li>College/Company FAQs</li>
  <li>Basic AI interaction projects</li>
</ul>

<hr>

<h2>⚙️ How the Project Works</h2>

<ol>
  <li><b>Data Collection:</b> 
    A set of frequently asked questions (FAQs) and their answers are stored in a text file.
  </li>

  <li><b>Text Preprocessing:</b>
    The input text is cleaned and processed using NLP techniques:
    <ul>
      <li>Tokenization</li>
      <li>Lowercasing</li>
      <li>Removing punctuation</li>
    </ul>
  </li>

  <li><b>Vectorization:</b>
    The text data is converted into numerical form using <b>TF-IDF Vectorizer</b>.
  </li>

  <li><b>Similarity Matching:</b>
    The chatbot calculates similarity between user input and stored questions using 
    <b>Cosine Similarity</b>.
  </li>

  <li><b>Response Generation:</b>
    The most similar question is selected and its corresponding answer is displayed.
  </li>
</ol>

<hr>

<h2>🛠️ Technologies Used</h2>

<ul>
  <li>Python 🐍</li>
  <li>NLTK (Natural Language Toolkit)</li>
  <li>Scikit-learn</li>
  <li>NumPy</li>
  <li>String Processing</li>
</ul>

<hr>

<h2>💻 Features</h2>

<ul>
  <li>Interactive chatbot in terminal</li>
  <li>Fast response using similarity matching</li>
  <li>Easy to customize FAQ dataset</li>
  <li>Lightweight and beginner-friendly</li>
</ul>

<hr>

<h2>📂 Project Structure</h2>

<pre>
faq-chatbot/
│
├── chatbot.py        # Main chatbot script
├── FAQs.txt          # Questions and Answers dataset
├── requirements.txt  # Required libraries
└── README.md         # Project documentation
</pre>

<hr>

<h2>▶️ How to Run</h2>

<ol>
  <li>Install required libraries:</li>
</ol>

<pre>
pip install nltk scikit-learn numpy
</pre>

<ol start="2">
  <li>Run the chatbot:</li>
</ol>

<pre>
python chatbot.py
</pre>

<ol start="3">
  <li>Start chatting in the terminal 🎉</li>
</ol>

<hr>

<h2>📌 Future Improvements</h2>

<ul>
  <li>Add GUI using Tkinter or Web Interface</li>
  <li>Integrate real-time APIs</li>
  <li>Improve accuracy using Deep Learning</li>
</ul>

<hr>

<h2>🙌 Conclusion</h2>

<p>
This project demonstrates how NLP can be used to build a simple yet powerful chatbot.
It is a great beginner project for understanding text processing, machine learning,
and chatbot development.
</p>

<p align="center">⭐ If you like this project, don't forget to star the repository!</p>
