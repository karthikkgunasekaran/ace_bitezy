# Bitezy - Online Food Ordering System

## Overview
Bitezy is a demo application designed to simulate an online food ordering system. This project aims to help students understand DevOps practices by providing a minimalistic UI built with Streamlit. Users can browse food items, place orders, and manage their wallets.

## Project Structure
```
bitezy-app
├── src
│   ├── app.py               # Main entry point for the Streamlit application
│   ├── components
│   │   └── __init__.py      # Initializes the components package
│   ├── tests
│   │   ├── __init__.py      # Initializes the tests package
│   │   └── test_wallet.py    # Unit tests for wallet functionality
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bitezy-app.git
   cd bitezy-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run src/app.py
   ```

## Usage
- Open your web browser and navigate to the URL provided by Streamlit after running the application.
- Browse through the available food items.
- Place orders and manage your wallet balance.

## Testing
To run the unit tests, navigate to the `src/tests` directory and execute:
```
pytest
```

## Contributing
Feel free to submit issues or pull requests to improve the application. Your contributions are welcome!

## License
This project is licensed under the MIT License.