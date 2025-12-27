 Slot Machine Web App (Python + Streamlit)

A fully interactive slot machine game built using Python and Streamlit, deployed as a live web application.
The project demonstrates game logic implementation, state management, UI rendering with images, and cloud deployment.


 Features

 Interactive 3×3 slot machine

 Deposit and balance management

 Configurable betting lines and bet amount

 Image-based slot symbols

 Randomized slot spin logic

 Accurate win calculation per line

 Deployed as a clickable live web app

 Tech Stack

Language: Python

Web Framework: Streamlit

UI Rendering: Streamlit components (st.image, st.button, st.columns)

State Management: st.session_state

Deployment: Streamlit Cloud

Version Control: Git & GitHub

 How the Game Works

User deposits an initial balance

User selects:

Number of lines (1–3)

Bet amount per line

On clicking SPIN:

Slot symbols are generated randomly

Results are displayed using images

Winnings are calculated based on matching symbols across selected lines

Balance is updated after each spin

📂 Project Structure
.
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── images/               # Slot symbol images
│   ├── A.png
│   ├── B.png
│   ├── C.png
│   └── D.png
└── README.md             # Project documentation

▶️ Run Locally

If you want to run this project on your local machine:

1️⃣ Clone the repository
git clone(https://github.com/pbiv-05/Slot-Machine)
cd slot-machine-streamlit

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run app.py


The app will open in your browser at:

http://localhost:8501



