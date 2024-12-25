# AI Agents Repository

Welcome to the **AI Agents** repository! This project is dedicated to developing modular AI agents for various purposes. Currently, it includes a module for `search_agent`, and the application is designed to be extensible for future agents.

---

## **Getting Started**

Follow these steps to set up and run the application:

### **1. Clone the Repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

### **2. Set Up a Virtual Environment**

It is highly recommended to use a virtual environment to avoid conflicts with your system Python packages.

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install Dependencies**

Use the `requirements.txt` file to install all necessary packages:

```bash
pip install -r requirements.txt
```

### **4. Set Environment Variables**

Before running the application, ensure you have the following environment variables set:

```plaintext
GROQ_API_KEY=
LANGCHAIN_TRACING_V2=
LANGCHAIN_API_KEY=
TAVILY_API_KEY=
```

Add these variables to your `.env` file or set them in your terminal/session manually. For example:

#### On Windows:

```bash
set GROQ_API_KEY=<your-api-key>
set LANGCHAIN_TRACING_V2=<your-value>
set LANGCHAIN_API_KEY=<your-api-key>
set TAVILY_API_KEY=<your-api-key>
```

#### On macOS/Linux:

```bash
export GROQ_API_KEY=<your-api-key>
export LANGCHAIN_TRACING_V2=<your-value>
export LANGCHAIN_API_KEY=<your-api-key>
export TAVILY_API_KEY=<your-api-key>
```

### **5. Run the Application**

Start the application using:

```bash
python main.py
```

---

## **Modules**

### **1. Search Agent**

The `search_agent` module is the first implementation in this repository. It integrates AI with search capabilities to provide intelligent query handling. More details on its functionality will be added as the project evolves.

---

## **Contributing**

We welcome contributions! Feel free to fork this repository, make your changes, and submit a pull request.

### **Development Notes**

- Ensure you are working within a virtual environment.
- Update the `requirements.txt` file if you add any new dependencies.
- Document any changes to the environment variables or configuration.

## **Contact**

If you encounter any issues or have suggestions for improvements, feel free to open an issue in the repository or contact the maintainers.
